import sqlite3

DB_NAME = "app.db"

def crear_tabla():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mesas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER UNIQUE NOT NULL,
        estado TEXT NOT NULL DEFAULT 'disponible'
    )
    """)
    conn.commit()
    conn.close()

def agregar_mesa(numero):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO mesas (numero) VALUES (?)", (numero,))
        conn.commit()
        print(f"Mesa número {numero} agregada con éxito.")
    except sqlite3.IntegrityError:
        print("Error: ya existe una mesa con ese número.")
    finally:
        conn.close()

def listar_mesas():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, numero, estado FROM mesas")
    mesas = cursor.fetchall()
    conn.close()
    return mesas

def eliminar_mesa(id_mesa):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mesas WHERE id = ?", (id_mesa,))
    conn.commit()
    cambios = cursor.rowcount
    conn.close()
    if cambios:
        print("Mesa eliminada con éxito.")
    else:
        print("No se encontró mesa con ese ID.")

def cambiar_estado_mesa(id_mesa, nuevo_estado):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE mesas SET estado = ? WHERE id = ?", (nuevo_estado, id_mesa))
    conn.commit()
    cambios = cursor.rowcount
    conn.close()
    if cambios:
        print(f"Estado de mesa actualizado a '{nuevo_estado}'.")
    else:
        print("No se encontró mesa con ese ID.")
