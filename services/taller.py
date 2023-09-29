from models.taller import Taller as TallerModel
from schemas.taller import Taller


class TallerService():
    def __init__(self, db) -> None:
        self.db = db

    def ver_registros(self):
        result = self.db.query(TallerModel).all()
        return result

    def ver_registro(self, id):
        result = self.db.query(TallerModel).filter(TallerModel.id == id).first()
        return result

    def ver_registro_por_tipo(self, vehiculo):
        result = self.db.query(TallerModel).filter(TallerModel.vehiculo == vehiculo).all()
        return result

    def crear_registro(self, taller: Taller):
        nuevo_registro = TallerModel(**taller.dict())
        self.db.add(nuevo_registro)
        self.db.commit()
        return

    def actualizar_registro(self, id: int, data: Taller):
        taller = self.db.query(TallerModel).filter(TallerModel.id == id).first()
        taller.fecha = data.fecha
        taller.cliente = data.cliente
        taller.email = data.email
        taller.telefono = data.telefono
        taller.dni = data.dni
        taller.vehiculo = data.vehiculo
        taller.modelo = data.modelo
        taller.status = data.status
        taller.descripcion = data.descripcion
        self.db.commit()
        return

    def eliminar_registro(self, id: int):
       self.db.query(TallerModel).filter(TallerModel.id == id).delete()
       self.db.commit()
       return