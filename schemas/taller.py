from pydantic import BaseModel, Field
from typing import Optional


class Taller(BaseModel):
    id: Optional[int] = None
    fecha: str = Field(min_length=5, max_length=12)
    cliente: str = Field(min_length=4, max_length=25)
    email: str = Field(min_length=10, max_length=50)
    telefono: str = Field(min_length=5, max_length=20)
    dni: str = Field(min_length=5, max_length=12)
    vehiculo: str = Field(min_length=5, max_length=15)
    modelo: str = Field(min_length=3, max_length=15)
    status: str = Field(min_length=5, max_length=15)
    descripcion: str = Field(min_length=5, max_length=80)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "fecha": "05/09/2022",
                "cliente": "Benito Camelo",
                "email": "benito@camelo.com",
                "telefono": 601666000,
                "dni": "Y1234567M",
                "vehiculo": "Patinete",
                "modelo": "Xiaomi",
                "status": "Cotización",
                "descripcion": "Ajuste de frenos"
            }
        }
