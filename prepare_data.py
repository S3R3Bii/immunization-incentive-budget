"""Rebuild anonymous village totals from the public endline file in memory."""

import csv
import hashlib
import io
from collections import Counter, defaultdict
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent
URL = "https://dataverse.harvard.edu/api/access/datafile/1581016"
DIGEST = "22dae428182d602acd9201d22989e52a97c36e5b20ca73b1247d5a8fb1caadde"
ARMS = {"NonTreat": "control", "TreatNonIncentive": "camp", "TreatIncentive": "camp_incentive"}


def csv_bytes(header, rows):
    out = io.StringIO()
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return out.getvalue().encode()


def main():
    response = requests.get(URL, timeout=90)
    response.raise_for_status()
    raw = response.content
    if hashlib.sha256(raw).hexdigest() != DIGEST:
        raise ValueError("Upstream bytes changed. Review the source before updating this release.")
    groups = defaultdict(Counter)
    flow = Counter()
    arm_by_village = {}
    for row in csv.DictReader(io.StringIO(raw.decode("utf-8-sig")), delimiter="\t"):
        flow["endline_rows"] += 1
        if float(row["spillover"]) == 1:
            flow["neighboring_village"] += 1
            continue
        assert float(row["spillover"]) == 0
        if not row["agemon"] or not 12 <= float(row["agemon"]) <= 36:
            flow["age_missing_or_outside_12_to_36"] += 1
            continue
        (arm,) = [name for col, name in ARMS.items() if float(row[col]) == 1]
        village = row["locid"]
        assert village and arm_by_village.setdefault(village, arm) == arm
        group = groups[arm, village]
        if not row["d2_5"]:
            group["missing"] += 1
            flow["eligible_missing_outcome"] += 1
            continue
        shots = int(float(row["d2_5"]))
        assert float(row["d2_5"]) == shots and 0 <= shots <= 6
        group["observed"] += 1
        group["completed"] += shots >= 5
        flow["eligible_observed"] += 1
    # Sorting on counts alone discards the village key and the source row order.
    rows = sorted(
        (arm, g["observed"], g["completed"], g["missing"]) for (arm, _), g in groups.items()
    )
    data = ROOT / "data"
    data.mkdir(exist_ok=True)
    (data / "village_counts.csv").write_bytes(
        csv_bytes(["arm", "observed", "completed", "missing"], rows)
    )
    (data / "cohort_flow.csv").write_bytes(csv_bytes(["stage", "rows"], sorted(flow.items())))


if __name__ == "__main__":
    main()
