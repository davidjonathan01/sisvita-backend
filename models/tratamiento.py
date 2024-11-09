from sqlalchemy.orm import relationship
from utils.db import db

class Tratamiento(db.Model):
    __tablename__ = 'tratamiento'

    id_tratamiento = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_resultado = db.Column(db.Integer, db.ForeignKey('resultado.id_evaluacion'), nullable=False)
    objetivo = db.Column(db.String(50), nullable=False)
    fec_asignacion = db.Column(db.Date, nullable=False)
    fec_inicio = db.Column(db.Date, nullable=False)
    fec_fin = db.Column(db.Date, nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'), nullable=False)
    observaciones = db.Column(db.String(500), nullable=True)
    
    # relaciones
    resultado = relationship('Resultado', back_populates='tratamientos')
    estado = relationship('Estado', backref='tratamiento1')

    indicaciones = relationship('Indicacion', back_populates='tratamiento')

    # constructor de la clase
    def __init__(self, id_resultado, objetivo, fec_asignacion, fec_inicio, fec_fin, id_estado, observaciones=None):
        self.id_resultado = id_resultado
        self.objetivo = objetivo
        self.fec_asignacion = fec_asignacion
        self.fec_inicio = fec_inicio
        self.fec_fin = fec_fin
        self.id_estado = id_estado
        if observaciones is not None:
            self.observaciones = observaciones