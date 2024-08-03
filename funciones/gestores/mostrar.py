import sqlite3
import pandas as pd

def mostrar_canciones():
    with sqlite3.connect("C:/Users/POWER/canciones_gestor.db") as canciones_mostrar:
        consulta_cursor = canciones_mostrar.cursor()
        consulta_cursor.execute("SELECT * FROM Canciones WHERE Nombre_cancion IS NOT NULL")
        resultado = consulta_cursor.fetchall()
        resultado_df = pd.DataFrame(resultado)
    print(resultado_df)
