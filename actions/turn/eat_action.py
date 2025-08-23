from logging import game_logger
from typing import TYPE_CHECKING

from config import config

if TYPE_CHECKING:
    from entities.base import Creature
    from world import Coordinate, Map


class EatAction:
    @staticmethod
    def execute(
        eater: "Creature",
        from_coord: "Coordinate",
        target_coord: "Coordinate",
        world_map: "Map",
    ) -> bool:
        """Eater tries to eat grass at target_coord."""
        target_entity = world_map.get_entity(target_coord)
        if (
            not target_entity
            or target_entity.entity_type != eater.get_target_type()
        ):
            return False

        world_map.remove_entity(target_coord)
        eater.restore_hp(config.grass_recovery_hp)

        game_logger.log(
            f"EAT: {eater.symbol} at {from_coord} ate {target_entity.symbol} "
            f"at {target_coord}"
        )
        return True
