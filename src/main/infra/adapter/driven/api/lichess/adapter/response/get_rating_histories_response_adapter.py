from typing import Dict, List

from src.main.domain.history import History


class ListRatingHistoriesResponseAdapter:
    def __init__(self, category: str, players_histories: List[Dict[str, Dict[str, int]]]):
        self.category = category
        self.players_histories = players_histories

    def adapt(self) -> List[History]:
        histories = []
        for player_history in self.players_histories:
            username = next(iter(player_history))
            rating_history = player_history[username]
            histories.append(History(category=self.category, player_username=username, rating_history=rating_history))
        return histories
