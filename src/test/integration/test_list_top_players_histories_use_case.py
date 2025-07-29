import pytest

from src.main.application.port.driven.api.player_gateway import PlayerGateway
from src.main.application.port.driven.ui.ui_handler import UIHandler
from src.main.application.port.driver.model.query.list_top_players_histories_query import ListTopPlayersHistoriesQuery
from src.main.application.usecase.list_top_players_histories_use_case import ListTopPlayersHistoriesUseCase
from src.test.integration.mock.mock_player_gateway import MockPlayerGateway
from src.test.integration.mock.mock_ui_handler import MockUIHandler


class TestListTopPlayersHistoriesUseCase:
    player_gateway: PlayerGateway
    ui_handler: UIHandler
    sut: ListTopPlayersHistoriesUseCase

    @pytest.fixture
    def setup(self):
        self.player_gateway = MockPlayerGateway()
        self.ui_handler = MockUIHandler()
        self.sut = ListTopPlayersHistoriesUseCase(self.player_gateway, self.ui_handler)

    def test_list_top_players_histories(self, setup):
        # Arrange
        category = 'bullet'
        num_players = 5
        num_days = 30
        query = ListTopPlayersHistoriesQuery(category, num_players, num_days)

        # Act
        output = self.sut.execute(query)

        # Assert
        assert len(output.histories) == num_players
        assert all(history['player'] == f'user{i}' for i, history in enumerate(output.histories))
        assert all(history['history'] == {f'{i}-07-01': i} for i, history in enumerate(output.histories))

    @pytest.mark.parametrize(
        'category, num_players, num_days, error_message',
        [
            (None, 5, 30, 'Invalid category'),
            (7, 5, 30, 'Invalid category'),
            ('', 5, 30, 'Invalid category'),
            ('ab', 3, 30, 'Category must be between 3 and 100 characters long'),
            ('a' * 101, 3, 30, 'Category must be between 3 and 100 characters long'),
            ('bullet', '-1', 30, 'Number of players must be a positive integer and cannot exceed 50'),
            ('bullet', 0, 30, 'Number of players must be a positive integer and cannot exceed 50'),
            ('bullet', -1, 30, 'Number of players must be a positive integer and cannot exceed 50'),
            ('bullet', 51, 30, 'Number of players must be a positive integer and cannot exceed 50'),
            ('bullet', 5, '-1', 'Number of days must be a positive integer and cannot exceed 30'),
            ('bullet', 5, -1, 'Number of days must be a positive integer and cannot exceed 30'),
            ('bullet', 5, 31, 'Number of days must be a positive integer and cannot exceed 30'),
        ],
    )
    def test_should_raise_error_when_query_is_invalid(
        self, setup, category: str, num_players: int, num_days: int, error_message: str
    ):
        # Act & Assert
        with pytest.raises(ValueError, match=error_message):
            ListTopPlayersHistoriesQuery(category=category, num_players=num_players, num_days=num_days)
