from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.jornada import Jornada
from schemas.jornada_schema import jornada_schema, jornadas_schema

jornada_routes = Blueprint("jornada_routes", __name__)

@jornada_routes.route('/create_jornada', methods=['POST'])
def create_jornada():
    id_especialista = request.json.get('id_especialista')
    id_dia = request.json.get('id_dia')
    hora_inicio = request.json.get('hora_inicio')
    hora_fin = request.json.get('hora_fin')

    new_jornada = Jornada(id_especialista=id_especialista, id_dia=id_dia, hora_inicio=hora_inicio, hora_fin=hora_fin)

    db.session.add(new_jornada)
    db.session.commit()

    result = jornada_schema.dump(new_jornada)

    data = {
        'message': 'Nueva jornada registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@jornada_routes.route('/get_jornadas', methods=['GET'])
def get_jornadas():
    jornadas = Jornada.query.all()

    if not jornadas:
        data = {
            'message': 'No se encontraron registros de jornadas',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = jornadas_schema.dump(jornadas)

    data = {
        'message': 'Lista de jornadas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@jornada_routes.route('/get_jornada/<int:id>', methods=['GET'])
def get_jornada(id):
    jornada = Jornada.query.get(id)

    if not jornada:
        data = {
            'message': 'Jornada no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = jornada_schema.dump(jornada)

    data = {
        'message': 'Jornada encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@jornada_routes.route('/update_jornada/<int:id>', methods=['PUT'])
def update_jornada(id):
    jornada = Jornada.query.get(id)

    if not jornada:
        data = {
            'message': 'Jornada no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_especialista = request.json.get('id_especialista')
    id_dia = request.json.get('id_dia')
    hora_inicio = request.json.get('hora_inicio')
    hora_fin = request.json.get('hora_fin')

    jornada.id_especialista = id_especialista
    jornada.id_dia = id_dia
    jornada.hora_inicio = hora_inicio
    jornada.hora_fin = hora_fin

    db.session.commit()

    result = jornada_schema.dump(jornada)

    data = {
        'message': 'Jornada actualizada!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@jornada_routes.route('/delete_jornada/<int:id>', methods=['DELETE'])
def delete_jornada(id):
    jornada = Jornada.query.get(id)

    if not jornada:
        data = {
            'message': 'Jornada no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(jornada)
    db.session.commit()

    data = {
        'message': 'Jornada eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)
