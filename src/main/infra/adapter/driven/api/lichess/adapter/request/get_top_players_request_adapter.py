from typing import Tuple


class ListTopPlayersRequestAdapter:
    def __init__(self, category: str, num_players: int):
        self.category = category.lower()
        self.num_players = num_players

    def adapt(self) -> Tuple:
        return self.category, self.num_players
