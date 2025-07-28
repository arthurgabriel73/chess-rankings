from abc import ABC, abstractmethod
from typing import List

from src.main.domain.history import History


class PlayerApi(ABC):
    @abstractmethod
    def get_top_players_usernames(self, category: str, num_players: int) -> List[str]:
        pass

    @abstractmethod
    def get_players_rating_histories(self, category: str, usernames: List[str], num_days: int) -> List[History]:
        pass
