from flask import Flask, jsonify, request, abort, make_response #pip install Flask
from flask_cors import CORS, cross_origin #CORs $pip install -U flask-cors

#Datos
from datos import series, usuarios
from plantillas import home

#Funciones
import seriesFunciones

#Bucle del servidor
app = Flask(__name__)
CORS(app)#CORs

#Aqui definimos las funciones que vamos a usar

def getUsers():
    return jsonify(usuarios)

def hasRoll(token, roll):
    tieneElRoll = False
    userFound = [user for user in usuarios if user['token'] == token]
    if len(userFound) > 0:
        for user_roll in userFound[0]['rolles']:
            if user_roll == roll:
                tieneElRoll = True
    
    return tieneElRoll

def getTokenUsuario(user_name, password):
    nameFound = [user for user in usuarios if user['nombre'] == user_name]
    respuesta = jsonify({"error":"Usuario no encontrado"})
    if len(nameFound) > 0:
        userFound = [pwd for pwd in nameFound if pwd['contrasenna'] == password]
        respuesta = jsonify({"error":"Contrasenna incorrecta"})
        if len(userFound) > 0:
            respuesta = {"usuario": userFound[0]}
    
    return respuesta

def home_f():
    return str(home)

#Aqui definimos los EndPoint
@app.route('/home')
def home_EP():
    return home_f()

@app.route('/series', methods=['GET'])
def series_EP():
    return seriesFunciones.getSeries(request.headers['token'])

@app.route('/serie/<int:serie_id>', methods=['GET'])
def getSerie_EP(serie_id):
    return seriesFunciones.getSerie(serie_id)

@app.route('/serie', methods=['POST'])
def postSerie_EP():
    return seriesFunciones.postSerie(request.json)

@app.route('/serie/<int:serie_id>', methods=['PUT'])
def putSerie_EP(serie_id):
    return seriesFunciones.putSerie(request.json, serie_id)

@app.route('/serie/<int:serie_id>', methods=['DELETE'])
def deleteSerie_EP(serie_id):
    respuesta = {
        "estado": "error",
        "tipo": "no_autorizado"
    }
    if hasRoll(request.headers['token'], 'administrador'):
        respuesta = seriesFunciones.deleteSerie(serie_id)
    return respuesta

@app.route('/usuarios', methods=['GET'])
def getUsers_EP():
    return getUsers()

@app.route('/usuario/<string:user_name>/<string:user_pwd>', methods=['GET'])
def getTokenUsuario_EP(user_name, user_pwd):
    return getTokenUsuario(user_name, user_pwd)

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='127.0.0.1')
