from flask import Flask, jsonify, request, abort, make_response
from datos import series

def getSeries(token):
    print('token',token)
    return jsonify(series)

def getSerie(serie_id):
    respuesta = jsonify({"error": "serie no encontrada"})
    serieFound = [serie for serie in series if serie['id'] == serie_id]
    if len(serieFound) > 0:
        respuesta = serieFound[0]
    return respuesta

def postSerie(serie_new):
    new_id = series[-1]['id']+1
    serie = {
        "id": new_id,
        "nombre": serie_new['nombre'],
        "pais": serie_new['pais'],
        "episodios": serie_new['episodios'],
        "genero": serie_new['genero'],
        "img": serie_new['img']
    }

    series.append(serie)

    return serie

def putSerie(serie_update, serie_id):
    respuesta = "error"
    serieFound = [serie for serie in series if serie['id'] == serie_id]
    if len(serieFound) > 0:
        serieFound[0]['id'] = serie_update['id']
        serieFound[0]['nombre'] = serie_update['nombre']
        serieFound[0]['pais'] = serie_update['pais']
        serieFound[0]['episodios'] = serie_update['episodios']
        serieFound[0]['genero'] = serie_update['genero']
        serieFound[0]['img'] = serie_update['img']

        respuesta = serieFound[0]
    return respuesta

def deleteSerie(serie_id):
    respuesta = "error"
    serieFound = [serie for serie in series if serie['id'] == serie_id][0]
    if len(serieFound) > 0:
        series.remove(serieFound)

        respuesta = jsonify(
            {"estado": "eliminado",
            "serie": serieFound
            })
    
    return respuesta