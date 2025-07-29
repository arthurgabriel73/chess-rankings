from typing import List

from src.main.application.port.driven.api.player_gateway import PlayerGateway
from src.main.application.port.driven.file.file_generator_service import FileGeneratorService
from src.main.application.port.driven.file.file_storage_service import FileStorageService
from src.main.application.port.driver.generate_top_players_histories_file_driver_port import (
    GenerateTopPlayersHistoriesFileDriverPort,
)
from src.main.application.port.driver.model.command.generate_top_players_histories_file_command import (
    GenerateTopPlayersHistoriesFileCommand,
)
from src.main.application.port.driver.model.command.generate_top_players_histories_file_command_output import (
    GenerateTopPlayersHistoriesFileCommandOutput,
)
from src.main.domain.history import History


class GenerateTopPlayersHistoriesFileUseCase(GenerateTopPlayersHistoriesFileDriverPort):
    def __init__(
        self,
        player_gateway: PlayerGateway,
        file_storage_service: FileStorageService,
        file_generator_service: FileGeneratorService,
    ):
        self._player_gateway = player_gateway
        self._file_storage_service = file_storage_service
        self._file_generator_service = file_generator_service

    def execute(self, command: GenerateTopPlayersHistoriesFileCommand) -> GenerateTopPlayersHistoriesFileCommandOutput:
        category, num_players, num_days, file_extension = (
            command.category,
            command.num_players,
            command.num_days,
            command.file_extension,
        )
        usernames = self._player_gateway.get_top_players_usernames(category, num_players)
        histories = self._player_gateway.get_players_rating_histories(category, usernames, num_days)
        file = self._generate_histories_file(histories)
        file_key = GenerateTopPlayersHistoriesFileUseCase._generate_file_key(
            category, num_players, num_days, file_extension
        )
        self._upload_file(file_key, file)
        file_url = self._file_storage_service.get_file_url(file_key)
        download_url = self._file_storage_service.get_file_download_url(file_key)
        return GenerateTopPlayersHistoriesFileCommandOutput(success=True, file_url=file_url, download_url=download_url)

    def _generate_histories_file(self, histories: List[History]) -> bytes:
        return self._file_generator_service.generate_history_file(histories)

    @staticmethod
    def _generate_file_key(category: str, num_players: int, num_days: int, file_extension: str) -> str:
        return f'top_{num_players}_{category}_players_histories_{num_days}_days.{file_extension}'

    def _upload_file(self, file_key: str, file: bytes) -> None:
        self._file_storage_service.upload_file(file_key, file)
