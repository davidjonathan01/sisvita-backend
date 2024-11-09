from utils.ma import ma
from models.asistencia import Asistencia
from marshmallow import fields
from schemas.taller_schema import Taller_Schema
from schemas.paciente_schema import Paciente_Schema

class Asistencia_Schema(ma.Schema):
    class Meta:
        model=Asistencia
        fields = ('id_asistencia',
                'fecha',
                'id_taller',
                'id_paciente',
                'taller',
                'paciente'
                )
    
    taller=ma.Nested(Taller_Schema)
    paciente=ma.Nested(Paciente_Schema)
        
asistencia_schema = Asistencia_Schema()
asistencias_schema = Asistencia_Schema(many=True)
