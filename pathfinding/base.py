from abc import ABC, abstractmethod


class PathFinder(ABC):
    """Strategy interface for pathfinding on the world map."""

    @abstractmethod
    def find_nearest_target_path(
        self, start_coord, world_map, targets
    ) -> list | None:
        """Return a path from start to one of targets (including both ends)."""
        raise NotImplementedError
