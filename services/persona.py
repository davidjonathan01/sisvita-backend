from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.persona import Persona
from schemas.persona_schema import persona_schema, personas_schema

persona_routes = Blueprint("persona_routes", __name__)

@persona_routes.route('/create_persona', methods=['POST'])
def create_persona():
    doc_identidad = request.json.get('doc_identidad')
    nombres = request.json.get('nombres')
    apellidos = request.json.get('apellidos')
    fec_nacimiento = request.json.get('fec_nacimiento')
    id_genero = request.json.get('id_genero')
    num_telefono = request.json.get('num_telefono')

    new_persona = Persona(doc_identidad=doc_identidad, nombres=nombres, apellidos=apellidos, fec_nacimiento=fec_nacimiento, id_genero=id_genero, num_telefono=num_telefono)

    db.session.add(new_persona)
    db.session.commit()

    result = persona_schema.dump(new_persona)

    data = {
        'message': 'Nueva persona registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@persona_routes.route('/get_personas', methods=['GET'])
def get_personas():
    personas = Persona.query.all()

    if not personas:
        data = {
            'message': 'No se encontraron registros de personas',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = personas_schema.dump(personas)

    data = {
        'message': 'Todos los registros de personas han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@persona_routes.route('/get_persona/<int:id>', methods=['GET'])
def get_persona(id):
    persona = Persona.query.get(id)

    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = persona_schema.dump(persona)

    data = {
        'message': 'Persona encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@persona_routes.route('/update_persona/<int:id>', methods=['PUT'])
def update_persona(id):
    persona = Persona.query.get(id)

    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    doc_identidad = request.json.get('doc_identidad')
    nombres = request.json.get('nombres')
    apellidos = request.json.get('apellidos')
    fec_nacimiento = request.json.get('fec_nacimiento')
    id_genero = request.json.get('id_genero')
    num_telefono = request.json.get('num_telefono')

    persona.doc_identidad = doc_identidad
    persona.nombres = nombres
    persona.apellidos = apellidos
    persona.fec_nacimiento = fec_nacimiento
    persona.id_genero = id_genero
    persona.num_telefono = num_telefono

    db.session.commit()

    result = persona_schema.dump(persona)

    data = {
        'message': 'Persona actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@persona_routes.route('/delete_persona/<int:id>', methods=['DELETE'])
def delete_persona(id):
    persona = Persona.query.get(id)

    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(persona)
    db.session.commit()

    data = {
        'message': 'Persona eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)
