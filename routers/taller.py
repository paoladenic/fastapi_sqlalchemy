from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.taller import Taller as TallerModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.taller import TallerService
from schemas.taller import Taller

taller_router = APIRouter()

@taller_router.get('/taller', tags=['taller'], response_model=List[Taller], status_code=200)
def ver_registros() -> List[Taller]:
    db = Session()
    result = TallerService(db).ver_registros()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@taller_router.get('/taller/{id}', tags=['taller'], response_model=Taller)
def ver_registro(id: int = Path(ge=1, le=2000)) -> Taller:
    db = Session()
    result = TallerService(db).ver_registro(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Registro no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@taller_router.get('/taller/', tags=['taller'], response_model=List[Taller])
def ver_registro_por_tipo(vehiculo: str = Query(min_length=5, max_length=15)) -> List[Taller]:
    db = Session()
    result = TallerService(db).ver_registro_por_tipo(vehiculo)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@taller_router.post('/taller', tags=['taller'], response_model=dict, status_code=201)
def crear_registro(taller: Taller) -> dict:
    db = Session()
    TallerService(db).crear_registro(taller)
    return JSONResponse(status_code=201, content={"message": "Registro creado con éxito"})


@taller_router.put('/taller/{id}', tags=['taller'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def actualizar_registro(id: int, taller: Taller)-> dict:
    db = Session()
    result = TallerService(db).ver_registro(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Registro no encontrado"})
    TallerService(db).actualizar_registro(id, taller)
    return JSONResponse(status_code=200, content={"message": "Registro modificado con éxito"})


@taller_router.delete('/taller/{id}', tags=['taller'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def eliminar_registro(id: int)-> dict:
    db = Session()
    result: TallerModel = db.query(TallerModel).filter(TallerModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Registro no encontrado"})
    TallerService(db).eliminar_registro(id)
    return JSONResponse(status_code=200, content={"message": "Registro eliminado con éxito"})