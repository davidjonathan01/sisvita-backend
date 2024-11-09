from utils.ma import ma
from models.resultado import Resultado
from marshmallow import fields
from schemas.especialista_schema import Especialista_Schema
from schemas.evaluacion_schema import Evaluacion_Schema
from schemas.escala_schema import Escala_Schema
from schemas.estado_schema import Estado_Schema

class Resultado_Schema(ma.Schema):
    class Meta:
        model = Resultado
        fields = ('id_resultado',
                  'id_evaluacion',
                  'id_especialista',
                  'id_estado',
                  'id_escala',
                  'fec_interpretacion',
                  'observacion',
                  'informe',
                  'recomendacion',
                  'evaluacion',
                  'especialista',
                  'estado',
                  'escala'
                 )
    
    evaluacion = fields.Nested(Evaluacion_Schema)
    especialista = fields.Nested(Especialista_Schema)
    escala = fields.Nested(Escala_Schema)
    estado = fields.Nested(Estado_Schema)


resultado_schema = Resultado_Schema()
resultados_schema = Resultado_Schema(many=True)