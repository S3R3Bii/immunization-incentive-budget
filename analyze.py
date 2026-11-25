"""Estimate the trial contrast and translate it to an incremental budget ceiling."""

import csv
import itertools
from collections import defaultdict
from dataclasses import dataclass
from math import sqrt
from pathlib import Path
from statistics import mean

from scipy.stats import t

ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Village:
    observed: int
    completed: int
    missing: int


def estimate(villages):
    people = sum(v.observed for v in villages)
    complete = sum(v.completed for v in villages)
    rate = complete / people
    n = len(villages)
    # Linearization of a ratio of village totals; villages are the sampling units.
    residual_ss = sum((v.completed - rate * v.observed) ** 2 for v in villages)
    variance = n / (n - 1) * residual_ss / people**2
    return rate, variance


def load():
    arms = defaultdict(list)
    with (ROOT / "data/village_counts.csv").open() as source:
        for row in csv.DictReader(source):
            village = Village(*(int(row[k]) for k in ("observed", "completed", "missing")))
            assert 0 <= village.completed <= village.observed and village.observed > 0
            arms[row["arm"]].append(village)
    return arms


def write_table(name, rows):
    path = ROOT / "results" / name
    with path.open("w", newline="", encoding="utf-8") as dest:
        writer = csv.DictWriter(dest, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        for record in rows:
            writer.writerow(
                {k: f"{v:.6f}" if isinstance(v, float) else v for k, v in record.items()}
            )


def compare(arms, treated, baseline):
    a, b = arms[treated], arms[baseline]
    ra, va = estimate(a)
    rb, vb = estimate(b)
    delta = ra - rb
    df = (va + vb) ** 2 / (va**2 / (len(a) - 1) + vb**2 / (len(b) - 1))
    margin = t.ppf(0.975, df) * sqrt(va + vb)
    equal_village = mean(v.completed / v.observed for v in a) - mean(
        v.completed / v.observed for v in b
    )
    omitted = [estimate(a[:i] + a[i + 1 :])[0] - rb for i in range(len(a))]
    omitted.extend(ra - estimate(b[:i] + b[i + 1 :])[0] for i in range(len(b)))
    return dict(
        arm=treated,
        comparator=baseline,
        gain_pp=100 * delta,
        ci_low_pp=100 * (delta - margin),
        ci_high_pp=100 * (delta + margin),
        equal_village_pp=100 * equal_village,
        omit_one_low_pp=100 * min(omitted),
        omit_one_high_pp=100 * max(omitted),
        welch_df=df,
    )


def max_budget(gain, retained, value):
    """Incremental dollars per eligible child, given gain in probability units."""
    if not 0 <= gain <= 1 or not 0 <= retained <= 1 or not value >= 0:
        raise ValueError("Expected probabilities in [0, 1] and a nonnegative ceiling")
    return gain * retained * value


def main():
    arms = load()
    (ROOT / "results").mkdir(exist_ok=True)
    summaries = []
    for arm, villages in sorted(arms.items()):
        observed = sum(v.observed for v in villages)
        complete = sum(v.completed for v in villages)
        missing = sum(v.missing for v in villages)
        summaries.append(
            dict(
                arm=arm,
                villages=len(villages),
                observed=observed,
                completed=complete,
                missing=missing,
                completion_pct=100 * complete / observed,
                missing_all_incomplete_pct=100 * complete / (observed + missing),
                missing_all_complete_pct=100 * (complete + missing) / (observed + missing),
            )
        )
    write_table("arms.csv", summaries)
    contrasts = [
        compare(arms, a, b)
        for a, b in [("camp_incentive", "camp"), ("camp", "control"), ("camp_incentive", "control")]
    ]
    write_table("contrasts.csv", contrasts)
    primary = contrasts[0]
    budgets = []
    for retained, value in itertools.product((0.25, 0.5, 1.0), (50, 100, 250)):
        bounds = [
            max_budget(primary[x] / 100, retained, value)
            for x in ("gain_pp", "ci_low_pp", "ci_high_pp")
        ]
        budgets.append(
            dict(
                retained_fraction=retained,
                ceiling_usd_per_additional_completion=value,
                max_usd_per_eligible=bounds[0],
                trial_low_implied_usd=bounds[1],
                trial_high_implied_usd=bounds[2],
            )
        )
    write_table("budget.csv", budgets)


if __name__ == "__main__":
    main()
