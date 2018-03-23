
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
from flask import send_file
import subprocess               # Para ejecutar llamadas al sistema.
import spawn_process
import copy_file


#Importa la capsula de c++
import hola
import example

app = Flask(__name__)           # Variable predifinida de python. Esto simplemente es una instancia de Flask.
api = Api(app)                  # http://flask-restful.readthedocs.io/en/latest/api.html#flask_restful.Api

class Saludo(Resource):
    def get(self, nombre):
        result = {'saludo': hola.Saluda(nombre)}
        return jsonify(result)

class Mult(Resource):
    def get(self, num1, num2):
        result = {'res': example.Suma(int(num1), int(num2))}
        return jsonify(result)


class execute_hard_spheere(Resource):
    def get(self, frac_vol):
        # result = subprocess.Popen(["touch", name_file], stdout=subprocess.PIPE) #I dont know
        # string = {'result', name_file}
        return spawn_process.exe_hard_sphere(frac_vol)


class exe_hard_sphere_get_file(Resource):
    def get(self):
        copy_file.copy_files('/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat')

        return send_file('./SKhard_sphere.dat', attachment_filename='SKhard_sphere.dat')


#add_resource(resource, *urls, **kwargs)
#resource (Resource) – the class name of your resource
api.add_resource(Saludo, '/saludo/<nombre>') # Route_3
api.add_resource(Mult, '/saludo/<num1>/<num2>')
api.add_resource(execute_hard_spheere, '/exe_hard_spheere/<frac_vol>')
api.add_resource(exe_hard_sphere_get_file, '/hard_sphere/SK.dat')


if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5002,debug=True)
