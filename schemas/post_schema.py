from utils.ma import ma
from models.post import Post
from marshmallow import fields
from schemas.paciente_schema import Paciente_Schema

class Post_Schema(ma.Schema):
    class Meta:
        model=Post
        fields=('id_post',
                'id_paciente',
                'descripcion',
                'fec_publicacion',
                'fec_edicion',
                'anonimo',
                'paciente'
               )
    
    paciente = fields.Nested(Paciente_Schema)

post_schema = Post_Schema()
posts_schema = Post_Schema(many=True)