from fastapi import APIRouter

from src.main.application.port.driver.model.command.generate_top_players_histories_file_command import (
    GenerateTopPlayersHistoriesFileCommand,
)
from src.main.application.port.driver.model.query.list_top_players_histories_query import ListTopPlayersHistoriesQuery
from src.main.application.port.driver.model.query.list_top_players_query import ListTopPlayersQuery
from src.main.infra.adapter.driver.rest.docs.generate_top_players_histories_file_response_model import (
    GenerateTopPlayersHistoriesFileResponseModel,
)
from src.main.infra.adapter.driver.rest.docs.list_top_players_rating_history_response_model import (
    ListTopPlayersRatingHistoryResponseModel,
)
from src.main.infra.adapter.driver.rest.docs.list_top_players_response_model import ListTopPlayersResponseModel
from src.main.infra.config.ioc import (
    generate_top_players_histories_file_driver_factory,
    list_top_players_driver_factory,
    list_top_players_histories_driver_factory,
)

PLAYER_URL = '/players'

players_router = APIRouter(prefix=PLAYER_URL, tags=['Players'])


@players_router.get('/top/{category}/{num_players}', status_code=200, response_model=ListTopPlayersResponseModel)
def list_top_players(category: str, num_players: int):
    driver = list_top_players_driver_factory()
    query = ListTopPlayersQuery(category, num_players)
    return driver.execute(query)


@players_router.get(
    '/top/rating-history/{category}/{num_players}',
    status_code=200,
    response_model=ListTopPlayersRatingHistoryResponseModel,
)
def list_top_players_rating_histories(category: str, num_players: int, num_days: int = 30):
    driver = list_top_players_histories_driver_factory()
    query = ListTopPlayersHistoriesQuery(category, num_players, num_days)
    return driver.execute(query)


@players_router.post(
    '/top/rating-history/{category}/{num_players}/generate-file',
    status_code=201,
    response_model=GenerateTopPlayersHistoriesFileResponseModel,
)
def generate_top_players_histories_file(
    category: str, num_players: int, num_days: int = 30, file_extension: str = 'csv'
):
    driver = generate_top_players_histories_file_driver_factory()
    command = GenerateTopPlayersHistoriesFileCommand(category, num_players, num_days, file_extension)
    return driver.execute(command)
