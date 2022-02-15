from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI

from src.routers import third_party


load_dotenv(f'{Path().absolute()}/src/secrets/.env')

app = FastAPI()

app.include_router(third_party.router)
