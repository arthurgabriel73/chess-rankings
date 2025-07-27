from src.main.domain.history import History


class TestHistory:
    def test_should_create_history_with_valid_data(self):
        # Arrange
        category = 'test_category'
        player_username = 'test_player'
        rating_history = {'2020-07-30': 1510, '2020-07-31': 2000}

        # Act
        history = History(category=category, player_username=player_username, rating_history=rating_history)

        # Assert
        assert history.category == category
        assert history.player_username == player_username
        assert history.rating_history == rating_history
        assert history.rating_history.get('2020-07-30') == 1510
        assert history.rating_history.get('2020-07-31') == 2000

    def test_should_create_history_with_empty_rating_history(self):
        # Arrange
        category = 'test_category'
        player_username = 'test_player'

        # Act
        history = History(category=category, player_username=player_username, rating_history=None)

        # Assert
        assert history.category == category
        assert history.player_username == player_username
        assert history.rating_history == {}
