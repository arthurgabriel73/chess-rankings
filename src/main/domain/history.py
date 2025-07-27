from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class History:
    category: str
    player_username: str
    rating_history: Optional[Dict[str, int]]

    def __post_init__(self):
        if not self.rating_history:
            self.rating_history = {}
