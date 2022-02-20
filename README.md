# Crehana

La aplicación está desarrollada en FastAPI. Para correrla localmente:
1. Tener una instancia de Postgres corriendo.
2. Renombrar el archivo `.env.local` dentro del directorio `secrets` a `.env`.
3. Completar con la información requerida en el archivo `.env`.
    * **Nota**: la variable `THIRD_PARTY_URL` es la URL de la integración.
4. Instalar las dependencias del proyecto (`pip install -r requirements.txt`), preferentemente en un virtualenv.
5. Ejecutar `uvicorn src.main:app --reload` desde la raíz del proyecto.  

### Cómo se usa

La aplicación tiene endpoints REST y endpoints implementados en GraphQL. Los primeros son los siguientes:
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

Aquellos que contienen el prefijo **thirdParty** traen información directamente de la API con la que se integró. Los que tienen el prefijo **synced** traen información de la DB. Y aquellos que tienen **integration** ejecutan acciones tanto sobre la DB como sobre la API.

Por otro lado, se encuentra también disponible un endpoint implementado en GraphQL:
- **POST** /graphql

Desde este endpoint se pueden realizar mutaciones y queries de la base de datos, de las tablas `cars` y `car_dealers`. A continuación, un ejemplo de mutación para crear un objeto en `cars`:

```
mutation createCar {
  createCar(carDetails: {
    brand: "Peugeot",
    model: "307",
    year: 2016
  })
  {
    id
    brand
    model
    year
  }
}
```

Y para realizar una query para un solo auto:

```
query getSingleCar {
  getCar(carId: "30e70221-4b5b-483c-ad7f-290a9f0a901a") {
    id
    brand
    model
    year
  }
}
```

### Tests

Los tests se encuentran en el directorio `Tests`. Para correrlos, ejecutar desde la raíz del repositorio `pytest`, o `coverage run -m pytest` para obtener un informe sobre el coverage del testeo (ejecutando `coverage report` finalizado el testing. El coverage alcanza el 87%. 

Por el momento solo se cuenta con tests de integración.

### MVPs

Los MVPs se pueden consultar [en este enlace](https://pastebin.com/raw/TcQvPWPw).
