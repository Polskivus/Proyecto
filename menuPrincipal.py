from piezasdb import (
    cargar_csv_a_db,
    mostrar_piezas,
    insert_piezas
)

def menu():

    while True:
        print("\n******** MENU PRINCIPAL ********")
        print("1. Ver piezas")
        print("2. Añadir pieza")
        print("3. Buscar pieza")
        print("4. Trabajadores")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                df = mostrar_piezas()
                print(df)

            case "2":
                nombre = input("Nombre de la pieza: ")
                qty = int(input("Cantidad: "))
                insert_piezas(nombre, qty)
                print("Pieza añadida correctamente")

            case "3":
                pass

            case "4":
                print("Módulo trabajadores (pendiente)")

            case "0":
                cargar_csv_a_db()
                print("Hasta pronto")
                break
            case _:
                print("Opción no válida")

if __name__ == "__main__":
    menu()