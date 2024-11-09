from datetime import datetime
from models.escala import Escala
from models.evaluacion import Evaluacion
from models.paciente import Paciente
from models.resultado import Resultado
from models.test import Test
from utils.db import db
from flask import Blueprint, jsonify, make_response, request
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize, LinearSegmentedColormap

cus_routes3 = Blueprint('cus_routes3', __name__)
@cus_routes3.route('/mapear_casos', methods=['POST'])
def mapear_casos():
    # Obtener datos de la solicitud
    data = request.get_json()
    lista_pacientes = data.get('lista_pacientes')
    id_test = data.get('id_test')

    # Guardar la fecha actual
    fec_realizacion = datetime.now()
    pacientes_encontrados = []
    pacientes_no_encontrados = []

    # Verificar si el test existe
    test = Test.query.get(id_test)
    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    # Obtener las escalas asociadas al test
    escalas = Escala.query.filter_by(id_test=id_test).all()
    if not escalas:
        data = {
            'message': 'No hay escalas asociadas al test',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    # Buscar evaluaciones asociadas al test y a los pacientes de la lista
    escalas_resultantes = {}
    for paciente_data in lista_pacientes:
        id_paciente = paciente_data.get('id_paciente')

        paciente = Paciente.query.get(id_paciente)
        if not paciente:
            pacientes_no_encontrados.append(id_paciente)
            continue

        pacientes_encontrados.append(id_paciente)

        evaluaciones = Evaluacion.query.filter_by(id_test=id_test, id_paciente=id_paciente).all()
        for evaluacion in evaluaciones:
            resultados = Resultado.query.filter_by(id_evaluacion=evaluacion.id_evaluacion).all()
            for resultado in resultados:
                id_escala = resultado.id_escala

                if id_escala in escalas_resultantes:
                    escalas_resultantes[id_escala].append(paciente.ubigeo)  # Asumiendo que ubigeo es un campo válido en Paciente
                else:
                    escalas_resultantes[id_escala] = [paciente.ubigeo]

    # Calcular colores utilizando matplotlib
    cmap = plt.cm.get_cmap('RdYlGn', len(escalas))  # Seleccionamos el mapa de colores RdYlGn (Rojo a Verde)
    norm = Normalize(vmin=0, vmax=len(escalas) - 1)

    resultado_mapa = {}
    for idx, (id_escala, ubicaciones) in enumerate(escalas_resultantes.items()):
        escala = Escala.query.get(id_escala)
        color = cmap(norm(idx))  # Asignamos un color de acuerdo a la escala y su posición en la lista

        resultado_mapa[escala.nombre] = {
            'ubicaciones': ubicaciones,
            'color': color
        }

    # Devolver respuesta JSON
    data = {
        'message': 'Mapa de calor generado correctamente',
        'status': 200,
        'resultados': resultado_mapa
    }

    return make_response(jsonify(data), 200)
