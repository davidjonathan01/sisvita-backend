from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.tipo_estado import Tipo_estado
from schemas.tipo_estado_schema import tipo_estado_schema, tipos_estado_schema

tipo_estado_routes = Blueprint("tipo_estado_routes", __name__)

@tipo_estado_routes.route('/create_tipo_estado', methods=['POST'])
def create_tipo_estado():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    new_tipo_estado = Tipo_estado(nombre=nombre, descripcion=descripcion)

    db.session.add(new_tipo_estado)
    db.session.commit()

    result = tipo_estado_schema.dump(new_tipo_estado)

    data = {
        'message': 'Nuevo tipo de estado registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@tipo_estado_routes.route('/get_tipos_estado', methods=['GET'])
def get_tipos_estado():
    all_tipos_estado = Tipo_estado.query.all()

    if not all_tipos_estado:
        data = {
            'message': 'No se encontraron registros de tipos de estado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = tipos_estado_schema.dump(all_tipos_estado)

    data = {
        'message': 'Todos los registros de tipos de estado han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_estado_routes.route('/get_tipo_estado/<int:id>', methods=['GET'])
def get_tipo_estado(id):
    tipo_estado = Tipo_estado.query.get(id)

    if not tipo_estado:
        data = {
            'message': 'Tipo de estado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = tipo_estado_schema.dump(tipo_estado)

    data = {
        'message': 'Tipo de estado encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_estado_routes.route('/update_tipo_estado/<int:id>', methods=['PUT'])
def update_tipo_estado(id):
    tipo_estado = Tipo_estado.query.get(id)

    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    tipo_estado.nombre = nombre
    tipo_estado.descripcion = descripcion

    db.session.commit()

    result = tipo_estado_schema.dump(tipo_estado)

    data = {
        'message': 'Tipo de estado actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_estado_routes.route('/delete_tipo_estado/<int:id>', methods=['DELETE'])
def delete_tipo_estado(id):
    tipo_estado = Tipo_estado.query.get(id)

    if not tipo_estado:
        data = {
            'message': 'Tipo de estado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(tipo_estado)
    db.session.commit()

    data = {
        'message': 'Tipo de estado eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)