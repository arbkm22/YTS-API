from fastapi import APIRouter

from src.controllers.helpers import get_movie, get_movie_detail, get_movie_list
from src.controllers.helpers_uno import get_latest_movies, get_most_liked_movies, get_popular_movies

router = APIRouter()

@router.get("/")
def root():
    return {
        "movies_list": "returns the list of all movies(page = optional)",
        "movie_detail": "returns the detail of a movie(id = mandatory)"
        }

@router.get("/movies_list")
async def movies_list(p: int = 1):
    return get_movie_list(p)

@router.get("/movie_detail")
async def movie_detail(id: int):
    return get_movie(id)

@router.get("/latest_movies")
async def latest_movies():
    return get_latest_movies()

@router.get("/popular_movies")
async def popular_movies():
    return get_popular_movies()

@router.get("/most_liked")
async def most_liked():
    return get_most_liked_movies()

@router.get("/movie_detailv2")
async def movie_detailv2(name: str, url: str):
    return get_movie_detail(name, url)