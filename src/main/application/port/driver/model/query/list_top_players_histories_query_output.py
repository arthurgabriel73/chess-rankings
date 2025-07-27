from dataclasses import dataclass
from typing import List

from src.main.domain.history import History


@dataclass
class ListTopPlayersHistoriesQueryOutput:
    histories: List[History]
