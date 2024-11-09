from sqlalchemy.orm import relationship

from utils.db import db

class Indicacion(db.Model):
    __tablename__ = 'indicacion'

    id_indicacion = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_tratamiento = db.Column(db.Integer, db.ForeignKey('tratamiento.id_tratamiento'), nullable=False)
    orden = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    
    # relaciones
    tratamiento = relationship('Tratamiento', back_populates='indicaciones')

    # constructor de la clase
    def __init__(self, nombre, id_tratamiento, orden, descripcion):
        self.nombre = nombre
        self.id_tratamiento = id_tratamiento
        self.orden = orden
        self.descripcion = descripcion