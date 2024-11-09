from sqlalchemy.orm import relationship

from utils.db import db

class Especialista(db.Model):
    __tablename__ = 'especialista'

    id_especialista = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_especialidad = db.Column(db.Integer, db.ForeignKey('especialidad.id_especialidad'), nullable=False)
    n_licencia = db.Column(db.String(11), nullable=False, unique=True)
    activo = db.Column(db.Boolean, nullable=False, default=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)

    # relaciones
    especialidad = relationship('Especialidad', backref='especialista1')

    usuario = relationship('Usuario', back_populates='especialistas')
    persona = relationship('Persona', back_populates='especialistas')

    citas = relationship('Cita', back_populates='especialista', cascade='all, delete-orphan')
    resultados = relationship('Resultado', back_populates='especialista', cascade='all, delete-orphan')
    talleres = relationship('Taller', back_populates='especialista', cascade='all, delete-orphan')
    recursos = relationship('Recurso', back_populates='especialista', cascade='all, delete-orphan')
    jornadas = relationship('Jornada', back_populates='especialista', cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, id_especialidad, n_licencia, activo, id_persona, id_usuario):
        self.id_especialidad = id_especialidad
        self.n_licencia = n_licencia
        self.activo = activo
        self.id_persona = id_persona
        self.id_usuario = id_usuario