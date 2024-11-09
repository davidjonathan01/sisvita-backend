from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.horario import Horario
from schemas.horario_schema import horario_schema, horarios_schema

horario_routes = Blueprint("horario_routes", __name__)

@horario_routes.route('/create_horario', methods=['POST'])
def create_horario():
    id_taller = request.json.get('id_taller')
    id_dia = request.json.get('dia')
    horario_inicio = request.json.get('horario_inicio')
    horario_fin = request.json.get('horario_fin')

    new_horario = Horario(id_taller=id_taller, id_dia=id_dia, horario_inicio=horario_inicio, horario_fin=horario_fin)

    db.session.add(new_horario)
    db.session.commit()

    result = horario_schema.dump(new_horario)

    data = {
        'message': 'Nuevo horario registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@horario_routes.route('/get_horarios', methods=['GET'])
def get_horarios():
    horarios = Horario.query.all()

    if not horarios:
        data = {
            'message': 'No se encontraron registros de horarios',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = horarios_schema.dump(horarios)

    data = {
        'message': 'Lista de horarios',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@horario_routes.route('/get_horario/<int:id>', methods=['GET'])
def get_horario(id):
    horario = Horario.query.get(id)

    if not horario:
        data = {
            'message': 'Horario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = horario_schema.dump(horario)

    data = {
        'message': 'Horario encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@horario_routes.route('/update_horario/<int:id>', methods=['PUT'])
def update_horario(id):
    horario = Horario.query.get(id)

    if not horario:
        data = {
            'message': 'Horario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_taller = request.json.get('id_taller')
    id_dia = request.json.get('id_dia')
    horario_inicio = request.json.get('horario_inicio')
    horario_fin = request.json.get('horario_fin')

    horario.id_taller = id_taller
    horario.dia = id_dia
    horario.hora_inicio = horario_inicio
    horario.hora_fin = horario_fin

    db.session.commit()

    result = horario_schema.dump(horario)

    data = {
        'message': 'Horario actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@horario_routes.route('/delete_horario/<int:id>', methods=['DELETE'])
def delete_horario(id):
    horario = Horario.query.get(id)

    if not horario:
        data = {
            'message': 'Horario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(horario)
    db.session.commit()

    result = horario_schema.dump(horario)

    data = {
        'message': 'Horario eliminado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)