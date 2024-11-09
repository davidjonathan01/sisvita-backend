from utils.ma import ma
from models.tipo_usuario import Tipo_usuario
from marshmallow import fields

class Tipo_usuario_Schema(ma.Schema):
    class Meta:
        model=Tipo_usuario
        fields=('id_tipo_usuario',
               'nombre',
               'descripcion'
               )

tipo_usuario_schema = Tipo_usuario_Schema()
tipos_usuario_schema = Tipo_usuario_Schema(many=True)