
# IMPORTAR LA BIBLIOTECA "SQLITE3" PARA MANEJAR LA BASE

import sqlite3


# DEFINIR UNA FUNCION PARA SER USADA EN EL INDEX

def agregar_artista():
    try:

        # CONECTAR CON LA BASE DE DATOS 

        with sqlite3.connect("C:/Users/POWER/canciones_gestor.db") as añadir_cancion:

            # USAMOS UN CURSOR PARA EL MANEJO DE LA BASE

            consulta_cursor = añadir_cancion.cursor()

            # INGRESO DEL USUARIO 

            usuario_artista = str(input("Ingresa el nombre del artista: "))

            # CONSULTA SQL PARA INGRESAR EL NOMBRE DEL ARTISTA 

            consulta_cursor.execute("INSERT INTO Artistas (Nombre_artista) VALUES (?)",(usuario_artista,))

            # SE REALIZAN LOS CAMBIOS EN LA BASE DE DATOS

            añadir_cancion.commit()

            # MENSAJE DE EXITO

            print("Artista ingresado con exito.")

    # MANEJO DE ERRORES

    except ValueError:
        print("Error de digitacion, vuelve a intentar.")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error}")