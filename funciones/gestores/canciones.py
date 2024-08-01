import sqlite3

def agregar_cancion():
    try:
        with sqlite3.connect("C:/Users/POWER/canciones_gestor.db") as añadir_cancion:
            consulta_cursor = añadir_cancion.cursor()
            usuario_cancion = str(input("ingresa una cancion: "))
            usuario_artista = str(input("Ingresa el nombre del artista: "))
            consulta_cursor.execute("SELECT Artista_ID FROM Artistas WHERE Nombre_artista = ?",(usuario_artista,))
            artista = consulta_cursor.fetchone()
            if artista:
                artista_id = artista[0]
            else:
                print("Artista no encontrado.")
            consulta_cursor.execute("INSERT INTO Canciones (Nombre_cancion, Artista_ID) VALUES (?,?)",(usuario_cancion,artista_id))
            añadir_cancion.commit()
            print("Cancion Guardada correctamente")
    except ValueError:
        print("Error de digitacion, volver a intentar.")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error} ")
