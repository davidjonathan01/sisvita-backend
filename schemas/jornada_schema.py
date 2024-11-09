from utils.ma import ma
from models.jornada import Jornada
from marshmallow import fields
from schemas.especialista_schema import Especialista_Schema
from schemas.dia_schema import Dia_Schema

class Jornada_Schema(ma.Schema):
    class Meta:
        model=Jornada
        fields=('id_jornada',
                'id_especialista',
                'id_dia',
                'hora_inicio',
                'hora_fin',
                'especialista',
                'dia'
                )
    
    especialista = fields.Nested(Especialista_Schema)
    dia = fields.Nested(Dia_Schema)

jornada_schema = Jornada_Schema()
jornadas_schema = Jornada_Schema(many=True)