from .base import PathFinder


class AStarPathFinder(PathFinder):
    """A* pathfinding strategy (placeholder)."""

    def find_nearest_target_path(
        self, start_coord, world_map, targets
    ) -> list:
        raise NotImplementedError("A* pathfinding not implemented")
