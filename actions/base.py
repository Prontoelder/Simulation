from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from world.map import Map


class Action(ABC):
    """
    An abstract base class for all actions in the game.
    """

    @abstractmethod
    def execute(self, world_map: "Map") -> None:
        pass
