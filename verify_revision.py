"""Independent arithmetic for the extension; run via verify.py or directly."""

import csv
from collections import defaultdict
from math import isclose, sqrt
from statistics import mean

from scipy.stats import t

from analyze import ROOT


def rows(path):
    with (ROOT / path).open() as f:
        return list(csv.DictReader(f))


def check(value, expected, tolerance=1e-6):
    if not isclose(float(value), float(expected), abs_tol=tolerance, rel_tol=1e-10):
        raise ValueError(f"Reported {value}, independently calculated {expected}")


def verify_outcomes():
    grouped = rows("data/mechanism_counts.csv")
    published = rows("results/mechanism.csv")
    assert len(grouped) == 5 and len(published) == 20
    lookup = {(int(r["neighbor"]), r["arm"], r["outcome"]): r for r in published}
    for row in grouped:
        n, started, complete, examined, scar = [
            int(row[k]) for k in ("observed", "started", "completed", "scar_observed", "scar")
        ]
        assert 0 <= complete <= started <= n and 0 <= scar <= examined
        for outcome, y, count in [
            ("started", started, n),
            ("completed", complete, n),
            ("bcg_scar", scar, examined),
            ("completion_among_starters", complete, started),
        ]:
            record = lookup[int(row["neighbor"]), row["arm"], outcome]
            assert (int(record["numerator"]), int(record["denominator"])) == (y, count)
            check(record["pct"], 100 * y / count)
    for arm, neighbor, y, n in [
        ("camp", 0, 68, 379),
        ("camp_incentive", 0, 148, 382),
        ("camp", 1, 28, 265),
        ("camp_incentive", 1, 61, 302),
    ]:
        r = lookup[neighbor, arm, "completed"]
        assert (int(r["numerator"]), int(r["denominator"])) == (y, n)


def verify_within_blocks():
    villages = rows("data/block_counts.csv")
    by_block = defaultdict(list)
    for r in villages:
        by_block[r["block"]].append(
            (int(r["arm"] == "camp_incentive"), int(r["observed"]), int(r["completed"]))
        )
    # Remove block means first; this yields the child-level OLS coefficient by residualization.
    pairs = []
    for records in by_block.values():
        n_total = sum(n for _, n, _ in records)
        avg_y = sum(y for _, _, y in records) / n_total
        avg_x = sum(n * x for x, n, _ in records) / n_total
        pairs.extend((x - avg_x, n, y - n * avg_y) for x, n, y in records)
    denominator = sum(n * x * x for x, n, y in pairs)
    slope = sum(x * y for x, n, y in pairs) / denominator
    meat = sum((x * (y - n * x * slope)) ** 2 for x, n, y in pairs)
    n = sum(n for x, n, y in pairs)
    g = len(villages)
    correction = g / (g - 1) * (n - 1) / (n - len(by_block) - 1)
    se = sqrt(meat * correction) / denominator
    (outcome,) = rows("results/block_robustness.csv")
    assert int(outcome["children"]) == n == 761 and int(outcome["villages"]) == g == 60
    margin = t.isf(0.025, g - 1) * se
    for key, val in [
        ("gain_pp", slope),
        ("se_pp", se),
        ("ci_low_pp", slope - margin),
        ("ci_high_pp", slope + margin),
    ]:
        check(outcome[key], 100 * val)


def verify_budgets():
    p = {r["input"]: float(r["value"]) for r in rows("data/bridge_inputs.csv")}
    clusters = defaultdict(list)
    for r in rows("data/block_counts.csv"):
        clusters[r["arm"]].append((int(r["observed"]), int(r["completed"])))
    rates = {}
    variances = []
    for arm, v in clusters.items():
        n = sum(n for n, y in v)
        rates[arm] = sum(y for n, y in v) / n
        variances.append(
            sum((y - rates[arm] * size) ** 2 for size, y in v) * len(v) / (len(v) - 1) / n**2
        )
    base = rates["camp"]
    d = rates["camp_incentive"] - base
    paid, sms, control = [
        p[f"kenya_{arm}_y"] / p[f"kenya_{arm}_n"] for arm in ("high", "sms", "control")
    ]
    prior = [
        1 / (1 + sum(variances) / s**2) for s in (paid - sms, paid - control, p["ni_full_gain"])
    ]
    error = p["overreport_difference"] - p["underreport_difference"]
    recall = [(d - error) / d, (d - error / 2) / d, 1.0]
    transfer = [(1 - control) / (1 - base), (1 - p["bauchi_basic"]) / (1 - base), 1.0]
    central = prior[1] * recall[1] * transfer[1]
    direct = p["measles_risk"] * p["measles_efficacy"]
    bar = p["benchmark"] * p["bar"]
    sensitivity = rows("results/validity_sensitivity.csv")
    triples = {"shrinkage": prior, "recall": recall, "transfer": transfer}
    assert len(sensitivity) == 9 and {(r["factor"], r["level"]) for r in sensitivity} == {
        (k, l) for k in triples for l in ("low", "central", "high")
    }
    for r in sensitivity:
        retain = 1.0
        for name, values in triples.items():
            i = ("low", "central", "high").index(r["level"]) if r["factor"] == name else 1
            check(r[name], values[i])
            retain *= values[i]
        check(r["retained"], retain)
        check(r["extra_per_eligible"], d * retain)
        check(r["completion_cap_usd"], 100 * d * retain)
        check(r["measles_cap_usd"], d * retain * direct * p["death_value"] / bar)
    equal = mean(y / n for n, y in clusters["camp_incentive"]) - mean(
        y / n for n, y in clusters["camp"]
    )
    weighting = rows("results/weighting_budget.csv")
    assert {r["estimand"] for r in weighting} == {"pooled_children", "equal_villages"} and len(
        weighting
    ) == 2
    for r in weighting:
        effect = d if r["estimand"] == "pooled_children" else equal
        check(r["trial_gain"], effect)
        check(r["retained"], central)
        check(r["extra_per_eligible"], effect * central)
        check(r["max_at_100_full_transfer"], 100 * effect)
        check(r["max_at_100_adjusted"], 100 * effect * central)
        check(r["needed_retention_at_12_and_100"], 0.12 / effect)
        check(r["max_at_6x_measles"], effect * central * direct * p["death_value"] / bar)
    cases = {
        "last_visit_measles": direct,
        "nigeria_package_pattern": p["vpd_risk"]
        * p["package_efficacy"]
        * p["ni_weighted_gain"]
        / p["ni_full_gain"],
    }
    bridge = rows("results/mortality_bridge.csv")
    assert {r["case"] for r in bridge} == cases.keys() and len(bridge) == len(cases)
    for r in bridge:
        cost = float(r["usd_per_eligible"])
        check(cost, 12)
        per_dollar = d * central / cost
        death_rate = per_dollar * cases[r["case"]]
        units = death_rate * p["death_value"]
        for key, val in [
            ("completions_per_usd", per_dollar),
            ("under5_deaths_per_usd", death_rate),
            ("usd_per_under5_death", 1 / death_rate),
            ("under5_deaths_per_1000_eligible", death_rate * 1000 * cost),
            ("units_per_usd", units),
            ("multiple", units / p["benchmark"]),
            ("max_usd_per_eligible", units * cost / bar),
            ("needed_retention", cost * bar / (d * cases[r["case"]] * p["death_value"])),
        ]:
            check(r[key], val, 1e-10)


def main():
    verify_outcomes()
    verify_within_blocks()
    verify_budgets()
    print(
        "Verified secondary outcomes, block-adjusted uncertainty, validity scenarios and funding thresholds."
    )


if __name__ == "__main__":
    main()
