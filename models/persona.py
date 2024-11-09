from sqlalchemy.orm import relationship

from utils.db import db

class Persona(db.Model):
    __tablename__ = 'persona'

    id_persona = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    doc_identidad = db.Column(db.String(9), nullable=False, unique=True)
    nombres = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(70), nullable=False)
    fec_nacimiento = db.Column(db.Date, nullable=False)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id_genero'), nullable=False)
    num_telefono = db.Column(db.String(9), nullable=False)
    
    # relaciones
    genero = relationship('Genero', backref='persona1')

    administradores = relationship('Administrador', back_populates='persona')
    pacientes = relationship('Paciente', back_populates='persona')
    especialistas = relationship('Especialista', back_populates='persona')

    # constructor de la clase
    def __init__(self, doc_identidad, nombres, apellidos, fec_nacimiento, id_genero, num_telefono):
        self.doc_identidad = doc_identidad
        self.nombres = nombres
        self.apellidos = apellidos
        self.fec_nacimiento = fec_nacimiento
        self.id_genero = id_genero
        self.num_telefono = num_telefono
        