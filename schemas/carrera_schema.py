from utils.ma import ma
from models.carrera import Carrera
from marshmallow import fields

class Carrera_Schema(ma.Schema):
    class Meta:
        model=Carrera
        fields = ('id_carrera',
                'nombre',
                'descripcion'
                )
        
carrera_schema = Carrera_Schema()
carreras_schema = Carrera_Schema(many=True)
