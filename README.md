# Student Performance Prediction

A Flask web app that predicts a student's exam score from study habits,
attendance, family background, and other factors, using a trained
XGBoost regression model. Predictions are logged to a local SQLite
database and viewable on a history page.

## Project structure

```
Student_Performance_Prediction/
├── app.py                     # Flask app (routes: / and /history)
├── model.pkl                  # Trained XGBRegressor model
├── encoders.pkl               # Dict of sklearn LabelEncoders for categorical fields
├── columns.pkl                # Exact column order expected by the model
├── requirements.txt
├── database/
│   ├── __init__.py            # Makes this a proper Python package
│   └── db.py                  # SQLite helpers (init_db, save_prediction, get_all_predictions)
├── dataset/
│   └── Student_Performance_Prediction.csv   # Training data
├── notebook/
│   └── student_performance_prediction.ipynb # EDA + model training notebook
├── templates/
│   ├── index.html             # Prediction form
│   └── history.html           # Prediction history table
└── screenshots/               # App screenshots used in docs
```

## What was fixed

The zip as provided would not run because of a broken module reference:

- **`app.py` had `import db`**, but `db.py` actually lives inside the
  `database/` subfolder. Python couldn't find a top-level `db` module, so
  the app crashed on startup with `ModuleNotFoundError: No module named 'db'`.
  - Fixed by changing the import to `from database import db`.
  - Added `database/__init__.py` so `database/` is recognized as a proper
    Python package (required for the import to work reliably in all
    environments).
- **`model.pkl` requires `xgboost`** to unpickle (the model is an
  `XGBRegressor`), which was missing from the project — there was no
  `requirements.txt` at all. Added one below with the exact versions the
  app was verified against.
- Verified end-to-end after the fix: app boots, `/` renders and accepts a
  POST, a prediction is returned, and a row is written to the SQLite
  history that `/history` displays correctly.

## Setup

```bash
cd Student_Performance_Prediction
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Then open **http://127.0.0.1:5000/** in your browser.

- The home page lets you set study/lifestyle inputs (sliders, dropdowns,
  radio buttons) and returns a predicted exam score.
- Every prediction is saved to `predictions.db` (created automatically on
  first run) and can be reviewed at **http://127.0.0.1:5000/history**.

## Notes

- `predictions.db` is created in the working directory the first time you
  run the app — it's local application state, not source, so you may want
  to add it (and `venv/`, `__pycache__/`) to a `.gitignore` if you version
  this project with git.
- You may see a harmless `InconsistentVersionWarning` / xgboost
  serialization warning on load if your installed `scikit-learn`/`xgboost`
  versions differ slightly from the ones the models were trained with.
  This doesn't affect prediction correctness in testing, but if you
  retrain the model, re-export it with the versions pinned in
  `requirements.txt` to avoid the warning.
- The training/EDA process (including the model comparison and plots in
  `screenshots/`) is documented in
  `notebook/student_performance_prediction.ipynb`.
