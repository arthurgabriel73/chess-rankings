import uvicorn
from fastapi import FastAPI

from src.test.resources.json_data.top_players import get_top_players_test_response
from src.test.resources.json_data.top_players_rating_histories import get_player_rating_history_test_response

app = FastAPI()


@app.get('/player/top/{amount}/classical')
def get_player(amount: int):
    return get_top_players_test_response(amount)


@app.get('/user/{username}/rating-history')
def get_rating_history(username: str):
    return get_player_rating_history_test_response(username)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)
