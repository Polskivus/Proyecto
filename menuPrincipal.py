
opcion = 0
vuelta = 0

while opcion != 4:

    if vuelta == 0:
        print("**************************************")
        print("Bienvenido al menu principal\n")
        print("Teclea la opcion para acceder:\n"
        "1. Piezas"
        "\n2. Pedidos"
        "\n3. Trabajadores"
        "\n4. Salir")

        vuelta += 1

        opcion = int(input("\nInsertar tu opcion: "))

        match opcion:
            
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                print("**************************************")
                print("************Hasta pronto**************")
                print("**************************************")
                
    
    else:
        print("**************************************")
        print("Elija otra opcion\n")
        print("Teclea la opcion para acceder:\n"
        "1. Piezas"
        "\n2. Pedidos"
        "\n3. Trabajadores"
        "\n4. Salir")

        opcion = int(input("\nInsertar tu opcion: "))
        
        match opcion:
            
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                print("**************************************")
                print("************Hasta pronto**************")
                print("**************************************")
