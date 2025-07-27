from abc import ABC, abstractmethod

from src.main.application.port.driver.model.query.list_top_players_histories_query import ListTopPlayersHistoriesQuery
from src.main.application.port.driver.model.query.list_top_players_histories_query_output import (
    ListTopPlayersHistoriesQueryOutput,
)


class ListTopPlayersHistoriesDriverPort(ABC):
    @abstractmethod
    def execute(self, query: ListTopPlayersHistoriesQuery) -> ListTopPlayersHistoriesQueryOutput:
        pass
