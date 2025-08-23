from entities.base import Entity
from utils.enums import EntityType

from .herbivore import Herbivore
from .predator import Predator
from .static.grass import Grass
from .static.rock import Rock
from .static.tree import Tree


class EntityFactory:
    # Registry: a dictionary that associates entity types with their classes
    _registry: dict[EntityType, type] = {
        EntityType.HERBIVORE: Herbivore,
        EntityType.PREDATOR: Predator,
        EntityType.GRASS: Grass,
        EntityType.ROCK: Rock,
        EntityType.TREE: Tree,
    }

    @classmethod
    def create_entity(cls, entity_type: EntityType) -> Entity:
        """
        Creates and returns an instance of an entity of the specified type.
        """
        if entity_type not in cls._registry:
            raise ValueError
        return cls._registry[entity_type]()
