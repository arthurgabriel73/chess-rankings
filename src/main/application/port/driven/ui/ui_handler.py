from abc import ABC, abstractmethod
from typing import List

from src.main.domain.history import History
from src.main.domain.player_username import PlayerUsername


class UIHandler(ABC):
    @abstractmethod
    def render_players_usernames(self, usernames: List[PlayerUsername]) -> None:
        pass

    @abstractmethod
    def render_players_rating_histories(self, history: List[History]) -> None:
        pass
