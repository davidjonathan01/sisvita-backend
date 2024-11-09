from utils.ma import ma
from models.idioma import Idioma
from marshmallow import fields

class Idioma_Schema(ma.Schema):
    class Meta:
        model=Idioma
        fields=('id_idioma',
                'nombre',
                'descripcion'
                )

idioma_schema = Idioma_Schema()
idiomas_schema = Idioma_Schema(many=True)