from utils.ma import ma
from models.ubigeo import Ubigeo
from marshmallow import fields

class Ubigeo_Schema(ma.Schema):
    class Meta:
        model=Ubigeo
        fields=('id_ubigeo',
               'codigo',
               'departamento',
               'provincia',
               'distrito',
               'latitud',
               'longitud'
               )
        

ubigeo_schema = Ubigeo_Schema()
ubigeos_schema = Ubigeo_Schema(many=True)