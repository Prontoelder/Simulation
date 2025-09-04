from random import random
from typing import TYPE_CHECKING

from actions import Action
from config import config
from entities.entity_factory import EntityFactory
from sim_logging import game_logger
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
        """Spawns grass on random empty cells."""
        empty_cells = [
            Coordinate(x, y)
            for x in range(world_map.width)
            for y in range(world_map.height)
            if world_map.is_cell_empty(x, y)
        ]

        for coord in empty_cells:
            if random() < config.initial_grass_regrowth_rate:
                grass = EntityFactory.create_entity(EntityType.GRASS)
                world_map.add_entity(coord, grass)
                game_logger.log(f"ADD: {config.grass_symbol} to {coord}")
