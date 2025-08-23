from abc import ABC, abstractmethod
from logging import game_logger
from random import choice
from typing import TYPE_CHECKING

from pathfinding import BFSPathFinder
from world import Coordinate, Map

from .entity import Entity

if TYPE_CHECKING:
    from utils import EntityType


class Creature(Entity, ABC):
    """Abstract base class for all creatures in the simulation."""

    def __init__(
        self, symbol: str, entity_type: "EntityType", speed: int, hp: float
    ) -> None:
        super().__init__(symbol, entity_type)
        self.speed = speed
        self.max_hp = hp
        self.hp = hp

    def make_move(self, start_coord: Coordinate, world_map: Map) -> None:
        """Template method for creature movement logic."""
        target_type = self.get_target_type()

        nearby_target = self._find_nearby_entity(
            start_coord, world_map, target_type
        )
        if nearby_target and self.perform_action(
            start_coord, nearby_target, world_map
        ):
            return

        target_coords = self.get_movement_targets(world_map, target_type)
        self._move_towards_targets(start_coord, world_map, target_coords)

    @abstractmethod
    def get_target_type(self) -> "EntityType": ...

    @abstractmethod
    def perform_action(
        self, start_coord: Coordinate, target_coord: Coordinate, world_map: Map
    ) -> bool: ...

    @abstractmethod
    def get_movement_targets(
        self, world_map: Map, target_type: "EntityType"
    ) -> list[Coordinate]: ...

    def _find_nearby_entity(
        self,
        start_coord: Coordinate,
        world_map: Map,
        entity_type: "EntityType",
    ) -> Coordinate | None:
        """Find entity of specified type in neighboring cells."""
        for neighbor_coord in world_map.get_neighbors_cells(start_coord):
            entity = world_map.get_entity(neighbor_coord)
            if entity and entity.entity_type == entity_type:
                return neighbor_coord
        return None

    def _move_towards_targets(
        self,
        start_coord: Coordinate,
        world_map: Map,
        target_coords: list[Coordinate],
    ) -> None:
        """Move creature towards targets or make random move."""
        if target_coords:
            path = BFSPathFinder.find_nearest_target_path(
                start_coord, world_map, target_coords
            )
            if path and len(path) > 1:
                steps = min(self.speed, len(path) - 1)
                next_coord = path[steps]
                if self._try_move(start_coord, next_coord, world_map):
                    return

        self._make_random_move(start_coord, world_map)

    def _try_move(
        self, start_coord: Coordinate, target_coord: Coordinate, world_map: Map
    ) -> bool:
        """Try to move to target coordinate. Return True if successful."""
        if world_map.is_cell_empty(target_coord.x, target_coord.y):
            world_map.move_entity(start_coord, target_coord)
            game_logger.log(
                f"MOVE: {self.symbol} at {start_coord} -> {target_coord}"
            )
            return True
        else:
            game_logger.log(
                f"MOVE_FAIL: {self.symbol} at {start_coord} "
                f"cant move to {target_coord}, cell occupied."
            )
            return False

    def _make_random_move(
        self, start_coord: Coordinate, world_map: Map
    ) -> None:
        """Make a random move to an available neighboring cell."""
        available_moves = [
            neighbor
            for neighbor in world_map.get_neighbors_cells(start_coord)
            if world_map.is_cell_empty(neighbor.x, neighbor.y)
        ]
        if available_moves:
            next_position = choice(available_moves)
            self._try_move(start_coord, next_position, world_map)

    def is_alive(self) -> bool:
        """Check if the creature is alive."""
        return self.hp > 0

    def take_damage(self, amount: float) -> None:
        """Take damage and reduce health."""
        self.hp -= amount

    def restore_hp(self, amount: float) -> None:
        """Restore creature's health, not exceeding the maximum."""
        healed_amount = min(self.max_hp - self.hp, amount)
        self.hp += healed_amount
        if healed_amount > 0:
            game_logger.log(
                f"HEAL: {self.symbol} recovered {healed_amount:.0f} HP."
            )
