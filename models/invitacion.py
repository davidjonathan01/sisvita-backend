from utils.db import db
from sqlalchemy.orm import relationship

class Invitacion(db.Model):
    __tablename__ = 'invitacion'

    id_invitacion = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    id_resultado=db.Column(db.Integer, db.ForeignKey('resultado.id_resultado'), nullable=False)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)
    fec_invitacion = db.Column(db.Date, nullable=False)

    especialista = relationship('Especialista', backref='invitacion1')
    resultado = relationship('Resultado', backref='invitacion2')
    test = relationship('Test', backref='invitacion3')
    
    # constructor de la clase
    def __init__(self, id_especialista, id_resultado, id_test,fec_invitacion):
        self.id_especialista = id_especialista
        self.id_resultado = id_resultado
        self.id_test = id_test
        self.fec_invitacion = fec_invitacion