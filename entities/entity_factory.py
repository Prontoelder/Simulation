from entities.base import Entity
from pathfinding import AStarPathFinder, BFSPathFinder
from utils.enums import EntityType

from .herbivore import Herbivore
from .predator import Predator
from .static.grass import Grass
from .static.rock import Rock
from .static.tree import Tree


class EntityFactory:
    _registry: dict[EntityType, type] = {
        EntityType.HERBIVORE: Herbivore,
        EntityType.PREDATOR: Predator,
        EntityType.GRASS: Grass,
        EntityType.ROCK: Rock,
        EntityType.TREE: Tree,
    }

    _path_finders = {
        EntityType.HERBIVORE: BFSPathFinder(),
        EntityType.PREDATOR: AStarPathFinder(),
    }

    @classmethod
    def create_entity(cls, entity_type: EntityType) -> Entity:
        if entity_type not in cls._registry:
            raise ValueError(f"Entity type {entity_type} is not registered")

        # Obtain the corresponding pathfinding strategy
        path_finder = cls._path_finders.get(entity_type, BFSPathFinder())

        entity_class = cls._registry[entity_type]
        try:
            return entity_class(path_finder)
        except TypeError:
            return entity_class()
