from utils.ma import ma
from models.horario import Horario
from marshmallow import fields
from schemas.taller_schema import Taller_Schema
from schemas.dia_schema import Dia_Schema

class Horario_Schema(ma.Schema):
    class Meta:
        model=Horario
        fields=('id_horario',
                'id_taller',
                'id_dia',
                'horario_inicio',
                'horario_fin',
                'taller',
                'dia'
                )
    
    taller = fields.Nested(Taller_Schema)
    dia = fields.Nested(Dia_Schema)

horario_schema = Horario_Schema()
horarios_schema = Horario_Schema(many=True)