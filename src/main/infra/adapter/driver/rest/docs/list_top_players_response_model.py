from typing import List

from pydantic import BaseModel


class ListTopPlayersResponseModel(BaseModel):
    # This will automatically parse and validate the route response;
    # if there is a field that is not defined in this model, it will be removed,
    # and if a field is missing in the return, it will throw an error
    usernames: List[str]
    model_config = {'json_schema_extra': {'example': {'usernames': ['Vladmir-38-', 'rorouni-kenshin-123']}}}
