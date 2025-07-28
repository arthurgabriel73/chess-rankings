from fastapi import APIRouter

from src.main.application.port.driver.model.query.list_top_players_histories_query import ListTopPlayersHistoriesQuery
from src.main.application.port.driver.model.query.list_top_players_query import ListTopPlayersQuery
from src.main.infra.config.ioc import list_top_players_driver_factory, list_top_players_histories_driver_factory

PLAYER_URL = '/players'

players_router = APIRouter(prefix=PLAYER_URL, tags=['Players'])


@players_router.get('/top/{category}/{num_players}', status_code=200)
def list_top_players(category: str, num_players: int):
    driver = list_top_players_driver_factory()
    query = ListTopPlayersQuery(category, num_players)
    return driver.execute(query)


@players_router.get('/top/rating-history/{category}/{num_players}', status_code=200)
def list_top_players_rating_histories(category: str, num_players: int, num_days: int):
    driver = list_top_players_histories_driver_factory()
    query = ListTopPlayersHistoriesQuery(category, num_players, num_days)
    return driver.execute(query)
