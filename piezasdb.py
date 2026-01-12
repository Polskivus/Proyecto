import sqlite3
import pandas as pd

# Leer CSV
df = pd.read_csv('Datos/piezas.txt')
print(df)
# Conectar a SQLite
conn = sqlite3.connect('Datos/piezas.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS piezas_coche (
    id_pieza INTEGER PRIMARY KEY,
    nombre_pieza TEXT NOT NULL,
    qty INTEGER NOT NULL
)
''')

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

# Leer tabla actualizada desde SQLite
df_actualizado = pd.read_sql('SELECT * FROM piezas_coche', conn)
print("\nTabla actualizada en SQLite3:")

df_actualizado.to_csv('Datos/piezas.txt', index=False)

conn.close()

"""
df.to_sql(
    'piezas_coche',
    conn,
    if_exists='append',
    index=False
)

conn = sqlite3.connect('base_de_datos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE piezas_coche (
    id_pieza INTEGER PRIMARY KEY,
    nombre_pieza TEXT,
    qty INTEGER
)''')

df.to_sql('piezas_coche', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print("Datos del txt insertados en SQLite")

"""