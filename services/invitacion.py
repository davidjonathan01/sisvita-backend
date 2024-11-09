from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.invitacion import Invitacion
from schemas.invitacion_schema import invitacion_schema, invitaciones_schema

invitacion_routes = Blueprint("invitacion_routes", __name__)

@invitacion_routes.route('/create_invitacion', methods=['POST'])
def create_invitacion():
    id_especialista = request.json.get('id_especialista')
    id_resultado = request.json.get('id_resultado')
    id_test = request.json.get('id_test')
    fec_invitacion = request.json.get('fec_invitacion')

    new_invitacion = Invitacion(id_especialista=id_especialista, id_resultado=id_resultado, id_test=id_test, fec_invitacion=fec_invitacion)

    db.session.add(new_invitacion)
    db.session.commit()

    result = invitacion_schema.dump(new_invitacion)

    data = {
        'message': 'Nueva invitación registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@invitacion_routes.route('/get_invitaciones', methods=['GET'])
def get_invitaciones():
    all_invitaciones = Invitacion.query.all()
    result = invitaciones_schema.dump(all_invitaciones)

    data = {
        'message': 'Todas las invitaciones han sido encontradas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@invitacion_routes.route('/get_invitacion/<int:id>', methods=['GET'])
def get_invitacion(id):
    invitacion = Invitacion.query.get(id)

    if not invitacion:
        data = {
            'message': 'Invitación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = invitacion_schema.dump(invitacion)

    data = {
        'message': 'Invitación encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@invitacion_routes.route('/update_invitacion/<int:id>', methods=['PUT'])
def update_invitacion(id):
    invitacion = Invitacion.query.get(id)

    if not invitacion:
        data = {
            'message': 'Invitación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    invitacion.id_especialista = request.json.get('id_especialista')
    invitacion.id_resultado = request.json.get('id_resultado')
    invitacion.id_test = request.json.get('id_test')
    invitacion.fec_invitacion = request.json.get('fec_invitacion')

    db.session.commit()

    result = invitacion_schema.dump(invitacion)

    data = {
        'message': 'Invitación actualizada!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@invitacion_routes.route('/delete_invitacion/<int:id>', methods=['DELETE'])
def delete_invitacion(id):
    invitacion = Invitacion.query.get(id)

    if not invitacion:
        data = {
            'message': 'Invitación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(invitacion)
    db.session.commit()

    data = {
        'message': 'Invitación eliminada!',
        'status': 200
    }

    return make_response(jsonify(data), 200)
