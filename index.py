from funciones.gestores.artistas import agregar_artista
from funciones.gestores.canciones import agregar_cancion


while True:
    print("""
          Gestor de canciones:
          1. Ingresar un artista.
          2. Ingresar una cancion.
          3. Eliminar canciones.
          4. Mostrar canciones.
          5. Salir.
          """)
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            agregar_artista()
        elif usuario == 2:
            agregar_cancion()
        elif usuario == 3:
            print("Proxima funcionalidad")
        elif usuario == 4:
            print("Proxima funcionalidad")
        elif usuario == 5:
            print("Gracias por gestionar tus canciones.")
            break
    except ValueError:
        print("Error de digitacion, vuelve a intentarlo.")
