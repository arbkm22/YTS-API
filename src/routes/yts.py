from fastapi import APIRouter

from src.controllers.helpers import get_movie, get_movie_list

router = APIRouter()

@router.get("/")
def root():
    return {
        "movie_list": "returns the list of all movies(page optional)",
        "movie_detail": "returns the detail of a movie(id = mandatory)"
        }

@router.get("/movies_list")
async def movies_list(p: int = 1):
    return get_movie_list(p)

@router.get("/movie_detail")
async def movie_detail(id: int):
    return get_movie(id)