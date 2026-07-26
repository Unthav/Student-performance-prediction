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

Features

✔ Predict Exam Score,
✔ Prediction History,
✔ Machine Learning Model,
✔ Flask Web Application,
✔ SQLite Database,
✔ Responsive UI

Machine Learning
Linear Regression,
Random Forest Regression,
Decision Tree Regression,
XGBoost Regressor

Dataset

Student Performance Prediction Dataset

Tech Stack

Python,
Flask,
Pandas,
numpy,
Scikit-learn,
joblib,
SQLite,
HTML,
CSS,
JavaScript

Installation

git clone ...

pip install -r requirements.txt

python app.py

Future Improvements

User Login
Charts
Export PDF
REST API

