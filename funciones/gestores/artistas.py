import sqlite3

def agregar_artista():
    try:
        with sqlite3.connect("C:/Users/POWER/canciones_gestor.db") as añadir_cancion:
            consulta_cursor = añadir_cancion.cursor()
            usuario_artista = str(input("Ingresa el nombre del artista: "))
            consulta_cursor.execute("INSERT INTO Artistas (Nombre_artista) VALUES (?)",(usuario_artista,))
            añadir_cancion.commit()
            print("Artista ingresado con exito.")
    except ValueError:
        print("Error de digitacion, vuelve a intentar.")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error}")