from actions.turn.eat_action import EatAction
from config import config
from entities.base import Creature
from utils import EntityType
from world import Coordinate, Map


class Herbivore(Creature):
    """
    A herbivore that eats grass to restore health.

    Behavior:
    - Targets grass entities
    - Eats grass when adjacent
    - Moves towards grass when not adjacent
    """

    def __init__(self) -> None:
        super().__init__(
            symbol=config.herbivore_symbol,
            entity_type=EntityType.HERBIVORE,
            speed=config.herbivore_speed,
            hp=config.base_herbivore_hp,
        )

    def get_target_type(self) -> EntityType:
        """Herbivores target grass."""
        return EntityType.GRASS

    def perform_action(
        self, start_coord: Coordinate, target_coord: Coordinate, world_map: Map
    ) -> bool:
        """Eat grass at target location."""
        return EatAction.execute(self, start_coord, target_coord, world_map)

    def get_movement_targets(
        self, world_map: Map, target_type: EntityType
    ) -> list[Coordinate]:
        """Get all grass coordinates for movement."""
        return world_map.get_coords_by_type(target_type)
