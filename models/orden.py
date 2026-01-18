import sqlite3

def crear_tabla():
    con = sqlite3.connect("bar_comandas.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ordenes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_mesa INTEGER,
            estado TEXT,  -- 'abierta', 'cerrada', 'pagada'
            total REAL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    con.commit()
    con.close()

def crear_orden(id_mesa, total=0.0):
    con = sqlite3.connect("bar_comandas.db")
    cur = con.cursor()
    cur.execute("INSERT INTO ordenes (id_mesa, estado, total) VALUES (?, 'abierta', ?)", (id_mesa, total))
    con.commit()
    con.close()

def cerrar_orden(id_orden, total):
    con = sqlite3.connect("bar_comandas.db")
    cur = con.cursor()
    cur.execute("UPDATE ordenes SET estado='cerrada', total=? WHERE id=?", (total, id_orden))
    con.commit()
    con.close()

def pagar_orden(id_orden):
    con = sqlite3.connect("bar_comandas.db")
    cur = con.cursor()
    cur.execute("UPDATE ordenes SET estado='pagada' WHERE id=?", (id_orden,))
    con.commit()
    con.close()

def listar_ordenes_pendientes():
    con = sqlite3.connect("bar_comandas.db")
    cur = con.cursor()
    cur.execute("SELECT id, id_mesa, estado, total FROM ordenes WHERE estado='cerrada'")
    res = cur.fetchall()
    con.close()
    return res

def obtener_orden_por_id(id_orden):
    con = sqlite3.connect("bar_comandas.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM ordenes WHERE id=?", (id_orden,))
    orden = cur.fetchone()
    con.close()
    return orden
