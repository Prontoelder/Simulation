from logging import game_logger
from random import random
from typing import TYPE_CHECKING

from actions import Action
from config import config
from utils import EntityType
from world import Coordinate

if TYPE_CHECKING:
    from world.map import Map


class SpawnGrassAction(Action):
    @staticmethod
    def _should_regrow_grass() -> bool:
        """Checks if grass should regrow."""
        return random() < config.initial_grass_regrowth_rate

    def execute(self, world_map: "Map") -> None:
        """Spawns grass on the random empty cells."""
        from entities.entity_factory import EntityFactory

        for x in range(world_map.width):
            for y in range(world_map.height):
                if (
                    world_map.is_cell_empty(x, y)
                    and self._should_regrow_grass()
                ):
                    grass = EntityFactory.create_entity(EntityType.GRASS)
                    world_map.add_entity(
                        Coordinate(x, y),
                        grass,
                    )
                    game_logger.log(
                        f"ADD: {config.grass_symbol} to ({x}, {y})"
                    )
