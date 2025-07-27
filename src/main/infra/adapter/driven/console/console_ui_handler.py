from logging import Logger
from typing import List

from src.main.application.port.driven.ui.ui_handler import UIHandler
from src.main.domain.history import History
from src.main.domain.player_username import PlayerUsername


class ConsoleUIHandler(UIHandler):
    def __init__(self, logger: Logger):
        self.logger = logger

    def render_players_usernames(self, usernames: List[PlayerUsername]) -> None:
        self.logger.info([username.value() for username in usernames])

    def render_players_rating_histories(self, histories: List[History]) -> None:
        pass
