import sqlite3
from pathlib import Path

# Ajustá la ruta a tu base de datos
DB_PATH = Path(__file__).parent / "db" / "bar.db"

def actualizar_status():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Actualiza 'disponible' a 'libre'
    cursor.execute("UPDATE tables SET status = 'libre' WHERE status = 'disponible';")
    
    conn.commit()
    conn.close()
    print("Estados actualizados correctamente.")

if __name__ == "__main__":
    actualizar_status()
