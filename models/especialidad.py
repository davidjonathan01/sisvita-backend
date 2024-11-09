from sqlalchemy.orm import relationship

from utils.db import db

class Especialidad(db.Model):
    __tablename__ = 'especialidad'

    id_especialidad = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.String(250), nullable=True)
    
    # constructor de la clase
    def __init__(self, titulo, descripcion=None):
        self.titulo = titulo
        if descripcion is not None:
            self.descripcion = descripcion