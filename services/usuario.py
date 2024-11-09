from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.usuario import Usuario
from schemas.usuario_schema import usuario_schema, usuarios_schema
from functions.contrasena import hash_password

usuario_routes = Blueprint("usuario_routes", __name__)

@usuario_routes.route('/create_usuario', methods=['POST'])
def create_usuario():
    
    email = request.json.get('email')
    contrasenia = request.json.get('contrasenia')
    id_tipo_usuario = request.json.get('id_tipo_usuario')

    # Encriptar contrasenia
    contrasenia = hash_password(contrasenia)

    new_usuario = Usuario(email=email, contrasenia=contrasenia, id_tipo_usuario=id_tipo_usuario)

    db.session.add(new_usuario)
    db.session.commit()

    result = usuario_schema.dump(new_usuario)

    data = {
        'message': 'Nuevo usuario registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@usuario_routes.route('/get_usuarios', methods=['GET'])
def get_usuarios():
    all_usuarios = Usuario.query.all()

    if not all_usuarios:
        data = {
            'message': 'No se encontraron usuarios',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = usuarios_schema.dump(all_usuarios)

    data = {
        'message': 'Todos los usuarios han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@usuario_routes.route('/get_usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = usuario_schema.dump(usuario)

    data = {
        'message': 'Usuario encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@usuario_routes.route('/update_usuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    usuario.email = request.json.get('email')
    contrasenia = request.json.get('contrasenia')

    # Encriptar contrasenia
    usuario.contrasenia = hash_password(contrasenia)
    
    usuario.id_tipo_usuario = request.json.get('id_tipo_usuario')

    db.session.commit()

    result = usuario_schema.dump(usuario)

    data = {
        'message': 'Usuario actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@usuario_routes.route('/delete_usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)

    db.session.delete(usuario)
    db.session.commit()

    data = {
        'message': 'Usuario eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)