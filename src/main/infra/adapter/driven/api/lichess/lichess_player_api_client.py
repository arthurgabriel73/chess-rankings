import concurrent
from datetime import datetime, timedelta
from typing import Dict, List

import requests

from src.main.domain.history import History
from src.main.infra.adapter.driven.api.lichess.adapter.request.get_rating_histories_request_adapter import (
    ListRatingHistoriesRequestAdapter,
)
from src.main.infra.adapter.driven.api.lichess.adapter.request.get_top_players_request_adapter import (
    ListTopPlayersRequestAdapter,
)
from src.main.infra.adapter.driven.api.lichess.adapter.response.get_rating_histories_response_adapter import (
    ListRatingHistoriesResponseAdapter,
)
from src.main.infra.adapter.driven.api.lichess.adapter.response.get_top_players_response_adapter import (
    ListTopPlayersResponseAdapter,
)
from src.main.infra.adapter.driven.api.player_api import PlayerApi
from src.main.infra.config.environment_settings import get_environment_variables


class LichessApiClient(PlayerApi):
    def __init__(self, base_url: str = None):
        env = get_environment_variables()
        self._base_url = base_url or env.LICHESS_API_BASE_URL

    def get_top_players_usernames(self, category: str, num_players: int) -> List[str]:
        category, num_players = ListTopPlayersRequestAdapter(category, num_players).adapt()
        response = requests.get(f'{self._base_url}/player/top/{num_players}/{category}')
        if response.status_code != 200:
            raise Exception(f'Failed to fetch top players: {response.status_code} - {response.text}')
        return ListTopPlayersResponseAdapter(response.json()).adapt()

    def get_players_rating_histories(self, category: str, usernames: List[str], num_days: int) -> List[History]:
        category, players_ids, num_days = ListRatingHistoriesRequestAdapter(category, usernames, num_days).adapt()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(self._fetch_player_history, players_ids))
        return ListRatingHistoriesResponseAdapter(category, results).adapt()

    def _fetch_player_history(self, player_id: str, category: str, num_days: int) -> Dict[str, List[Dict[str, str]]]:
        response = requests.get(self._base_url + f'/user/{player_id}/rating-history')
        category_history = LichessApiClient._filter_category(response.json(), category)
        return LichessApiClient._generate_history(category_history, player_id, num_days)

    @staticmethod
    def _filter_category(data: List[Dict], category: str) -> Dict[str, str] | None:
        return next((item for item in data if item['name'] == category), None)

    @staticmethod
    def _generate_history(
        category_history: Dict[str, str], player_id: str, num_days: int
    ) -> Dict[str, List[Dict[str, str]]]:
        points = []
        for item in category_history['points']:
            year, month, day, rating = item
            date = datetime(year, month + 1, day)
            points.append({'date': date, 'rating': rating})
        points.sort(key=lambda item: item['date'], reverse=True)
        reference_date = datetime.today()
        date_rating_map = {}
        for point in points:
            date_str = point['date'].strftime('%Y-%m-%d')
            date_rating_map[date_str] = point['rating']
        last_days = []
        current_rating = points[0]['rating']

        for i in range(num_days):
            current_date = reference_date - timedelta(days=i)
            date_str = current_date.strftime('%Y-%m-%d')
            formatted_date = current_date.strftime('%Y-%m-%d')
            if date_str in date_rating_map:
                current_rating = date_rating_map[date_str]

            last_days.append({'date': formatted_date, 'rating': current_rating})
        return {player_id: last_days}
