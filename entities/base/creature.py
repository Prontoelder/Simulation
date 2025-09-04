from abc import ABC, abstractmethod
from random import choice
from typing import TYPE_CHECKING

from config import config
from pathfinding import BFSPathFinder
from sim_logging import game_logger
from world import Coordinate, Map

from .entity import Entity

if TYPE_CHECKING:
    from utils import EntityType


class Creature(Entity, ABC):
    """Abstract base class for all creatures in the simulation."""

    def __init__(
        self,
        symbol: str,
        entity_type: "EntityType",
        speed: int,
        hp: float,
        path_finder=None,
    ) -> None:
        super().__init__(symbol, entity_type)
        self.speed = speed
        self.max_hp = hp
        self.hp = hp
        # Strategy for pathfinding (default: BFS)
        self.path_finder = path_finder or BFSPathFinder()

    def take_turn(self, start_coord: Coordinate, world_map: Map) -> None:
        """Full turn: attempt an action, then move."""
        target_type = self.get_target_type()

        nearby_target = self._find_nearby_entity(
            start_coord, world_map, target_type
        )
        if nearby_target:
            try:
                self.perform_action(start_coord, nearby_target, world_map)
                return
            except ValueError as err:
                game_logger.log(
                    f"ACTION_FAIL: {self.symbol} at {start_coord} "
                    f"-> {nearby_target}: {err}"
                )

        target_coords = self.get_movement_targets(world_map, target_type)
        self._move_towards_targets(start_coord, world_map, target_coords)

    @abstractmethod
    def get_target_type(self) -> "EntityType": ...

    @abstractmethod
    def perform_action(
        self, start_coord: Coordinate, target_coord: Coordinate, world_map: Map
    ) -> None: ...

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
            try:
                path = self.path_finder.find_nearest_target_path(
                    start_coord, world_map, target_coords
                )
            except NotImplementedError:
                # Fallback to BFS if current strategy is not implemented
                fallback = BFSPathFinder()
                path = fallback.find_nearest_target_path(
                    start_coord, world_map, target_coords
                )
            if path and len(path) > 1:
                steps = min(self.speed, len(path) - 1)
                next_coord = path[steps]
                try:
                    self._move_to(start_coord, next_coord, world_map)
                    return
                except ValueError as err:
                    game_logger.log(
                        f"MOVE_FAIL: {self.symbol} {start_coord} -> "
                        f"{next_coord} error: {err}"
                    )

        self._make_random_move(start_coord, world_map)

    def _move_to(
        self, start_coord: Coordinate, target_coord: Coordinate, world_map: Map
    ) -> None:
        """Move to target cell."""
        if not world_map.is_cell_empty(target_coord.x, target_coord.y):
            raise ValueError("target cell is occupied")

        world_map.move_entity(start_coord, target_coord)
        game_logger.log(f"MOVE {self.symbol}: {start_coord} -> {target_coord}")

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
            try:
                self._move_to(start_coord, next_position, world_map)
            except ValueError as err:
                game_logger.log(
                    f"MOVE_FAIL: {self.symbol} {start_coord} -> "
                    f"{next_position} error: {err}"
                )

    @property
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
                f"HEAL: {self.symbol} {config.health_symbol}"
                f" {healed_amount:.0f} HP"
            )
