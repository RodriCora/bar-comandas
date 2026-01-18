from models.mesa import crear_tabla as crear_tabla_mesas, agregar_mesa, listar_mesas, eliminar_mesa, cambiar_estado_mesa
from menus.submenus.supervisor_mesera import alta_mesera, baja_mesera
# Creamos la tabla si no existe (esto corre al importar el módulo)
crear_tabla_mesas()

def alta_mesa():
    try:
        numero = int(input("Ingrese número de la nueva mesa: "))
        agregar_mesa(numero)
    except ValueError:
        print("Número inválido.\n")

def baja_mesa():
    mesas = listar_mesas()
    if not mesas:
        print("No hay mesas para eliminar.\n")
        return
    print("Mesas actuales:")
    for id_, numero, estado in mesas:
        print(f"{id_} - Mesa {numero} (Estado: {estado})")
    try:
        op = int(input("ID de mesa para dar de baja: "))
        eliminar_mesa(op)
    except ValueError:
        print("Entrada inválida.\n")

def cambiar_estado():
    mesas = listar_mesas()
    if not mesas:
        print("No hay mesas para modificar.\n")
        return
    print("Mesas actuales:")
    for id_, numero, estado in mesas:
        print(f"{id_} - Mesa {numero} (Estado: {estado})")
    try:
        id_mesa = int(input("ID de mesa a modificar: "))
        nuevo_estado = input("Nuevo estado (disponible/ocupada/reservada): ").strip().lower()
        if nuevo_estado not in ("disponible", "ocupada", "reservada"):
            print("Estado inválido.\n")
            return
        cambiar_estado_mesa(id_mesa, nuevo_estado)
    except ValueError:
        print("Entrada inválida.\n")

def gestion_mesas():
    while True:
        print("\n--- Gestión de Mesas ---")
        print("1 - Alta mesa")
        print("2 - Baja mesa")
        print("3 - Cambiar estado mesa")
        print("0 - Volver")
        choice = input("Elegí una opción: ")
        if choice == "1":
            alta_mesa()
        elif choice == "2":
            baja_mesa()
        elif choice == "3":
            cambiar_estado()
        elif choice == "0":
            break
        else:
            print("❌ Opción inválida")

def submenu_supervisor():
    while True:
        print("\n--- MENÚ SUPERVISOR ---")
        print("1 - Alta mesera")
        print("2 - Baja mesera")
        print("3 - Gestión mesas")
        print("0 - Volver")
        choice = input("Elegí una opción: ")
        if choice == "1":
            alta_mesera()
        elif choice == "2":
            baja_mesera()
        elif choice == "3":
            gestion_mesas()
        elif choice == "0":
            break
        else:
            print("❌ Opción inválida")