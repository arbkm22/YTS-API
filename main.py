from fastapi import FastAPI

from helpers import get_movie, get_movie_list

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

@app.get("/movieList")
async def movieList(p: int = 1):
    return get_movie_list(p)

@app.get("/movieDetail")
async def movieDetail(id: int):
    return get_movie(id)