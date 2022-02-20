from pathlib import Path

import graphene
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp

from src.routers import integration, synced, third_party
from src.database.connection import Base, engine
from src.schemas.query import Query, Mutation


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
