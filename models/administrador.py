from sqlalchemy.orm import relationship

from utils.db import db

class Administrador(db.Model):
    __tablename__ = 'administrador'

    id_administrador = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False, unique=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False, unique=True)

    # relaciones
    persona = relationship('Persona', back_populates='administradores')
    usuario = relationship('Usuario', back_populates='administradores')
    
    # constructor de la clase
    def __init__(self, id_persona, id_usuario):
        self.id_persona = id_persona
        self.id_usuario = id_usuario