from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.indicacion import Indicacion
from schemas.indicacion_schema import indicacion_schema, indicaciones_schema

indicacion_routes = Blueprint("indicacion_routes", __name__)

@indicacion_routes.route('/create_indicacion', methods=['POST'])
def create_indicacion():
    id_tratamiento = request.json.get('id_tratamiento')
    orden = request.json.get('orden')
    descripcion = request.json.get('descripcion')

    new_indicacion = Indicacion(id_tratamiento=id_tratamiento, orden=orden, descripcion=descripcion)

    db.session.add(new_indicacion)
    db.session.commit()

    result = indicacion_schema.dump(new_indicacion)

    data = {
        'message': 'Nueva indicacion registrada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@indicacion_routes.route('/get_indicaciones', methods=['GET'])
def get_indicaciones():
    all_indicaciones = Indicacion.query.all()

    if not all_indicaciones:
        data = {
            'message': 'No se encontraron registros de indicaciones',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = indicaciones_schema.dump(all_indicaciones)

    data = {
        'message': 'Todos los registros de indicaciones han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@indicacion_routes.route('/get_indicacion/<int:id>', methods=['GET'])
def get_indicacion(id):
    indicacion = Indicacion.query.get(id)

    if not indicacion:
        data = {
            'message': 'Indicacion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = indicacion_schema.dump(indicacion)

    data = {
        'message': 'Indicacion encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@indicacion_routes.route('/update_indicacion/<int:id>', methods=['PUT'])
def update_indicacion(id):
    indicacion = Indicacion.query.get(id)

    if not indicacion:
        data = {
            'message': 'Indicacion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    indicacion.id_tratamiento = request.json.get('id_tratamiento')
    indicacion.orden = request.json.get('orden')
    indicacion.descripcion = request.json.get('descripcion')

    db.session.commit()

    result = indicacion_schema.dump(indicacion)

    data = {
        'message': 'Indicacion actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@indicacion_routes.route('/delete_indicacion/<int:id>', methods=['DELETE'])
def delete_indicacion(id):
    indicacion = Indicacion.query.get(id)

    if not indicacion:
        data = {
            'message': 'Indicacion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(indicacion)
    db.session.commit()

    data = {
        'message': 'Indicacion eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)