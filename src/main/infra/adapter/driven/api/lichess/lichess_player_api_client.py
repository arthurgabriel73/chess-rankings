import requests

from src.main.infra.adapter.driven.api.dto.request.list_top_players_request import ListTopPlayersRequest
from src.main.infra.adapter.driven.api.dto.response.list_top_players_response import ListTopPlayersResponse
from src.main.infra.adapter.driven.api.player_api import PlayerApi
from src.main.infra.config.environment_settings import get_environment_variables


class LichessApiClient(PlayerApi):
    def __init__(self, base_url: str = None):
        env = get_environment_variables()
        self._base_url = base_url or env.LICHESS_API_BASE_URL

    def list_top_players(self, request: ListTopPlayersRequest) -> ListTopPlayersResponse:
        category, num_players = request
        response = requests.get(f'{self._base_url}/player/top/{num_players}/{category}')
        if response.status_code != 200:
            raise Exception(f'Failed to fetch top players: {response.status_code} - {response.text}')
        data = response.json()
        return ListTopPlayersResponse(data)
