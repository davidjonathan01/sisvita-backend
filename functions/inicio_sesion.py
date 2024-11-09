from flask import Blueprint, jsonify, make_response, request
from models.tipo_usuario import Tipo_usuario
from schemas.tipo_usuario_schema import tipo_usuario_schema, tipos_usuario_schema
from models.usuario import Usuario
from models.paciente import Paciente
from models.especialista import Especialista
from models.administrador import Administrador
from functions.contrasena import check_password, hash_password

cus_routes10 = Blueprint('cus_routes10', __name__)

@cus_routes10.route('/login', methods=['POST'])
def login():
    print('Solicitud de inicio de sesión recibida')
    data = request.get_json()
    email = data.get('email')
    contrasenia = data.get('contrasenia')
    id_tipo_usuario = data.get('id_tipo_usuario')
    
    print(email)
    print(contrasenia)
    print(id_tipo_usuario)
    print(type(id_tipo_usuario))  # Verificar el tipo de dato

    try:
        id_tipo_usuario = int(id_tipo_usuario)  # Convertir a entero
    except ValueError:
        data = {
            'message': 'Tipo de usuario inválido',
            'status': 400
        }
        return make_response(jsonify(data), 400)

    hashed_password = hash_password(contrasenia)
    valida_contraseña = check_password(hashed_password, contrasenia) # true or false

    usuario = Usuario.query.filter_by(email=email, contrasenia=contrasenia, id_tipo_usuario=id_tipo_usuario).first()

    if not usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    if id_tipo_usuario == 1:  # Paciente
        paciente = Paciente.query.filter_by(id_usuario=usuario.id_usuario).first()
        if not paciente:
            data = {
                'message': 'Paciente no encontrado para el usuario autenticado',
                'status': 404
            }
            return make_response(jsonify(data), 404)
        data = {
            'message': 'Usuario autenticado correctamente',
            'status': 200,
            'id_tipo_usuario': usuario.id_tipo_usuario,
            'id_usuario': usuario.id_usuario,
            'id_paciente': paciente.id_paciente
        }
        print(data)

    elif id_tipo_usuario == 2:  # Especialista
        especialista = Especialista.query.filter_by(id_usuario=usuario.id_usuario).first()
        if not especialista:
            data = {
                'message': 'Especialista no encontrado para el usuario autenticado',
                'status': 404
            }
            return make_response(jsonify(data), 404)
        data = {
            'message': 'Usuario autenticado correctamente',
            'status': 200,
            'id_tipo_usuario': usuario.id_tipo_usuario,
            'id_usuario': usuario.id_usuario,
            'id_especialista': especialista.id_especialista
        }
        print(data)

    elif id_tipo_usuario == 3:  # Administrador
        administrador = Administrador.query.filter_by(id_usuario=usuario.id_usuario).first()
        if not administrador:
            data = {
                'message': 'Administrador no encontrado para el usuario autenticado',
                'status': 404
            }
            return make_response(jsonify(data), 404)
        data = {
            'message': 'Usuario autenticado correctamente',
            'status': 200,
            'id_tipo_usuario': usuario.id_tipo_usuario,
            'id_usuario': usuario.id_usuario,
            'id_administrador': administrador.id_administrador
        }
        print(data)
    else:
        print('El tipo de usuario no coincide con ninguno de los valores esperados.')
        data = {
            'message': 'Tipo de usuario no coincide con los valores esperados',
            'status': 400
        }
        return make_response(jsonify(data), 400)

    return make_response(jsonify(data), 200)


@cus_routes10.route('/tipo_usuarios', methods=['GET'])
def get_tipo_usuarios():
    tipos_usuarios = Tipo_usuario.query.all()  # Obtener todos los tipos de usuario
    result = tipos_usuario_schema.dump(tipos_usuarios)  # Utilizar el schema para serializar todas los tipos de usuario

    data = {
        'message': 'Lista de tipos de usuario',
        'status': 200,
        'data': result
    }
    print(data)

    return make_response(jsonify(data), 200)
