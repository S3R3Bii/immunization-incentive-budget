"""Plot the price a grant can support as the assumed local impact changes."""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter, MultipleLocator

ROOT = Path(__file__).resolve().parent
with (ROOT / "results/contrasts.csv").open() as f:
    row = next(
        r for r in csv.DictReader(f) if (r["arm"], r["comparator"]) == ("camp_incentive", "camp")
    )
gain, low, high = (float(row[k]) / 100 for k in ("gain_pp", "ci_low_pp", "ci_high_pp"))
retained = np.arange(101)
fig, ax = plt.subplots(figsize=(9.4, 4.8))
fig.subplots_adjust(left=0.11, right=0.97, top=0.82, bottom=0.2)
fig.text(
    0.11,
    0.94,
    "What can a funder pay for the incentive?",
    fontsize=19,
    weight="bold",
    color="#19384a",
)
fig.text(
    0.11,
    0.865,
    "Illustrative ceiling of $100 per additional child completing the series",
    fontsize=11,
)
ax.fill_between(
    retained, retained * low, retained * high, color="#c8e1dc", label="Trial 95% interval, scaled"
)
ax.plot(
    retained, retained * gain, color="#17665b", linewidth=3, label="Trial point estimate, scaled"
)
ax.axhline(12, color="#8f5026", linestyle="--", linewidth=1.6)
cross = 12 / gain
ax.scatter([cross], [12], color="#8f5026", zorder=4)
ax.annotate(
    "Example bid: $12 per eligible child\nRequires 58% of the trial gain",
    (cross, 12),
    xytext=(4, 19.2),
    fontsize=10,
    color="#764320",
    arrowprops={"arrowstyle": "-", "color": "#8f5026"},
)
ax.set(
    xlim=(0, 100),
    ylim=(0, 34),
    xlabel="Share of the trial gain retained locally",
    ylabel="Maximum extra cost per eligible child",
)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f}%"))
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x:.0f}"))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.legend(loc="upper left", frameon=False, fontsize=9)
ax.spines[["top", "right"]].set_visible(False)
ax.set_axisbelow(True)
ax.grid(axis="y", color="#dce4e6")
fig.text(
    0.11,
    0.035,
    "Trial source: Banerjee et al. (2010). Local retention and the bid are planning assumptions.",
    fontsize=9,
)
fig.savefig(ROOT / "results/budget-threshold.png", dpi=150)
