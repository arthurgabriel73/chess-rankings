from dataclasses import dataclass


@dataclass
class ListTopPlayersHistoriesQuery:
    category: str
    num_players: int
    num_days: int

    def __post_init__(self):
        self.validate_category()
        self.validate_num_players()
        self.validate_num_days()

    def validate_category(self):
        if not self.category or not isinstance(self.category, str):
            raise ValueError('Invalid category')
        if len(self.category) < 3 or len(self.category) > 100:
            raise ValueError(
                'Category must be between 3 and 100 characters long'
            )

    def validate_num_players(self):
        if not isinstance(self.num_players, int) or self.num_players <= 0:
            raise ValueError('Number of players must be a positive integer')

    def validate_num_days(self):
        if not isinstance(self.num_days, int) or self.num_days <= 0:
            raise ValueError('Number of days must be a positive integer')
        if self.num_days > 1000:
            raise ValueError('Number of days cannot exceed 1000')
