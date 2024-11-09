import datetime
from utils.db import db

from flask import Blueprint, jsonify, make_response, request
from models.pregunta import Pregunta
from models.test import Test
from models.opcion import Opcion
from models.evaluacion import Evaluacion
from models.resultado import Resultado
from models.invitacion import Invitacion
from schemas.invitacion_schema import invitacion_schema, invitaciones_schema
from schemas.resultado_schema import resultado_schema, resultados_schema
from schemas.evaluacion_schema import evaluacion_schema, evaluaciones_schema
from schemas.opcion_schema import opcion_schema, opciones_schema
from schemas.test_schema import test_schema, tests_schema
from schemas.pregunta_schema import pregunta_schema, preguntas_schema



cus_evaluar_resultados_test= Blueprint('cus_evaluar_resultados_test', __name__)

@cus_evaluar_resultados_test.route('/resultados_especialista/<int:id_especialista>', methods=['GET'])
def obtener_resultados_especialista(id_especialista):
    resultados = Resultado.query.filter_by(id_especialista=id_especialista).all()
    result = resultados_schema.dump(resultados, many=True)

    data = {
        'message': 'Resultados obtenidos correctamente',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)

@cus_evaluar_resultados_test.route('/update_resultado/<int:id>', methods=['PUT'])
def update_resultado(id):
    resultado = Resultado.query.get(id)
    if not resultado:
        data = {
            'message': 'Resultado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    observacion = request.json.get('observacion')
    
    if observacion:
        resultado.id_estado =5
        resultado.observacion = observacion
        resultado.fec_interpretacion = datetime.date.today()
    db.session.commit()
    result = resultado_schema.dump(resultado)

    data = {
        'message': 'Resultado actualizado!',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)

@cus_evaluar_resultados_test.route('/get_tests', methods=['GET'])
def get_tests():
    all_tests = Test.query.all()
    result = tests_schema.dump(all_tests)

    data = {
        'message': 'Todos los tests han sido encontrados',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)

@cus_evaluar_resultados_test.route('/invitar_test', methods=['POST'])
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