from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ListTopPlayersResponseAdapter:
    response: Dict

    def adapt(self) -> List[str]:
        return [player['username'] for player in self.response.get('users', [])]
