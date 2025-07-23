import sqlite3

DB_PATH = "patient_reports.db"

def save_patient_report(patient_id: str, diagnosis: str, risk: str, recommendations: str, pdf_summary: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id TEXT,
                diagnosis TEXT,
                risk_prediction TEXT,
                recommendations TEXT,
                pdf_summary TEXT
            )
        """)

        cursor.execute("""
            INSERT INTO reports (patient_id, diagnosis, risk_prediction, recommendations, pdf_summary)
            VALUES (?, ?, ?, ?, ?)
        """, (patient_id, diagnosis, risk, recommendations, pdf_summary))

        conn.commit()
        conn.close()
        print(f"[DB] Saved report for Patient ID: {patient_id}")
    except Exception as e:
        print(f"[DB ERROR] Failed to save report: {e}")
