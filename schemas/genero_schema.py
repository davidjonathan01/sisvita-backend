from utils.ma import ma
from models.genero import Genero
from marshmallow import fields

class Genero_Schema(ma.Schema):
    class Meta:
        model=Genero
        fields=('id_genero',
                'nombre',
                'descripcion'
               )

genero_schema = Genero_Schema()
generos_schema = Genero_Schema(many=True)