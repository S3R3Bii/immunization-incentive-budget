"""Translate a real incremental bid into a required local gain in coverage."""

import argparse
import math

from analyze import estimate, load


def positive(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("supply a positive finite number")
    return number


def price(incremental_cost, eligible, ceiling, trial_gain):
    per_child = incremental_cost / eligible
    required_gain = per_child / ceiling
    return per_child, required_gain, required_gain / trial_gain


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--incremental-cost", required=True, type=positive, help="total extra program cost, USD"
    )
    parser.add_argument(
        "--eligible", required=True, type=int, help="eligible children over the budget period"
    )
    parser.add_argument(
        "--ceiling", required=True, type=positive, help="USD per additional completion"
    )
    args = parser.parse_args()
    if args.eligible < 1:
        parser.error("--eligible must be at least one")
    arms = load()
    gain = estimate(arms["camp_incentive"])[0] - estimate(arms["camp"])[0]
    per_child, required, fraction = price(args.incremental_cost, args.eligible, args.ceiling, gain)
    print(f"Incremental cost per eligible child: ${per_child:.2f}")
    print(f"Required local completion gain: {100*required:.2f} percentage points")
    print(f"Required share of the trial point estimate: {100*fraction:.1f}%")
    if required > 1:
        print("Even a 100-percentage-point gain would fall short at this price.")
    else:
        print(
            "Compare the required gain with a credible local counterfactual and baseline headroom."
        )


if __name__ == "__main__":
    main()
