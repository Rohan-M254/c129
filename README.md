# Exoplanet CSV Processing

A Python CSV-processing exercise that sorts one exoplanet dataset and combines it with a second dataset.

## Files

- `c129/dataset_1.csv` — first source dataset.
- `c129/dataset_2.csv` — second source dataset.
- `c129/main.py` — sorts the second dataset by its third column and writes `dataset_2_sorted.csv`.
- `c129/final.py` — combines the two datasets by row position and writes `final.csv`.

## Run

Requires Python 3. Run both commands from the `c129` directory:

```bash
python main.py
python final.py
```

## Important data limitation

The original workflow pairs rows by position, not by a verified planet identifier. The updated merge script now refuses to proceed if row counts differ, but equal row counts do not prove that rows refer to the same planets. Confirm a shared key and perform a key-based join before treating the merged output as scientifically reliable.

Generated CSV outputs are intentionally not committed; the scripts recreate them.