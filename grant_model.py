"""Compare an incremental camp bid to a completion ceiling and a mortality benchmark."""

import csv
from math import prod, sqrt
from statistics import mean

from analyze import ROOT, estimate, load


def read_inputs():
    with (ROOT / "data/bridge_inputs.csv").open() as source:
        return {r["input"]: float(r["value"]) for r in csv.DictReader(source)}


def validity_cases(p, gain, se, camp_rate):
    kenya_paid = p["kenya_high_y"] / p["kenya_high_n"]
    kenya_sms = p["kenya_sms_y"] / p["kenya_sms_n"]
    kenya_control = p["kenya_control_y"] / p["kenya_control_n"]
    # The external trials set the scale of a zero-centered normal prior, not its mean.
    widths = (kenya_paid - kenya_sms, kenya_paid - kenya_control, p["ni_full_gain"])
    shrink = [sd**2 / (sd**2 + se**2) for sd in widths]
    discrepancy = p["overreport_difference"] - p["underreport_difference"]
    recall = [max(0, 1 - discrepancy / gain), 1 - p["ni_internal_discount"], 1.0]
    headroom = [
        (1 - rate) / (1 - camp_rate) for rate in (kenya_control, p["bauchi_basic"], camp_rate)
    ]
    return {"shrinkage": shrink, "recall": recall, "transfer": headroom}


def mortality_cases(p):
    return {
        "last_visit_measles": (
            p["measles_risk"] * p["measles_efficacy"] * (1 + p["indirect_per_direct"])
        ),
        # This ratio maps overall program changes, not individual vaccination histories.
        "nigeria_package_pattern": (
            p["ni_weighted_gain"] / p["ni_full_gain"] * p["vpd_risk"] * p["package_efficacy"]
        ),
    }


def write(name, rows):
    path = ROOT / "results" / name
    with path.open("w", newline="") as dest:
        writer = csv.DictWriter(dest, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: f"{v:.12f}" if isinstance(v, float) else v for k, v in row.items()})


def main():
    p = read_inputs()
    arms = load()
    treated, vt = estimate(arms["camp_incentive"])
    baseline, vb = estimate(arms["camp"])
    pooled = treated - baseline
    levels = validity_cases(p, pooled, sqrt(vt + vb), baseline)
    central = {k: v[1] for k, v in levels.items()}
    retained = prod(central.values())
    mortality = mortality_cases(p)
    benchmark_bar = p["bar"] * p["benchmark"]
    # The example bid and the legacy ceiling use the original repository's units.
    bid, completion_ceiling = 12, 100
    scenarios = []
    for factor in levels:
        for pos, label in enumerate(("low", "central", "high")):
            applied = dict(central)
            applied[factor] = levels[factor][pos]
            local = pooled * prod(applied.values())
            scenarios.append(
                dict(
                    factor=factor,
                    level=label,
                    **applied,
                    retained=prod(applied.values()),
                    extra_per_eligible=local,
                    completion_cap_usd=local * completion_ceiling,
                    measles_cap_usd=local
                    * mortality["last_visit_measles"]
                    * p["death_value"]
                    / benchmark_bar,
                )
            )
    write("validity_sensitivity.csv", scenarios)
    budgets = []
    equal = mean(v.completed / v.observed for v in arms["camp_incentive"]) - mean(
        v.completed / v.observed for v in arms["camp"]
    )
    for estimand, d in (("pooled_children", pooled), ("equal_villages", equal)):
        local = d * retained
        budgets.append(
            dict(
                estimand=estimand,
                trial_gain=d,
                retained=retained,
                extra_per_eligible=local,
                max_at_100_full_transfer=d * 100,
                max_at_100_adjusted=local * 100,
                needed_retention_at_12_and_100=bid / (100 * d),
                max_at_6x_measles=local
                * mortality["last_visit_measles"]
                * p["death_value"]
                / benchmark_bar,
            )
        )
    write("weighting_budget.csv", budgets)
    # Half the selected card subgroup discrepancy is a conservative sensitivity.
    half_gap = (p["overreport_difference"] - p["underreport_difference"]) / 2
    conservative = central["shrinkage"] * max(0, 1 - half_gap / pooled) * central["transfer"]
    conversions = []
    for label, retention in (("conservative", conservative), ("reference", retained)):
        local = pooled * retention
        for case, risk_change in mortality.items():
            deaths = local * risk_change
            conversions.append(
                dict(
                    scenario=label,
                    case=case,
                    retained=retention,
                    usd_per_eligible=bid,
                    completions_per_usd=local / bid,
                    under5_deaths_per_usd=deaths / bid,
                    under5_deaths_per_1000_eligible=deaths * 1000,
                    usd_per_under5_death=bid / deaths,
                    units_per_usd=deaths * p["death_value"] / bid,
                    multiple=deaths * p["death_value"] / bid / p["benchmark"],
                    max_usd_per_eligible=deaths * p["death_value"] / benchmark_bar,
                    needed_retention=bid * benchmark_bar / (pooled * risk_change * p["death_value"]),
                )
            )
    write("mortality_bridge.csv", conversions)

    # GiveWell's published, rounded full-to-under-five ratio is illustrative here.
    uplift = p["ni_full_multiple"] / p["ni_under5_multiple"]
    scope = []
    for row in conversions:
        if row["case"] == "nigeria_package_pattern":
            scope.append(
                dict(
                    scenario=row["scenario"],
                    retained=row["retained"],
                    under5_ceiling_usd=row["max_usd_per_eligible"],
                    illustrative_full_ceiling_usd=row["max_usd_per_eligible"] * uplift,
                    under5_break_even_retention=row["needed_retention"],
                    illustrative_full_break_even_retention=row["needed_retention"] / uplift,
                )
            )
    write("package_scope.csv", scope)


if __name__ == "__main__":
    main()
