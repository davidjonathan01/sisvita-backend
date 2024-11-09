from sqlalchemy.orm import relationship

from utils.db import db

class Tipo_estado(db.Model):
    __tablename__ = 'tipo_estado'

    id_tipo_estado = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)

    estados = relationship('Estado', back_populates='tipo_estado')
    
    # constructor de la clase
    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion