from flask import Blueprint, jsonify, make_response, request

from models.ubigeo import Ubigeo

identificar_ubigeo_routes = Blueprint('identificar_ubigeo_routes', __name__)

@identificar_ubigeo_routes.route('/departamentos_unicos', methods=['GET'])
def identificar_departamentos_unicos():
    print('Solicitud para identificar departamentos únicos recibida')
    all_ubigeos = Ubigeo.query.all()

    if not all_ubigeos:
        data = {
            'message': 'No se encontraron registros de ubigeos',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    departamentos = []
    for ubigeo in all_ubigeos:
        if ubigeo.departamento not in departamentos:
            departamentos.append(ubigeo.departamento)
        
    data = {
        'message': 'Departamentos únicos identificados',
        'status': 200,
        'data': departamentos
    }

    return make_response(jsonify(data), 200)

@identificar_ubigeo_routes.route('/provincias_unicas', methods=['POST'])
def identificar_provincias_unicas(): # considerando la elección previa de un departamento
    print('Solicitud para identificar provincias únicas recibida')
    departamento = request.json.get('departamento')

    all_ubigeos = Ubigeo.query.all()

    if not all_ubigeos:
        data = {
            'message': 'No se encontraron registros de ubigeos',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    provincias = []
    for ubigeo in all_ubigeos:
        if (ubigeo.departamento == departamento) and (ubigeo.provincia not in provincias):
            provincias.append(ubigeo.provincia)
        
    data = {
        'message': 'Provincias únicas identificadas para el departamento seleccionado',
        'status': 200,
        'data': provincias
    }

    return make_response(jsonify(data), 200)

@identificar_ubigeo_routes.route('/distritos_unicos', methods=['POST'])
def identificar_distritos_unicos(): # considerando la elección previa de un provincia
    print('Solicitud para identificar distritos únicos recibida')
    departamento = request.json.get('departamento')
    provincia = request.json.get('provincia')

    all_ubigeos = Ubigeo.query.all()

    if not all_ubigeos:
        data = {
            'message': 'No se encontraron registros de ubigeos',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    distritos = []
    for ubigeo in all_ubigeos:
        if (ubigeo.departamento == departamento) and (ubigeo.provincia == provincia) and (ubigeo.distrito not in distritos):
            distritos.append(ubigeo.distrito)
        
    data = {
        'message': 'Provincias únicas identificadas para el departamento seleccionado',
        'status': 200,
        'data': distritos
    }

    return make_response(jsonify(data), 200)

@identificar_ubigeo_routes.route('/identificar_ubigeo', methods=['POST'])
def identificar_ubigeo():
    print('Solicitud para identificar ubigeo recibida')
    departamento = request.json.get('departamento')
    provincia = request.json.get('provincia')
    distrito = request.json.get('distrito')

    ubigeo = Ubigeo.query.filter_by(departamento=departamento, provincia=provincia, distrito=distrito).first()

    if not ubigeo:
        data = {
            'message': 'Ubigeo no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    data = {
        'message': 'Ubigeo encontrado',
        'status': 200,
        'data': {
            'id_ubigeo': ubigeo.id_ubigeo,
            'departamento': ubigeo.departamento,
            'provincia': ubigeo.provincia,
            'distrito': ubigeo.distrito,
            'codigo': ubigeo.codigo
        }
    }

    return make_response(jsonify(data), 200)