# insert / update / delete / select / select_all
import bcrypt

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.paciente import Paciente
from schemas.paciente_schema import paciente_schema, pacientes_schema

paciente_routes = Blueprint("paciente_routes", __name__)

@paciente_routes.route('/create_paciente', methods=['POST'])
def create_paciente():
    id_ubigeo = request.json.get('id_ubigeo')
    id_condicion = request.json.get('id_condicion')
    id_carrera = request.json.get('id_carrera')
    id_persona = request.json.get('id_persona')
    id_usuario = request.json.get('id_usuario')

    #contrasenia = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    #print(contrasenia)

    new_paciente = Paciente(id_ubigeo=id_ubigeo, id_condicion=id_condicion, id_carrera=id_carrera, id_persona=id_persona, id_usuario=id_usuario)

    db.session.add(new_paciente)
    db.session.commit()

    result = paciente_schema.dump(new_paciente)

    data = {
        'message': 'Nuevo paciente registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@paciente_routes.route('/get_pacientes', methods=['GET'])
def get_pacientes():
    all_pacientes = Paciente.query.all()

    if not all_pacientes:
        data = {
            'message': 'No se encontraron registros de pacientes',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = pacientes_schema.dump(all_pacientes)

    data = {
        'message': 'Todos los registros de pacientes han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@paciente_routes.route('/get_paciente/<int:id>', methods=['GET'])
def get_paciente(id):
    paciente = Paciente.query.get(id)

    if not paciente:
        data = {
            'message': 'Paciente no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = paciente_schema.dump(paciente)

    data = {
        'message': 'Paciente encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@paciente_routes.route('/update_paciente/<int:id>', methods=['PUT'])
def update_paciente(id):
    paciente = Paciente.query.get(id)

    if not paciente:
        data = {
            'message': 'Paciente no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_ubigeo = request.json.get('id_ubigeo')
    id_condicion = request.json.get('id_condicion')
    id_carrera = request.json.get('id_carrera')
    id_persona = request.json.get('id_persona')
    id_usuario = request.json.get('id_usuario')

    #contrasenia = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())

    paciente.id_ubigeo = id_ubigeo
    paciente.id_condicion = id_condicion
    paciente.id_carrera = id_carrera
    paciente.id_persona = id_persona
    paciente.id_usuario = id_usuario

    db.session.commit()

    result = paciente_schema.dump(paciente)

    data = {
        'message': 'Paciente actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@paciente_routes.route('/delete_paciente/<int:id>', methods=['DELETE'])
def delete_paciente(id):
    paciente = Paciente.query.get(id)

    if not paciente:
        data = {
            'message': 'Paciente no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(paciente)
    db.session.commit()

    data = {
        'message': 'Paciente eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)