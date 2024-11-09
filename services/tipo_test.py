from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.tipo_test import Tipo_test
from schemas.tipo_test_schema import tipo_test_schema, tipos_test_schema

tipo_test_routes = Blueprint("tipo_test_routes", __name__)

@tipo_test_routes.route('/create_tipo_test', methods=['POST'])
def create_tipo_test():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    new_tipo_test = Tipo_test(nombre=nombre, descripcion=descripcion)

    db.session.add(new_tipo_test)
    db.session.commit()

    result = tipo_test_schema.dump(new_tipo_test)

    data = {
        'message': 'Nuevo tipo de test registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@tipo_test_routes.route('/get_tipos_test', methods=['GET'])
def get_tipos_test():
    all_tipos_test = Tipo_test.query.all()

    if not all_tipos_test:
        data = {
            'message': 'No se encontraron registros de tipos de test',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = tipos_test_schema.dump(all_tipos_test)

    data = {
        'message': 'Todos los registros de tipos de test han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_test_routes.route('/get_tipo_test/<int:id>', methods=['GET'])
def get_tipo_test(id):
    tipo_test = Tipo_test.query.get(id)

    if not tipo_test:
        data = {
            'message': 'Tipo de test no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = tipo_test_schema.dump(tipo_test)

    data = {
        'message': 'Tipo de test encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_test_routes.route('/update_tipo_test/<int:id>', methods=['PUT'])
def update_tipo_test(id):
    tipo_test = Tipo_test.query.get(id)

    if not tipo_test:
        data = {
            'message': 'Tipo de test no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    tipo_test.nombre = request.json.get('nombre')
    tipo_test.descripcion = request.json.get('descripcion')

    db.session.commit()

    result = tipo_test_schema.dump(tipo_test)

    data = {
        'message': 'Tipo de test actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_test_routes.route('/delete_tipo_test/<int:id>', methods=['DELETE'])
def delete_tipo_test(id):
    tipo_test = Tipo_test.query.get(id)

    if not tipo_test:
        data = {
            'message': 'Tipo de test no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(tipo_test)
    db.session.commit()

    data = {
        'message': 'Tipo de test eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)