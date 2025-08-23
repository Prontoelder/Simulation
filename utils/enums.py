from enum import Enum, unique


@unique
class EntityType(Enum):
    """Types of entities in the simulation."""

    HERBIVORE = "herbivore"
    PREDATOR = "predator"
    GRASS = "grass"
    ROCK = "rock"
    TREE = "tree"

    @classmethod
    def creatures(cls) -> list["EntityType"]:
        """Returns types of creatures that can move."""
        return [cls.HERBIVORE, cls.PREDATOR]

    @classmethod
    def static_objects(cls) -> list["EntityType"]:
        """Returns types of static objects."""
        return [cls.ROCK, cls.TREE]

    @classmethod
    def resources(cls) -> list["EntityType"]:
        """Returns types of resources."""
        return [cls.GRASS]

@unique
class Direction(Enum):
    """Movement directions."""

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @classmethod
    def movement_directions(cls) -> list["Direction"]:
        """Returns movement directions."""
        return [cls.UP, cls.DOWN, cls.LEFT, cls.RIGHT]
