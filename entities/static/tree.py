from config import config
from entities import Entity
from utils import EntityType


class Tree(Entity):
    def __init__(self) -> None:
        """
        A class that represents a tree on the game map.

        Tree is a static entity that:
        - Cannot be moved or interacted with
        - Blocks movement of other entities
        """
        super().__init__(config.tree_symbol, EntityType.TREE)
