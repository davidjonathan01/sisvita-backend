from sqlalchemy.orm import relationship

from utils.db import db

class Genero(db.Model):
    __tablename__ = 'genero'

    id_genero = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(200), nullable=True)
    
    # constructor de la clase
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion