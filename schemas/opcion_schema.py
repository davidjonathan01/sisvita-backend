from utils.ma import ma
from models.opcion import Opcion
from marshmallow import fields

class Opcion_Schema(ma.Schema):
    class Meta:
        model=Opcion
        fields=('id_opcion',
                'id_test',
                'nombre',
                'puntaje',
                'orden',
                'descripcion',
                'test'
               )
        
    test=ma.Nested('Test_Schema')

opcion_schema = Opcion_Schema()
opciones_schema = Opcion_Schema(many=True)