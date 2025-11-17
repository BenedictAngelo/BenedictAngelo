# generate_db.py
import sqlite3
from datetime import datetime

DB = "data.db"

# sample dataset: 5 people with device and geolocation
# Note: one of the failed attempts is outside working hours (suspicious)
data = [
    # name, ip, device, geolocation (city,country), status, timestamp
    ("Alice Rivera",   "192.168.1.10",  "Laptop-Ubuntu",   "Abu Dhabi, UAE",     "success", "2025-11-14 10:15:00"),
    ("Bob Santos",     "10.0.0.15",     "Android-Phone",   "Lisbon, Portugal",   "failed",  "2025-11-14 21:03:00"),  # suspicious (outside hours)
    ("Charlie Cruz",   "172.16.5.22",   "Workstation-PC",  "Madrid, Spain",      "success", "2025-11-14 11:48:00"),
    ("Diana Lopez",    "192.168.1.55",  "MacBook-Pro",     "Seville, Spain",     "failed",  "2025-11-14 14:20:00"),
    ("Evan Morales",   "192.0.2.89",    "Surface-Pro",     "Barcelona, Spain",   "success", "2025-11-14 16:55:00"),
]

def create_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    # drop table if exists to be repeatable
    c.execute("DROP TABLE IF EXISTS logins;")
    c.execute("""
    CREATE TABLE logins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ip TEXT NOT NULL,
        device TEXT,
        geolocation TEXT,
        status TEXT CHECK(status IN ('success','failed')) NOT NULL,
        timestamp TEXT NOT NULL
    );
    """)
    c.executemany(
        "INSERT INTO logins (name, ip, device, geolocation, status, timestamp) VALUES (?, ?, ?, ?, ?, ?);",
        data
    )
    conn.commit()
    conn.close()
    print(f"Database '{DB}' created and populated with sample data.")

if __name__ == "__main__":
    create_db()



