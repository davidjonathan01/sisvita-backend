from sqlalchemy.orm import relationship

from utils.db import db

class Asistencia(db.Model):
    __tablename__ = 'asistencia'

    id_asistencia = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    id_taller = db.Column(db.Integer, db.ForeignKey('taller.id_taller'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'), nullable=False)

    # relaciones
    taller = relationship('Taller', back_populates='asistencias')
    paciente = relationship('Paciente', back_populates='asistencias')
    
    # constructor de la clase
    def __init__(self, fecha, id_taller, id_paciente):
        self.fecha = fecha
        self.id_taller = id_taller
        self.id_paciente = id_paciente