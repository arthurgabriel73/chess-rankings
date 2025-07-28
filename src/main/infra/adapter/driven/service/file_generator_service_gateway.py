from typing import List

from src.main.application.port.driven.file.file_generator_service import FileGeneratorService
from src.main.domain.history import History
from src.main.infra.adapter.driven.service.csv_generator import CSVGenerator


class FileGeneratorServiceGateway(FileGeneratorService):
    def __init__(self, csv_generator: CSVGenerator):
        self._csv_generator = csv_generator

    def generate_history_file(self, histories: List[History]) -> bytes:
        pass
