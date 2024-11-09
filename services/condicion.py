# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.condicion import Condicion
from schemas.condicion_schema import condicion_schema, condiciones_schema

condicion_routes = Blueprint("condicion_routes", __name__)

@condicion_routes.route('/create_condicion', methods=['POST'])
def create_condicion():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    new_condicion = Condicion(nombre=nombre, descripcion=descripcion)

    db.session.add(new_condicion)
    db.session.commit()

    result = condicion_schema.dump(new_condicion)

    data = {
        'message': 'Nueva condicion registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@condicion_routes.route('/get_condiciones', methods=['GET'])
def get_condiciones():
    all_condiciones = Condicion.query.all()

    if not all_condiciones:
        data = {
            'message': 'No se encontraron registros de condiciones',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = condiciones_schema.dump(all_condiciones)

    data = {
        'message': 'Todos los registros de condiciones han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@condicion_routes.route('/get_condicion/<int:id>', methods=['GET'])
def get_condicion(id):
    condicion = Condicion.query.get(id)

    if not condicion:
        data = {
            'message': 'Condicion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = condicion_schema.dump(condicion)

    data = {
        'message': 'Condicion encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@condicion_routes.route('/update_condicion/<int:id>', methods=['PUT'])
def update_condicion(id):
    condicion = Condicion.query.get(id)

    if not condicion:
        data = {
            'message': 'Condicion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    condicion.nombre = nombre
    condicion.descripcion = descripcion

    db.session.commit()

    result = condicion_schema.dump(condicion)

    data = {
        'message': 'Condicion actualizada!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@condicion_routes.route('/delete_condicion/<int:id>', methods=['DELETE'])
def delete_condicion(id):
    condicion = Condicion.query.get(id)

    if not condicion:
        data = {
            'message': 'Condicion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(condicion)
    db.session.commit()

    data = {
        'message': 'Condicion eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)