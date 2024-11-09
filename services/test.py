from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.test import Test
from schemas.test_schema import test_schema, tests_schema

test_routes = Blueprint("test_routes", __name__)

@test_routes.route('/create_test', methods=['POST'])
def create_test():
    nombre = request.json.get('nombre')
    id_tipo_test = request.json.get('id_tipo_test')
    n_preguntas = request.json.get('n_preguntas')
    id_idioma = request.json.get('id_idioma')
    n_version = request.json.get('n_version')
    descripcion = request.json.get('descripcion')

    new_test = Test(nombre=nombre, id_tipo_test=id_tipo_test, n_preguntas=n_preguntas, id_idioma=id_idioma, n_version=n_version, descripcion=descripcion)

    db.session.add(new_test)
    db.session.commit()

    result = test_schema.dump(new_test)

    data = {
        'message': 'Nuevo test creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@test_routes.route('/get_tests', methods=['GET'])
def get_tests():
    all_tests = Test.query.all()

    if not all_tests:
        data = {
            'message': 'No se encontraron tests',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = tests_schema.dump(all_tests)

    data = {
        'message': 'Todos los tests han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@test_routes.route('/get_test/<int:id>', methods=['GET'])
def get_test(id):
    test = Test.query.get(id)

    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = test_schema.dump(test)

    data = {
        'message': 'Test encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@test_routes.route('/update_test/<int:id>', methods=['PUT'])
def update_test(id):
    test = Test.query.get(id)

    test.nombre = request.json.get('nombre')
    test.id_tipo_test = request.json.get('id_tipo_test')
    test.n_preguntas = request.json.get('n_preguntas')
    test.id_idioma = request.json.get('id_idioma')
    test.n_version = request.json.get('n_version')
    test.descripcion = request.json.get('descripcion')

    db.session.commit()

    result = test_schema.dump(test)

    data = {
        'message': 'Test actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@test_routes.route('/delete_test/<int:id>', methods=['DELETE'])
def delete_test(id):
    test = Test.query.get(id)

    db.session.delete(test)
    db.session.commit()

    data = {
        'message': 'Test eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)