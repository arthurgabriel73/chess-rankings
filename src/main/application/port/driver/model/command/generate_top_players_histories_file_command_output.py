from dataclasses import dataclass


@dataclass
class GenerateTopPlayersHistoriesFileCommandOutput:
    success: bool
    file_url: str
    download_url: str
