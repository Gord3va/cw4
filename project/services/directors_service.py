from project.dao import DirectorsDAO
from project.services.base import BaseService


class DirectorsService(BaseService[DirectorsDAO]):
    def __init__(self, dao: DirectorsDAO):
        self._dao = dao
