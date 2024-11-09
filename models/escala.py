from sqlalchemy.orm import relationship

from utils.db import db

class Escala(db.Model):
    __tablename__ = 'escala'

    id_escala = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)
    puntaje_min = db.Column(db.Integer, nullable=False)
    puntaje_max = db.Column(db.Integer, nullable=False)

    # relaciones
    test = relationship('Test', back_populates='escalas')
    
    # constructor de la clase
    def __init__(self, nombre, id_test, puntaje_min, puntaje_max, descripcion=None):
        self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion
        self.id_test = id_test
        self.puntaje_min = puntaje_min
        self.puntaje_max = puntaje_max