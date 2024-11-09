from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.especialidad import Especialidad
from schemas.especialidad_schema import especialidad_schema, especialidades_schema

especialidad_routes = Blueprint("especialidad_routes", __name__)

@especialidad_routes.route('/create_especialidad', methods=['POST'])
def create_especialidad():
    titulo = request.json.get('titulo')
    descripcion = request.json.get('descripcion')

    new_especialidad = Especialidad(titulo=titulo, descripcion=descripcion)

    db.session.add(new_especialidad)
    db.session.commit()

    result = especialidad_schema.dump(new_especialidad)

    data = {
        'message': 'Nueva especialidad registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@especialidad_routes.route('/get_especialidades', methods=['GET'])
def get_especialidades():
    all_especialidades = Especialidad.query.all()

    if not all_especialidades:
        data = {
            'message': 'No se encontraron registros de especialidades',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = especialidades_schema.dump(all_especialidades)

    data = {
        'message': 'Todos los registros de especialidades han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialidad_routes.route('/get_especialidad/<int:id>', methods=['GET'])
def get_especialidad(id):
    especialidad = Especialidad.query.get(id)

    if not especialidad:
        data = {
            'message': 'Especialidad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = especialidad_schema.dump(especialidad)

    data = {
        'message': 'Especialidad encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialidad_routes.route('/update_especialidad/<int:id>', methods=['PUT'])
def update_especialidad(id):
    especialidad = Especialidad.query.get(id)

    if not especialidad:
        data = {
            'message': 'Especialidad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    titulo = request.json.get('titulo')
    descripcion = request.json.get('descripcion')

    especialidad.titulo = titulo
    especialidad.descripcion = descripcion

    db.session.commit()

    result = especialidad_schema.dump(especialidad)

    data = {
        'message': 'Especialidad actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialidad_routes.route('/delete_especialidad/<int:id>', methods=['DELETE'])
def delete_especialidad(id):
    especialidad = Especialidad.query.get(id)

    if not especialidad:
        data = {
            'message': 'Especialidad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(especialidad)
    db.session.commit()

    data = {
        'message': 'Especialidad eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)

