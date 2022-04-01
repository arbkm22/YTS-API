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
    genres: List[str]
    large_cover_image: str


class Cast(BaseModel):
    name: str
    character_name: str
    url_image: str
    imdb_code: str


class MovieDetail(MovieList):
    download_count: int
    like_count: int
    cast: List[Cast]
    runtime: int
    description: str
    yt_trailer_code: str
    background_image_original: str
    lsi1: str
    lsi2: str
    lsi3: str
    torrents: List[Torrents]