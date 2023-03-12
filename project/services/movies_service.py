from typing import Optional, List

from .base import BaseService
from project.exceptions import BadRequestData
from project.dao import MoviesDAO
from ..setup.db.models import Base


class MoviesService(BaseService[MoviesDAO]):
    def __init__(self, dao: MoviesDAO):
        super(MoviesService, self).__init__(dao)
        self._dao = dao

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> List[Base]:
        if status is None:
            return super(MoviesService, self).get_all(page=page)
        if isinstance(status, str) and status.lower() == "new":
            return self._dao.get_all_and_order_by_newest(page=page)
        raise BadRequestData()
