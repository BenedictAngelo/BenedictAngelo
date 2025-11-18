# analyzer.py (fixed)
import sqlite3
from datetime import datetime, time

DB = "data.db"
OUTPUT_TXT = "suspicious.txt"
OUTPUT_SQL = "suspicious.sql"

# define working hours (inclusive)
WORK_START = time(9, 0, 0)
WORK_END   = time(18, 0, 0)

def is_outside_working_hours(ts_str):
    # timestamps are stored as "YYYY-MM-DD HH:MM:SS"
    ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
    return not (WORK_START <= ts.time() <= WORK_END)

def escape_sql(val):
    """Escape single quotes for SQL INSERT generation (very simple)."""
    if val is None:
        return ""
    return str(val).replace("'", "''")

def analyze():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    # find failed attempts
    c.execute("SELECT id, name, ip, device, geolocation, status, timestamp FROM logins WHERE status='failed'")
    rows = c.fetchall()

    suspicious = []
    for row in rows:
        id_, name, ip, device, geolocation, status, timestamp = row
        if is_outside_working_hours(timestamp):
            suspicious.append({
                "id": id_,
                "name": name,
                "ip": ip,
                "device": device,
                "geolocation": geolocation,
                "timestamp": timestamp
            })

    conn.close()

    # write report
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        if not suspicious:
            f.write("No suspicious logins found.\n")
        else:
            f.write("Suspicious Login Attempts (Outside Working Hours)\n")
            f.write("-------------------------------------------------\n\n")
            for s in suspicious:
                f.write(f"ID: {s['id']}\n")
                f.write(f"User: {s['name']}\n")
                f.write(f"IP: {s['ip']}\n")
                f.write(f"Device: {s['device']}\n")
                f.write(f"Geo: {s['geolocation']}\n")
                f.write(f"Time: {s['timestamp']}\n")
                f.write("\n")
    print(f"Analysis complete. Output written to {OUTPUT_TXT}")

    # optional: export suspicious rows to SQL file for reference
    if suspicious:
        with open(OUTPUT_SQL, "w", encoding="utf-8") as sfile:
            sfile.write("-- Export of suspicious rows\n")
            for row in suspicious:
                id_ = row["id"]
                name = escape_sql(row["name"])
                ip = escape_sql(row["ip"])
                device = escape_sql(row["device"])
                geo = escape_sql(row["geolocation"])
                ts = escape_sql(row["timestamp"])

                insert_stmt = (
                    "INSERT INTO logins (id, name, ip, device, geolocation, status, timestamp) "
                    f"VALUES ({id_}, '{name}', '{ip}', '{device}', '{geo}', 'failed', '{ts}');\n"
                )
                sfile.write(insert_stmt)
        print(f"Optional SQL export written to {OUTPUT_SQL}")

if __name__ == "__main__":
    analyze()
