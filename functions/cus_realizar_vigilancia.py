import datetime
from utils.db import db
from utils.mail import send_mail


from flask import Blueprint, jsonify, make_response, request
from models.pregunta import Pregunta
from models.test import Test
from models.opcion import Opcion
from models.evaluacion import Evaluacion
from models.resultado import Resultado
from models.invitacion import Invitacion
from models.escala import Escala
from models.estado import Estado
from models.tipo_test import Tipo_test
from schemas.tipo_test_schema import tipo_test_schema, tipos_test_schema
from schemas.estado_schema import estado_schema, estados_schema
from schemas.escala_schema import escala_schema, escalas_schema
from schemas.invitacion_schema import invitacion_schema, invitaciones_schema
from schemas.resultado_schema import resultado_schema, resultados_schema
from schemas.evaluacion_schema import evaluacion_schema, evaluaciones_schema
from schemas.opcion_schema import opcion_schema, opciones_schema
from schemas.test_schema import test_schema, tests_schema
from schemas.pregunta_schema import pregunta_schema, preguntas_schema


cus_realizar_vigilancia= Blueprint('cus_realizar_vigilancia', __name__)

@cus_realizar_vigilancia.route('/resultados_especialista/<int:id_especialista>', methods=['GET'])
def obtener_resultados_especialista(id_especialista):
    resultados = Resultado.query.filter_by(id_especialista=id_especialista).all()
    result = resultados_schema.dump(resultados, many=True)

    data = {
        'message': 'Resultados obtenidos correctamente',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)

@cus_realizar_vigilancia.route('/update_resultado/<int:id>', methods=['PUT'])
def update_resultado(id):
    resultado = Resultado.query.get(id)
    if not resultado:
        data = {
            'message': 'Resultado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    id_escala = request.json.get('id_escala')
    observacion = request.json.get('observacion')
    informe = request.json.get('informe')
    recomendacion = request.json.get('recomendacion')
    
    if id_escala:
        resultado.id_escala = id_escala
    if observacion:
        resultado.observacion = observacion
    if informe:
        resultado.informe = informe
    if recomendacion:
        resultado.recomendacion = recomendacion
        
    resultado.id_estado = 5
    resultado.fec_interpretacion = datetime.date.today()
    
    db.session.commit()
    result = resultado_schema.dump(resultado)

    data = {
        'message': 'Resultado actualizado!',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)

@cus_realizar_vigilancia.route('/get_tests', methods=['GET'])
def get_tests():
    all_tests = Test.query.all()
    result = tests_schema.dump(all_tests)

    data = {
        'message': 'Todos los tests han sido encontrados',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)

@cus_realizar_vigilancia.route('/invitar_test', methods=['POST'])
def invitar_test():
    data = request.get_json()
    id_resultado = data.get('id_resultado')
    id_test = data.get('id_test')
    id_especialista = data.get('id_especialista')

    print(id_especialista)
    print(id_resultado)
    print(id_test)

    if not id_resultado or not id_test or not id_especialista:
        return jsonify({
            'message': 'Datos incompletos',
            'status': 400
        }), 400

    # Lógica para crear una nueva invitación para el resultado con el test seleccionado
    new_invitacion = Invitacion(
        id_especialista=id_especialista,
        id_resultado=id_resultado,
        id_test=id_test,
        fec_invitacion=datetime.date.today()
    )

    db.session.add(new_invitacion)
    db.session.commit()

    result = invitacion_schema.dump(new_invitacion)
    
    data = {
        'message': 'Test invitado correctamente',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)


@cus_realizar_vigilancia.route('/get_escalas_by_test/<int:id_test>', methods=['GET'])
def get_escalas_by_test(id_test):
    escalas = Escala.query.filter_by(id_test=id_test).all()
    result = escalas_schema.dump(escalas, many=True)

    data = {
        'message': 'Escalas obtenidas correctamente',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)


@cus_realizar_vigilancia.route('/get_tipo_tests', methods=['GET'])
def get_tipo_tests():
    all_tipo_tests = Tipo_test.query.all()
    result = tipos_test_schema.dump(all_tipo_tests)

    data = {
        'message': 'Todos los tipos de tests han sido encontrados',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@cus_realizar_vigilancia.route('/enviar_correo', methods=['POST'])
def enviar_correo():
    data = request.json
    correo = data.get('correo')
    mensaje = data.get('mensaje')
    
    if not correo or not mensaje:
        return jsonify({'message': 'Datos incompletos', 'status': 400}), 400

    print(correo)
    print(mensaje)
    try:
        send_mail(correo, 'Resultados de tu evaluación', mensaje)
        return jsonify({'message': 'Correo enviado correctamente', 'status': 200}), 200
    except Exception as e:
        return jsonify({'message': f'Error al enviar correo: {e}', 'status': 500}), 500