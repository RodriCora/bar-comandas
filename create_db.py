import sqlite3
from pathlib import Path

# Definimos la ruta a 'db/bar.db' dentro de la carpeta actual (bar-comandas)
DB_DIR = Path(__file__).parent / "db"
DB_PATH = DB_DIR / "bar.db"

def create_db():
    # Creamos la carpeta db si no existe
    DB_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Crear tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS system_user (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    """)

    # Insertar usuario ejemplo
    cursor.execute("""
        INSERT OR REPLACE INTO system_user (username, password_hash)
        VALUES (?, ?)
    """, ("bar", "1234"))

    conn.commit()
    conn.close()
    print(f"Base de datos y usuario creados en {DB_PATH}!")

if __name__ == "__main__":
    create_db()
