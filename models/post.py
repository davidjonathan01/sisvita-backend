from sqlalchemy.orm import relationship

from utils.db import db

class Post(db.Model):
    __tablename__ = 'post'

    id_post = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    fec_publicacion = db.Column(db.Date, nullable=False)
    fec_edicion = db.Column(db.Date, nullable=True)
    anonimo = db.Column(db.Boolean, nullable=False)

    # relaciones
    paciente = relationship('Paciente', back_populates='posts')

    comentarios = relationship('Comentario', back_populates='post', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, id_paciente, descripcion, fec_publicacion, anonimo, fec_edicion=None):
        self.id_paciente = id_paciente
        self.descripcion = descripcion
        self.fec_publicacion = fec_publicacion
        if fec_edicion is not None:
            self.fec_edicion = fec_edicion
        self.anonimo = anonimo