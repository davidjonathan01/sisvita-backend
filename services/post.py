from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.post import Post
from schemas.post_schema import post_schema, posts_schema

post_routes = Blueprint("post_routes", __name__)

@post_routes.route('/create_post', methods=['POST'])
def create_post():
    id_paciente = request.json.get('id_paciente')
    descripcion = request.json.get('descripcion')
    fec_publicacion = request.json.get('fec_publicacion')
    fec_edicion = request.json.get('fec_edicion')
    anonimo = request.json.get('anonimo')

    new_post = Post(id_paciente=id_paciente, descripcion=descripcion, fec_publicacion=fec_publicacion, fec_edicion=fec_edicion, anonimo=anonimo)

    db.session.add(new_post)
    db.session.commit()

    result = post_schema.dump(new_post)

    data = {
        'message': 'Nuevo post registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@post_routes.route('/get_posts', methods=['GET'])
def get_posts():
    all_posts = Post.query.all()

    if not all_posts:
        data = {
            'message': 'No se encontraron registros de posts',
            'status': 404
        }
        return make_response(jsonify(data), 404)
                                     
    result = posts_schema.dump(all_posts)

    data = {
        'message': 'Todos los registros de posts han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@post_routes.route('/get_post/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get(id)

    if not post:
        data = {
            'message': 'Post no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = post_schema.dump(post)

    data = {
        'message': 'Post encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@post_routes.route('/update_post/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get(id)

    post.id_paciente = request.json.get('id_paciente')
    post.descripcion = request.json.get('descripcion')
    post.fec_publicacion = request.json.get('fec_publicacion')
    post.fec_edicion = request.json.get('fec_edicion')
    post.anonimo = request.json.get('anonimo')

    db.session.commit()

    result = post_schema.dump(post)

    data = {
        'message': 'Post actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@post_routes.route('/delete_post/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)

    if not post:
        data = {
            'message': 'Post no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(post)
    db.session.commit()

    data = {
        'message': 'Post eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)