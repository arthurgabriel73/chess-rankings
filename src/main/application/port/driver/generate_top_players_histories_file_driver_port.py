from abc import ABC, abstractmethod

from src.main.application.port.driver.model.command.generate_top_players_histories_file_command import (
    GenerateTopPlayersHistoriesFileCommand,
)
from src.main.application.port.driver.model.command.generate_top_players_histories_file_command_output import (
    GenerateTopPlayersHistoriesFileCommandOutput,
)


class GenerateTopPlayersHistoriesFileDriverPort(ABC):
    @abstractmethod
    def execute(self, command: GenerateTopPlayersHistoriesFileCommand) -> GenerateTopPlayersHistoriesFileCommandOutput:
        pass
