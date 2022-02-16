# crehana_challenge

### MVPs

1. Crear integración con el API Publica (https://jsonplaceholder.typicode.com/) y Guarda la información en una DB Postgres:

    Dicha integración debe tener todo lo relacionado a una integración, como validación de datos enviados, validación de datos obtenidos y todas las capas necesarias para esta API.
    
    Debe integrar todos los métodos disponibles:
    
    GET 	/posts
    GET 	/posts/1
    GET 	/posts/1/comments
    GET 	/comments?postId=1
    POST 	/posts
    PUT 	/posts/1
    PATCH 	/posts/1
    DELETE 	/posts/1
    
    Para esta integración no puede usar Django, tampoco puede usar Flask. Puede usar cualquier otra librería.


2. Con la data fake que se guardo en la DB, se debe hacer un API que pueda guardar mas data (cualquier otra que no sea de la integracion) y consultar la información. El Api debe ser desarrollada en GraphQL. Librería recomendada: Graphene

**Importante**:

El código realizado puede subirlo a un repositorio publico para poder revisarlo. Recuerde que deben tener un README.md para conocer mas información del proyecto, también debe tener una manera fácil de como levantar el proyecto para que pueda ser probado de ser necesario.

- Debe tener en cuenta los estándares al escribir código python.
- Hacer pruebas unitarias es un plus.

## Challenge

La aplicación está desarrollada en FastAPI. Para correrla localmente:
1. Tener una instancia de Postgres corriendo.
2. Renombrar el archivo `.env.local` dentro del directorio `secrets` a `.env`.
3. Completar con la información requerida en el archivo `.env`.
    * **Nota**: la variable `THIRD_PARTY_URL` es la URL de la integración.
4. Instalar las dependencias del proyecto (`pip install -r requirements.txt`), preferentemente en un virtualenv.
5. Ejecutar `uvicorn src.main:app --reload` desde la raíz del proyecto.  

Los endpoints de esta aplicación son los siguientes:
- **GET** /thirdParty/posts
- **GET** /thirdParty/posts/{id}
- **GET** /thirdParty/posts/{id}/comments
- **GET** /thirdParty/comments
- **GET** /synced/posts
- **GET** /synced/posts/{id}
- **POST** /integration
- **PUT** /integration/{id}
- **PATCH** /integration/{id}
- **DELETE** /integration/{id}

Los endpoints con el prefijo **thirdParty** traen información directamente de la API con la que se integró. Los que tienen el prefijo **synced** traen información de la DB. Y aquellos que tienen **integration** ejecutan acciones tanto sobre la DB como sobre la API.

## Tests

Los tests se encuentran en el directorio `Tests`. Para correrlos, ejecutar desde la raíz del repositorio `pytest`. Por el momento solo se cuenta con tests de integración.