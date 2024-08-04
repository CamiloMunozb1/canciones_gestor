
# IMPORTAR LA BIBLIOTECA "SQLITE3"

import sqlite3

# IMPORTAR ÑA BIBLIOTECA "PANDAS" 

import pandas as pd


# DEFINIR UNA FUNCION PARA USAR EN EL INDEX

def mostrar_canciones():

    # CONECTAR A LA BASE DE DATOS 

    with sqlite3.connect("C:/Users/POWER/canciones_gestor.db") as canciones_mostrar:

        # DEFINIR UN CURSOR PARA MANEJAR LA BASE DE DATOS

        consulta_cursor = canciones_mostrar.cursor()

        # CONSULTA QUE MUESTRA LA TABLA "Canciones" EN LA FILA "Nombre_cacnion" SIN LOS VALORES NULOS

        consulta_cursor.execute("SELECT * FROM Canciones WHERE Nombre_cancion IS NOT NULL")

        # SE USA "fetchall" UN METODO DE LECTURA

        resultado = consulta_cursor.fetchall()

        # SE UTILIZA EL MODULO "DataFrame" PARA MOSTAR LA TABLA

        resultado_df = pd.DataFrame(resultado)

    # SE MUESTRA LA TABLA
    
    print(resultado_df)
