from utils.ma import ma
from models.test import Test
from marshmallow import fields
from schemas.idioma_schema import Idioma_Schema
from schemas.tipo_test_schema import Tipo_test_Schema

class Test_Schema(ma.Schema):
    class Meta:
        model=Test
        fields=('id_test',
               'nombre',
               'id_tipo_test',
               'n_preguntas',
               'id_idioma',
               'n_version',
               'descripcion',
               'tipo_test',
               'idioma'
               )
        
    tipo_test = fields.Nested(Tipo_test_Schema)
    idioma = fields.Nested(Idioma_Schema)

test_schema = Test_Schema()
tests_schema = Test_Schema(many=True)