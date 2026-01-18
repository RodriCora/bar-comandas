from menus.submenus.caja import submenu_caja
from menus.submenus.supervisor import submenu_supervisor
from menus.submenus.mesera import submenu_mesera
from menus.submenus.cocina import submenu_cocina
from menus.submenus.supervisor_mesera import alta_mesera, baja_mesera
from menus.submenus.supervisor_mesas import gestion_mesas  # fijate que el archivo sea supervisor_mesa.py

def login_role(user_db, role_name):
    print(f"\n🔐 Login {role_name}")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    if username in user_db and user_db[username] == password:
        print(f"✅ Bienvenido {username}!")
        return True
    else:
        print("❌ Usuario o contraseña incorrecta")
        return False

def choose_name(role_list, role_name):
    print(f"\n👩‍💼 Seleccioná {role_name}:")
    for i, name in enumerate(role_list, 1):
        print(f"{i} - {name}")
    try:
        option = int(input("Opción: "))
        if 1 <= option <= len(role_list):
            print(f"✅ Entraste como {role_list[option-1]}")
            return True
        else:
            print("❌ Opción inválida")
            return False
    except ValueError:
        print("❌ Opción inválida")
        return False

def main_menu():
    admin_users = {
        "admin": "admin123",
        "caja": "caja123"
    }
    supervisor_users = {
        "jefe": "super123",
        "supervisor": "clave456"
    }

    meseras = ["Ana", "Laura", "Sofía"]
    cocina = ["Pepe", "Marta", "Luis"]

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1 - Caja / Admin")
        print("2 - Supervisor")
        print("3 - Mesera")
        print("4 - Cocina")
        print("0 - Salir")

        option = input("Seleccioná una opción: ")

        if option == "1":
            if login_role(admin_users, "Caja / Admin"):
                submenu_caja()
        elif option == "2":
            if login_role(supervisor_users, "Supervisor"):
                submenu_supervisor()
        elif option == "3":
            if choose_name(meseras, "Mesera"):
                submenu_mesera()
        elif option == "4":
            if choose_name(cocina, "Cocina"):
                submenu_cocina()
        elif option == "0":
            print("👋 Saliendo del sistema")
            break
        else:
            print("❌ Opción inválida")
