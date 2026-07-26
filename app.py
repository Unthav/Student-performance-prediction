import pandas as pd
import joblib
from flask import Flask, request, render_template
from database import db
 
app = Flask(__name__)
db.init_db()
 
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")
columns = joblib.load("columns.pkl")

SLIDERS = {
    "Hours_Studied": ("Hours Studied (per week)", 1, 44, 20),
    "Attendance": ("Attendance (%)", 60, 100, 80),
    "Previous_Scores": ("Previous Scores", 50, 100, 70),
    "Tutoring_Sessions": ("Tutoring Sessions (per month)", 0, 8, 1),
    "Sleep_Hours": ("Sleep Hours (per night)", 4, 10, 7),
    "Physical_Activity": ("Physical Activity (hrs/week)", 0, 6, 3),
}

DROPDOWNS = [
    "Parental_Involvement", "Family_Income", "Teacher_Quality",
    "School_Type", "Parental_Education_Level", "Distance_from_Home",
    "Motivation_Level",
]

RADIOS = ["Extracurricular_Activities", "Internet_Access", "Learning_Disabilities", "Gender"]
 
NUMERIC = list(SLIDERS.keys())
 
 
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        data: dict = {c: float(request.form[c]) for c in NUMERIC}
        data.update({c: request.form[c] for c in DROPDOWNS + RADIOS})
 
        row = pd.DataFrame([data])[columns]
        for col, le in encoders.items():
            row[col] = le.transform(row[col])
 
        prediction = round(float(model.predict(row)[0]), 2)
        db.save_prediction(data, prediction)
 
    return render_template(
        "index.html",
        sliders=SLIDERS,
        dropdowns={f: encoders[f].classes_ for f in DROPDOWNS},
        radios={f: encoders[f].classes_ for f in RADIOS},
        prediction=prediction,
    )
 
 
@app.route("/history")
def history():
    rows = db.get_all_predictions()
    return render_template("history.html", rows=rows, fields=db.FIELDS)
 
 
if __name__ == "__main__":
    app.run(debug=True, port=5000)