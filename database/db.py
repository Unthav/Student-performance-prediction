import sqlite3

DB_FILE = "predictions.db"

FIELDS = [
    "Hours_Studied", "Attendance", "Previous_Scores", "Tutoring_Sessions",
    "Sleep_Hours", "Physical_Activity", "Parental_Involvement", "Family_Income",
    "Teacher_Quality", "School_Type", "Parental_Education_Level",
    "Distance_from_Home", "Motivation_Level", "Extracurricular_Activities",
    "Internet_Access", "Learning_Disabilities", "Gender",
]


def init_db():
    conn = sqlite3.connect(DB_FILE)
    columns_sql = ", ".join(f"{f} TEXT" for f in FIELDS)
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {columns_sql},
            predicted_score REAL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def save_prediction(data: dict, predicted_score: float):
    conn = sqlite3.connect(DB_FILE)
    placeholders = ", ".join("?" for _ in FIELDS)
    columns_sql = ", ".join(FIELDS)
    values = [str(data[f]) for f in FIELDS]
    conn.execute(
        f"INSERT INTO predictions ({columns_sql}, predicted_score) VALUES ({placeholders}, ?)",
        values + [predicted_score],
    )
    conn.commit()
    conn.close()


def get_all_predictions():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM predictions ORDER BY id DESC").fetchall()
    conn.close()
    return rows
