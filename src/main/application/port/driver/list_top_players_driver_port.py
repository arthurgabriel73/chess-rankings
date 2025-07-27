from abc import ABC, abstractmethod

from src.main.application.port.driver.model.query.list_top_players_query import ListTopPlayersQuery
from src.main.application.port.driver.model.query.list_top_players_query_output import ListTopPlayersQueryOutput


class ListTopPlayersDriverPort(ABC):
    @abstractmethod
    def execute(self, query: ListTopPlayersQuery) -> ListTopPlayersQueryOutput:
        pass
