from typing import List, Tuple


class ListRatingHistoriesRequestAdapter:
    def __init__(self, category: str, usernames: List[str], num_days: int):
        self.category = category[0].upper() + category[1:].lower()
        self.usernames = usernames
        self.num_days = num_days

    def adapt(self) -> Tuple:
        return self.category, self.usernames, self.num_days
