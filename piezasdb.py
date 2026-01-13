#Importamos lo necesario para trabajar en CSV y SQL
import sqlite3
import pandas as pd

DB_PATH = "Datos/piezas.db"
CSV_PATH = "Datos/piezas.csv"

def conectar_db():
    return sqlite3.connect(DB_PATH)

def crear_tabla():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS piezas_coche (
            id_pieza INTEGER PRIMARY KEY,
            nombre_pieza TEXT NOT NULL,
            qty INTEGER NOT NULL
        )
    """)

    cursor.close()
    conn.commit()
    conn.close()

def cargar_csv_a_db():
    conn = conectar_db()
    df = pd.read_csv(CSV_PATH)
    df.to_sql("piezas_coche", conn, if_exists="replace", index=False)
    conn.close()

def insertar_piezas(nombre, qty):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(id_pieza) FROM piezas_coche")
    ultimo_id = cursor.fetchone()[0]
    nuevo_id = ultimo_id + 1

    cursor.execute("""
        INSERT INTO piezas_coche (id_pieza, nombre_pieza, qty)
        VALUES (?, ?, ?)
    """, (nuevo_id, nombre, qty))

    df = pd.read_sql("SELECT * FROM piezas_coche", conn)
    df.to_csv(CSV_PATH, index=False)

    cursor.close()
    conn.commit()
    conn.close()

def mostrar_piezas():
    conn = conectar_db()
    df = pd.read_sql("SELECT * FROM piezas_coche", conn)
    conn.close()
    return df

"""

Esta es la version original, para mirar cosas

import sqlite3
import pandas as pd

# Leer CSV
def leer_csv():
    return pd.read_csv('Datos/piezas.csv')

df = leer_csv()

def conectar_db():
    return sqlite3.connect('Datos/piezas.db')

# Conectar a SQLite
# conn = sqlite3.connect('Datos/piezas.db')
cursor = conn.cursor()


# Crear tabla si no existe
def crear_table_piezas(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS piezas_coche (
            id_pieza INTEGER PRIMARY KEY,
            nombre_pieza TEXT NOT NULL,
            qty INTEGER NOT NULL
        )
        ''')
    conn.commit()



# Volcar CSV a SQLite (reemplaza tabla)
df.to_sql(
    'piezas_coche',
    conn,
    if_exists='replace',
    index=False
)

# Pedir datos nuevos

cursor.execute("SELECT MAX(id_pieza) FROM piezas_coche")

ultimo_id = cursor.fetchone()[0]

nuevo_id = int(ultimo_id) + 1
nombre = input("Introduce el nombre de pieza: ")
qty = int(input("Introduce la cantidad: "))

# Insertar fila nueva en SQLite
cursor.execute('''
INSERT INTO piezas_coche (id_pieza,nombre_pieza, qty)
VALUES (?, ?, ?)
''', (nuevo_id,nombre, qty))

conn.commit()

def mostrarDB(conn):
    return pd.read_sql('SELECT * FROM piezas_coches', conn)





"""