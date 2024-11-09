from utils.ma import ma
from models.taller import Taller
from marshmallow import fields
from schemas.especialista_schema import Especialista_Schema
from schemas.modalidad_schema import Modalidad_Schema
from schemas.estado_schema import Estado_Schema

class Taller_Schema(ma.Schema):
    class Meta:
        model = Taller
        fields = ('id_taller',
                  'nombre',
                  'id_especialista',
                  'n_vacantes',
                  'fec_inicio',
                  'fec_fin',
                  'id_modalidad',
                  'id_estado',
                  'especialista',
                  'modalidad',
                  'estado'
                 )
    
    especialista = fields.Nested(Especialista_Schema)
    modalidad = fields.Nested(Modalidad_Schema)
    estado = fields.Nested(Estado_Schema)


taller_schema = Taller_Schema()
talleres_schema = Taller_Schema(many=True)