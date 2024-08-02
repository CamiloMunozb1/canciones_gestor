import sqlite3

def eliminar_cancion():
    try:
        with sqlite3.connect("C:/Users/POWER/canciones_gestor.db") as cancion_eliminar:
            consulta_cursor = cancion_eliminar.cursor()
            usuario_eliminar= str(input("Ingresa el nombre de la cancion a eliminar: "))
            consulta_cursor.execute("DELETE FROM Canciones WHERE Nombre_cancion = ?", (usuario_eliminar,))
            cancion_eliminar.commit()
            print("Cancion eliminada correctamente.")
    except ValueError:
        print("Error de digitiacion, intentar de nuevo.")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error}")