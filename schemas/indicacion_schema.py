from schemas.tratamiento_schema import Tratamiento_Schema
from utils.ma import ma
from models.indicacion import Indicacion
from marshmallow import fields

class Indicacion_Schema(ma.Schema):
    class Meta:
        model=Indicacion
        fields=('id_indicacion',
                'id_tratamiento',
                'orden',
                'descripcion'
                'tratamiento'
                )
    
    tratamiento=ma.Nested(Tratamiento_Schema)

indicacion_schema = Indicacion_Schema()
indicaciones_schema = Indicacion_Schema(many=True)