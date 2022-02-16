from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI

from src.routers import integration, synced, third_party
from src.database.connection import Base, engine


Base.metadata.create_all(bind=engine)


load_dotenv(f'{Path().absolute()}/src/secrets/.env')

app = FastAPI()

app.include_router(integration.router)
app.include_router(synced.router)
app.include_router(third_party.router)
