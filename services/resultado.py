from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.resultado import Resultado
from schemas.resultado_schema import resultado_schema, resultados_schema

resultado_routes = Blueprint("resultado_routes", __name__)

@resultado_routes.route('/create_resultado', methods=['POST'])
def create_resultado():
    id_evaluacion = request.json.get('id_evaluacion')
    id_especialista = request.json.get('id_especialista')
    id_estado = request.json.get('id_estado')
    id_escala = request.json.get('id_escala')
    fec_interpretacion = request.json.get('fec_interpretacion')
    observacion = request.json.get('observacion')
    informe = request.json.get('informe')
    recomendacion = request.json.get('recomendacion')
    
    new_resultado = Resultado(id_evaluacion=id_evaluacion, id_especialista=id_especialista, id_estado=id_estado, id_escala=id_escala, fec_interpretacion=fec_interpretacion, observacion=observacion, informe=informe, recomendacion=recomendacion)

    db.session.add(new_resultado)
    db.session.commit()

    result = resultado_schema.dump(new_resultado)

    data = {
        'message': 'Nuevo resultado registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@resultado_routes.route('/get_resultados', methods=['GET'])
def get_resultados():
    all_resultados = Resultado.query.all()

    if not all_resultados:
        data = {
            'message': 'No se encontraron registros de resultados',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = resultados_schema.dump(all_resultados)

    data = {
        'message': 'Todos los registros de resultados han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@resultado_routes.route('/get_resultado/<int:id>', methods=['GET'])
def get_resultado(id):
    resultado = Resultado.query.get(id)

    if not resultado:
        data = {
            'message': 'Resultado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = resultado_schema.dump(resultado)

    data = {
        'message': 'Resultado encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@resultado_routes.route('/update_resultado/<int:id>', methods=['PUT'])
def update_resultado(id):
    resultado = Resultado.query.get(id)

    if not resultado:
        data = {
            'message': 'Resultado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    resultado.id_evaluacion = request.json.get('id_evaluacion')
    resultado.id_especialista = request.json.get('id_especialista')
    resultado.id_estado = request.json.get('id_estado')
    resultado.id_escala = request.json.get('id_escala')
    resultado.fec_interpretacion = request.json.get('fec_interpretacion')
    resultado.observacion = request.json.get('observacion')
    resultado.informe=request.json.get('informe')
    resultado.recomendacion=request.json.get('recomendacion')

    db.session.commit()

    result = resultado_schema.dump(resultado)

    data = {
        'message': 'Resultado actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@resultado_routes.route('/delete_resultado/<int:id>', methods=['DELETE'])
def delete_resultado(id):
    resultado = Resultado.query.get(id)

    if not resultado:
        data = {
            'message': 'Resultado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(resultado)
    db.session.commit()

    data = {
        'message': 'Resultado eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)