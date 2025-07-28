from typing import List, Tuple


class ListRatingHistoriesRequestAdapter:
    def __init__(self, category: str, usernames: List[str], num_days: int):
        self.category = category[0].upper() + category[1:].lower()
        self.players_ids = [user.lower() for user in usernames]
        self.num_days = num_days

    def adapt(self) -> Tuple:
        return self.category, self.players_ids, self.num_days
