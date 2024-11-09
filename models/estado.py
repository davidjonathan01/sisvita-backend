from sqlalchemy.orm import relationship

from utils.db import db

class Estado(db.Model):
    __tablename__ = 'estado'

    id_estado = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(20), nullable=False, unique=True)
    descripcion = db.Column(db.String(200), nullable=True)
    id_tipo_estado = db.Column(db.Integer, db.ForeignKey('tipo_estado.id_tipo_estado'), nullable=False)
    
    # relaciones
    tipo_estado = relationship('Tipo_estado', back_populates='estados')
    
    # constructor de la clase
    def __init__(self, nombre, id_tipo_estado, descripcion=None):
        self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion
        self.id_tipo_estado = id_tipo_estado