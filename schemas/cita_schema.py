from utils.ma import ma
from models.cita import Cita
from marshmallow import fields
from schemas.paciente_schema import Paciente_Schema
from schemas.especialista_schema import Especialista_Schema
from schemas.estado_schema import Estado_Schema
from schemas.modalidad_schema import Modalidad_Schema

class Cita_Schema(ma.Schema):
    class Meta:
        model=Cita
        fields = ('id_cita',
                  'id_paciente',
                  'id_especialista',
                  'motivo',
                  'id_estado',
                  'id_modalidad',
                  'fec_programada',
                  'hora_inicio',
                  'hora_fin',
                  'paciente',
                  'especialista',
                  'estado',
                  'modalidad'
                  )
        
    paciente=ma.Nested(Paciente_Schema)
    especialista=ma.Nested(Especialista_Schema)
    estado=ma.Nested(Estado_Schema)
    modalidad=ma.Nested(Modalidad_Schema)
        
cita_schema = Cita_Schema()
citas_schema = Cita_Schema(many=True)
