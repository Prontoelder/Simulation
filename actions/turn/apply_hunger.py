from logging import game_logger
from typing import TYPE_CHECKING

from actions import Action
from config import config
from entities.base import Creature

if TYPE_CHECKING:
    from world.map import Map


class ApplyHungerAction(Action):
    def execute(self, world_map: "Map") -> None:
        """Applies hunger (HP loss) to all creatures on the map."""
        entities_with_coords = list(
            world_map.get_all_entities_with_coords().items()
        )

        for coord, entity in entities_with_coords:
            if isinstance(entity, Creature):
                entity.take_damage(config.hunger_hp_loss_per_turn)
                if not entity.is_alive:
                    game_logger.log(
                        f"DEATH (starvation): {entity.symbol} {coord} "
                        f"{config.death_symbol}"
                    )
                    world_map.remove_entity(coord)
