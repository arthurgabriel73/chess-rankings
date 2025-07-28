from typing import List

from src.main.application.port.driven.file.file_generator_service import FileGeneratorService
from src.main.domain.history import History
from src.main.infra.adapter.driven.service.csv_generator import CSVGenerator


class FileGeneratorServiceGateway(FileGeneratorService):
    def __init__(self, csv_generator: CSVGenerator):
        self._csv_generator = csv_generator

    def generate_history_file(self, histories: List[History]) -> bytes:
        headers = self._generate_history_headers(histories)
        rows = self._generate_history_rows(histories)
        return self._csv_generator.generate_csv(headers, rows, delimiter=',')

    def _generate_history_headers(self, histories: List[History]) -> List[str]:
        pass

    def _generate_history_rows(self, histories: List[History]) -> List[str]:
        pass
