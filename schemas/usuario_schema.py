from utils.ma import ma
from models.usuario import Usuario
from marshmallow import fields
from schemas.tipo_usuario_schema import Tipo_usuario_Schema

class Usuario_Schema(ma.Schema):
    class Meta:
        model=Usuario
        fields = ('id_usuario',
                'email',
                'contrasenia',
                'id_tipo_usuario',
                'tipo_usuario'
                )
        
    tipo_usuario=ma.Nested(Tipo_usuario_Schema)
        
usuario_schema = Usuario_Schema()
usuarios_schema = Usuario_Schema(many=True)
