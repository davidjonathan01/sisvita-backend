# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.genero import Genero
from schemas.genero_schema import genero_schema, generos_schema

genero_routes = Blueprint("genero_routes", __name__)

@genero_routes.route('/create_genero', methods=['POST'])
def create_genero():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    new_genero = Genero(nombre=nombre, descripcion=descripcion)

    db.session.add(new_genero)
    db.session.commit()

    result = genero_schema.dump(new_genero)

    data = {
        'message': 'Nuevo género registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@genero_routes.route('/get_generos', methods=['GET'])
def get_generos():
    all_generos = Genero.query.all()

    if not all_generos:
        data = {
            'message': 'No se encontraron registros de géneros',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = generos_schema.dump(all_generos)

    data = {
        'message': 'Todos los registros de géneros han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@genero_routes.route('/get_genero/<int:id>', methods=['GET'])
def get_genero(id):
    genero = Genero.query.get(id)

    if not genero:
        data = {
            'message': 'Género no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = genero_schema.dump(genero)

    data = {
        'message': 'Género encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@genero_routes.route('/update_genero/<int:id>', methods=['PUT'])
def update_genero(id):
    genero = Genero.query.get(id)

    if not genero:
        data = {
            'message': 'Género no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    genero.nombre = nombre
    genero.descripcion = descripcion

    db.session.commit()

    result = genero_schema.dump(genero)

    data = {
        'message': 'Género actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@genero_routes.route('/delete_genero/<int:id>', methods=['DELETE'])
def delete_genero(id):
    genero = Genero.query.get(id)

    if not genero:
        data = {
            'message': 'Género no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(genero)
    db.session.commit()

    data = {
        'message': 'Género eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)