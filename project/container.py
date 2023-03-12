from project.dao import GenresDAO, DirectorsDAO, MoviesDAO, UsersDAO, FavoriteMovieDAO

from project.services import GenresService, DirectorsService, MoviesService, UsersService, FavoriteMovieService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)
favorite_movie_dao = FavoriteMovieDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao)
favorite_movie_service = FavoriteMovieService(dao=favorite_movie_dao)
