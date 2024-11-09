from utils.ma import ma
from models.modalidad import Modalidad
from marshmallow import fields

class Modalidad_Schema(ma.Schema):
    class Meta:
        model=Modalidad
        fields=('id_modalidad',
                'nombre',
                'descripcion'
               )

modalidad_schema = Modalidad_Schema()
modalidades_schema = Modalidad_Schema(many=True)