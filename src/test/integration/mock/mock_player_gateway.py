from typing import List

from src.main.application.port.driven.api.player_gateway import PlayerGateway
from src.main.domain.history import History


class MockPlayerGateway(PlayerGateway):
    def get_top_players_usernames(self, category: str, num_players: int) -> List[str]:
        usernames = [f'user{i}' for i in range(num_players)]
        return usernames

    def get_players_rating_histories(self, category: str, usernames: List[str], num_days: int) -> List[History]:
        return [
            History(category=category, player_username=username, rating_history={f'{index}-07-01': index})
            for index, username in enumerate(usernames)
        ]
