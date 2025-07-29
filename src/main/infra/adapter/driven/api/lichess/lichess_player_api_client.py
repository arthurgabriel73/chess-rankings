import concurrent
from datetime import datetime, timedelta
from typing import Any, Dict, List

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
from src.main.infra.adapter.driven.api.lichess.processed_player_history import ProcessedPlayerHistory
from src.main.infra.adapter.driven.api.player_api import PlayerApi
from src.main.infra.config.environment_settings import get_environment_variables
from src.main.infra.config.exception.failed_dependency_exception import FailedDependencyException


class LichessApiClient(PlayerApi):
    _TOP_PLAYERS_ENDPOINT = '/player/top/{num_players}/{category}'
    _RATING_HISTORY_ENDPOINT = '/user/{username}/rating-history'
    _FAILED_FETCH_MESSAGE = 'Failed to fetch data from Lichess API'

    def __init__(self, base_url: str = None):
        env = get_environment_variables()
        self._base_url = base_url or env.LICHESS_API_BASE_URL

    def _make_request(self, url: str) -> Dict[str, Any] | List[Dict[str, Any]]:
        response = requests.get(url)
        if response.status_code != 202:
            raise FailedDependencyException(f'{self._FAILED_FETCH_MESSAGE}: {response.status_code}')
        return response.json()

    def get_top_players_usernames(self, category: str, num_players: int) -> List[str]:
        adapted_category, adapted_num_players = ListTopPlayersRequestAdapter(category, num_players).adapt()
        url = f'{self._base_url}{self._TOP_PLAYERS_ENDPOINT.format(num_players=adapted_num_players, category=adapted_category)}'
        response = self._make_request(url)
        return ListTopPlayersResponseAdapter(response).adapt()

    def get_players_rating_histories(self, category: str, usernames: List[str], num_days: int) -> List[History]:
        adapted_category, adapted_usernames, adapted_num_days = ListRatingHistoriesRequestAdapter(
            category, usernames, num_days
        ).adapt()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self._fetch_player_history, username, position, adapted_category, adapted_num_days)
                for position, username in enumerate(adapted_usernames)
            ]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        return ListRatingHistoriesResponseAdapter(adapted_category, results).adapt()

    def _fetch_player_history(
        self, username: str, position: int, category: str, num_days: int
    ) -> ProcessedPlayerHistory:
        url = f'{self._base_url}{self._RATING_HISTORY_ENDPOINT.format(username=username)}'
        player_raw_data = self._make_request(url)
        return self._process_player_history(player_raw_data, category, username, position, num_days)

    @staticmethod
    def _process_player_history(
        data: List[Dict], category: str, username: str, position: int, num_days: int
    ) -> ProcessedPlayerHistory:
        category_data = LichessApiClient._filter_history_by_category(data, category)
        sorted_points = LichessApiClient._extract_and_sort_points(category_data)
        date_rating_map = LichessApiClient._create_date_rating_map(sorted_points)
        last_days_ratings = LichessApiClient._generate_daily_ratings(date_rating_map, sorted_points, num_days)
        return {'username': username, 'rating_history': last_days_ratings, 'position': position}

    @staticmethod
    def _filter_history_by_category(data: List[Dict], category: str) -> Dict:
        return next((item for item in data if item.get('name') == category), {'points': []})

    @staticmethod
    def _extract_and_sort_points(category_data: Dict) -> List[Dict[str, Any]]:
        points = []
        for item in category_data.get('points', []):
            year, month, day, rating = item
            date = datetime(year, month + 1, day)
            points.append({'date': date, 'rating': rating})
        points.sort(key=lambda record: record['date'], reverse=True)
        return points

    @staticmethod
    def _create_date_rating_map(points: List[Dict[str, Any]]) -> Dict[str, int]:
        date_rating_map = {}
        for record in points:
            date_str = record['date'].strftime('%Y-%m-%d')
            date_rating_map[date_str] = record['rating']
        return date_rating_map

    @staticmethod
    def _generate_daily_ratings(
        date_rating_map: Dict[str, int], sorted_points: List[Dict[str, int]], num_days: int
    ) -> Dict[str, int]:
        current_rating = sorted_points[0]['rating']
        daily_ratings: Dict[str, int] = {}
        for i in range(num_days + 1):
            current_date_str = (datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d')
            if current_date_str in date_rating_map:
                current_rating = date_rating_map[current_date_str]
            daily_ratings[current_date_str] = current_rating
        sorted_daily_ratings = {date: daily_ratings[date] for date in sorted(daily_ratings.keys(), reverse=True)}
        return sorted_daily_ratings
