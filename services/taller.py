from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.taller import Taller
from schemas.taller_schema import taller_schema, talleres_schema

taller_routes = Blueprint("taller_routes", __name__)

@taller_routes.route('/create_taller', methods=['POST'])
def create_taller():
    nombre = request.json.get('nombre')
    id_especialista = request.json.get('id_especialista')
    n_vacantes = request.json.get('n_vacantes')
    fec_inicio = request.json.get('fec_inicio')
    fec_fin = request.json.get('fec_fin')
    id_modalidad = request.json.get('id_modalidad')
    id_estado = request.json.get('id_estado')

    new_taller = Taller(nombre=nombre, id_especialista=id_especialista, n_vacantes=n_vacantes, fec_inicio=fec_inicio, fec_fin=fec_fin, id_modalidad=id_modalidad, id_estado=id_estado)

    db.session.add(new_taller)
    db.session.commit()

    result = taller_schema.dump(new_taller)

    data = {
        'message': 'Nuevo taller registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@taller_routes.route('/get_talleres', methods=['GET'])
def get_talleres():
    all_talleres = Taller.query.all()

    if not all_talleres:
        data = {
            'message': 'No se encontraron registros de talleres',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = talleres_schema.dump(all_talleres)

    data = {
        'message': 'Todos los registros de talleres han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@taller_routes.route('/get_taller/<int:id>', methods=['GET'])
def get_taller(id):
    taller = Taller.query.get(id)

    if not taller:
        data = {
            'message': 'Taller no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = taller_schema.dump(taller)

    data = {
        'message': 'Taller encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@taller_routes.route('/update_taller/<int:id>', methods=['PUT'])
def update_taller(id):
    taller = Taller.query.get(id)

    if not taller:
        data = {
            'message': 'Taller no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')
    id_especialista = request.json.get('id_especialista')
    n_vacantes = request.json.get('n_vacantes')
    fec_inicio = request.json.get('fec_inicio')
    fec_fin = request.json.get('fec_fin')
    id_modalidad = request.json.get('id_modalidad')
    id_estado = request.json.get('id_estado')

    taller.nombre = nombre
    taller.id_especialista = id_especialista
    taller.n_vacantes = n_vacantes
    taller.fec_inicio = fec_inicio
    taller.fec_fin = fec_fin
    taller.id_modalidad = id_modalidad
    taller.id_estado = id_estado

    db.session.commit()

    result = taller_schema.dump(taller)

    data = {
        'message': 'Taller actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@taller_routes.route('/delete_taller/<int:id>', methods=['DELETE'])
def delete_taller(id):
    taller = Taller.query.get(id)

    if not taller:
        data = {
            'message': 'Taller no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(taller)
    db.session.commit()

    data = {
        'message': 'Taller eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)