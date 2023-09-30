# API RESTful con SQLAlchemy para la gestión de los registros del taller "Avila Bikes"

Este repositorio es una web-app creada con FastAPI, utiliza el ORM SQLAlchemy, y esta contenerizada utilizando Docker. El objetivo principal de esta aplicación es proporcionar endpoints CRUD (Crear, Leer, Actualizar y Eliminar) para gestionar los registros de un taller de bicicletas de manera eficiente. 

## Deploy:
El proyecto se encuentra desplegado en Google Cloud en esta url:

https://fastapi-web-server-yehkvd5kba-od.a.run.app/


## Características de seguridad:
-. **Autenticación con JWT**: Para garantizar la seguridad de la aplicación, se ha implementado la autenticación con JSON Web Tokens (JWT) en las operaciones de actualización y eliminación de registros. Solo los usuarios autenticados tienen acceso a estas funciones. 

## Cómo utilizar el programa
Para utilizar esta app, sigue estos pasos:

1. Clona este repositorio en tu máquina local.

2. Crea un entorno virtual e instala las dependencias del proyecto.

3. Inicia la aplicación con el comando: uvicorn app.main:app --reload. 

4. La aplicación se ejecutará localmente y estará disponible en http://localhost:8000. Puedes acceder a la documentación de la API en http://localhost:8000/docs para obtener información detallada sobre los endpoints disponibles y cómo usarlos.
