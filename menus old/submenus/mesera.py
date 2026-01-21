# menus/submenus/mesera.py

mesas_asignadas = [1, 3, 5]

def tomar_pedido():
    mesa = input("Número de mesa para tomar pedido: ")
    pedido = input("Detalle del pedido: ")
    print(f"Pedido para mesa {mesa} registrado: {pedido}\n")

def ver_mesas_asignadas():
    print("Mesas asignadas:")
    for m in mesas_asignadas:
        print(f"- Mesa {m}")
    print()

def submenu_mesera():
    while True:
        print("\n--- MENÚ MESERA ---")
        print("1 - Tomar pedido")
        print("2 - Ver mesas asignadas")
        print("0 - Volver")
        choice = input("Elegí una opción: ")
        if choice == "1":
            tomar_pedido()
        elif choice == "2":
            ver_mesas_asignadas()
        elif choice == "0":
            break
        else:
            print("❌ Opción inválida")
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
