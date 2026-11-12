import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_1 = BASE_DIR / "dataset_1.csv"
INPUT_2 = BASE_DIR / "dataset_2_sorted.csv"
OUTPUT = BASE_DIR / "final.csv"

def read_csv(path):
    with path.open("r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    if not rows:
        raise ValueError(f"{path.name} is empty")
    return rows[0], rows[1:]

headers_1, data_1 = read_csv(INPUT_1)
headers_2, data_2 = read_csv(INPUT_2)

if len(data_1) != len(data_2):
    raise ValueError(
        "The datasets have different row counts; refusing to merge by row position "
        f"({len(data_1)} vs {len(data_2)}). Join on a verified shared key instead."
    )

if any(len(row) != len(headers_1) for row in data_1):
    raise ValueError("dataset_1.csv contains rows with inconsistent column counts")
if any(len(row) != len(headers_2) for row in data_2):
    raise ValueError("dataset_2_sorted.csv contains rows with inconsistent column counts")

with OUTPUT.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers_1 + headers_2)
    writer.writerows(left + right for left, right in zip(data_1, data_2))

print(f"Wrote {len(data_1)} merged rows to {OUTPUT.name}")
