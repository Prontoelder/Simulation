from typing import TYPE_CHECKING

from actions import Action
from entities import Creature
from sim_logging import game_logger

if TYPE_CHECKING:
    from world.map import Map


class MoveCreaturesAction(Action):
    def execute(self, world_map: "Map") -> None:
        """Moves all creatures on the map."""
        entities_with_coords = list(
            world_map.get_all_entities_with_coords().items()
        )

        for coord, entity in entities_with_coords:
            if isinstance(entity, Creature):
                try:
                    entity.take_turn(coord, world_map)
                except ValueError as err:
                    game_logger.log(
                        f"ACTION_FAIL: {entity.symbol} at {coord}: {err}"
                    )
