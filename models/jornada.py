from sqlalchemy.orm import relationship

from utils.db import db

class Jornada(db.Model):
    __tablename__ = 'jornada'

    id_jornada = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    id_dia = db.Column(db.Integer, db.ForeignKey('dia.id_dia'), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=False)

    # relaciones
    especialista = relationship('Especialista', back_populates='jornadas')
    dia = relationship('Dia', backref='jornada1')
    
    # constructor de la clase
    def __init__(self, id_especialista, id_dia, hora_inicio, hora_fin):
        self.id_especialista = id_especialista
        self.id_dia = id_dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin