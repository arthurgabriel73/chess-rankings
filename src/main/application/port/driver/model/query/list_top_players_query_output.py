from typing import List

from src.main.domain.player_username import PlayerUsername


class ListTopPlayersQueryOutput:
    def __init__(self, usernames: List[PlayerUsername]):
        self.usernames = [usernames.value() for usernames in usernames]
