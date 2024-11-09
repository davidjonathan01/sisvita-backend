from utils.db import db

class Evaluacion(db.Model):
    __tablename__ = 'evaluacion'

    id_evaluacion = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'), nullable=False)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)
    respuestas = db.Column(db.String(500), nullable=False)
    fec_realizacion = db.Column(db.Date, nullable=False)
    puntaje = db.Column(db.Integer, nullable=True)
    id_escala = db.Column(db.Integer, db.ForeignKey('escala.id_escala'), nullable=True)

    # relaciones
    escala = db.relationship('Escala', backref='evaluacion1')

    paciente = db.relationship('Paciente', back_populates='evaluaciones')
    test = db.relationship('Test', back_populates='evaluaciones')

    resultados = db.relationship('Resultado', back_populates='evaluacion', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, id_paciente, id_test, respuestas, fec_realizacion, puntaje, id_escala):
        self.id_paciente = id_paciente
        self.id_test = id_test
        self.respuestas = respuestas
        self.fec_realizacion = fec_realizacion
        self.puntaje = puntaje
        self.id_escala = id_escala