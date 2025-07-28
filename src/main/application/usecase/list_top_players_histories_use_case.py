from src.main.application.port.driven.api.player_gateway import PlayerGateway
from src.main.application.port.driven.ui.ui_handler import UIHandler
from src.main.application.port.driver.list_top_players_histories_driver_port import ListTopPlayersHistoriesDriverPort
from src.main.application.port.driver.model.query.list_top_players_histories_query import ListTopPlayersHistoriesQuery
from src.main.application.port.driver.model.query.list_top_players_histories_query_output import (
    ListTopPlayersHistoriesQueryOutput,
)


class ListTopPlayersHistoriesUseCase(ListTopPlayersHistoriesDriverPort):
    def __init__(self, player_gateway: PlayerGateway, ui_handler: UIHandler):
        self.player_gateway = player_gateway
        self._ui_handler = ui_handler

    def execute(self, query: ListTopPlayersHistoriesQuery) -> ListTopPlayersHistoriesQueryOutput:
        category, num_players, num_days = query.category, query.num_players, query.num_days
        usernames = self.player_gateway.get_top_players_usernames(category, num_players)
        histories = self.player_gateway.get_players_rating_histories(category, usernames, num_days)
        self._ui_handler.render_rating_histories(histories)
        return ListTopPlayersHistoriesQueryOutput(histories)
