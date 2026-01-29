from piezasdb import (
    cargar_csv_a_db,
    mostrar_piezas,
    insert_piezas,
    buscar_por_id,
    eliminar_piezas
)

from empleadosdb import(
    listar_empleados,
    buscar_empleado_por_dni,
    agregar_empleado,
    cargar_empleados,
    editar_empleado,
    eliminar_empleado,
    mostrar_empleado,
    guardar_empleados
)

def menu():

    while True:
        print("  ______")
        print(" /|_||_\`.__")
        print("(   _    _ _\ ")
        print("=`-(_)--(_)-'")

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
                print("Módulo trabajadores")

                while True:

                    print(str(" ///-\\\ "))
                    print(" |^   ^| ")
                    print(" |O   O| ")
                    print(" |  ~  | ")
                    print("  \ O / ")
                    print("   | | ")

                    print("\n===== GESTIÓN DE EMPLEADOS =====")
                    print("1. Listar empleados")
                    print("2. Ver empleado por DNI")
                    print("3. Añadir empleado")
                    print("4. Editar empleado")
                    print("5. Eliminar empleado")
                    print("0. Guardar y salir")

                    opcion_submenu = input("Selecciona una opción: ")

                    dfe = cargar_empleados()

                    match opcion_submenu:

                        case "1":
                            listar_empleados(dfe)

                        case "2":
                            id_buscar = input("DNI empleado: ")
                            emp = buscar_empleado_por_dni(dfe, id_buscar)
                            mostrar_empleado(emp)

                        case "3":
                            df = agregar_empleado(dfe)

                        case "4":
                            df = editar_empleado(dfe)

                        case "5":
                            df = eliminar_empleado(dfe)

                        case "0":
                            guardar_empleados(dfe)
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