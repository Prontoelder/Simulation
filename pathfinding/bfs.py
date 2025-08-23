from collections import deque

from world import Coordinate, Map


class BFSPathFinder:
    @staticmethod
    def find_nearest_target_path(
        start_coord: Coordinate,
        world_map: Map,
        target_coords: list[Coordinate],
    ) -> list[Coordinate] | None:
        """
        Find the nearest path to a target coordinate using BFS.
        Returns:
            The path to the target coordinate or None if no path is found.
        """
        queue = deque([start_coord])

        # Dictionary for path restoration: {child_cell: parent_cell}
        came_from = {start_coord: None}

        while queue:
            current = queue.popleft()

            if current in target_coords and current != start_coord:
                # Restore path from target to start
                path = []
                path_node = current
                while path_node is not None:
                    path.append(path_node)
                    path_node = came_from[path_node]
                path.reverse()  # Reverse to get path from start to target
                return path

            for neighbor in world_map.get_neighbors_cells(current):
                if neighbor in came_from:
                    continue

                if (
                    world_map.is_cell_empty(neighbor.x, neighbor.y)
                    or neighbor in target_coords
                ):
                    came_from[neighbor] = current
                    queue.append(neighbor)
        return None
