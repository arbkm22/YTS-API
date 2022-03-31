from lib2to3.pytree import Base
from turtle import st
from typing import List
from pydantic import BaseModel


class Torrents(BaseModel):
    url: str
    hash: str
    quality: str
    type: str
    seeds: int 
    peers: int 
    size: str


class MovieList(BaseModel):
    id: int
    url: str
    imdb_code: str
    title_eng: str
    year: int
    rating: float
    runtime: int
    genres: List[str]
    summary: str
    yt_trailer_code: str
    language: str
    mpa_rating: str
    background_image_original: str
    medium_cover_image: str
    large_cover_image: str
    torrents: List[Torrents]


class Cast(BaseModel):
    name: str
    character_name: str
    url_image: str
    imdb_code: str


class MovieDetail(MovieList):
    download_count: int
    like_count: int
    cast: List[Cast]
    lsi1: str
    lsi2: str
    lsi3: str