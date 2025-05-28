from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

movies = db.query(Movie).limit(10).all()
action_movies = db.query(Movie).filter(Movie.genres.contains("Action")).limit(5).all()

#for movie in action_movies:
#   print(f"ID : {movie.movieId}, Titre : {movie.title}, Genre : {movie.genres}")


ratings = db.query(Rating).limit(10).all()

#for rating in ratings:
#    print(f"ID : {rating.userId}, Titre : {rating.movieId}, Rating : {rating.rating}")


tags = db.query(Tag).limit(50).all()

#for tag in tags:
#    print(f"ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}")


links = db.query(Link).limit(10).all()

for link in links:
    print(f"{link.imdbId}, {link.movieId}, {link.tmdbId}")


db.close()