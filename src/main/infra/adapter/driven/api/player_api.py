from abc import ABC, abstractmethod

from src.main.infra.adapter.driven.api.dto.request.list_top_players_request import ListTopPlayersRequest
from src.main.infra.adapter.driven.api.dto.response.list_top_players_response import ListTopPlayersResponse


class PlayerApi(ABC):
    @abstractmethod
    def list_top_players(self, request: ListTopPlayersRequest) -> ListTopPlayersResponse:
        pass
