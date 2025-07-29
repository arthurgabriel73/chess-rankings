from typing import List

from pydantic import BaseModel


class ListTopPlayersRatingHistoryResponseModel(BaseModel):
    histories: List
    model_config = {
        'json_schema_extra': {
            'example': {
                'histories': [
                    {
                        'player': 'Vladlazev_433',
                        'history': {'2025-07-29': 2595, '2025-07-28': 2595, '2025-07-27': 2595, '2025-07-26': 2595},
                    },
                    {
                        'player': 'rorouni-kenshin-123',
                        'history': {'2025-07-29': 2574, '2025-07-28': 2574, '2025-07-27': 2574, '2025-07-26': 2570},
                    },
                    {
                        'player': 'lucas-bahia-123',
                        'history': {'2025-07-29': 2539, '2025-07-28': 2539, '2025-07-27': 2539, '2025-07-26': 2539},
                    },
                ]
            }
        }
    }
