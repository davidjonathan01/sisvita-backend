from sqlalchemy.orm import relationship

from utils.db import db

class Opcion(db.Model):
    __tablename__ = 'opcion'

    id_opcion = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    puntaje = db.Column(db.Integer, nullable=False)
    orden = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)

    # relaciones
    test = relationship('Test', back_populates='opciones')
    
    # constructor de la clase
    def __init__(self, id_test, nombre, puntaje, orden, descripcion=None):
        self.id_test = id_test
        self.nombre = nombre
        self.puntaje = puntaje
        self.orden = orden
        if descripcion is not None:
            self.descripcion = descripcion