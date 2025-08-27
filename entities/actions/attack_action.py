from logging import game_logger
from typing import TYPE_CHECKING

from config import config
from entities.base import Creature

if TYPE_CHECKING:
    from world import Coordinate, Map


class AttackAction:
    @staticmethod
    def execute(
        attacker: "Creature",
        from_coord: "Coordinate",
        target_coord: "Coordinate",
        world_map: "Map",
    ) -> bool:
        """Attacker tries to attack creature at target_coord."""
        target_entity = world_map.get_entity(target_coord)

        if (
            not isinstance(target_entity, Creature)
            or target_entity.entity_type != attacker.get_target_type()
        ):
            return False

        damage = getattr(attacker, "attack_power", 0)
        target_entity.take_damage(damage)

        game_logger.log(
            f"ATTACK: {attacker.symbol} {from_coord} "
            f"{config.attack_symbol} {target_entity.symbol} "
            f"{target_coord} {config.damage_symbol} {int(damage)}"
        )

        if not target_entity.is_alive:
            game_logger.log(
                f"DEATH (battle): {target_entity.symbol} {config.death_symbol}"
                f" {target_coord} by {attacker.symbol}"
            )
            world_map.remove_entity(target_coord)

            if hasattr(attacker, "restore_hp") and damage > 0:
                attacker.restore_hp(config.predator_hp_gain_on_kill)
        return True
