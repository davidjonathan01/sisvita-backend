from sqlalchemy.orm import relationship

from utils.db import db

class Paciente(db.Model):
    __tablename__ = 'paciente'

    id_paciente = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_ubigeo = db.Column(db.Integer, db.ForeignKey('ubigeo.id_ubigeo'), nullable=False)
    id_condicion = db.Column(db.Integer, db.ForeignKey('condicion.id_condicion'), nullable=False)
    id_carrera = db.Column(db.Integer, db.ForeignKey('carrera.id_carrera'), nullable=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    
    # relaciones
    ubigeo = relationship('Ubigeo', backref='paciente1')
    condicion = relationship('Condicion', backref='paciente2')
    carrera = relationship('Carrera', backref='paciente3')

    persona = relationship('Persona', back_populates='pacientes')
    usuario = relationship('Usuario', back_populates='pacientes')

    citas = relationship('Cita', back_populates='paciente', cascade='all, delete-orphan')
    posts = relationship('Post', back_populates='paciente', cascade='all, delete-orphan')
    comentarios = relationship('Comentario', back_populates='paciente', cascade='all, delete-orphan')
    evaluaciones = relationship('Evaluacion', back_populates='paciente', cascade='all, delete-orphan')
    asistencias = relationship('Asistencia', back_populates='paciente', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, id_ubigeo, id_condicion, id_persona, id_usuario, id_carrera=None):
        self.id_ubigeo = id_ubigeo
        self.id_condicion = id_condicion
        self.id_persona = id_persona
        self.id_usuario = id_usuario
        if id_carrera is not None:
            self.id_carrera = id_carrera