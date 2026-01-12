import sqlite3

conn = sqlite3.connect('Datos/piezas.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM piezas_coche")
print(cursor.fetchall())