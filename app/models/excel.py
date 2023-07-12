# models.py
import pandas as pd

def generar_recomendaciones_graficos(df, tipo_datos, columna_x, columna_y):
    # Realiza el procesamiento y análisis de los datos según las especificaciones del usuario
    # Genera las recomendaciones de gráficos basadas en los datos y las especificaciones
    recomendaciones = []

    # Ejemplo de recomendación de gráfico: Gráfico de dispersión
    if tipo_datos == 'numeric':
        recomendaciones.append({
            'nombre': 'Gráfico de Dispersión',
            'tipo': 'scatter',
            'columna_x': columna_x,
            'columna_y': columna_y
        })

    # Agrega más recomendaciones de gráficos según sea necesario

    return recomendaciones