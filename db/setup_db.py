import sqlite3
from pathlib import Path

# Ruta de la base de datos
DB_PATH = Path(__file__).parent / "bar.db"

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ---------- LOGIN GENERAL ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS system_user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)

    # ---------- ROLES ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)

    # ---------- USUARIOS INTERNOS ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role_id INTEGER NOT NULL,
        active INTEGER DEFAULT 1,
        FOREIGN KEY (role_id) REFERENCES roles(id)
    )
    """)

    # ---------- MESAS ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number INTEGER UNIQUE NOT NULL,
        active INTEGER DEFAULT 1
    )
    """)

    # ---------- PEDIDOS / COMANDAS ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_id INTEGER NOT NULL,
        waiter_id INTEGER NOT NULL,
        status TEXT NOT NULL, -- abierta / enviada / cerrada
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (table_id) REFERENCES tables(id),
        FOREIGN KEY (waiter_id) REFERENCES staff(id)
    )
    """)

    # ---------- ITEMS DEL PEDIDO ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        item_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        kitchen_status TEXT DEFAULT 'pendiente', -- pendiente / preparando / listo
        FOREIGN KEY (order_id) REFERENCES orders(id)
    )
    """)

    conn.commit()
    conn.close()

def insert_initial_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Roles
    roles = ["caja", "supervisor", "mesera", "cocina"]
    for role in roles:
        cursor.execute("INSERT OR IGNORE INTO roles (name) VALUES (?)", (role,))

    # Usuario general (password ficticia por ahora)
    cursor.execute("""
    INSERT OR IGNORE INTO system_user (username, password_hash)
    VALUES ('admin', 'hash_demo')
    """)

    # Crear 50 mesas
    for i in range(1, 51):
        cursor.execute("INSERT OR IGNORE INTO tables (number) VALUES (?)", (i,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    insert_initial_data()
    print("Base de datos creada correctamente.")
