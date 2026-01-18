from models.mesera import crear_tabla, agregar_mesera, listar_meseras, eliminar_mesera

crear_tabla()  # aseguramos que la tabla exista al iniciar el submenú

def alta_mesera():
    nombre = input("Ingrese nombre de la nueva mesera: ").strip()
    if nombre:
        agregar_mesera(nombre)
    else:
        print("Nombre vacío, no se agregó.\n")

def baja_mesera():
    meseras = listar_meseras()
    if not meseras:
        print("No hay meseras para eliminar.\n")
        return
    print("Meseras actuales:")
    for id_, nombre in meseras:
        print(f"{id_} - {nombre}")
    try:
        op = int(input("ID de mesera para dar de baja: "))
        eliminar_mesera(op)
    except ValueError:
        print("Entrada inválida.\n")
