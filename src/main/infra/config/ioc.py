import logging
from functools import lru_cache

from src.main.application.port.driver.list_top_players_driver_port import ListTopPlayersDriverPort
from src.main.application.usecase.list_top_players_use_case import ListTopPlayersUseCase
from src.main.infra.adapter.driven.api.lichess.lichess_player_api_client import LichessApiClient
from src.main.infra.adapter.driven.api.player_gateway_adapter import PlayerGatewayAdapter
from src.main.infra.adapter.driven.console.console_ui_handler import ConsoleUIHandler


@lru_cache
def list_top_players_driver_factory() -> ListTopPlayersDriverPort:
    logger = logging.getLogger(' ConsoleUIHandler')
    logging.basicConfig(level=logging.INFO)
    return ListTopPlayersUseCase(PlayerGatewayAdapter(LichessApiClient()), ConsoleUIHandler(logger))
