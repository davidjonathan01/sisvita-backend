from utils.ma import ma
from models.especialidad import Especialidad
from marshmallow import fields

class Especialidad_Schema(ma.Schema):
    class Meta:
        model=Especialidad
        fields = ('id_especialidad',
                  'titulo',
                  'descripcion'
                  )
        
especialidad_schema = Especialidad_Schema()
especialidades_schema = Especialidad_Schema(many=True)
