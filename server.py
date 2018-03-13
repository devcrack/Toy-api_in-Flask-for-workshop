from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
#####
#Importa la capsula de c++
import hola
import example

app = Flask(__name__)
api = Api(app)

class Saludo(Resource):
    def get(self, nombre):
        result = {'saludo': hola.Saluda(nombre)}
        return jsonify(result)

class Mult(Resource):
    def get(self, num1, num2):
        result = {'res': example.Suma(int(num1), int(num2))}
        return jsonify(result)

api.add_resource(Saludo, '/saludo/<nombre>') # Route_3
api.add_resource(Mult, '/saludo/<num1>/<num2>')


if __name__ == '__main__':
    app.run(host="localhost" ,port=5002)
