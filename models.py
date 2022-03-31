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
    large_cover_image: str
    torrents: List[Torrents]