"""Render the portfolio funding-ceiling figure from the committed CSVs."""

import csv
from decimal import Decimal
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
INK, MUTED, TEAL = "#142e45", "#506b7e", "#006d75"


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def load_figure_data():
    bridge = read_csv(RESULTS / "mortality_bridge.csv")
    ceilings = {
        (r["scenario"], r["case"]): Decimal(r["max_usd_per_eligible"]) for r in bridge
    }
    (full_reference,) = [
        r for r in read_csv(RESULTS / "package_scope.csv") if r["scenario"] == "reference"
    ]
    (bid,) = {Decimal(r["usd_per_eligible"]) for r in bridge}
    (bar,) = [
        Decimal(r["value"]) for r in read_csv(ROOT / "data/bridge_inputs.csv") if r["input"] == "bar"
    ]
    rows = [
        ("Measles floor", "Reference", ceilings["reference", "last_visit_measles"]),
        ("Broader vaccine mix", "Conservative", ceilings["conservative", "nigeria_package_pattern"]),
        ("Broader vaccine mix", "Reference", ceilings["reference", "nigeria_package_pattern"]),
        ("Mix + broader benefits", "Reference sensitivity",
         Decimal(full_reference["illustrative_full_ceiling_usd"])),
    ]
    return rows, bid, bar


def main():
    rows, bid, bar = load_figure_data()
    title = "What could a funder pay per child?"
    bid_label = f"${bid:f} bid"
    floor, conservative, reference, broader = (row[2] for row in rows)
    alt = (
        f"Maximum extra cost per eligible child at GiveWell’s {bar:f}× funding bar. "
        f"The reference measles floor is ${floor:.2f}. The broader vaccine mix supports "
        f"${conservative:.2f} in the conservative case and ${reference:.2f} in the reference case. "
        f"The reference sensitivity with broader benefits reaches ${broader:.2f}. "
        f"A dashed line marks the {bid_label}."
    )

    with plt.rc_context({"font.family": "DejaVu Sans", "text.color": INK}):
        fig, ax = plt.subplots(figsize=(8, 4.5))
        fig.subplots_adjust(left=0.356, right=0.968, top=0.754, bottom=0.157)
        fig.text(0.043, 0.943, title, ha="left", va="top", size=21, weight="bold")
        fig.text(0.043, 0.847, f"Maximum extra cost per eligible child at GiveWell’s {bar:f}× funding bar",
                 ha="left", va="top", size=11.8, color=MUTED)

        values = [float(row[2]) for row in rows]
        ax.set_xlim(0, max(max(values), float(bid)) * 1.27)
        ax.set_ylim(len(rows) - 0.43, -0.61)
        ax.barh(range(len(rows)), values, height=0.45,
                color=["#91a8b7", "#91a8b7", TEAL, "#e4f0f1"],
                edgecolor=["none", "none", "none", TEAL], linewidth=1.25)
        # A separate fill and explicit row label distinguish the broader-benefit sensitivity.
        ax.axvline(float(bid), color=INK, linestyle=(0, (4, 3)), linewidth=1.25)
        ax.text(float(bid), 1.012, bid_label, transform=ax.get_xaxis_transform(),
                ha="center", va="bottom", size=12, color=INK, weight="bold")

        for y, (case, scenario, ceiling) in enumerate(rows):
            center = ax.transData.transform((0, y))[1]
            label_y = fig.transFigure.inverted().transform((0, center))[1]
            fig.text(0.043, label_y + 0.003, case, va="bottom", size=12.5, weight="bold")
            fig.text(0.043, label_y - 0.005, scenario, va="top", size=10.7, color=MUTED)
            # Keep the reference label clear of the nearby bid line.
            inside = (case, scenario) == ("Broader vaccine mix", "Reference")
            ax.annotate(f"${ceiling:.2f}", (float(ceiling), y),
                        xytext=(-5 if inside else 5, 0), textcoords="offset points",
                        va="center", ha="right" if inside else "left", size=13,
                        color="white" if inside else INK, weight="bold")

        ax.set_yticks([])
        ax.xaxis.set_major_locator(MultipleLocator(5))
        ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:g}"))
        ax.tick_params(axis="x", length=3, pad=4, labelsize=10.5,
                       color="#b7c7d0", labelcolor=MUTED)
        ax.spines[["top", "left", "right"]].set_visible(False)
        ax.spines["bottom"].set_color("#c8d5dc")
        fig.text(0.043, 0.032, "The first three cases count under-five mortality. The last also credits broader benefits.",
                 ha="left", va="bottom", size=9.3, color=MUTED)
        fig.savefig(RESULTS / "funding-ceilings.png", dpi=400, facecolor="white",
                    metadata={"Title": title, "Description": alt})
        plt.close(fig)


if __name__ == "__main__":
    main()
