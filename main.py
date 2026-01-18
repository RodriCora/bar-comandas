from auth.login import login
from menus.main_menu import main_menu

def main():
    if not login():
        return

    print("Bienvenido al sistema del bar")
    main_menu()

if __name__ == "__main__":
    main()
