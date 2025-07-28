from typing import Dict, TypedDict


class ProcessedPlayerHistory(TypedDict):
    username: str
    position: int
    rating_history: Dict[str, int]