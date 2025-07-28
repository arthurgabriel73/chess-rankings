from src.main.application.port.driven.api.player_gateway import PlayerGateway
from src.main.application.port.driven.ui.ui_handler import UIHandler
from src.main.application.port.driver.list_top_players_driver_port import ListTopPlayersDriverPort
from src.main.application.port.driver.model.query.list_top_players_query import ListTopPlayersQuery
from src.main.application.port.driver.model.query.list_top_players_query_output import ListTopPlayersQueryOutput


class ListTopPlayersUseCase(ListTopPlayersDriverPort):
    def __init__(self, player_gateway: PlayerGateway, ui_handler: UIHandler):
        self._player_gateway = player_gateway
        self._ui_handler = ui_handler

    def execute(self, query: ListTopPlayersQuery) -> ListTopPlayersQueryOutput:
        usernames = self._player_gateway.get_top_players_usernames(query.category, query.num_players)
        self._ui_handler.render_usernames(usernames)
        return ListTopPlayersQueryOutput(usernames)
