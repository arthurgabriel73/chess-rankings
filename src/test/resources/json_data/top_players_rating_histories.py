import random
from datetime import datetime, timedelta


def get_player_rating_history_test_response(username: str) -> list:
    today = datetime.now()
    offsets_in_days = list(range(29, -1, -1))
    initial_rating_for_oldest_day = 1500
    rating_increase_per_day = 17

    dynamic_points = []
    for i, days_ago in enumerate(offsets_in_days):
        past_date = today - timedelta(days=days_ago * 2)
        current_day_rating = initial_rating_for_oldest_day + i * rating_increase_per_day
        current_day_rating += random.randint(-5, 5)
        current_day_rating = max(1400, current_day_rating)

        dynamic_points.append([past_date.year, past_date.month, past_date.day, current_day_rating])

    return [
        {'name': 'UltraBullet', 'points': dynamic_points},
        {'name': 'Bullet', 'points': dynamic_points},
        {'name': 'Classical', 'points': dynamic_points},
        {'name': 'Blitz', 'points': dynamic_points},
        {'name': 'Rapid', 'points': dynamic_points},
    ]
