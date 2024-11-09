from utils.ma import ma
from models.escala import Escala
from marshmallow import fields
from schemas.test_schema import Test_Schema

class Escala_Schema(ma.Schema):
    class Meta:
        model=Escala
        fields = ('id_escala',
                'nombre',
                'descripcion',
                'id_test',
                'puntaje_min',
                'puntaje_max',
                'test'
                )
        
    test=ma.Nested(Test_Schema)
        
escala_schema = Escala_Schema()
escalas_schema = Escala_Schema(many=True)
