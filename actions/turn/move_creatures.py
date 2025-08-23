from typing import TYPE_CHECKING

from actions import Action
from utils import EntityType

if TYPE_CHECKING:
    from world.map import Map


class MoveCreaturesAction(Action):
    def execute(self, world_map: "Map") -> None:
        """Moves all creatures on the map."""
        entities_with_coords = list(
            world_map.get_all_entities_with_coords().items()
        )

        for coord, entity in entities_with_coords:
            if entity.entity_type in EntityType.creatures():
                entity.make_move(coord, world_map)
