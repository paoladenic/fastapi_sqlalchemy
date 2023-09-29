from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.taller import taller_router
from routers.user import user_router

app = FastAPI()
app.title = "FASTAPI b2b AVILA BIKES"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(taller_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h2>API RESTful con SQLAlchemy para la gestión de los registros del taller "Avila Bikes"</h2> <a href="/docs">DOCS</a>')
