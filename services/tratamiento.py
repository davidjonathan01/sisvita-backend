from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.tratamiento import Tratamiento
from schemas.tratamiento_schema import tratamiento_schema, tratamientos_schema

tratamiento_routes = Blueprint("tratamiento_routes", __name__)

@tratamiento_routes.route('/create_tratamiento', methods=['POST'])
def create_tratamiento():
    id_resultado = request.json.get('id_resultado')
    objetivo = request.json.get('objetivo')
    fec_asignacion = request.json.get('fec_asignacion')
    fec_inicio = request.json.get('fec_inicio')
    fec_fin = request.json.get('fec_fin')
    id_estado = request.json.get('id_estado')
    observaciones = request.json.get('observaciones')

    new_tratamiento = Tratamiento(id_resultado=id_resultado, objetivo=objetivo, fec_asignacion=fec_asignacion, fec_inicio=fec_inicio, fec_fin=fec_fin, id_estado=id_estado, observaciones=observaciones)

    db.session.add(new_tratamiento)
    db.session.commit()

    result = tratamiento_schema.dump(new_tratamiento)

    data = {
        'message': 'Nuevo tratamiento registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@tratamiento_routes.route('/get_tratamientos', methods=['GET'])
def get_tratamientos():
    all_tratamientos = Tratamiento.query.all()

    if not all_tratamientos:
        data = {
            'message': 'No se encontraron registros de tratamientos',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = tratamientos_schema.dump(all_tratamientos)

    data = {
        'message': 'Todos los registros de tratamientos han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tratamiento_routes.route('/get_tratamiento/<int:id>', methods=['GET'])
def get_tratamiento(id):
    tratamiento = Tratamiento.query.get(id)

    if not tratamiento:
        data = {
            'message': 'Tratamiento no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = tratamiento_schema.dump(tratamiento)

    data = {
        'message': 'Tratamiento encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tratamiento_routes.route('/update_tratamiento/<int:id>', methods=['PUT'])
def update_tratamiento(id):
    tratamiento = Tratamiento.query.get(id)

    if not tratamiento:
        data = {
            'message': 'Tratamiento no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_resultado = request.json.get('id_resultado')
    objetivo = request.json.get('objetivo')
    fec_asignacion = request.json.get('fec_asignacion')
    fec_inicio = request.json.get('fec_inicio')
    fec_fin = request.json.get('fec_fin')
    id_estado = request.json.get('id_estado')
    observaciones = request.json.get('observaciones')

    tratamiento.id_resultado = id_resultado
    tratamiento.objetivo = objetivo
    tratamiento.fec_asignacion = fec_asignacion
    tratamiento.fec_inicio = fec_inicio
    tratamiento.fec_fin = fec_fin
    tratamiento.id_estado = id_estado
    tratamiento.observaciones = observaciones

    db.session.commit()

    result = tratamiento_schema.dump(tratamiento)

    data = {
        'message': 'Tratamiento actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tratamiento_routes.route('/delete_tratamiento/<int:id>', methods=['DELETE'])
def delete_tratamiento(id):
    tratamiento = Tratamiento.query.get(id)

    if not tratamiento:
        data = {
            'message': 'Tratamiento no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(tratamiento)
    db.session.commit()

    data = {
        'message': 'Tratamiento eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)