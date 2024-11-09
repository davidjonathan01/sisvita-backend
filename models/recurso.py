from sqlalchemy.orm import relationship

from utils.db import db

class Recurso(db.Model):
    __tablename__ = 'recurso'

    id_recurso = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    titulo = db.Column(db.String(100), nullable=False, unique=True)
    contenido = db.Column(db.String(1000), nullable=False)
    fec_publicacion = db.Column(db.Date, nullable=False)
    fec_edicion = db.Column(db.Date, nullable=True)

    # relaciones
    especialista = relationship('Especialista', back_populates='recursos')

    # constructor de la clase
    def __init__(self, id_especialista, titulo, contenido, fec_publicacion, fec_edicion):
        self.id_especialista = id_especialista
        self.titulo = titulo
        self.contenido = contenido
        self.fec_publicacion = fec_publicacion
        if fec_edicion is not None:
            self.fec_edicion = fec_edicion