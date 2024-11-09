# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.carrera import Carrera
from schemas.carrera_schema import carrera_schema, carreras_schema

carrera_routes = Blueprint("carrera_routes", __name__)

@carrera_routes.route('/create_carrera', methods=['POST'])
def create_carrera():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    new_carrera = Carrera(nombre=nombre, descripcion=descripcion)

    db.session.add(new_carrera)
    db.session.commit()

    result = carrera_schema.dump(new_carrera)

    data = {
        'message': 'Nueva carrera registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@carrera_routes.route('/get_carreras', methods=['GET'])
def get_carreras():
    all_carreras = Carrera.query.all()

    if not all_carreras:
        data = {
            'message': 'No se encontraron registros de carreras',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = carreras_schema.dump(all_carreras)

    data = {
        'message': 'Todos los registros de carreras han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@carrera_routes.route('/get_carrera/<int:id>', methods=['GET'])
def get_carrera(id):
    carrera = Carrera.query.get(id)

    if not carrera:
        data = {
            'message': 'Carrera no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = carrera_schema.dump(carrera)

    data = {
        'message': 'Carrera encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@carrera_routes.route('/update_carrera/<int:id>', methods=['PUT'])
def update_carrera(id):
    carrera = Carrera.query.get(id)

    if not carrera:
        data = {
            'message': 'Carrera no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    carrera.nombre = nombre
    carrera.descripcion = descripcion

    db.session.commit()

    result = carrera_schema.dump(carrera)

    data = {
        'message': 'Carrera actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@carrera_routes.route('/delete_carrera/<int:id>', methods=['DELETE'])
def delete_carrera(id):
    carrera = Carrera.query.get(id)

    if not carrera:
        data = {
            'message': 'Carrera no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(carrera)
    db.session.commit()

    data = {
        'message': 'Carrera eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)