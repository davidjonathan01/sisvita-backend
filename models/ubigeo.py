from sqlalchemy.orm import relationship

from utils.db import db

class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'

    id_ubigeo = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    codigo = db.Column(db.String(6), nullable=False, unique=True)
    departamento = db.Column(db.String(50), nullable=False)
    provincia = db.Column(db.String(50), nullable=False)
    distrito = db.Column(db.String(50), nullable=False)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    
    # constructor de la clase
    def __init__(self, codigo, departamento, provincia, distrito, latitud, longitud):
        self.codigo = codigo
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.latitud = latitud
        self.longitud = longitud