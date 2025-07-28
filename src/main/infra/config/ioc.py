import logging
from functools import lru_cache

from src.main.application.port.driver.generate_top_players_histories_file_driver_port import (
    GenerateTopPlayersHistoriesFileDriverPort,
)
from src.main.application.port.driver.list_top_players_driver_port import ListTopPlayersDriverPort
from src.main.application.port.driver.list_top_players_histories_driver_port import ListTopPlayersHistoriesDriverPort
from src.main.application.usecase.generate_top_players_histories_file_use_case import (
    GenerateTopPlayersHistoriesFileUseCase,
)
from src.main.application.usecase.list_top_players_histories_use_case import ListTopPlayersHistoriesUseCase
from src.main.application.usecase.list_top_players_use_case import ListTopPlayersUseCase
from src.main.infra.adapter.driven.api.lichess.lichess_player_api_client import LichessApiClient
from src.main.infra.adapter.driven.api.player_gateway_adapter import PlayerGatewayAdapter
from src.main.infra.adapter.driven.console.console_ui_handler import ConsoleUIHandler
from src.main.infra.adapter.driven.service.csv_generator import CSVGenerator
from src.main.infra.adapter.driven.service.file_generator_service_gateway import FileGeneratorServiceGateway
from src.main.infra.adapter.driven.storage.aws.aws_s3_service import AwsS3Service
from src.main.infra.adapter.driven.storage.file_storage_service_gateway import FileStorageServiceGateway


@lru_cache
def list_top_players_driver_factory() -> ListTopPlayersDriverPort:
    logger = logging.getLogger(' ConsoleUIHandler')
    logging.basicConfig(level=logging.INFO)
    return ListTopPlayersUseCase(PlayerGatewayAdapter(LichessApiClient()), ConsoleUIHandler(logger))


@lru_cache
def list_top_players_histories_driver_factory() -> ListTopPlayersHistoriesDriverPort:
    logger = logging.getLogger(' ConsoleUIHandler')
    logging.basicConfig(level=logging.INFO)
    return ListTopPlayersHistoriesUseCase(PlayerGatewayAdapter(LichessApiClient()), ConsoleUIHandler(logger))


@lru_cache
def generate_top_players_histories_file_driver_factory() -> GenerateTopPlayersHistoriesFileDriverPort:
    return GenerateTopPlayersHistoriesFileUseCase(
        PlayerGatewayAdapter(LichessApiClient()),
        FileStorageServiceGateway(AwsS3Service()),
        FileGeneratorServiceGateway(CSVGenerator()),
    )
