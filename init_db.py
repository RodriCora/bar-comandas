import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "db" / "bar.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# ROLES
cur.execute("""
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
""")

# USUARIOS
cur.execute("""
CREATE TABLE IF NOT EXISTS system_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role_id INTEGER NOT NULL,
    active INTEGER DEFAULT 1,
    FOREIGN KEY (role_id) REFERENCES roles(id)
)
""")

# MESAS
cur.execute("""
CREATE TABLE IF NOT EXISTS tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER UNIQUE NOT NULL,
    status TEXT NOT NULL DEFAULT 'libre'
)
""")

# PRODUCTOS
cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    active INTEGER DEFAULT 1
)
""")

# COMANDAS
cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_id INTEGER NOT NULL,
    waitress_id INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'abierta',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (table_id) REFERENCES tables(id),
    FOREIGN KEY (waitress_id) REFERENCES system_user(id)
)
""")

# ITEMS
cur.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    status TEXT NOT NULL DEFAULT 'pendiente',
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

# PAGOS
cur.execute("""
CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_id INTEGER NOT NULL,
    total REAL NOT NULL,
    method TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    cashier_id INTEGER NOT NULL,
    FOREIGN KEY (table_id) REFERENCES tables(id),
    FOREIGN KEY (cashier_id) REFERENCES system_user(id)
)
""")

conn.commit()
conn.close()

print("✅ Base de datos inicializada correctamente")
