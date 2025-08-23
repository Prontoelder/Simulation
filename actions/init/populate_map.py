from typing import TYPE_CHECKING

from actions.base import Action
from config import config
from entities import EntityFactory
from utils import EntityType, calculate_entity_counts

if TYPE_CHECKING:
    from world.map import Map


class PopulateMapAction(Action):
    def execute(self, world_map: "Map") -> None:
        """Fills the map with entities"""
        grass_count, rock_count, tree_count, _ = calculate_entity_counts(
            world_map.width, world_map.height
        )
        entities_to_place = [
            (EntityType.GRASS, grass_count),
            (EntityType.ROCK, rock_count),
            (EntityType.TREE, tree_count),
            (EntityType.HERBIVORE, config.initial_herbivores),
            (EntityType.PREDATOR, config.initial_predators),
        ]
        for entity_type, count in entities_to_place:
            self._place_entities(world_map, entity_type, count)

    @staticmethod
    def _place_entities(
        world_map: "Map", entity_type: EntityType, count: int
    ) -> None:
        """
        Places the specified number of entities of a given type on the map.
        """
        for _ in range(count):
            try:
                coord = world_map.find_random_empty_cell()
            except RuntimeError:
                break
            entity = EntityFactory.create_entity(entity_type)
            world_map.add_entity(coord, entity)
