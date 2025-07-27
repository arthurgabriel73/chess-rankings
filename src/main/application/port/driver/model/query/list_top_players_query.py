from dataclasses import dataclass


@dataclass
class ListTopPlayersQuery:
    category: str
    num_players: int
    _MAX_PLAYERS: int = 50
    _MIN_CATEGORY_LENGTH = 3
    _MAX_CATEGORY_LENGTH: int = 100

    def __post_init__(self):
        self.validate_category()
        self.validate_num_players()

    def validate_category(self):
        if not self.category or not isinstance(self.category, str):
            raise ValueError('Invalid category')
        if len(self.category) < self._MIN_CATEGORY_LENGTH or len(self.category) > self._MAX_CATEGORY_LENGTH:
            raise ValueError('Category must be between 3 and 100 characters long')

    def validate_num_players(self):
        if not isinstance(self.num_players, int) or self.num_players <= 0 or self.num_players > self._MAX_PLAYERS:
            raise ValueError('Number of players must be a positive integer and cannot exceed 50')
