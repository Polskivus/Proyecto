# PARTE AIMAR 
# empleados.py
import pandas as pd
from piezasdb import conectar_db
import sys
import os

def resource_path(relative_path):
    """
    Devuelve la ruta absoluta al recurso, funcionando también cuando se empaqueta con PyInstaller.
    """
    try:
        # Carpeta temporal creada por PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # Cuando ejecutamos en Python normal
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

DB_PATH = resource_path("Datos/baseDatosFabrica.db")
RUTA_FICHERO = resource_path("Datos/empleados.csv")


def cargar_empleados():
    """Lee empleados.csv con Pandas y devuelve DataFrame."""
    try:
        df = pd.read_csv(RUTA_FICHERO, sep=",", encoding="utf-8")
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["dni_empleado", "nombre", "edad", "puesto"])


def guardar_empleados(df):
    """Guarda DataFrame en la base de datos."""
    conn = conectar_db()
    df.to_sql("empleados", conn, if_exists="replace", index=False)
    conn.close()


def buscar_empleado_por_dni(df, dni_buscar):
    """Devuelve fila del DataFrame o None."""
    fila = df[df["dni_empleado"] == dni_buscar]
    if not fila.empty:
        return fila.iloc[0]
    return None


def mostrar_empleado(fila):
    """Imprime datos de un empleado."""
    if fila is None:
        print("Empleado no encontrado")
    else:
        print("----- EMPLEADO -----")
        print(f"DNI: {fila['dni_empleado']}")
        print(f"Nombre: {fila['nombre']}")
        print(f"Edad: {fila['edad']}")
        print(f"Puesto: {fila['puesto']}")
        print("--------------------")


def listar_empleados(df):
    """Muestra DataFrame con Pandas."""
    if df.empty:
        print("No hay empleados registrados")
        return
    print(df)


def agregar_empleado(df):
    """Añade fila nueva al DataFrame."""
    print("== Añadir empleado ==")
    dni = input("DNI: ")

    while dni in df["dni_empleado"].values:
        print("Ya existe un empleado con ese DNI")
        dni = input("Introduce otro DNI: ")

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    puesto = input("Puesto: ")

    nuevo_empleado = pd.DataFrame({
        "dni_empleado": [dni],
        "nombre": [nombre],
        "edad": [edad],
        "puesto": [puesto]
    })

    df = pd.concat([df, nuevo_empleado], ignore_index=True)
    df.to_csv(RUTA_FICHERO, index=False)
    return df


def editar_empleado(df):
    """Edita fila en DataFrame."""
    print("== Editar empleado ==")
    dni_editar = input("DNI del empleado a editar: ")

    fila = df[df["dni_empleado"] == dni_editar]
    while fila.empty:
        print("Empleado no encontrado")
        dni_editar = input("DNI del empleado a editar: ")
        fila = df[df["dni_empleado"] == dni_editar]

    print("Pulsa Enter para dejar el valor actual")
    nuevo_nombre = input(f"Nombre ({fila['nombre'].iloc[0]}): ") or fila['nombre'].iloc[0]
    nuevo_edad = input(f"Edad ({fila['edad'].iloc[0]}): ") or fila['edad'].iloc[0]
    nuevo_puesto = input(f"Puesto ({fila['puesto'].iloc[0]}): ") or fila['puesto'].iloc[0]

    df.loc[df["dni_empleado"] == dni_editar, "nombre"] = nuevo_nombre
    df.loc[df["dni_empleado"] == dni_editar, "edad"] = int(nuevo_edad)
    df.loc[df["dni_empleado"] == dni_editar, "puesto"] = nuevo_puesto

    df.to_csv(RUTA_FICHERO,index=False)

def eliminar_empleado(df):
    """Elimina fila del DataFrame y guarda cambios en el CSV."""
    print("== Eliminar empleado ==")
    dni_eliminar = input("DNI del empleado a eliminar: ")

    # Verificar si el empleado existe
    while dni_eliminar not in df["dni_empleado"].values:
        print("Empleado no encontrado")
        dni_eliminar = input("DNI del empleado a eliminar: ")

    # Eliminar empleado
    df = df[df["dni_empleado"] != dni_eliminar]

    # Guardar cambios automáticamente en el CSV
    df.to_csv(RUTA_FICHERO, index=False)
    print(f"Empleado con DNI {dni_eliminar} eliminado y guardado correctamente.")

    return df


"""
def eliminar_empleado(df):
    Elimina fila del DataFrame.
    print("== Eliminar empleado ==")
    dni_eliminar = input("DNI del empleado a eliminar: ")
    df = df[df["dni_empleado"] != dni_eliminar]
def menu():
    df = cargar_empleados()
    
    while True:
        print("\n===== GESTIÓN DE EMPLEADOS =====")
        print("1. Listar empleados")
        print("2. Ver empleado por ID")
        print("3. Añadir empleado")
        print("4. Editar empleado")
        print("5. Eliminar empleado")
        print("6. Guardar y salir")

        opcion = input("Opción: ")

        if opcion == "1":
            listar_empleados(df)
        elif opcion == "2":
            id_buscar = int(input("ID empleado: "))
            emp = buscar_empleado_por_id(df, id_buscar)
            mostrar_empleado(emp)
        elif opcion == "3":
            df = agregar_empleado(df)
        elif opcion == "4":
            df = editar_empleado(df)
        elif opcion == "5":
            df = eliminar_empleado(df)
        elif opcion == "6":
            guardar_empleados(df)

            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()

"""