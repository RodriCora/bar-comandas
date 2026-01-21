import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "db" / "bar.db"

def listar_estados():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT number, status FROM tables")
    rows = cursor.fetchall()
    conn.close()
    
    for number, status in rows:
        print(f"Mesa {number}: '{status}' (len={len(status)})")

if __name__ == "__main__":
    listar_estados()
