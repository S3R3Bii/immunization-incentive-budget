"""Build public grouped data and fit the prespecified-style block sensitivity."""
import csv

import numpy as np
from scipy.stats import t

from analyze import ROOT, write_table


def read(name):
    with (ROOT / "data" / name).open() as f:
        return list(csv.DictReader(f))


def block_fit():
    rows = read("block_counts.csv")
    blocks = sorted({r["block"] for r in rows})
    # Saturate the block means; the first column is the incentive coefficient.
    x = np.array([[r["arm"] == "camp_incentive", *(r["block"] == b for b in blocks)]
                  for r in rows], dtype=float)
    n = np.array([int(r["observed"]) for r in rows])
    y = np.array([int(r["completed"]) for r in rows])
    bread = np.linalg.inv(x.T @ (n[:, None] * x))
    beta = bread @ (x.T @ y)
    scores = x * (y - n * (x @ beta))[:, None]
    g, k = x.shape
    correction = g / (g - 1) * (n.sum() - 1) / (n.sum() - k)
    variance = correction * bread @ (scores.T @ scores) @ bread
    se = float(np.sqrt(variance[0, 0]))
    margin = t.ppf(.975, g - 1) * se
    return dict(estimator="child_ols_block_effects_village_cr1", villages=g, children=int(n.sum()),
                gain_pp=100 * beta[0], se_pp=100 * se, ci_low_pp=100 * (beta[0] - margin),
                ci_high_pp=100 * (beta[0] + margin))


def main():
    results = []
    for row in read("mechanism_counts.csv"):
        for measure, num, den in (
            ("started", "started", "observed"), ("bcg_scar", "scar", "scar_observed"),
            ("completed", "completed", "observed"),
            ("completion_among_starters", "completed", "started"),
        ):
            y, n = int(row[num]), int(row[den])
            results.append(dict(neighbor=int(row["neighbor"]), arm=row["arm"], outcome=measure,
                                numerator=y, denominator=n, pct=100*y/n))
    write_table("mechanism.csv", results)
    write_table("block_robustness.csv", [block_fit()])


if __name__ == "__main__":
    main()
