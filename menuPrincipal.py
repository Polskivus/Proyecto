from piezasdb import (
    cargar_csv_a_db,
    mostrar_piezas,
    insert_piezas,
    buscar_por_id,
    eliminar_piezas
)

def menu():

    while True:
        print("\n******** MENU PRINCIPAL ********")
        print("1. Ver piezas")
        print("2. Añadir pieza")
        print("3. Buscar o editar pieza")
        print("4. Borrar piezas")
        print("5. Trabajadores")
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
                try:
                    prueba = int(input("Dame un id que quieras editar o visualizar: "))
                    buscar_por_id(prueba)
                except:
                    print("Opcion no valida")
            

            case "4":
                try:
                    prueba2 = int(input("Dime el id que quieres borrar: "))
                    eliminar_piezas(prueba2)
                except:
                    print("Opcion no valida")
                

            case "5":
                print("Módulo trabajadores (pendiente)")

                while True:
                    print("\n******** SUBMENU EMPLEADOS ********")
                    print("1. Ver empleados")
                    print("2. Añadir empleado")
                    print("3. Buscar o editar empleado")
                    print("0. Salir")

                    opcion_submenu = input("Selecciona una opción: ")

                    match opcion_submenu:

                        case "1":
                            pass

                        case "2":
                            pass

                        case "3":
                            pass

                        case "0":
                            print("Guardando cambios y volviendo al menu principal")
                            break

                        case _:
                            print("Opción no válida")

            case "0":
                cargar_csv_a_db()
                print("Hasta pronto")
                break
            case _:
                print("Opción no válida")

if __name__ == "__main__":
    menu()