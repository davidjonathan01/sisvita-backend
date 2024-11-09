from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.idioma import Idioma
from schemas.idioma_schema import idioma_schema, idiomas_schema

idioma_routes = Blueprint("idioma_routes", __name__)

@idioma_routes.route('/create_idioma', methods=['POST'])
def create_idioma():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    new_idioma = Idioma(nombre=nombre, descripcion=descripcion)

    db.session.add(new_idioma)
    db.session.commit()

    result = idioma_schema.dump(new_idioma)

    data = {
        'message': 'Nuevo idioma registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@idioma_routes.route('/get_idiomas', methods=['GET'])
def get_idiomas():
    all_idiomas = Idioma.query.all()

    if not all_idiomas:
        data = {
            'message': 'No se encontraron registros de idiomas',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = idiomas_schema.dump(all_idiomas)

    data = {
        'message': 'Todos los registros de idiomas han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@idioma_routes.route('/get_idioma/<int:id>', methods=['GET'])
def get_idioma(id):
    idioma = Idioma.query.get(id)

    if not idioma:
        data = {
            'message': 'Idioma no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = idioma_schema.dump(idioma)

    data = {
        'message': 'Idioma encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@idioma_routes.route('/update_idioma/<int:id>', methods=['PUT'])
def update_idioma(id):
    idioma = Idioma.query.get(id)

    if not idioma:
        data = {
            'message': 'Idioma no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    idioma.nombre = request.json.get('nombre')
    idioma.descripcion = request.json.get('descripcion')

    db.session.commit()

    result = idioma_schema.dump(idioma)

    data = {
        'message': 'Idioma actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@idioma_routes.route('/delete_idioma/<int:id>', methods=['DELETE'])
def delete_idioma(id):
    idioma = Idioma.query.get(id)

    if not idioma:
        data = {
            'message': 'Idioma no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(idioma)
    db.session.commit()

    data = {
        'message': 'Idioma eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)