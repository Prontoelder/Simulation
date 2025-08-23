from config import config


def calculate_entity_counts(
    width: int, height: int
) -> tuple[int, int, int, int]:
    """Calculates the number of entities to populate the map."""
    total_cells = width * height
    grass_count = int(total_cells * config.initial_grass_percent)
    rock_count = int(total_cells * config.initial_rock_percent)
    tree_count = int(total_cells * config.initial_tree_percent)

    return grass_count, rock_count, tree_count, total_cells
