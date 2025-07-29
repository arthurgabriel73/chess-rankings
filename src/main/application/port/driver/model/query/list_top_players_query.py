from dataclasses import dataclass

from src.main.application.port.driver.model.category_validator import CategoryValidator


@dataclass
class ListTopPlayersQuery:
    category: str
    num_players: int
    _MAX_PLAYERS: int = 50
    _MIN_CATEGORY_LENGTH = 3
    _MAX_CATEGORY_LENGTH: int = 100

    def __post_init__(self):
        self._validate_category()
        self._validate_num_players()

    def _validate_category(self):
        CategoryValidator.validate_category(self.category)

    def _validate_num_players(self):
        if not isinstance(self.num_players, int) or self.num_players <= 0 or self.num_players > self._MAX_PLAYERS:
            raise ValueError(f'Number of players must be a positive integer and cannot exceed {self._MAX_PLAYERS}')
