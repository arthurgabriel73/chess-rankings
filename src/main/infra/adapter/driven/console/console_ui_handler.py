from datetime import datetime
from logging import Logger
from typing import List

from src.main.application.port.driven.ui.ui_handler import UIHandler
from src.main.domain.history import History


class ConsoleUIHandler(UIHandler):
    def __init__(self, logger: Logger):
        self.logger = logger

    def render_usernames(self, usernames: List[str]) -> None:
        self.logger.info(usernames)

    def render_rating_history(self, history: History) -> None:
        reformatted_rating_history = []
        for date_string, value in history.rating_history.items():
            new_date_key = datetime.strptime(date_string, '%Y-%m-%d').strftime('%b %d')
            reformatted_rating_history.append(f'{new_date_key}: {value}')
        history_display_string = ', '.join(reformatted_rating_history)
        self.logger.info(f'- {history.player_username}, {history_display_string}')
