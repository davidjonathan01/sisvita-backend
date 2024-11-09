from sqlalchemy.orm import relationship

from utils.db import db

class Modalidad(db.Model):
    __tablename__ = 'modalidad'

    id_modalidad = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(20), nullable=False, unique=True)
    descripcion = db.Column(db.String(200), nullable=True)
    
    # constructor de la clase
    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion