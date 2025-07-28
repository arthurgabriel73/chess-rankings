from dataclasses import dataclass


@dataclass
class ListTopPlayersHistoriesQuery:
    category: str
    num_players: int
    num_days: int
    _MAX_PLAYERS: int = 50
    _MAX_DAYS: int = 90
    _MIN_CATEGORY_LENGTH = 3
    _MAX_CATEGORY_LENGTH: int = 100

    def __post_init__(self):
        self.validate_category()
        self.validate_num_players()
        self.validate_num_days()

    def validate_category(self):
        if not self.category or not isinstance(self.category, str):
            raise ValueError('Invalid category')
        if len(self.category) < self._MIN_CATEGORY_LENGTH or len(self.category) > self._MAX_CATEGORY_LENGTH:
            raise ValueError(
                f'Category must be between {self._MIN_CATEGORY_LENGTH} and {self._MAX_CATEGORY_LENGTH} characters long'
            )

    def validate_num_players(self):
        if not isinstance(self.num_players, int) or self.num_players <= 0 or self.num_players > self._MAX_PLAYERS:
            raise ValueError(f'Number of players must be a positive integer and cannot exceed {self._MAX_PLAYERS}')

    def validate_num_days(self):
        if not isinstance(self.num_days, int) or self.num_days <= 0 or self.num_days > self._MAX_DAYS:
            raise ValueError('Number of days must be a positive integer and cannot exceed {self._MAX_DAYS}')
