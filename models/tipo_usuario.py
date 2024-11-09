from sqlalchemy.orm import relationship

from utils.db import db

class Tipo_usuario(db.Model):
    __tablename__ = 'tipo_usuario'

    id_tipo_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(200), nullable=True)

    # relaciones
    usuarios = relationship('Usuario', back_populates='tipo_usuario')
    
    # constructor de la clase
    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion