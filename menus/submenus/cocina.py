# menus/submenus/cocina.py

pedidos_pendientes = [
    {"mesa": 1, "pedido": "Ensalada César"},
    {"mesa": 2, "pedido": "Pizza muzzarella"},
]

def ver_pedidos_pendientes():
    print("\nPedidos pendientes:")
    for i, p in enumerate(pedidos_pendientes, 1):
        print(f"{i} - Mesa {p['mesa']}: {p['pedido']}")
    print()

def marcar_pedido_listo():
    ver_pedidos_pendientes()
    try:
        op = int(input("Número de pedido para marcar como listo: "))
        if 1 <= op <= len(pedidos_pendientes):
            pedido = pedidos_pendientes.pop(op - 1)
            print(f"Pedido de mesa {pedido['mesa']} marcado como listo.\n")
        else:
            print("Opción inválida.\n")
    except ValueError:
        print("Entrada inválida.\n")

def submenu_cocina():
    while True:
        print("\n--- MENÚ COCINA ---")
        print("1 - Ver pedidos pendientes")
        print("2 - Marcar pedido como listo")
        print("0 - Volver")
        choice = input("Elegí una opción: ")
        if choice == "1":
            ver_pedidos_pendientes()
        elif choice == "2":
            marcar_pedido_listo()
        elif choice == "0":
            break
        else:
            print("❌ Opción inválida")
