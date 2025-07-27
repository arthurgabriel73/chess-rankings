from typing import List

from src.main.application.port.driven.api.player_gateway import PlayerGateway
from src.main.domain.history import History
from src.main.domain.player import Player
from src.main.infra.adapter.driven.api.dto.request.list_top_players_request import ListTopPlayersRequest
from src.main.infra.adapter.driven.api.player_api import PlayerApi


class PlayerGatewayAdapter(PlayerGateway):
    def __init__(self, player_api: PlayerApi):
        self.player_api = player_api

    def list_top_players(self, category: str, num_players: int) -> List[Player]:
        request = ListTopPlayersRequest(category=category, num_players=num_players)
        response = self.player_api.list_top_players(request)
        return response.adapt()

    def list_players_rating_histories(self, category: str, usernames: List[str], num_days: int) -> List[History]:
        pass
