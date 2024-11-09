from flask import Flask
from flask_cors import CORS
from utils.db import db

from services.tipo_usuario import tipo_usuario_routes
from services.usuario import usuario_routes
from services.persona import persona_routes
from services.administrador import administrador_routes
from services.genero import genero_routes
from services.modalidad import modalidad_routes
from services.especialidad import especialidad_routes
from services.tipo_estado import tipo_estado_routes
from services.estado import estado_routes
from services.condicion import condicion_routes
from services.dia import dia_routes
from services.idioma import idioma_routes
from services.especialista import especialista_routes
from services.jornada import jornada_routes
from services.carrera import carrera_routes
from services.ubigeo import ubigeo_routes
from services.paciente import paciente_routes
from services.cita import cita_routes
from services.taller import taller_routes
from services.recurso import recurso_routes
from services.asistencia import asistencia_routes
from services.horario import horario_routes
from services.tipo_test import tipo_test_routes
from services.test import test_routes
from services.opcion import opcion_routes
from services.pregunta import pregunta_routes
from services.escala import escala_routes
from services.evaluacion import evaluacion_routes
from services.resultado import resultado_routes
from services.tratamiento import tratamiento_routes
from services.indicacion import indicacion_routes
from services.post import post_routes
from services.comentario import comentario_routes
from functions.iniciar_sesion import cus_routes1
from functions.cus_realizar_test import cus_realizar_test
from functions.cus_evaluar_resultados_test import cus_evaluar_resultados_test
from functions.results_paciente import results_paciente
from functions.cus_realizar_vigilancia import cus_realizar_vigilancia
from functions.identificar_ubigeo import identificar_ubigeo_routes
from functions.registrar_paciente import registrar_paciente
from functions.mostrar_perfil import monstrar_perfil

from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION


app=Flask(__name__)

CORS(app, origins=['http://localhost:4200'], 
     methods=['GET', 'POST', 'PUT', 'DELETE'], 
     allow_headers=['Content-Type', 'Authorization'])


app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(tipo_usuario_routes, url_prefix='/tipo_usuario_routes')
app.register_blueprint(usuario_routes, url_prefix='/usuario_routes')
app.register_blueprint(persona_routes, url_prefix='/persona_routes')
app.register_blueprint(administrador_routes, url_prefix='/administrador_routes')
app.register_blueprint(genero_routes, url_prefix='/genero_routes')
app.register_blueprint(modalidad_routes, url_prefix='/modalidad_routes')
app.register_blueprint(especialidad_routes, url_prefix='/especialidad_routes')
app.register_blueprint(tipo_estado_routes, url_prefix='/tipo_estado_routes')
app.register_blueprint(estado_routes, url_prefix='/estado_routes')
app.register_blueprint(condicion_routes, url_prefix='/condicion_routes')
app.register_blueprint(dia_routes, url_prefix='/dia_routes')
app.register_blueprint(idioma_routes, url_prefix='/idioma_routes')
app.register_blueprint(especialista_routes, url_prefix='/especialista_routes')
app.register_blueprint(jornada_routes, url_prefix='/jornada_routes')
app.register_blueprint(carrera_routes, url_prefix='/carrera_routes')
app.register_blueprint(ubigeo_routes, url_prefix='/ubigeo_routes')
app.register_blueprint(paciente_routes, url_prefix='/paciente_routes')
app.register_blueprint(cita_routes, url_prefix='/cita_routes')
app.register_blueprint(taller_routes, url_prefix='/taller_routes')
app.register_blueprint(recurso_routes, url_prefix='/recurso_routes')
app.register_blueprint(asistencia_routes, url_prefix='/asistencia_routes')
app.register_blueprint(horario_routes, url_prefix='/horario_routes')
app.register_blueprint(tipo_test_routes, url_prefix='/tipo_test_routes')
app.register_blueprint(test_routes, url_prefix='/test_routes')
app.register_blueprint(opcion_routes, url_prefix='/opcion_routes')
app.register_blueprint(pregunta_routes, url_prefix='/pregunta_routes')
app.register_blueprint(escala_routes, url_prefix='/escala_routes')
app.register_blueprint(evaluacion_routes, url_prefix='/evaluacion_routes')
app.register_blueprint(resultado_routes, url_prefix='/resultado_routes')
app.register_blueprint(tratamiento_routes, url_prefix='/tratamiento_routes')
app.register_blueprint(indicacion_routes, url_prefix='/indicacion_routes')
app.register_blueprint(post_routes, url_prefix='/post_routes')
app.register_blueprint(comentario_routes, url_prefix='/comentario_routes')
app.register_blueprint(cus_routes1, url_prefix='/cus_routes1')
app.register_blueprint(cus_realizar_test, url_prefix='/cus_realizar_test')
app.register_blueprint(cus_evaluar_resultados_test, url_prefix='/cus_evaluar_resultados_test')     
app.register_blueprint(results_paciente, url_prefix='/results_paciente')
app.register_blueprint(cus_realizar_vigilancia, url_prefix='/cus_realizar_vigilancia')
app.register_blueprint(identificar_ubigeo_routes, url_prefix='/identificar_ubigeo_routes')
app.register_blueprint(registrar_paciente,url_prefix='/registrar_paciente')
app.register_blueprint(monstrar_perfil,url_prefix='/monstrar_perfil')


with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True,port=5000)