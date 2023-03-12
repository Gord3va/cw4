from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db.models import BaseWithID, KeyType


class User(BaseWithID):
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String(40))
    surname = Column(String(40))
    favorite_genre = Column(KeyType, ForeignKey("genres.id"))
    favorite_genre_object = relationship("Genre")
    favorite_movies = relationship("Movie", secondary="favorite_movies")
