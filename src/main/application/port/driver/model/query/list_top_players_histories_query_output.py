from typing import List

from src.main.domain.history import History


class ListTopPlayersHistoriesQueryOutput:
    def __init__(self, histories: List[History]):
        self.histories = [{'player': record.player_username, 'history': record.rating_history} for record in histories]
