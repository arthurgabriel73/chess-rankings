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
