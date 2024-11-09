from sqlalchemy.orm import relationship

from utils.db import db

class Taller(db.Model):
    __tablename__ = 'taller'

    id_taller = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    n_vacantes = db.Column(db.Integer, nullable=False)
    fec_inicio = db.Column(db.Date, nullable=False)
    fec_fin = db.Column(db.Date, nullable=False)
    id_modalidad = db.Column(db.Integer, db.ForeignKey('modalidad.id_modalidad'), nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'), nullable=False)

    modalidad = relationship('Modalidad', backref='taller1')
    estado = relationship('Estado', backref='taller2')

    especialista = relationship('Especialista', back_populates='talleres')
    
    asistencias = relationship('Asistencia', back_populates='taller', cascade='all, delete-orphan')
    horarios = relationship('Horario', back_populates='taller', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, nombre, id_especialista, n_vacantes, fec_inicio, fec_fin, id_modalidad, id_estado):
        self.nombre = nombre
        self.id_especialista = id_especialista
        self.n_vacantes = n_vacantes
        self.fec_inicio = fec_inicio
        self.fec_fin = fec_fin
        self.id_modalidad = id_modalidad
        self.id_estado = id_estado