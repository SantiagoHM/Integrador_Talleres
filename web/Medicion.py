from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__, template_folder='templates')


variables_list =[
    {'fecha' : '12-08-2019', 'origenes':'Sensor en terreno','valor':'2', 'codigosensor':'3234','observacion':'Tomado de dia'},
    {'fecha' : '13-08-2019', 'origenes':'Imagen satelital','valor':'3', 'codigosensor':'2324','observacion':'Tomado de noche'}
]

origen_list= [
        'Sensor en terreno','Imagen Satelital','Imagen dron','Dato derivado'
]


@app.route('/crearMedicion', methods = ['GET'])
def crearMedicion():
    return render_template('crearMedicion.html', origenes = origen_list)

@app.route('/listarMediciones', methods =['GET'])
def listarMediciones():
    variables_list = requests.get('http://localhost:5000/mediciones_').json()
    return render_template('listarMedicion.html', medicion = variables_list)

@app.route('/guardarMedicion', methods = ['POST'])
def guardarMedicion():
    medicion = dict(request.values)
    medicion['valor'] = int(medicion['valor'])
    requests.post('http://localhost:5000/mediciones_', json = medicion)
    return(listarMediciones())
    

app.run(port=8080, debug=True)