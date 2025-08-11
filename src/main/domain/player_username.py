from dataclasses import dataclass


@dataclass
class PlayerUsername:
    _value: str
    _MIN_LENGTH: int = 3
    _MAX_LENGTH: int = 29
    # single _: is a convention to indicate to other developers that the attribute is "private", it is exclusively for internal use
    # double __: A double underscore prefix causes the Python interpreter to rewrite the attribute name in order to avoid naming conflicts in subclasses.
    # ex: __baz will be named as "_PlayerUsername__baz"

    def __post_init__(self):
        self.validate_username()

    def validate_username(self) -> None:
        if not self._value:
            raise ValueError('Username cannot be null or empty')
        if not isinstance(self._value, str):
            raise ValueError('Username must be a string')
        if len(self._value) < self._MIN_LENGTH or len(self._value) > self._MAX_LENGTH:
            raise ValueError(f'Username must be between {self._MIN_LENGTH} and {self._MAX_LENGTH} characters long')

    def value(self) -> str:
        return self._value
