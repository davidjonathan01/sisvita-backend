# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.comentario import Comentario
from schemas.comentario_schema import comentario_schema, comentarios_schema

comentario_routes = Blueprint("comentario_routes", __name__)

@comentario_routes.route('/create_comentario', methods=['POST'])
def create_comentario():
    id_post = request.json.get('id_post')
    id_paciente = request.json.get('id_paciente')
    descripcion = request.json.get('descripcion')
    fec_publicacion = request.json.get('fec_publicacion')
    fec_edicion = request.json.get('fec_edicion')
    anonimo = request.json.get('anonimo')

    new_comentario = Comentario(id_post=id_post, id_paciente=id_paciente, descripcion=descripcion, fec_publicacion=fec_publicacion, fec_edicion=fec_edicion, anonimo=anonimo)

    db.session.add(new_comentario)
    db.session.commit()

    result = comentario_schema.dump(new_comentario)

    data = {
        'message': 'Nuevo comentario registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@comentario_routes.route('/get_comentarios', methods=['GET'])
def get_comentarios():
    all_comentarios = Comentario.query.all()

    if not all_comentarios:
        data = {
            'message': 'No se encontraron registros de comentarios',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = comentarios_schema.dump(all_comentarios)

    data = {
        'message': 'Todos los registros de comentarios han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@comentario_routes.route('/get_comentario/<int:id>', methods=['GET'])
def get_comentario(id):
    comentario = Comentario.query.get(id)

    if not comentario:
        data = {
            'message': 'Comentario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = comentario_schema.dump(comentario)

    data = {
        'message': 'Comentario encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@comentario_routes.route('/update_comentario/<int:id>', methods=['PUT'])
def update_comentario(id):
    comentario = Comentario.query.get(id)

    if not comentario:
        data = {
            'message': 'Comentario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_post = request.json.get('id_post')
    id_paciente = request.json.get('id_paciente')
    descripcion = request.json.get('descripcion')
    fec_publicacion = request.json.get('fec_publicacion')
    fec_edicion = request.json.get('fec_edicion')
    anonimo = request.json.get('anonimo')

    comentario.id_post = id_post
    comentario.id_paciente = id_paciente
    comentario.descripcion = descripcion
    comentario.fec_publicacion = fec_publicacion
    comentario.fec_edicion = fec_edicion
    comentario.anonimo = anonimo

    db.session.commit()

    result = comentario_schema.dump(comentario)

    data = {
        'message': '¡Comentario actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@comentario_routes.route('/delete_comentario/<int:id>', methods=['DELETE'])
def delete_comentario(id):
    #comentario = db.session.query(Comentario).get(id)
    comentario = Comentario.query.get(id)

    if not comentario:
        data = {
            'message': 'Comentario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(comentario)
    db.session.commit()

    data = {
        'message': 'Comentario eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)