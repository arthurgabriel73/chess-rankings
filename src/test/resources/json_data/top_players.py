def get_top_players_test_response(amount: int) -> dict:
    return {
        'users': [
            {'id': f'user{i}', 'username': f'User{i}', 'perfs': {'classical': {'rating': 2595 - i, 'progress': 30}}}
            for i in range(1, amount + 1)
        ]
    }
