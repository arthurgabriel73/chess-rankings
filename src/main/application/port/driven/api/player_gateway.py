from abc import ABC, abstractmethod
from typing import List

from src.main.domain.history import History


# ABC: A helper class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by simply deriving from ABC avoiding sometimes confusing metaclass usage
class PlayerGateway(ABC):
    # @abstractmethod: A class that has a metaclass derived from ABCMeta cannot be instantiated unless all of its abstract methods and properties are overridden.
    # The abstract methods can be called using any of the normal ‘super’ call mechanisms. abstractmethod() may be used to declare abstract methods for properties and descriptors.
    @abstractmethod
    def get_top_players_usernames(self, category: str, num_players: int) -> List[str]:
        # pass: pass explicitly does nothing
        pass

        # ...: The ... is the shorthand for the Ellipsis global object in python.
        # Similar to None and NotImplemented it can be used as a marker value to indicate the absence of something.

    @abstractmethod
    def get_players_rating_histories(self, category: str, usernames: List[str], num_days: int) -> List[History]:
        pass
