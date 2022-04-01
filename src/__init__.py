from fastapi import FastAPI

from src.routes import yts

app = FastAPI()

app.include_router(yts.router)