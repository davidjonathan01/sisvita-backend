from flask import Blueprint, jsonify, make_response, request
from models.tipo_usuario import Tipo_usuario
from schemas.tipo_usuario_schema import tipo_usuario_schema, tipos_usuario_schema
from models.usuario import Usuario
from models.paciente import Paciente
from models.especialista import Especialista
from models.administrador import Administrador
from schemas.administrador_schema import administrador_schema, administradores_schema
from schemas.especialista_schema import especialista_schema, especialistas_schema
from schemas.paciente_schema import paciente_schema, pacientes_schema

monstrar_perfil = Blueprint('monstrar_perfil', __name__)

@monstrar_perfil.route('/get_paciente/<int:idPaciente>', methods=['GET'])
def get_paciente(idPaciente):
    print(idPaciente)
    paciente = Paciente.query.filter_by(id_paciente=idPaciente).first()
    if not paciente:
        return make_response(jsonify({'message': 'Paciente no encontrado'}), 404)

    result = paciente_schema.dump(paciente)

    data = {
        'message': 'Paciente obtenido correctamente',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)

@monstrar_perfil.route('/get_especialista/<int:id_especialista>', methods=['GET'])
def get_especialista(id_especialista):
    especialista = Especialista.query.filter_by(id_especialista=id_especialista).first()
    if not especialista:
        return make_response(jsonify({'message': 'Especialista no encontrado'}), 404)

    result = especialista_schema.dump(especialista)
    
    data = {
        'message': 'Especialista obtenido correctamente',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)

@monstrar_perfil.route('/get_administrador/<int:id_administrador>', methods=['GET'])
def get_administrador(id_administrador):
    administrador = Administrador.query.filter_by(id_administrador=id_administrador).first()
    if not administrador:
        return make_response(jsonify({'message': 'Administrador no encontrado'}), 404)

    result = administrador_schema.dump(administrador)
    
    data = {
        'message': 'Administrador obtenido correctamente',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)