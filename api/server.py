from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.mediciones import medicione

app = Flask(__name__)
CORS(app)

@app.route('/mediciones_', methods = ['GET'])
def getAll():
    return (medicione.list())

@app.route('/mediciones_', methods = ['POST'])
def postOne():
    body = request.json 
    return (medicione.create(body))

#app.run(port = 5000, debug = True)