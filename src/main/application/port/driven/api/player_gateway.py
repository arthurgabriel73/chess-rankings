from abc import ABC, abstractmethod
from typing import List

from src.main.domain.history import History
from src.main.domain.player import Player


class PlayerGateway(ABC):
    @abstractmethod
    def list_top_players(self, category: str, num_players: int) -> List[Player]:
        pass

    @abstractmethod
    def list_players_rating_histories(self, category: str, usernames: List[str], num_days: int) -> List[History]:
        pass
