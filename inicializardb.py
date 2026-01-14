#Este programa se utiliza para inicializar la base de datos, la idea es solo ejecutarlo una vez cuando la base de datos este disponible
import sqlite3


def crear_tablas():
    conn = sqlite3.connect("Datos/baseDatosFabrica.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS piezas_coche (
            id_pieza INTEGER PRIMARY KEY,
            nombre_pieza TEXT NOT NULL,
            qty INTEGER NOT NULL
        )
    """)

    conn.commit()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id_empleado INTEGER PRIMARY KEY,
                edad INTEGER NOT NULL,
                nombre TEXT NOT NULL,
                puesto TEXT NOT NULL           
           )
    """)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    crear_tablas()