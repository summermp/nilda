from flask import Flask, render_template, request
from datos import dato
app = Flask(__name__)
app.config["DEBUG"] = True  # Modo debug habilitado


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/acerca', methods=['GET'])
def acerca():
    return render_template('acerca.html')


@app.route('/region', methods=['GET'])
def region():
    return render_template('/region.html')

@app.route('/mostrar', methods=['POST'])
def show_region_page():
    # Obtener el valor de 'region' del formulario
    region = request.form.get('region')
    nombre = request.form['nombre']

    # Validar si 'region' es nulo o una cadena vacía
    if not region:
        return render_template('region.html', mensaje='Debe seleccionar una región.')  # Puedes pasar un mensaje opcional

    # Accede a la región específica
    region_dato = dato.get(region.lower())
    
    # Validar si la región existe en el diccionario 'dato'
    if not region_dato:
        return "No hay datos disponibles para esta región.", 404

    # Obtener el mapa y la lista de desastres
    mapa = region_dato.get('mapa')
    capital = region_dato.get('capital')
    provincias = region_dato.get('provincias')
    desastres = region_dato.get('desastres', [])

    return render_template('resultado.html',nombre=nombre, capital=capital, mapa=mapa, provincias=provincias, region=region.capitalize(), desastres=desastres)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
