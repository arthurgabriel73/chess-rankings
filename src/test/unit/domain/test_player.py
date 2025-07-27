import pytest

from src.main.domain.player import Player
from src.main.domain.player_username import PlayerUsername


class TestPlayer:
    def test_should_create_player_with_valid_data(self):
        # Arrange
        username = PlayerUsername('test_player')

        # Act
        player = Player(username=username)

        # Assert
        assert player.username == username
        assert player.username.value() == 'test_player'

    def test_should_raise_error_when_username_is_too_short(self):
        # Act & Assert
        with pytest.raises(ValueError, match='Username must be between 3 and 29 characters'):
            PlayerUsername('ab')

    def test_should_raise_error_when_username_is_too_long(self):
        # Act & Assert
        with pytest.raises(ValueError, match='Username must be between 3 and 29 characters'):
            PlayerUsername('a' * 30)

    def test_should_raise_error_when_username_is_empty(self):
        # Act & Assert
        with pytest.raises(ValueError, match='Username cannot be null or empty'):
            PlayerUsername('')

    def test_should_raise_error_when_username_is_not_string(self):
        # Act & Assert
        with pytest.raises(TypeError, match='Username must be a string'):
            PlayerUsername(12345)

    def test_should_raise_error_when_username_is_null(self):
        # Act & Assert
        with pytest.raises(ValueError, match='Username cannot be null or empty'):
            PlayerUsername(None)
