from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.modalidad import Modalidad
from schemas.modalidad_schema import modalidad_schema, modalidades_schema

modalidad_routes = Blueprint("modalidad_routes", __name__)

@modalidad_routes.route('/create_modalidad', methods=['POST'])
def create_modalidad():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    new_modalidad = Modalidad(nombre=nombre, descripcion=descripcion)

    db.session.add(new_modalidad)
    db.session.commit()

    result = modalidad_schema.dump(new_modalidad)

    data = {
        'message': 'Nueva modalidad registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@modalidad_routes.route('/get_modalidades', methods=['GET'])
def get_modalidades():
    all_modalidades = Modalidad.query.all()

    if not all_modalidades:
        data = {
            'message': 'No se encontraron registros de modalidades',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = modalidades_schema.dump(all_modalidades)

    data = {
        'message': 'Todos los registros de modalidades han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@modalidad_routes.route('/get_modalidad/<int:id>', methods=['GET'])
def get_modalidad(id):
    modalidad = Modalidad.query.get(id)

    if not modalidad:
        data = {
            'message': 'Modalidad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = modalidad_schema.dump(modalidad)

    data = {
        'message': 'Modalidad encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@modalidad_routes.route('/update_modalidad/<int:id>', methods=['PUT'])
def update_modalidad(id):
    modalidad = Modalidad.query.get(id)

    if not modalidad:
        data = {
            'message': 'Modalidad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    modalidad.nombre = request.json.get('nombre')
    modalidad.descripcion = request.json.get('descripcion')

    db.session.commit()

    result = modalidad_schema.dump(modalidad)

    data = {
        'message': 'Modalidad actualizada!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@modalidad_routes.route('/delete_modalidad/<int:id>', methods=['DELETE'])
def delete_modalidad(id):
    modalidad = Modalidad.query.get(id)

    if not modalidad:
        data = {
            'message': 'Modalidad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(modalidad)
    db.session.commit()

    data = {
        'message': 'Modalidad eliminada!',
        'status': 200
    }

    return make_response(jsonify(data), 200)