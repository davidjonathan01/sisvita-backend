from utils.ma import ma
from models.comentario import Comentario
from marshmallow import fields
from schemas.post_schema import Post_Schema
from schemas.paciente_schema import Paciente_Schema

class Comentario_Schema(ma.Schema):
    class Meta:
        model=Comentario
        fields = ('id_comentario',
                  'id_post',
                  'id_paciente',
                  'descripcion',
                  'fec_publicacion',
                  'fec_edicion',
                  'anonimo',
                  'post',
                  'paciente'
                  )
        
    post=ma.Nested(Post_Schema)
    paciente=ma.Nested(Paciente_Schema)
        
comentario_schema = Comentario_Schema()
comentarios_schema = Comentario_Schema(many=True)
