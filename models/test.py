from utils.db import db
from datetime import datetime

class Test(db.Model):
    __tablename__ = 'test'
    
    id_test = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    id_tipo_test = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'), nullable=False)
    n_preguntas = db.Column(db.Integer, nullable=False)
    id_idioma = db.Column(db.Integer, db.ForeignKey('idioma.id_idioma'), nullable=False)
    n_version = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    
    # relaciones
    tipo_test = db.relationship('Tipo_test', back_populates='tests')
    idioma = db.relationship('Idioma', backref='test1')

    evaluaciones = db.relationship('Evaluacion', back_populates='test', cascade='all, delete-orphan')
    preguntas = db.relationship('Pregunta', back_populates='test', cascade='all, delete-orphan')
    escalas = db.relationship('Escala', back_populates='test', cascade='all, delete-orphan')
    opciones = db.relationship('Opcion', back_populates='test', cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, nombre, id_tipo_test, n_preguntas, id_idioma, n_version, descripcion=None):
        self.nombre = nombre
        self.id_tipo_test = id_tipo_test
        self.n_preguntas = n_preguntas
        self.id_idioma = id_idioma
        self.n_version = n_version
        if descripcion is not None:
            self.descripcion = descripcion