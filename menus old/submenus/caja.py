from models.caja import crear_tabla, registrar_movimiento, obtener_saldo_actual, listar_movimientos
from models.orden import listar_ordenes_pendientes, pagar_orden

# Crear tabla de caja al importar módulo
crear_tabla()

def ver_caja():
    saldo = obtener_saldo_actual()
    print(f"\nSaldo actual en caja: ${saldo:.2f}\n")
    movimientos = listar_movimientos()
    if movimientos:
        print("Movimientos recientes:")
        for m in movimientos[:10]:  # últimos 10 movimientos
            print(f"{m[4]} - {m[1].capitalize()}: ${m[2]:.2f} ({m[3]})")
    else:
        print("No hay movimientos registrados.\n")

def cerrar_caja():
    print("\nCerrando caja...")
    saldo = obtener_saldo_actual()
    print(f"Saldo final: ${saldo:.2f}")
    print("¡Caja cerrada correctamente!\n")

def registrar_ingreso():
    try:
        monto = float(input("Monto ingreso: "))
        descripcion = input("Descripción: ")
        registrar_movimiento('ingreso', monto, descripcion)
        print("Ingreso registrado correctamente.\n")
    except ValueError:
        print("Monto inválido.\n")

def registrar_egreso():
    try:
        monto = float(input("Monto egreso: "))
        descripcion = input("Descripción: ")
        registrar_movimiento('egreso', monto, descripcion)
        print("Egreso registrado correctamente.\n")
    except ValueError:
        print("Monto inválido.\n")

def ver_ordenes_pendientes():
    ordenes = listar_ordenes_pendientes()
    if not ordenes:
        print("No hay órdenes pendientes de cobro.\n")
        return
    print("\nÓrdenes cerradas pendientes de cobro:")
    for id_, id_mesa, estado, total in ordenes:
        print(f"ID: {id_} | Mesa: {id_mesa} | Total: ${total:.2f}")

def cobrar_orden():
    try:
        id_orden = int(input("ID de orden para cobrar: "))
        pagar_orden(id_orden)
        # Registrar ingreso automáticamente al cobrar la orden
        # Podés agregar descripción o poner "Cobro orden mesa X"
        registrar_movimiento('ingreso', obtener_total_orden(id_orden), f'Cobro orden ID {id_orden}')
        print("Orden pagada y registrada en caja.\n")
    except ValueError:
        print("ID inválido.\n")

def obtener_total_orden(id_orden):
    # Función para obtener el total de la orden (para registrar en caja)
    # Podés implementar esta función o hacerla en models.orden
    from models.orden import obtener_orden_por_id
    orden = obtener_orden_por_id(id_orden)
    if orden:
        return orden[3]  # asumimos que el total está en la 4ta columna
    return 0.0

def submenu_caja():
    while True:
        print("\n--- MENÚ CAJA / ADMIN ---")
        print("1 - Ver caja")
        print("2 - Registrar ingreso")
        print("3 - Registrar egreso")
        print("4 - Ver órdenes cerradas pendientes")
        print("5 - Cobrar orden")
        print("6 - Cerrar caja")
        print("0 - Volver")
        choice = input("Elegí una opción: ")
        if choice == "1":
            ver_caja()
        elif choice == "2":
            registrar_ingreso()
        elif choice == "3":
            registrar_egreso()
        elif choice == "4":
            ver_ordenes_pendientes()
        elif choice == "5":
            cobrar_orden()
        elif choice == "6":
            cerrar_caja()
        elif choice == "0":
            break
        else:
            print("❌ Opción inválida")
