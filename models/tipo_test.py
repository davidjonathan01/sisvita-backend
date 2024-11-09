from sqlalchemy.orm import relationship

from utils.db import db

class Tipo_test(db.Model):
    __tablename__ = 'tipo_test'

    id_tipo_test = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(200), nullable=True)

    tests = relationship('Test', back_populates='tipo_test')
    
    # constructor de la clase
    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion