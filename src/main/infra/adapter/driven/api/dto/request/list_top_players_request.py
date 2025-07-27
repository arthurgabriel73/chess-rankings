class ListTopPlayersRequest:
    def __init__(self, category: str, num_players: int):
        self.category = category.lower()
        self.num_players = num_players
