from utils.ma import ma
from models.tipo_test import Tipo_test
from marshmallow import fields

class Tipo_test_Schema(ma.Schema):
    class Meta:
        model=Tipo_test
        fields=('id_tipo_test',
               'nombre',
               'descripcion'
               )
        

tipo_test_schema = Tipo_test_Schema()
tipos_test_schema = Tipo_test_Schema(many=True)