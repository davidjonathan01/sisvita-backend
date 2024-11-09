import bcrypt

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.especialista import Especialista
from schemas.especialista_schema import especialista_schema, especialistas_schema

especialista_routes = Blueprint("especialista_routes", __name__)

@especialista_routes.route('/create_especialista', methods=['POST'])
def create_especialista():
    id_especialidad = request.json.get('id_especialidad')
    n_licencia = request.json.get('n_licencia')
    activo = request.json.get('activo')
    id_persona = request.json.get('id_persona')
    id_usuario = request.json.get('id_usuario')

    #contrasenia2 = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    #print(contrasenia2)

    new_especialista = Especialista(id_especialidad=id_especialidad, n_licencia=n_licencia, activo=activo, id_persona=id_persona, id_usuario=id_usuario)

    db.session.add(new_especialista)
    db.session.commit()

    result = especialista_schema.dump(new_especialista)

    data = {
        'message': 'Nuevo especialista registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@especialista_routes.route('/get_especialistas', methods=['GET'])
def get_especialistas():
    all_especialistas = Especialista.query.all()

    if not all_especialistas:
        data = {
            'message': 'No se encontraron registros de especialistas',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = especialistas_schema.dump(all_especialistas)

    data = {
        'message': 'Todos los registros de especialistas han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialista_routes.route('/get_especialista/<int:id>', methods=['GET'])
def get_especialista(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = especialista_schema.dump(especialista)

    data = {
        'message': 'Especialista encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialista_routes.route('/update_especialista/<int:id>', methods=['PUT'])
def update_especialista(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    especialista.id_especialidad = request.json.get('id_especialidad')
    especialista.n_licencia = request.json.get('n_licencia')
    especialista.activo = request.json.get('activo')
    especialista.id_persona = request.json.get('id_persona')
    especialista.id_usuario = request.json.get('id_usuario')

    #contrasenia = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())

    db.session.commit()

    result = especialista_schema.dump(especialista)

    data = {
        'message': 'Especialista actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialista_routes.route('/delete_especialista/<int:id>', methods=['DELETE'])
def delete_especialista(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(especialista)
    db.session.commit()

    data = {
        'message': 'Especialista eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)