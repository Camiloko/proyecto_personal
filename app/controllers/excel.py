# controllers.py
from flask import render_template, request, jsonify
from app import app
from models import generar_recomendaciones_graficos

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        archivo_excel = request.files['archivo_excel']
        tipo_datos = request.form['tipo_datos']
        columna_x = request.form['columna_x']
        columna_y = request.form['columna_y']

        # Cargar el archivo Excel y obtener los datos
        df = pd.read_excel(archivo_excel)
        
        # Generar recomendaciones de gráficos
        recomendaciones_graficos = generar_recomendaciones_graficos(df, tipo_datos, columna_x, columna_y)

        return jsonify(recomendaciones_graficos=recomendaciones_graficos)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

