from config import config
from entities import Entity
from utils import EntityType


class Rock(Entity):
    def __init__(self) -> None:
        """
        A class that represents a rock on the game map.

        Rock is a static entity that:
        - Cannot be moved or interacted with
        - Blocks movement of other entities
        """
        super().__init__(config.rock_symbol, EntityType.ROCK)
