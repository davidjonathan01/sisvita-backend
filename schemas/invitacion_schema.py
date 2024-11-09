from utils.ma import ma
from models.invitacion import Invitacion
from marshmallow import fields
from schemas.especialista_schema import Especialista_Schema
from schemas.test_schema import Test_Schema
from schemas.resultado_schema import Resultado_Schema

class Invitacion_Schema(ma.Schema):
    class Meta:
        model = Invitacion
        fields = ('id_invitacion',
                  'id_especialista',
                  'id_resultado',
                  'id_test',
                  'fec_invitacion',
                  'especialista',
                  'resultado',
                  'test'
                 )
    especialista = fields.Nested(Especialista_Schema)
    resultado = fields.Nested(Resultado_Schema)
    test = fields.Nested(Test_Schema)

invitacion_schema=Invitacion_Schema()
invitaciones_schema=Invitacion_Schema(many=True)
