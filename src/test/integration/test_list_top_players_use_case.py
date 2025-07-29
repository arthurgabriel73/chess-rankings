import pytest

from src.main.application.port.driven.api.player_gateway import PlayerGateway
from src.main.application.port.driven.ui.ui_handler import UIHandler
from src.main.application.port.driver.model.category_validator import CategoryValidator
from src.main.application.port.driver.model.query.list_top_players_query import ListTopPlayersQuery
from src.main.application.usecase.list_top_players_use_case import ListTopPlayersUseCase
from src.test.integration.mock.mock_player_gateway import MockPlayerGateway
from src.test.integration.mock.mock_ui_handler import MockUIHandler


class TestListTopPlayersUseCase:
    player_gateway: PlayerGateway
    ui_handler: UIHandler
    sut: ListTopPlayersUseCase

    @pytest.fixture
    def setup(self):
        self.player_gateway = MockPlayerGateway()
        self.ui_handler = MockUIHandler()
        self.sut = ListTopPlayersUseCase(self.player_gateway, self.ui_handler)

    def test_list_top_players(self, setup):
        # Arrange
        category = 'bullet'
        num_players = 5
        query = ListTopPlayersQuery(category=category, num_players=num_players)

        # Act
        output = self.sut.execute(query)

        # Assert
        assert len(output.usernames) == num_players
        assert all(isinstance(username, str) for username in output.usernames)
        assert all(len(username) > 0 for username in output.usernames)

    @pytest.mark.parametrize(
        'category, num_players, error_message',
        [
            (None, 5, f'Invalid category: must be one of: {", ".join(CategoryValidator.valid_categories)}'),
            (7, 5, f'Invalid category: must be one of: {", ".join(CategoryValidator.valid_categories)}'),
            ('', 5, f'Invalid category: must be one of: {", ".join(CategoryValidator.valid_categories)}'),
            ('ab', 3, f'Invalid category: must be one of: {", ".join(CategoryValidator.valid_categories)}'),
            ('a' * 101, 3, f'Invalid category: must be one of: {", ".join(CategoryValidator.valid_categories)}'),
            ('bullet', '-1', 'Number of players must be a positive integer and cannot exceed 50'),
            ('bullet', 0, 'Number of players must be a positive integer and cannot exceed 50'),
            ('bullet', -1, 'Number of players must be a positive integer and cannot exceed 50'),
            ('bullet', 51, 'Number of players must be a positive integer and cannot exceed 50'),
        ],
    )
    def test_should_raise_error_when_query_is_invalid(self, setup, category: str, num_players: int, error_message: str):
        # Act & Assert
        with pytest.raises(ValueError, match=error_message):
            ListTopPlayersQuery(category=category, num_players=num_players)
