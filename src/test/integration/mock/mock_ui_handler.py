from typing import List

from src.main.application.port.driven.ui.ui_handler import UIHandler
from src.main.domain.history import History
from src.main.domain.player_username import PlayerUsername


class MockUIHandler(UIHandler):
    def render_rating_histories(self, histories: List[History]) -> None:
        print(histories)

    def render_usernames(self, usernames: List[PlayerUsername]) -> None:
        print([username.value() for username in usernames])
