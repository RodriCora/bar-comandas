import sqlite3

DB_NAME = "app.db"

def crear_tabla():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meseras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE
    )
    """)
    conn.commit()
    conn.close()

def agregar_mesera(nombre):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO meseras (nombre) VALUES (?)", (nombre,))
        conn.commit()
        print(f"Mesera '{nombre}' agregada con éxito.")
    except sqlite3.IntegrityError:
        print("Error: ya existe una mesera con ese nombre.")
    finally:
        conn.close()

def listar_meseras():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM meseras")
    meseras = cursor.fetchall()
    conn.close()
    return meseras

def eliminar_mesera(id_mesera):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM meseras WHERE id = ?", (id_mesera,))
    conn.commit()
    cambios = cursor.rowcount
    conn.close()
    if cambios:
        print("Mesera eliminada con éxito.")
    else:
        print("No se encontró mesera con ese ID.")
