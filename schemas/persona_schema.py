from utils.ma import ma
from models.persona import Persona
from schemas.genero_schema import Genero_Schema
from marshmallow import fields

class Persona_Schema(ma.Schema):
    class Meta:
        model=Persona
        fields=('id_persona',
                'doc_identidad',
                'nombres',
                'apellidos',
                'fec_nacimiento',
                'id_genero',
                'num_telefono',
                'genero'
               )
    
    genero=ma.Nested(Genero_Schema)

persona_schema = Persona_Schema()
personas_schema = Persona_Schema(many=True)