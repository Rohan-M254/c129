import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SOURCE = BASE_DIR / "dataset_2.csv"
OUTPUT = BASE_DIR / "dataset_2_sorted.csv"

with SOURCE.open("r", newline="", encoding="utf-8") as source_file:
    rows = list(csv.reader(source_file))

if not rows:
    raise SystemExit("dataset_2.csv is empty")

header, records = rows[0], rows[1:]
if any(len(row) <= 2 for row in records):
    raise SystemExit("A dataset row is missing the third column used for sorting")

records.sort(key=lambda row: row[2].casefold())

with OUTPUT.open("w", newline="", encoding="utf-8") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(header)
    writer.writerows(records)

print(f"Wrote {len(records)} sorted records to {OUTPUT.name}")
