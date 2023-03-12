from project.dao import GenresDAO
from project.services.base import BaseService


class GenresService(BaseService[GenresDAO]):
    def __init__(self, dao: GenresDAO):
        self._dao = dao
