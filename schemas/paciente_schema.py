from utils.ma import ma
from models.paciente import Paciente
from marshmallow import fields
from schemas.ubigeo_schema import Ubigeo_Schema
from schemas.carrera_schema import Carrera_Schema
from schemas.condicion_schema import Condicion_Schema
from schemas.usuario_schema import Usuario_Schema
from schemas.persona_schema import Persona_Schema

class Paciente_Schema(ma.Schema):
    class Meta:
        model=Paciente
        fields = ('id_paciente',
              'id_ubigeo',
              'id_condicion',
              'id_carrera',
              'id_persona',
              'id_usuario',
              'ubigeo',
              'condicion'
              'carrera',
              'persona',
              'usuario'
              )
    
    ubigeo=ma.Nested(Ubigeo_Schema)
    condicion=ma.Nested(Condicion_Schema)
    carrera=ma.Nested(Carrera_Schema)
    persona=ma.Nested(Persona_Schema)
    usuario=ma.Nested(Usuario_Schema)
        
paciente_schema = Paciente_Schema()
pacientes_schema = Paciente_Schema(many=True)
