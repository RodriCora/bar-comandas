import sqlite3
from pathlib import Path
import getpass

DB_PATH = Path(__file__).resolve().parents[1] / "db" / "bar.db"

def login():
    print("=== LOGIN DEL SISTEMA ===")

    username = input("Usuario: ")
    password = getpass.getpass("Contraseña: ")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password_hash FROM system_user WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    conn.close()

    if not result:
        print("❌ Usuario no encontrado")
        return False

    stored_password = result[0]

    # ⚠️ Comparación simple (después se mejora)
    if password == stored_password:
        print("✅ Acceso concedido\n")
        return True
    else:
        print("❌ Contraseña incorrecta")
        return False
