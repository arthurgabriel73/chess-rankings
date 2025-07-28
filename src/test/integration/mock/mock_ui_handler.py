from typing import List

from src.main.application.port.driven.ui.ui_handler import UIHandler
from src.main.domain.history import History


class MockUIHandler(UIHandler):
    def render_usernames(self, usernames: List[str]) -> None:
        print(usernames)

    def render_rating_history(self, history: History) -> None:
        print(history)
