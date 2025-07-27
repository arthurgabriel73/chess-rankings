from dataclasses import dataclass


@dataclass
class ListTopPlayersQuery:
    category: str
    num_players: int

    def __post_init__(self):
        self.validate_category()
        self.validate_num_players()

    def validate_category(self):
        if not self.category or not isinstance(self.category, str):
            raise ValueError('Invalid category')
        if len(self.category) < 3 or len(self.category) > 100:
            raise ValueError('Category must be between 3 and 100 characters long')

    def validate_num_players(self):
        if not isinstance(self.num_players, int) or self.num_players <= 0:
            raise ValueError('Number of players must be a positive integer')
