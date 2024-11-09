from utils.ma import ma
from models.evaluacion import Evaluacion
from marshmallow import fields
from schemas.test_schema import Test_Schema
from schemas.paciente_schema import Paciente_Schema

class Evaluacion_Schema(ma.Schema):
    class Meta:
        model=Evaluacion
        fields=('id_evaluacion',
                'id_paciente',
                'id_test',
                'respuestas',
                'fec_realizacion',
                'puntaje',
                'id_escala',
                'paciente',
                'test',
                'escala'
               )

    paciente=ma.Nested(Paciente_Schema)
    test=ma.Nested(Test_Schema)  
    escala=ma.Nested(Test_Schema)

evaluacion_schema = Evaluacion_Schema()
evaluaciones_schema = Evaluacion_Schema(many=True)