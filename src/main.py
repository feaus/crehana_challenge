from pathlib import Path

import graphene
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp

from src.database.connection import Base, engine
from src.exceptions import (
    ExternalError,
    external_error,
    ResourceAlreadySynced,
    ResourceNotFound,
    resource_already_synced,
    resource_not_found,
)
from src.routers import integration, synced, third_party
from src.schemas.query_and_mutations import Query, Mutation


Base.metadata.create_all(bind=engine)


load_dotenv(f'{Path().absolute()}/src/secrets/.env')

app = FastAPI()

app.include_router(integration.router)
app.include_router(synced.router)
app.include_router(third_party.router)
app.add_route(
    '/graphql',
    GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation))
)
app.add_exception_handler(ExternalError, external_error)
app.add_exception_handler(ResourceAlreadySynced, resource_already_synced)
app.add_exception_handler(ResourceNotFound, resource_not_found)
