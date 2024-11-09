from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.escala import Escala
from schemas.escala_schema import escala_schema, escalas_schema

escala_routes = Blueprint("escala_routes", __name__)

@escala_routes.route('/create_escala', methods=['POST'])
def create_escala():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')
    id_test = request.json.get('id_test')
    puntaje_min = request.json.get('puntaje_min')
    puntaje_max = request.json.get('puntaje_max')

    new_escala = Escala(nombre=nombre, descripcion=descripcion, id_test=id_test, puntaje_min=puntaje_min, puntaje_max=puntaje_max)

    db.session.add(new_escala)
    db.session.commit()

    result = escala_schema.dump(new_escala)

    data = {
        'message': 'Nueva escala registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@escala_routes.route('/get_escalas', methods=['GET'])
def get_escalas():
    all_escalas = Escala.query.all()

    if not all_escalas:
        data = {
            'message': 'No se encontraron registros de escalas',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = escalas_schema.dump(all_escalas)

    data = {
        'message': 'Todos los registros de escalas han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@escala_routes.route('/get_escala/<int:id>', methods=['GET'])
def get_escala(id):
    escala = Escala.query.get(id)
    result = escala_schema.dump(escala)

    data = {
        'message': 'Registro de escala encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@escala_routes.route('/update_escala/<int:id>', methods=['PUT'])
def update_escala(id):
    escala = Escala.query.get(id)

    if not escala:
        data = {
            'message': 'Escala no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    escala.nombre = request.json.get('nombre')
    escala.descripcion = request.json.get('descripcion')
    escala.id_test = request.json.get('id_test')
    escala.puntaje_min = request.json.get('puntaje_min')
    escala.puntaje_max = request.json.get('puntaje_max')

    db.session.commit()

    result = escala_schema.dump(escala)

    data = {
        'message': 'Escala actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@escala_routes.route('/delete_escala/<int:id>', methods=['DELETE'])
def delete_escala(id):
    escala = Escala.query.get(id)

    if not escala:
        data = {
            'message': 'Escala no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(escala)
    db.session.commit()

    data = {
        'message': 'Escala eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)