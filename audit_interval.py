"""Compare two random-intercept hierarchies on the verified, public endline file."""

import csv
import hashlib
import io
from collections import defaultdict

import numpy as np
import requests
from scipy.linalg import cho_factor, cho_solve
from scipy.optimize import minimize
from scipy.stats import norm

from prepare_data import URL, DIGEST


def design(raw, outer, inner):
    groups = defaultdict(list)
    for r in csv.DictReader(io.StringIO(raw.decode("utf-8-sig")), delimiter="\t"):
        if (
            float(r["spillover"])
            or float(r["NonTreat"])
            or not r["d2_5"]
            or not r["agemon"]
            or not 12 <= float(r["agemon"]) <= 36
        ):
            continue
        groups[r[outer]].append((r[inner], float(r["TreatIncentive"]), float(r["d2_5"]) >= 5))
    blocks = []
    for rows in groups.values():
        ids, treatment, y = zip(*rows)
        group = np.array(ids)
        x = np.column_stack([np.ones(len(y)), treatment])
        blocks.append(
            (
                np.eye(len(y)),
                (group[:, None] == group[None, :]).astype(float),
                np.column_stack([x, y]),
            )
        )
    return blocks


def fit(blocks):
    # Profile the residual variance and fixed effects. Each covariance block is
    # a common outer-group intercept plus one intercept per nested group and noise.
    n = sum(len(z) for _, _, z in blocks)

    def profile(ratios, give_estimate=False):
        logdet, cross = 0.0, np.zeros((3, 3))
        for eye, shared, z in blocks:
            chol = cho_factor(eye + ratios[0] + ratios[1] * shared, lower=True)
            cross += z.T @ cho_solve(chol, z)
            logdet += 2 * np.log(np.diag(chol[0])).sum()
        info = cross[:2, :2]
        b = np.linalg.solve(info, cross[:2, 2])
        residual_var = (cross[2, 2] - b @ cross[:2, 2]) / n
        if give_estimate:
            se = np.sqrt(residual_var * np.linalg.inv(info)[1, 1])
            return b[1], se
        return logdet + n * np.log(residual_var)

    result = minimize(
        profile,
        [0.1, 0.1],
        bounds=[(0, None), (0, None)],
        method="L-BFGS-B",
        options={"ftol": 1e-13},
    )
    if not result.success:
        raise RuntimeError(result.message)
    return profile(result.x, True)


def main():
    response = requests.get(URL, timeout=90)
    response.raise_for_status()
    raw = response.content
    if hashlib.sha256(raw).hexdigest() != DIGEST:
        raise ValueError("Endline source changed")
    for outer, inner in (("hidno", "locid"), ("locid", "hidno")):
        blocks = design(raw, outer, inner)
        assert sum(len(z) for _, _, z in blocks) == 761
        gain, se = fit(blocks)
        margin = norm.ppf(0.975) * se
        print(
            f"{outer} then {inner}: {100*gain:.2f} pp "
            f"(95% model-based interval {100*(gain-margin):.2f} to {100*(gain+margin):.2f})"
        )


if __name__ == "__main__":
    main()
