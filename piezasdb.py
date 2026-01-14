#Importamos lo necesario para trabajar en CSV y SQL
#Para hacer, ver la manera de hacer todo con el pandas, y solo cuando le des a salir, que coja todo la info y actualize el SQL (HECHO👌)
import sqlite3
import pandas as pd

DB_PATH = "Datos/baseDatosFabrica.db"
CSV_PATH = "Datos/piezas.csv"

#Funciona para conectarse a la base de datos
def conectar_db():
    return sqlite3.connect(DB_PATH)

def insert_piezas(nombre_pieza, qty):
    df = pd.read_csv(CSV_PATH)
    nuevo_id = df["id_pieza"].max() + 1

    df.loc[len(df)] = [nuevo_id, nombre_pieza, qty]
    df.to_csv(CSV_PATH, index=False)

#Lee el archivo csv para poder mostrar la tabla completa con todos los datos de las piezas
def mostrar_piezas():
    df = pd.read_csv(CSV_PATH)
    return df

def buscar_por_id():
    pass

def buscar_por_nombre():
    pass

def cargar_csv_a_db():
    conn = conectar_db()
    df = pd.read_csv(CSV_PATH)
    df.to_sql("piezas_coche", conn, if_exists="replace", index=False)
    conn.close()