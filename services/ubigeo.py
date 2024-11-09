from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.ubigeo import Ubigeo
from schemas.ubigeo_schema import ubigeo_schema, ubigeos_schema

ubigeo_routes = Blueprint("ubigeo_routes", __name__)

@ubigeo_routes.route('/create_ubigeo', methods=['POST'])
def create_ubigeo():
    codigo = request.json.get('codigo')
    departamento = request.json.get('departamento')
    provincia = request.json.get('provincia')
    distrito = request.json.get('distrito')
    latitud = request.json.get('latitud')
    longitud = request.json.get('longitud')

    new_ubigeo = Ubigeo(codigo=codigo, departamento=departamento, provincia=provincia, distrito=distrito, latitud=latitud, longitud=longitud)

    db.session.add(new_ubigeo)
    db.session.commit()

    result = ubigeo_schema.dump(new_ubigeo)

    data = {
        'message': 'Nuevo ubigeo registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@ubigeo_routes.route('/get_ubigeos', methods=['GET'])
def get_ubigeos():
    all_ubigeos = Ubigeo.query.all()

    if not all_ubigeos:
        data = {
            'message': 'No se encontraron registros de ubigeos',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = ubigeos_schema.dump(all_ubigeos)

    data = {
        'message': 'Todos los registros de ubigeos han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/get_ubigeo/<int:id>', methods=['GET'])
def get_ubigeo(id):
    ubigeo = Ubigeo.query.get(id)

    if not ubigeo:
        data = {
            'message': 'Ubigeo no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = ubigeo_schema.dump(ubigeo)

    data = {
        'message': 'Ubigeo encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/update_ubigeo/<int:id>', methods=['PUT'])
def update_ubigeo(id):
    ubigeo = Ubigeo.query.get(id)

    if not ubigeo:
        data = {
            'message': 'Ubigeo no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    ubigeo.codigo = request.json.get('codigo')
    ubigeo.departamento = request.json.get('departamento')
    ubigeo.provincia = request.json.get('provincia')
    ubigeo.distrito = request.json.get('distrito')
    ubigeo.latitud = request.json.get('latitud')
    ubigeo.longitud = request.json.get('longitud')

    db.session.commit()

    result = ubigeo_schema.dump(ubigeo)

    data = {
        'message': 'Ubigeo actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/delete_ubigeo/<int:id>', methods=['DELETE'])
def delete_ubigeo(id):
    ubigeo = Ubigeo.query.get(id)

    if not ubigeo:
        data = {
            'message': 'Ubigeo no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(ubigeo)
    db.session.commit()

    data = {
        'message': 'Ubigeo eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)