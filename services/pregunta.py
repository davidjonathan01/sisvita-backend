from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.pregunta import Pregunta
from schemas.pregunta_schema import pregunta_schema, preguntas_schema

pregunta_routes = Blueprint("pregunta_routes", __name__)

@pregunta_routes.route('/create_pregunta', methods=['POST'])
def create_pregunta():
    id_test = request.json.get('id_test')
    interrogante = request.json.get('interrogante')
    orden = request.json.get('orden')
    descripcion = request.json.get('descripcion')

    new_pregunta = Pregunta(id_test=id_test, interrogante=interrogante, orden=orden, descripcion=descripcion)

    db.session.add(new_pregunta)
    db.session.commit()

    result = pregunta_schema.dump(new_pregunta)

    data = {
        'message': 'Nueva pregunta registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@pregunta_routes.route('/get_preguntas', methods=['GET'])
def get_preguntas():
    preguntas = Pregunta.query.all()

    if not preguntas:
        data = {
            'message': 'No se encontraron registros de preguntas',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = preguntas_schema.dump(preguntas)

    data = {
        'message': 'Lista de preguntas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@pregunta_routes.route('/get_pregunta/<int:id>', methods=['GET'])
def get_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = pregunta_schema.dump(pregunta)

    data = {
        'message': 'Pregunta encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@pregunta_routes.route('/update_pregunta/<int:id>', methods=['PUT'])
def update_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    pregunta.id_test = request.json.get('id_test')
    pregunta.interrogante = request.json.get('interrogante')
    pregunta.orden = request.json.get('orden')
    pregunta.descripcion = request.json.get('descripcion')

    db.session.commit()

    result = pregunta_schema.dump(pregunta)

    data = {
        'message': 'Pregunta actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@pregunta_routes.route('/delete_pregunta/<int:id>', methods=['DELETE'])
def delete_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(pregunta)
    db.session.commit()

    data = {
        'message': 'Pregunta eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)