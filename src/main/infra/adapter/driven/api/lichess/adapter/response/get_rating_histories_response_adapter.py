from typing import List

from src.main.domain.history import History
from src.main.infra.adapter.driven.api.lichess.processed_player_history import ProcessedPlayerHistory


class ListRatingHistoriesResponseAdapter:
    def __init__(self, category: str, rating_histories: List[ProcessedPlayerHistory]):
        self.category = category
        self.rating_histories = rating_histories

    def adapt(self) -> List[History]:
        histories = []
        for item in self.rating_histories:
            histories.append(History(self.category, item['username'], item['rating_history']))
        return histories
