
# IMPORTAMOS LA LIBRERIA "SQLITE3" PARA MANEJAR LA BASE DE DATOS

import sqlite3


# DEFINIR UNA FUNCION PARA USARLO EN EL INDEX

def eliminar_cancion():
    try:

        # CONCTAR A LA BASE DE DATOS 

        with sqlite3.connect("C:/Users/POWER/canciones_gestor.db") as cancion_eliminar:

            # SE DEFINE UN CURSOR PARA MANEJAR LA BASE DE DATOS 

            consulta_cursor = cancion_eliminar.cursor()

            # ENTARDA DE USUARIO PARA ELIMINAR RL NOMBRE DE LA CANCION

            usuario_eliminar= str(input("Ingresa el nombre de la cancion a eliminar: "))

            # CONSULTA QUE BORRA LA CANCION DE LA TABLA "Canciones"

            consulta_cursor.execute("DELETE FROM Canciones WHERE Nombre_cancion = ?", (usuario_eliminar,))

            # SE SUBRE LOS CAMBIOS DE LA BASE DE DATOS

            cancion_eliminar.commit()

            # MENSAJE DE EXITO

            print("Cancion eliminada correctamente.")

    # MANEJO DE ERRORES
    
    except ValueError:
        print("Error de digitiacion, intentar de nuevo.")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error}")