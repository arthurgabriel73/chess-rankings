from dataclasses import dataclass

from src.main.application.port.driver.model.category_validator import CategoryValidator


@dataclass
class GenerateTopPlayersHistoriesFileCommand:
    category: str
    num_players: int
    num_days: int
    file_extension: str = 'csv'
    _MAX_PLAYERS: int = 50
    _MAX_DAYS: int = 30
    _MIN_CATEGORY_LENGTH = 3
    _MAX_CATEGORY_LENGTH: int = 100

    def __post_init__(self):
        self._validate_category()
        self._validate_num_players()
        self._validate_num_days()
        self._validate_file_extension()

    def _validate_category(self):
        CategoryValidator.validate_category(self.category)

    def _validate_num_players(self):
        if not isinstance(self.num_players, int) or self.num_players <= 0 or self.num_players > self._MAX_PLAYERS:
            raise ValueError(f'Number of players must be a positive integer and cannot exceed {self._MAX_PLAYERS}')

    def _validate_num_days(self):
        if not isinstance(self.num_days, int) or self.num_days <= 0 or self.num_days > self._MAX_DAYS:
            raise ValueError(f'Number of days must be a positive integer and cannot exceed {self._MAX_DAYS}')

    def _validate_file_extension(self):
        if not isinstance(self.file_extension, str) or not self.file_extension == 'csv':
            raise ValueError('File extension must be "csv"')
