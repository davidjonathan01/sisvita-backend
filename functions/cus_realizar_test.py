import datetime
from utils.db import db

from flask import Blueprint, jsonify, make_response, request
from models.pregunta import Pregunta
from models.test import Test
from models.opcion import Opcion
from models.evaluacion import Evaluacion
from models.escala import Escala
from models.resultado import Resultado
from schemas.evaluacion_schema import evaluacion_schema, evaluaciones_schema
from schemas.opcion_schema import opcion_schema, opciones_schema
from schemas.test_schema import test_schema, tests_schema
from schemas.pregunta_schema import pregunta_schema, preguntas_schema


cus_realizar_test= Blueprint('cus_realizar_test', __name__)

@cus_realizar_test.route('/get_preguntas/<int:id_test>', methods=['GET'])
def get_preguntas_por_test(id_test):
    preguntas = Pregunta.query.filter_by(id_test=id_test).all()  # Obtener todas las preguntas para el id_test dado
    result = preguntas_schema.dump(preguntas)  # Utilizar el schema para serializar todas las preguntas

    data = {
        'message': 'Lista de preguntas del testss',
        'status': 200,
        'data': result
    }
    print(data)

    return make_response(jsonify(data), 200)


@cus_realizar_test.route('/get_opciones/<int:id_test>', methods=['GET'])
def get_opciones_por_test(id_test):
    opciones = Opcion.query.filter_by(id_test=id_test).all()  # Obtener todas las opciones para el id_test dado
    result = opciones_schema.dump(opciones)  # Utilizar el schema para serializar todas las opciones

    data = {
        'message': 'Lista de preguntas del testss',
        'status': 200,
        'data': result
    }
    print(data)

    return make_response(jsonify(data), 200)

# PARA LA FUNCION DETERMINAR ESCALA
def calcular_puntaje(respuestas):
    puntaje = 0

    # Convertir la cadena de texto en un arreglo evitando los espacios
    respuestas = respuestas
    
    # Verificar si las respuestas están separadas por comas o espacios y limpiar espacios adicionales
    if ',' in respuestas:
        respuestas = [int(respuesta.strip()) for respuesta in respuestas.split(',') if respuesta.strip() != '']
    else:
        respuestas = [int(respuesta.strip()) for respuesta in respuestas.split() if respuesta.strip() != '']

    for respuesta in respuestas:
        puntaje += respuesta
    
    return puntaje


@cus_realizar_test.route('/realizar_evaluacion', methods=['POST'])
def realizar_evaluacion():
    data = request.json
    print(data)
    id_test = data.get('id_test')
    id_paciente = data.get('id_paciente')
    id_especialista = data.get('id_especialista')  # Aceptar id_especialista desde el frontend
    respuestas_list = data.get('respuestas')

   # Convertir la lista de respuestas a una cadena de números separados por espacios
    respuestas_str = ' '.join(map(str, respuestas_list))

    # Calcular puntaje
    puntaje = calcular_puntaje(respuestas_str)
    print(puntaje)

    # Buscar las escalas asociadas a ese test
    escalas = Escala.query.filter_by(id_test=id_test)

    # Comparar el puntaje con el rango de cada escala
    for escala in escalas:
        if puntaje >= escala.puntaje_min and puntaje <= escala.puntaje_max:
            escala_elegida = escala
            break
        else:
            escala_elegida = None
    
    if not escala_elegida:
        data = {
            'message': 'Escala no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    

    # Crear una nueva instancia de Evaluacion
    new_evaluacion = Evaluacion(
        id_paciente=id_paciente,
        id_test=id_test,
        respuestas=respuestas_str,
        fec_realizacion=datetime.date.today(),
        puntaje=puntaje,
        id_escala=escala_elegida.id_escala

    )
    # Imprimir los datos de la nueva evaluación después de confirmar
    print("Nueva evaluación creada:", new_evaluacion)

    db.session.add(new_evaluacion)
    db.session.commit()
    print(new_evaluacion)

    # Asignar la evaluación a un especialista
    nuevo_resultado = Resultado(
        id_evaluacion=new_evaluacion.id_evaluacion,
        id_especialista=id_especialista,  # Usar el id_especialista proporcionado
        id_estado=4,  # Asigna que el estado inicial es 1, resultado aun no revisado
        id_escala=escala_elegida.id_escala,
        fec_interpretacion=None,
        observacion=None,
        informe=None,
        recomendacion=None
    )

    db.session.add(nuevo_resultado)
    db.session.commit()

    result= evaluacion_schema.dump(new_evaluacion)

    data = {
        'message': 'Evaluación realizada con éxito y asignada a un especialista',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)


