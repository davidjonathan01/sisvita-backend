import datetime
from utils.db import db


from flask import Blueprint, jsonify, make_response, request
from models.carrera import Carrera
from models.ubigeo import Ubigeo
from models.persona import Persona
from models.usuario import Usuario
from models.paciente import Paciente
from functions.contrasena import hash_password

from schemas.carrera_schema import carrera_schema, carreras_schema


registrar_paciente= Blueprint('registrar_paciente', __name__)
@registrar_paciente.route('/departamentos', methods=['GET'])
def get_departamentos():
    departamentos = db.session.query(Ubigeo.departamento).distinct().all()
    return jsonify({'data': [d[0] for d in departamentos]})

@registrar_paciente.route('/provincias/<departamento>', methods=['GET'])
def get_provincias(departamento):
    provincias = db.session.query(Ubigeo).filter_by(departamento=departamento).distinct(Ubigeo.provincia).all()
    return jsonify({'data': [{'provincia': p.provincia} for p in provincias]})

@registrar_paciente.route('/distritos/<provincia>', methods=['GET'])
def get_distritos(provincia):
    distritos = db.session.query(Ubigeo).filter_by(provincia=provincia).all()
    return jsonify({'data': [{'id_ubigeo': d.id_ubigeo, 'distrito': d.distrito} for d in distritos]})

@registrar_paciente.route('/carreras', methods=['GET'])
def get_carreras():
    carreras = Carrera.query.all()
    result = carreras_schema.dump(carreras, many=True)

    data = {
        'message': 'Carreras obtenidas correctamente',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)

@registrar_paciente.route('/registrar', methods=['POST'])
def registrar_paciente_func():
    data = request.json
    print("1")
    print(data)

    # Crear instancia de Persona
    doc_identidad = data.get('doc_identidad')
    nombres = data.get('nombres')
    apellidos = data.get('apellidos')
    fec_nacimiento = data.get('fec_nacimiento')
    id_genero = data.get('id_genero')
    num_telefono = data.get('num_telefono')

    nueva_persona = Persona(
        doc_identidad=doc_identidad,
        nombres=nombres,
        apellidos=apellidos,
        fec_nacimiento=fec_nacimiento,
        id_genero=id_genero,
        num_telefono=num_telefono
    )
    db.session.add(nueva_persona)
    db.session.commit()
    
    id_persona = nueva_persona.id_persona

    # Crear instancia de Usuario
    email = data.get('email')
    contrasenia = data.get('contrasenia')
    id_tipo_usuario = 1  # Suponiendo que es tipo paciente

    nueva_usuario = Usuario(
        email=email,
        contrasenia=hash_password(contrasenia),
        id_tipo_usuario=id_tipo_usuario
    )
    db.session.add(nueva_usuario)
    db.session.commit()
    
    id_usuario = nueva_usuario.id_usuario

    # Crear instancia de Paciente
    id_ubigeo = data.get('id_ubigeo')
    id_condicion = data.get('id_condicion')
    id_carrera = data.get('id_carrera') if id_condicion == '2' else None

    nuevo_paciente = Paciente(
        id_ubigeo=id_ubigeo,
        id_condicion=id_condicion,
        id_carrera=id_carrera,
        id_persona=id_persona,
        id_usuario=id_usuario
    )
    db.session.add(nuevo_paciente)
    db.session.commit()

    return make_response(jsonify({
        'message': 'Paciente registrado exitosamente',
        'status': 200
    }), 200)
