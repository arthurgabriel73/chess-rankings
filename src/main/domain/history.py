from dataclasses import dataclass
from typing import Dict, Optional


# @dataclass: it will add various “dunder” methods to the class such as __init__() and __repr__()
@dataclass
class History:
    category: str
    player_username: str
    rating_history: Optional[Dict[str, int]]

    def __post_init__(self):
        if not self.rating_history:
            self.rating_history = {}
