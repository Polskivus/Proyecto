#Importamos lo necesario para trabajar en CSV y SQL
#Para hacer, ver la manera de hacer todo con el pandas, y solo cuando le des a salir, que coja todo la info y actualize el SQL (HECHO👌)
import sqlite3
import pandas as pd

DB_PATH = "Datos/baseDatosFabrica.db"
CSV_PATH = "Datos/piezas.csv"

#Funciona para conectarse a la base de datos
def conectar_db():
    return sqlite3.connect(DB_PATH)

#Función para insertar piezas en el CSV
def insert_piezas(nombre_pieza, qty):
    df = pd.read_csv(CSV_PATH)
    nuevo_id = df["id_pieza"].max() + 1

    df.loc[len(df)] = [nuevo_id, nombre_pieza, qty]
    df.to_csv(CSV_PATH, index=False)

#Lee el archivo csv para poder mostrar la tabla completa con todos los datos de las piezas
def mostrar_piezas():
    df = pd.read_csv(CSV_PATH)
    return df

#Con esta función buscas el id de la piezas y te permite editar, el nombre y la cantidad
def buscar_por_id(id_pieza):#Echo
    df = pd.read_csv(CSV_PATH)
    opcion_cantidad = " "

    while True:
        #Busco si el id esta dentro de los id del CSV
        if id_pieza not in df["id_pieza"].values:
            print(f"ID {id_pieza} no encontrado.")
            id_pieza = int(input("Dame otro ID: "))
        else: 
            print(f"ID {id_pieza} encontrado.\n")
            #Aqui paso a la fila, la linea del df, que coincide con el id de buqueda
            fila = df.loc[df["id_pieza"] == id_pieza].iloc[0]

            nuevo_nombre = input(f"Para editar introduce el nuevo nombre, si no solo dale al enter\nNOMBRE ACTUAL: {fila["nombre_pieza"]} -> ")

            if nuevo_nombre == "":
                pass

            else:
                fila["nombre_pieza"] = nuevo_nombre

                df.loc[fila.name, ["nombre_pieza"]] = fila[["nombre_pieza"]]
                df.to_csv(CSV_PATH, index=False)

            while opcion_cantidad not in ("s","n"):

                opcion_cantidad = input("Quieres cambiar la cantida de piezas. (s/n)").lower()

                if opcion_cantidad == "s":
                    
                    nuevas_cantidad = int(input(f"Dame la nueva cantidad de piezas.\nNUMERO ACTUAL: {fila["qty"]} -> "))
                    df.loc[fila.name, ["qty"]] = nuevas_cantidad
                    df.to_csv(CSV_PATH, index=False)

                elif opcion_cantidad == "n":
                    break
                else:
                    print("Opcion no valida.")
             
            break

    return print("\nTransacción completada")

def eliminar_piezas(id_pieza_a_eliminar):
    df = pd.read_csv(CSV_PATH)

    if id_pieza_a_eliminar not in df["id_pieza"].values:
        print(f"ID {id_pieza} no encontrado.")
        id_pieza = int(input("Dame otro ID: "))
    else:
        df_eliminado = df[df["id_pieza"] != id_pieza_a_eliminar]
        df_eliminado.to_csv(CSV_PATH, index=False)
        print(f"Pieza con el id {id_pieza_a_eliminar}, Eliminado.")

def cargar_csv_a_db():
    conn = conectar_db()
    df = pd.read_csv(CSV_PATH)
    df.to_sql("piezas_coche", conn, if_exists="replace", index=False)
    conn.close()