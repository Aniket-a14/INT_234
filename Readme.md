# INT_234 — Classwork (LPU)

This repository contains coursework and practical scripts for INT-234 at Lovely Professional University (LPU). It collects weekly lab exercises, small experiments, and datasets created during the 3rd-year Data Science course.

Student: 3rd Year, Data Science

Primary goals
- Keep classwork organized and runnable from the repository root.
- Make it easy to add new weekly folders or datasets without changing the repository layout.

Stable repository structure (expected and extensible)

The repository is intentionally simple and stable. New files or folders (for additional days or datasets) should follow the patterns below so they do not change the overall structure.

- `dataset/`
	- Store CSVs and other data files here. Example: `dataset/ecommerce_customers_unit1.csv`.
	- Naming convention suggestion: use lowercase, words separated by underscores, and include a short note in the filename if needed (e.g., `ecommerce_customers_unit1.csv`).

- `day_<n>/` (example: `day_1/`, `day_2/`, `day_7/`)
	- Each day's folder holds exercises from a class session. Add new folders as `day_7`, `day_8`, etc., when new labs are done.
	- Inside each `day_*` folder prefer a short README (`README.md`) describing that day's exercises and the main script(s).
	- File naming: small scripts like `encoding.py`, `regression.py`, `plot.py`. Avoid renaming top-level folders — add new `day_*` folders alongside the existing ones.

Why this is stable
- Adding a new `day_*` folder or a new file in `dataset/` does not require changing any other files. Code in the repository should reference files by relative paths (example: `dataset/your_file.csv`) and assume scripts run from the repository root.
- If you add automation (scripts that iterate `day_*` folders), keep the pattern `day_\d+` to allow simple globbing and discovery.

How to add new content (recommended minimal steps)

1. To add a new weekly folder:
	 - Create `day_7/` (or next available number).
	 - Add `README.md` inside `day_7/` with a 1–3 line summary and list of scripts.
	 - Add scripts named for their purpose (e.g., `preprocessing.py`, `model.py`).

2. To add a dataset:
	 - Put the CSV or data file in `dataset/`.
	 - Name it clearly (e.g., `dataset/sales_2025_q1.csv`).
	 - If large, consider adding a small `dataset/README.md` describing source and license.

Quick start (PowerShell)

From the repository root:

Create & activate virtual environment
```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

Install typical packages used across exercises
```powershell
python -m pip install --upgrade pip;

pip install pandas numpy scikit-learn matplotlib seaborn
```

Run an example script
```powershell
python .\day_1\panda.py
```

Best practices for contributors

- Run scripts from the repo root so relative paths in scripts keep working.
- Add a short `README.md` to new `day_*` folders explaining the exercise and expected outputs.
- Keep scripts reproducible: include dataset path assumptions and any parameter settings at the top of the file.

Notes and further improvements (optional)

- Add a `requirements.txt` with pinned package versions to make installs reproducible.
- Add small per-day notebooks for richer explanations and visual output.
- Optionally add a lightweight `utils/` module to hold shared preprocessing functions used across days.

Contact and license

- This repository is classwork for academic use. Reuse or sharing should give appropriate attribution.
- For questions or to add collaboration details, update this `Readme.md` with a contact email or GitHub handle.
