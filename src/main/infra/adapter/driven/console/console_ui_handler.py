from logging import Logger
from typing import List

from src.main.application.port.driven.ui.ui_handler import UIHandler
from src.main.domain.history import History


class ConsoleUIHandler(UIHandler):
    def __init__(self, logger: Logger):
        self.logger = logger

    def render_players_usernames(self, usernames: List[str]) -> None:
        self.logger.info(usernames)

    def render_players_rating_histories(self, histories: List[History]) -> None:
        pass
