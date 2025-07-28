from typing import Dict, List, Union

from src.main.domain.history import History


class ListRatingHistoriesResponseAdapter:
    def __init__(self, category: str, rating_histories: List[Dict[str, Union[str, Dict]]]):
        self.category = category
        self.rating_histories = rating_histories

    def adapt(self) -> List[History]:
        histories = []
        for item in self.rating_histories:
            histories.append(History(self.category, item['username'], item['rating_history']))
        return histories
