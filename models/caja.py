import sqlite3

def crear_tabla():
    con = sqlite3.connect("bar_comandas.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS caja (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,       -- 'ingreso' o 'egreso'
            monto REAL NOT NULL,
            descripcion TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    con.commit()
    con.close()

def registrar_movimiento(tipo, monto, descripcion=""):
    con = sqlite3.connect("bar_comandas.db")
    cur = con.cursor()
    cur.execute("INSERT INTO caja (tipo, monto, descripcion) VALUES (?, ?, ?)", (tipo, monto, descripcion))
    con.commit()
    con.close()

def obtener_saldo_actual():
    con = sqlite3.connect("bar_comandas.db")
    cur = con.cursor()
    cur.execute("""
        SELECT
            (SELECT IFNULL(SUM(monto),0) FROM caja WHERE tipo='ingreso') -
            (SELECT IFNULL(SUM(monto),0) FROM caja WHERE tipo='egreso')
    """)
    saldo = cur.fetchone()[0]
    con.close()
    return saldo

def listar_movimientos():
    con = sqlite3.connect("bar_comandas.db")
    cur = con.cursor()
    cur.execute("SELECT id, tipo, monto, descripcion, fecha FROM caja ORDER BY fecha DESC")
    filas = cur.fetchall()
    con.close()
    return filas
