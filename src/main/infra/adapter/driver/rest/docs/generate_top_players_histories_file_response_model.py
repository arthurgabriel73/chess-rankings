from pydantic import BaseModel


class GenerateTopPlayersHistoriesFileResponseModel(BaseModel):
    success: bool
    file_url: str
    download_url: str

    model_config = {
        'json_schema_extra': {
            'example': {
                'success': True,
                'file_url': 'https://example.com/files/top_players_histories.csv',
                'download_url': 'https://example.com/files/download/top_players_histories.csv',
            }
        }
    }
