from utils.ma import ma
from models.administrador import Administrador
from marshmallow import fields
from schemas.usuario_schema import Usuario_Schema
from schemas.persona_schema import Persona_Schema

class Administrador_Schema(ma.Schema):
    class Meta:
        model=Administrador
        fields = ('id_administrador',
                'id_persona',
                'id_usuario',
                'persona',
                'usuario'
                )
    
    persona=ma.Nested(Persona_Schema)
    usuario=ma.Nested(Usuario_Schema)
        
administrador_schema = Administrador_Schema()
administradores_schema = Administrador_Schema(many=True)
