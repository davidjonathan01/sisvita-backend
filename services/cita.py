# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.cita import Cita
from schemas.cita_schema import cita_schema, citas_schema

cita_routes = Blueprint("cita_routes", __name__)

@cita_routes.route('/create_cita', methods=['POST'])
def create_cita():
    id_paciente = request.json.get('id_paciente')
    id_especialista = request.json.get('id_especialista')
    motivo = request.json.get('motivo')
    id_estado = request.json.get('id_estado')
    id_modalidad = request.json.get('id_modalidad')
    fec_programada = request.json.get('fec_programada')
    hora_inicio = request.json.get('hora_inicio')
    hora_fin = request.json.get('hora_fin')

    new_cita = Cita(id_paciente=id_paciente, id_especialista=id_especialista, motivo=motivo, id_estado=id_estado, id_modalidad=id_modalidad, fec_programada=fec_programada, hora_inicio=hora_inicio, hora_fin=hora_fin)

    db.session.add(new_cita)
    db.session.commit()

    result = cita_schema.dump(new_cita)

    data = {
        'message': 'Nueva cita registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@cita_routes.route('/get_citas', methods=['GET'])
def get_citas():
    all_citas = Cita.query.all()

    if not all_citas:
        data = {
            'message': 'No se encontraron registros de citas',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = citas_schema.dump(all_citas)

    data = {
        'message': 'Todos los registros de citas han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@cita_routes.route('/get_cita/<int:id>', methods=['GET'])
def get_cita(id):
    cita = Cita.query.get(id)

    if not cita:
        data = {
            'message': 'Cita no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = cita_schema.dump(cita)

    data = {
        'message': 'Cita encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@cita_routes.route('/update_cita/<int:id>', methods=['PUT'])
def update_cita(id):
    cita = Cita.query.get(id)

    if not cita:
        data = {
            'message': 'Cita no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_paciente = request.json.get('id_paciente')
    id_especialista = request.json.get('id_especialista')
    motivo = request.json.get('motivo')
    id_estado = request.json.get('id_estado')
    id_modalidad = request.json.get('id_modalidad')
    fec_programada = request.json.get('fec_programada')
    hora_inicio = request.json.get('hora_inicio')
    hora_fin = request.json.get('hora_fin')

    cita.id_paciente = id_paciente
    cita.id_especialista = id_especialista
    cita.motivo = motivo
    cita.id_estado = id_estado
    cita.id_modalidad = id_modalidad
    cita.fec_programada = fec_programada
    cita.hora_inicio = hora_inicio
    cita.hora_fin = hora_fin

    db.session.commit()

    result = cita_schema.dump(cita)

    data = {
        'message': '¡Cita actualizada!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@cita_routes.route('/delete_cita/<int:id>', methods=['DELETE'])
def delete_cita(id):
    cita = Cita.query.get(id)

    if not cita:
        data = {
            'message': 'Cita no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(cita)
    db.session.commit()

    data = {
        'message': 'Cita eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)