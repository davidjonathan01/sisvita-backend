# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.dia import Dia
from schemas.dia_schema import dia_schema, dias_schema

dia_routes = Blueprint("dia_routes", __name__)

@dia_routes.route('/create_dia', methods=['POST'])
def create_dia():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    new_dia = Dia(nombre=nombre, descripcion=descripcion)

    db.session.add(new_dia)
    db.session.commit()

    result = dia_schema.dump(new_dia)

    data = {
        'message': 'Nuevo dia registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@dia_routes.route('/get_dias', methods=['GET'])
def get_dias():
    all_dias = Dia.query.all()

    if not all_dias:
        data = {
            'message': 'No se encontraron registros de dias',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = dias_schema.dump(all_dias)

    data = {
        'message': 'Todos los registros de dias han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@dia_routes.route('/get_dia/<int:id>', methods=['GET'])
def get_dia(id):
    dia = Dia.query.get(id)

    if not dia:
        data = {
            'message': 'Dia no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = dia_schema.dump(dia)

    data = {
        'message': 'Dia encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@dia_routes.route('/update_dia/<int:id>', methods=['PUT'])
def update_dia(id):
    dia = Dia.query.get(id)

    if not dia:
        data = {
            'message': 'Dia no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    dia.nombre = nombre
    dia.descripcion = descripcion

    db.session.commit()

    result = dia_schema.dump(dia)

    data = {
        'message': 'Dia actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@dia_routes.route('/delete_dia/<int:id>', methods=['DELETE'])
def delete_dia(id):
    dia = Dia.query.get(id)

    if not dia:
        data = {
            'message': 'Dia no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(dia)
    db.session.commit()

    data = {
        'message': 'Dia eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)