# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.asistencia import Asistencia
from schemas.asistencia_schema import asistencia_schema, asistencias_schema

asistencia_routes = Blueprint("asistencia_routes", __name__)

@asistencia_routes.route('/create_asistencia', methods=['POST'])
def create_asistencia():
    fecha = request.json.get('fecha')
    id_taller = request.json.get('id_taller')
    id_paciente = request.json.get('id_paciente')

    new_asistencia = Asistencia(fecha=fecha, id_taller=id_taller, id_paciente=id_paciente)

    db.session.add(new_asistencia)
    db.session.commit()

    result = asistencia_schema.dump(new_asistencia)

    data = {
        'message': '¡Nueva asistencia registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@asistencia_routes.route('/get_asistencias', methods=['GET'])
def get_asistencias():
    all_asistencias = Asistencia.query.all()
    
    if not all_asistencias:
        data = {
            'message': 'No hay registros de asistencias',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = asistencias_schema.dump(all_asistencias)

    data = {
        'message': 'Todos los registros de asistencias han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@asistencia_routes.route('/get_asistencia/<int:id>', methods=['GET'])
def get_asistencia(id):
    asistencia = Asistencia.query.get(id)

    if not asistencia:
        data = {
            'message': 'Asistencia no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = asistencia_schema.dump(asistencia)

    data = {
        'message': 'Asistencia encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@asistencia_routes.route('/update_asistencia/<int:id>', methods=['PUT'])
def update_asistencia(id):
    asistencia = Asistencia.query.get(id)

    if not asistencia:
        data = {
            'message': 'Asistencia no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    fecha = request.json.get('fecha')
    id_taller = request.json.get('id_taller')
    id_paciente = request.json.get('id_paciente')

    asistencia.fecha = fecha
    asistencia.id_taller = id_taller
    asistencia.id_paciente = id_paciente

    db.session.commit()

    result = asistencia_schema.dump(asistencia)

    data = {
        'message': '¡Asistencia actualizada!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@asistencia_routes.route('/delete_asistencia/<int:id>', methods=['DELETE'])
def delete_asistencia(id):
    asistencia = Asistencia.query.get(id)

    if not asistencia:
        data = {
            'message': 'Asistencia no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(asistencia)
    db.session.commit()

    data = {
        'message': 'Asistencia eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)