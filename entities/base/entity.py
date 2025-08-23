from abc import ABC

from utils import EntityType


class Entity(ABC):
    def __init__(self, symbol: str, entity_type: EntityType) -> None:
        """
        A base class for all entities in the game.
        """
        self.symbol = symbol
        self.entity_type = entity_type
