from actions.turn.attack_action import AttackAction
from config import config
from entities.base import Creature
from utils import EntityType
from world import Coordinate, Map


class Predator(Creature):
    """
    A predator that hunts herbivores.

    Behavior:
    - Targets herbivore entities
    - Attacks herbivores when adjacent
    - Moves towards herbivores when not adjacent
    """

    def __init__(self) -> None:
        super().__init__(
            symbol=config.predator_symbol,
            entity_type=EntityType.PREDATOR,
            speed=config.predator_speed,
            hp=config.base_predator_hp,
        )
        self.attack_power = config.predator_attack_damage

    def get_target_type(self) -> EntityType:
        """Predators target herbivores."""
        return EntityType.HERBIVORE

    def perform_action(
        self, start_coord: Coordinate, target_coord: Coordinate, world_map: Map
    ) -> bool:
        """Attack herbivore at target location."""
        return AttackAction.execute(self, start_coord, target_coord, world_map)

    def get_movement_targets(
        self, world_map: Map, target_type: EntityType
    ) -> list[Coordinate]:
        """Get coordinates around herbivores for movement."""
        herbivore_coords = world_map.get_coords_by_type(target_type)
        if not herbivore_coords:
            return []

        target_coords = []
        for coord in herbivore_coords:
            for neighbor in world_map.get_neighbors_cells(coord):
                if (
                    world_map.is_cell_empty(neighbor.x, neighbor.y)
                    and neighbor not in target_coords
                ):
                    target_coords.append(neighbor)

        return target_coords
