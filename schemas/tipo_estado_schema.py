from utils.ma import ma
from models.tipo_estado import Tipo_estado
from marshmallow import fields

class Tipo_estado_Schema(ma.Schema):
    class Meta:
        model=Tipo_estado
        fields=('id_tipo_estado',
               'nombre',
               'descripcion'
               )
        

tipo_estado_schema = Tipo_estado_Schema()
tipos_estado_schema = Tipo_estado_Schema(many=True)