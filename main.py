from fastapi import FastAPI

from helpers import get_movie, get_movie_list

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

@app.get("/movies_list")
async def movies_list(p: int = 1):
    return get_movie_list(p)

@app.get("/movie_detail")
async def movie_detail(id: int):
    return get_movie(id)