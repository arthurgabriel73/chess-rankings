from dataclasses import dataclass
from typing import List


@dataclass
class ListTopPlayersQueryOutput:
    usernames: List[str]
