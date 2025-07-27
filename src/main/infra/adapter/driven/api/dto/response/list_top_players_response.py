from typing import List, Dict

from src.main.domain.player import Player
from src.main.domain.player_username import PlayerUsername


class ListTopPlayersResponse:
    def __init__(self, data: Dict):
        self.usernames = [player['username'] for player in data.get('users', [])]

    def adapt(self) -> List[Player]:
        return [Player(username=PlayerUsername(username)) for username in self.usernames]
