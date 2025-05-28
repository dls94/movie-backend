from database import SessionLocal
from query_helpers import *

db = SessionLocal()

movies = get_movies(db, limit=5)
for movie in movies:
    print(f"ID : {movie.movieId}, Titre : {movie.title}, Genre : {movie.genres}")

db.close()