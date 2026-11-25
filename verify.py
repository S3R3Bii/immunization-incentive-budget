"""Independently reconstruct the reported results with SQL and published arm counts."""

import csv
import math
import sqlite3
from pathlib import Path
from statistics import NormalDist

from scipy.stats import t

ROOT = Path(__file__).resolve().parent


def read(relative):
    with (ROOT / relative).open() as source:
        return list(csv.DictReader(source))


def close(actual, expected):
    if not math.isclose(float(actual), expected, abs_tol=0.000001):
        raise AssertionError((actual, expected))


def main():
    villages = read("data/village_counts.csv")
    db = sqlite3.connect(":memory:")
    db.execute("create table v(arm text, n integer, y integer, m integer)")
    db.executemany("insert into v values (:arm,:observed,:completed,:missing)", villages)
    counts = {
        arm: (clusters, n, y, missing)
        for arm, clusters, n, y, missing in db.execute(
            "select arm, count(*), sum(n), sum(y), sum(m) from v group by arm"
        )
    }
    # Observed child denominators and numerators agree with the published corrected abstract.
    assert counts == {
        "camp": (30, 379, 68, 0),
        "camp_incentive": (30, 382, 148, 0),
        "control": (73, 860, 50, 6),
    }
    stages = {row["stage"]: int(row["rows"]) for row in read("data/cohort_flow.csv")}
    assert stages.pop("endline_rows") == sum(stages.values()) == 5565
    assert stages["eligible_observed"] == sum(x[1] for x in counts.values())
    summary = read("results/arms.csv")
    assert {r["arm"] for r in summary} == counts.keys() and len(summary) == len(counts)
    for record in summary:
        k, n, y, m = counts[record["arm"]]
        assert [int(record[c]) for c in ("villages", "observed", "completed", "missing")] == [
            k,
            n,
            y,
            m,
        ]
        for key, rate in (
            ("completion_pct", y / n),
            ("missing_all_incomplete_pct", y / (n + m)),
            ("missing_all_complete_pct", (y + m) / (n + m)),
        ):
            close(record[key], 100 * rate)
    # Independent ratio variance computed from sums of cross-products rather than residual vectors.
    stats = {}
    for arm, (k, n, y, _) in counts.items():
        yy, yn, nn, equal = db.execute(
            "select sum(y*y),sum(y*n),sum(n*n),avg(1.0*y/n) from v where arm=?", (arm,)
        ).fetchone()
        p = y / n
        v = (yy - 2 * p * yn + p * p * nn) * k / ((k - 1) * n * n)
        omissions = [
            (y - yi) / (n - ni) for ni, yi in db.execute("select n,y from v where arm=?", (arm,))
        ]
        stats[arm] = p, v, equal, omissions
    pairs = read("results/contrasts.csv")
    assert {(x["arm"], x["comparator"]) for x in pairs} == {
        ("camp_incentive", "camp"),
        ("camp", "control"),
        ("camp_incentive", "control"),
    } and len(pairs) == 3
    for row in pairs:
        a, b = row["arm"], row["comparator"]
        pa, va, ea, la = stats[a]
        pb, vb, eb, lb = stats[b]
        df = (va + vb) ** 2 / (va**2 / (counts[a][0] - 1) + vb**2 / (counts[b][0] - 1))
        se = math.sqrt(va + vb)
        critical = t.isf(0.025, df)
        assert critical > NormalDist().inv_cdf(0.975)
        leave = [x - pb for x in la] + [pa - x for x in lb]
        for key, value in (
            ("gain_pp", pa - pb),
            ("ci_low_pp", pa - pb - critical * se),
            ("ci_high_pp", pa - pb + critical * se),
            ("equal_village_pp", ea - eb),
            ("omit_one_low_pp", min(leave)),
            ("omit_one_high_pp", max(leave)),
        ):
            close(row[key], 100 * value)
        close(row["welch_df"], df)
    budget = read("results/budget.csv")
    combos = {
        (float(r["retained_fraction"]), int(r["ceiling_usd_per_additional_completion"]))
        for r in budget
    }
    assert combos == {(p, v) for p in (0.25, 0.5, 1) for v in (50, 100, 250)} and len(budget) == 9
    main_contrast = next(
        x for x in pairs if x["arm"] == "camp_incentive" and x["comparator"] == "camp"
    )
    for row in budget:
        factor = (
            float(row["retained_fraction"])
            * int(row["ceiling_usd_per_additional_completion"])
            / 100
        )
        for budget_key, estimate_key in [
            ("max_usd_per_eligible", "gain_pp"),
            ("trial_low_implied_usd", "ci_low_pp"),
            ("trial_high_implied_usd", "ci_high_pp"),
        ]:
            assert (
                abs(float(row[budget_key]) - factor * float(main_contrast[estimate_key])) < 0.000003
            )
    print(
        "Verified 133 village summaries against published arm totals, all contrasts and nine budgets."
    )


if __name__ == "__main__":
    main()
    import verify_revision

    verify_revision.main()
