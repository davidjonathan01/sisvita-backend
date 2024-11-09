from utils.ma import ma
from models.especialista import Especialista
from marshmallow import fields
from schemas.especialidad_schema import Especialidad_Schema
from schemas.genero_schema import Genero_Schema
from schemas.usuario_schema import Usuario_Schema
from schemas.persona_schema import Persona_Schema

class Especialista_Schema(ma.Schema):
    class Meta:
        model=Especialista
        fields = ('id_especialista',
                  'id_especialidad',
                  'n_licencia',
                  'activo',
                  'id_persona',
                  'id_usuario',
                  'especialidad',
                  'genero',
                  'usuario',
                  'persona'
                  )
        
    especialidad=ma.Nested(Especialidad_Schema)
    genero=ma.Nested(Genero_Schema)
    usuario=ma.Nested(Usuario_Schema)
    persona=ma.Nested(Persona_Schema)

especialista_schema = Especialista_Schema()
especialistas_schema = Especialista_Schema(many=True)