from src.main.application.port.driven.api.player_gateway import PlayerGateway
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


class GenerateTopPlayersHistoriesFileUseCase(GenerateTopPlayersHistoriesFileDriverPort):
    def __init__(self, player_gateway: PlayerGateway, file_storage_service: FileStorageService):
        self._player_gateway = player_gateway
        self._file_storage_service = file_storage_service

    def execute(self, command: GenerateTopPlayersHistoriesFileCommand) -> GenerateTopPlayersHistoriesFileCommandOutput:
        pass
