from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

tipo_medicion = {'sensor': 'DS18B20', 'variable': 'centigrados', 'unidades': 'grados centigrados'}

mediciones = [
    {'fecha': '22-08-2019', **tipo_medicion, 'valor': 22},
    {'fecha': '22-08-2019', **tipo_medicion, 'valor': 24},
    {'fecha': '22-08-2019', **tipo_medicion, 'valor': 22},
    {'fecha': '22-08-2019', **tipo_medicion, 'valor': 24}
]

@app.route('/mediciones', methods =['GET'])
def getAll():
    return jsonify(mediciones)


@app.route('/mediciones/cMedia', methods =['GET'])
def getMedia():
    x = 0
    contador = 0
    for elemento in mediciones:
        x += elemento['valor']
        contador+= 1
    return jsonify(x/contador)
    


@app.route('/mediciones/post', methods =['POST'])
def postOne():
    now = datetime.now()
    body = request.json
    body['fecha']= datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    mediciones.append({**body, **tipo_medicion})
    return jsonify(mediciones)

app.run(port=5000, debug=True)

