import random

from config import config
from entities.base.entity import Entity
from utils import Direction, EntityType

from .coordinate import Coordinate


class Map:
    """Represents the game map."""

    def __init__(self) -> None:
        self.width = config.map_width
        self.height = config.map_height
        self._entities = {}

    def add_entity(self, coord: Coordinate, entity: Entity) -> None:
        """Add an entity to the specified coordinate."""
        self._entities[coord] = entity

    def remove_entity(self, coord: Coordinate) -> Entity | None:
        """Remove an entity from the specified coordinate and return it."""
        return self._entities.pop(coord, None)

    def get_entity(self, coord: Coordinate) -> Entity | None:
        """Get the entity at the specified coordinate."""
        return self._entities.get(coord)

    def get_coords_by_type(
        self, entity_type: "EntityType"
    ) -> list[Coordinate]:
        """Get all coordinates containing entities of the specified type."""
        return [
            coord
            for coord, entity in self._entities.items()
            if entity.entity_type == entity_type
        ]

    def get_entity_by_type(self, entity_type: "EntityType") -> list[Entity]:
        """Get all entities of the specified type."""
        return [
            entity
            for entity in self._entities.values()
            if entity.entity_type == entity_type
        ]

    def get_all_entities_with_coords(self) -> dict[Coordinate, Entity]:
        """
        Returns a copy of dictionary with all entities
        and their coordinates.
        """
        return self._entities.copy()

    def get_creatures_count(self) -> tuple[int, int]:
        """Return number of herbivores and predators on the map."""
        herbivores = len(self.get_entity_by_type(EntityType.HERBIVORE))
        predators = len(self.get_entity_by_type(EntityType.PREDATOR))
        return herbivores, predators

    def is_valid_coord(self, x: int, y: int) -> bool:
        """Check if the coordinates are within the map bounds."""
        return 0 <= x < self.width and 0 <= y < self.height

    def is_cell_empty(self, x: int, y: int) -> bool:
        """Check if the cell is empty."""
        return self.get_entity(Coordinate(x, y)) is None

    def find_random_empty_cell(self) -> Coordinate:
        """Find a random empty cell on the map."""
        attempts = 0
        max_attempts = self.width * self.height
        while attempts < max_attempts:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.is_cell_empty(x, y):
                return Coordinate(x, y)
            attempts += 1
        raise RuntimeError("Failed to find an empty cell on the map.")

    def move_entity(
        self, current_coord: Coordinate, target_coord: Coordinate
    ) -> bool:
        """
        Move an entity from one coordinate to another.
        If the target cell is occupied,
        the existing entity will be overwritten.

        Args:
            current_coord: Current coordinates of the entity
            target_coord: Target coordinates to move to
        Returns:
            True if movement was successful, False if no entity
            at current coordinate
        """
        entity_to_move = self._entities.pop(current_coord, None)
        if entity_to_move is None:
            return False
        self._entities[target_coord] = entity_to_move
        return True

    def get_neighbors_cells(self, coord: Coordinate) -> list[Coordinate]:
        """
        Get all valid neighboring cells in 4 cardinal directions.

        Args:
            coord: Center coordinate to get neighbors for

        Returns:
            List of valid neighboring coordinates
        """
        neighbors = []
        for direction in Direction.movement_directions():
            dx, dy = direction.value
            nx, ny = coord.x + dx, coord.y + dy
            if self.is_valid_coord(nx, ny):
                neighbors.append(Coordinate(nx, ny))
        return neighbors
