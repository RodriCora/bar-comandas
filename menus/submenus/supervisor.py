from menus.submenus.supervisor_mesera import alta_mesera, baja_mesera
from menus.submenus.supervisor_mesas import gestion_mesas

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
