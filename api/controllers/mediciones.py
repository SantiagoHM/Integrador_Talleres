from flask import jsonify
from flask import request
from db.db import cnx

class medicione():
    global cur
    cur = cnx.cursor()
    
    def list():
        lista = []
        cur.execute("SELECT * FROM mediciones_")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns, row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
    cnx.close
    
    def create(body):
        data = (body['fecha'], body['observacion'], body['codigosensor'], body['valor'], body['origenes'])
        sql = "INSERT INTO mediciones_(fecha, observacion, codigosensor, valor, origenes) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(sql, data)
        cnx.commit()
        return {'Estado' : "se ha insertado"}, 200