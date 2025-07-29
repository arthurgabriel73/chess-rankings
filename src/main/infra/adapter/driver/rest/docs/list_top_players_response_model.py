from typing import List

from pydantic import BaseModel


class ListTopPlayersResponseModel(BaseModel):
    usernames: List[str]
    model_config = {'json_schema_extra': {'example': {'usernames': ['Vladmir-38-', 'rorouni-kenshin-123']}}}
