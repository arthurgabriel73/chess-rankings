from dataclasses import dataclass


@dataclass
class PlayerUsername:
    _value: str
    _MIN_LENGTH: int = 3
    _MAX_LENGTH: int = 29


    def __post_init__(self):
        self.validate_username(self._value)

    @staticmethod
    def validate_username(username: str) -> None:
        if not username:
            raise ValueError('Username cannot be null or empty')
        if not isinstance(username, str):
            raise TypeError('Username must be a string')
        if len(username) < PlayerUsername._MIN_LENGTH or len(username) > PlayerUsername._MAX_LENGTH:
            raise ValueError(
                f'Username must be between {PlayerUsername._MIN_LENGTH} and {PlayerUsername._MAX_LENGTH} characters long'
            )

    def value(self) -> str:
        return self._value