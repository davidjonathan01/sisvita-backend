from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.estado import Estado
from schemas.estado_schema import estado_schema, estados_schema

estado_routes = Blueprint("estado_routes", __name__)

@estado_routes.route('/create_estado', methods=['POST'])
def create_estado():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')
    id_tipo_estado = request.json.get('id_tipo_estado')

    new_estado = Estado(nombre=nombre, descripcion=descripcion, id_tipo_estado=id_tipo_estado)

    db.session.add(new_estado)
    db.session.commit()

    result = estado_schema.dump(new_estado)

    data = {
        'message': 'Nuevo estado registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@estado_routes.route('/get_estados', methods=['GET'])
def get_estados():
    all_estados = Estado.query.all()

    if not all_estados:
        data = {
            'message': 'No se encontraron registros de estados',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = estados_schema.dump(all_estados)

    data = {
        'message': 'Todos los registros de estados han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estado_routes.route('/get_estado/<int:id>', methods=['GET'])
def get_estado(id):
    estado = Estado.query.get(id)

    if not estado:
        data = {
            'message': 'Estado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = estado_schema.dump(estado)

    data = {
        'message': 'Estado encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estado_routes.route('/update_estado/<int:id>', methods=['PUT'])
def update_estado(id):
    estado = Estado.query.get(id)

    if not estado:
        data = {
            'message': 'Estado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    estado.nombre = request.json.get('nombre')
    estado.descripcion = request.json.get('descripcion')
    estado.id_tipo_estado = request.json.get('id_tipo_estado')

    db.session.commit()

    result = estado_schema.dump(estado)

    data = {
        'message': 'Estado actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estado_routes.route('/delete_estado/<int:id>', methods=['DELETE'])
def delete_estado(id):
    estado = Estado.query.get(id)

    if not estado:
        data = {
            'message': 'Estado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(estado)
    db.session.commit()

    data = {
        'message': 'Estado eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)