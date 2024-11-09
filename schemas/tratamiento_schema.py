from utils.ma import ma
from models.tratamiento import Tratamiento
from marshmallow import fields
from schemas.especialista_schema import Especialista_Schema
from schemas.evaluacion_schema import Evaluacion_Schema
from schemas.estado_schema import Estado_Schema

class Tratamiento_Schema(ma.Schema):
    class Meta:
        model = Tratamiento
        fields = ('id_tratamiento',
                  'id_resultado',
                  'id_especialista',
                  'objetivo',
                  'fec_asignacion',
                  'fec_inicio',
                  'fec_fin',
                  'id_estado',
                  'resultado',
                  'especialista',
                  'estado'
                 )
    
    resultado = fields.Nested(Evaluacion_Schema)
    especialista = fields.Nested(Especialista_Schema)
    estado = fields.Nested(Estado_Schema)


tratamiento_schema = Tratamiento_Schema()
tratamientos_schema = Tratamiento_Schema(many=True)