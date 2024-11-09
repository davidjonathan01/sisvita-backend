from sqlalchemy.orm import relationship

from utils.db import db

class Comentario(db.Model):
    __tablename__ = 'comentario'

    id_comentario = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_post = db.Column(db.Integer, db.ForeignKey('post.id_post'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    fec_publicacion = db.Column(db.Date, nullable=False)
    fec_edicion = db.Column(db.Date, nullable=True)
    anonimo = db.Column(db.Boolean, nullable=False)

    # relaciones
    post = relationship('Post', back_populates='comentarios') #lazy='joined'
    paciente = relationship('Paciente', back_populates='comentarios') #lazy='joined'
    
    # constructor de la clase
    def __init__(self, id_post, id_paciente, descripcion, fec_publicacion, anonimo, fec_edicion=None):
        self.id_post = id_post
        self.id_paciente = id_paciente
        self.descripcion = descripcion
        self.fec_publicacion = fec_publicacion
        if fec_edicion is not None:
            self.fec_edicion = fec_edicion
        self.anonimo = anonimo