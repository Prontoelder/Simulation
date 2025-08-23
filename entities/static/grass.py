from config import config
from entities.base import Entity
from utils import EntityType


class Grass(Entity):
    def __init__(self) -> None:
        """
        A class that represents grass on the game map.

        Grass is a static entity that:
        - Can be eaten by herbivores
        - Restores health to herbivores
        - Can regenerate on empty cells
        """
        super().__init__(config.grass_symbol, EntityType.GRASS)
