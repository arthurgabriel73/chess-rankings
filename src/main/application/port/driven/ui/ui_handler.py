from abc import ABC, abstractmethod
from typing import List

from src.main.domain.history import History


class UIHandler(ABC):
    @abstractmethod
    def render_usernames(self, usernames: List[str]) -> None:
        pass

    @abstractmethod
    def render_rating_histories(self, histories: List[History]) -> None:
        pass
