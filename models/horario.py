from sqlalchemy.orm import relationship

from utils.db import db

class Horario(db.Model):
    __tablename__ = 'horario'

    id_horario = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_taller = db.Column(db.Integer, db.ForeignKey('taller.id_taller'), nullable=False)
    id_dia = db.Column(db.Integer, db.ForeignKey('dia.id_dia'), nullable=False)
    horario_inicio = db.Column(db.Time, nullable=False)
    horario_fin = db.Column(db.Time, nullable=False)

    taller = relationship('Taller', back_populates='horarios')
    
    dia = relationship('Dia', backref='horario1')
    
    # constructor de la clase
    def __init__(self, id_taller, id_dia, horario_inicio, horario_fin):
        self.id_taller = id_taller
        self.id_dia = id_dia
        self.hora_inicio = horario_inicio
        self.hora_fin = horario_fin