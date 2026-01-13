from piezasdb import (
    crear_tabla,
    cargar_csv_a_db,
    insertar_piezas,
    mostrar_piezas
)

def menu():
    crear_tabla()
    cargar_csv_a_db()

    while True:
        print("\n******** MENU PRINCIPAL ********")
        print("1. Ver piezas")
        print("2. Añadir pieza")
        print("3. Trabajadores")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                df = mostrar_piezas()
                print(df)

            case "2":
                nombre = input("Nombre de la pieza: ")
                qty = int(input("Cantidad: "))
                insertar_piezas(nombre, qty)
                print("Pieza añadida correctamente")

            case "3":
                print("Módulo trabajadores (pendiente)")

            case "4":
                print("Hasta pronto")
                break

            case _:
                print("Opción no válida")

if __name__ == "__main__":
    menu()