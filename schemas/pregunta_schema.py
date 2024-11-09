from utils.ma import ma
from models.pregunta import Pregunta
from marshmallow import fields
from schemas.test_schema import Test_Schema

class Pregunta_Schema(ma.Schema):
    class Meta:
        model=Pregunta
        fields=('id_pregunta',
                'id_test',
                'interrogante',
                'orden',
                'descripcion',
                'test'
               )
    
    test = fields.Nested(Test_Schema)

pregunta_schema = Pregunta_Schema()
preguntas_schema = Pregunta_Schema(many=True)