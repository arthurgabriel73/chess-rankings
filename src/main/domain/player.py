from dataclasses import dataclass

from src.main.domain.player_username import PlayerUsername


@dataclass
class Player:
    username: PlayerUsername