from config.database import Base
from sqlalchemy import Column, Integer, String

class Taller(Base):
    __tablename__ = "bicicletas"

    id = Column(Integer, primary_key = True)
    fecha = Column(Integer)
    cliente = Column(String)
    email = Column(String)
    telefono = Column(Integer)
    dni = Column(Integer)
    vehiculo = Column(String)
    modelo = Column(String)
    status = Column(String)
    descripcion = Column(String)