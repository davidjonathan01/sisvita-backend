from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.opcion import Opcion
from schemas.opcion_schema import opcion_schema, opciones_schema

opcion_routes = Blueprint("opcion_routes", __name__)

@opcion_routes.route('/create_opcion', methods=['POST'])
def create_opcion():
    id_test = request.json.get('id_test')
    nombre = request.json.get('nombre')
    puntaje = request.json.get('puntaje')
    orden = request.json.get('orden')
    descripcion = request.json.get('descripcion')

    new_opcion = Opcion(id_test=id_test, nombre=nombre, puntaje=puntaje, orden=orden, descripcion=descripcion)

    db.session.add(new_opcion)
    db.session.commit()

    result = opcion_schema.dump(new_opcion)

    data = {
        'message': 'Nueva opcion registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@opcion_routes.route('/get_opciones', methods=['GET'])
def get_opciones():
    opciones = Opcion.query.all()

    if not opciones:
        data = {
            'message': 'No se encontraron registros de opciones',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = opciones_schema.dump(opciones)

    data = {
        'message': 'Lista de opciones',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@opcion_routes.route('/get_opcion/<int:id>', methods=['GET'])
def get_opcion(id):
    opcion = Opcion.query.get(id)

    if not opcion:
        data = {
            'message': 'Opcion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = opcion_schema.dump(opcion)

    data = {
        'message': 'Opcion encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@opcion_routes.route('/update_opcion/<int:id>', methods=['PUT'])
def update_opcion(id):
    opcion = Opcion.query.get(id)

    if not opcion:
        data = {
            'message': 'Opcion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    opcion.id_test = request.json.get('id_test')
    opcion.nombre = request.json.get('nombre')
    opcion.puntaje = request.json.get('puntaje')
    opcion.orden = request.json.get('orden')
    opcion.descripcion = request.json.get('descripcion')

    db.session.commit()

    result = opcion_schema.dump(opcion)

    data = {
        'message': 'Opcion actualizada!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@opcion_routes.route('/delete_opcion/<int:id>', methods=['DELETE'])
def delete_opcion(id):
    opcion = Opcion.query.get(id)

    if not opcion:
        data = {
            'message': 'Opcion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(opcion)
    db.session.commit()

    data = {
        'message': 'Opcion eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)