import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "db" / "bar.db"

def add_status_column():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("ALTER TABLE tables ADD COLUMN status TEXT DEFAULT 'disponible'")
        print("Columna 'status' agregada correctamente.")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("La columna 'status' ya existe, no se agrega.")
        else:
            raise e
    finally:
        conn.commit()
        conn.close()

if __name__ == "__main__":
    add_status_column()
