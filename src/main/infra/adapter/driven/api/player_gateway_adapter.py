from typing import List

from src.main.application.port.driven.api.player_gateway import PlayerGateway
from src.main.domain.history import History
from src.main.infra.adapter.driven.api.dto.request.list_rating_histories_request import ListRatingHistoriesRequest
from src.main.infra.adapter.driven.api.dto.request.list_top_players_request import ListTopPlayersRequest
from src.main.infra.adapter.driven.api.player_api import PlayerApi


class PlayerGatewayAdapter(PlayerGateway):
    def __init__(self, player_api: PlayerApi):
        self.player_api = player_api

    def get_top_players_usernames(self, category: str, num_players: int) -> List[str]:
        request = ListTopPlayersRequest(category=category, num_players=num_players)
        return self.player_api.get_top_players_usernames(request).adapt()

    def get_players_rating_histories(self, category: str, usernames: List[str], num_days: int) -> List[History]:
        request = ListRatingHistoriesRequest(category=category, usernames=usernames, num_days=num_days)
        return self.player_api.get_players_rating_histories(request).adapt()
