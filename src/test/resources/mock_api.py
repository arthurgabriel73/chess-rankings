import random
from datetime import datetime, timedelta

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/player/top/{amount}/classical')
def get_player(amount: int):
    return {
        'users': [
            {'id': f'user{i}', 'username': f'User{i}', 'perfs': {'classical': {'rating': 2595 - i, 'progress': 30}}}
            for i in range(1, amount + 1)
        ]
    }


@app.get('/user/{username}/rating-history')
def get_rating_history(username: str):
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


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)
