
# IMPORTAMOS LA LIBRERIA "SQLITE3" PATA MANEJAR LA BASE DE DATOS

import sqlite3


# USAMOS UNA FUNCION PARA SER USADA EN EL INDEX

def agregar_cancion():
    try:

        # CONECTAR CON LA BASE DE DATOS 

        with sqlite3.connect("C:/Users/POWER/canciones_gestor.db") as añadir_cancion:

            # AÑADIMOS UNA CURSOR PARA MANEJAR LA BASE DE DATOS

            consulta_cursor = añadir_cancion.cursor()

            # ENTRADAS DE USUARIO PAA INGRESAR TANTO LA CANCION  Y EL ARTISTA

            usuario_cancion = str(input("ingresa una cancion: "))
            usuario_artista = str(input("Ingresa el nombre del artista: "))

            # CONSULTA HACIA LA BASE DE DATOA PARA SELECCIONAR LA CLAVE FORANEA DE LA TABLA "Nombre_artista"

            consulta_cursor.execute("SELECT Artista_ID FROM Artistas WHERE Nombre_artista = ?",(usuario_artista,))

            # USO DE "fetchone" PARA DEVOLVER UNA SOLA FILA DE RESULTADOS DE UNA CONSULTA SQL.

            artista = consulta_cursor.fetchone()
            if artista:

                # SE BUSCA EL ID EN LA BASE DE DATOS EN ESTE CASO EL DEL ARTISTA 

                artista_id = artista[0]
            else:

                # MENSAJE DE ERROR SI NO SE ENCUENTRA EL ARTISTA

                print("Artista no encontrado.")

            # CON UNA NUEVA CONSULTA SE AGREFA EL NOMBRE DE LA CANCION EN LA BASE DE DATOS Y TAMBIEN LA CLAVE FORANEA EN LA TABLA 

            consulta_cursor.execute("INSERT INTO Canciones (Nombre_cancion, Artista_ID) VALUES (?,?)",(usuario_cancion,artista_id))

            # SE AÑADEN LOS CAMBIOS 

            añadir_cancion.commit()

            # MENSAJE DE EXITO

            print("Cancion Guardada correctamente")

    # MANEJO DE ERRORES 
    
    except ValueError:
        print("Error de digitacion, volver a intentar.")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error} ")
