import os
from logging import game_logger
from typing import TYPE_CHECKING

from config import config
from world import Coordinate

if TYPE_CHECKING:
    from world import Map


class MapRenderer:
    """Class for rendering the game map."""

    @staticmethod
    def render_frame(world_map: "Map", turn_count: int) -> None:
        """Prints the full simulation frame: header, logs, and map."""
        MapRenderer._clear_console()
        MapRenderer._print_header(turn_count)
        game_logger.print_game_logs()
        MapRenderer.render_map(world_map)

    @staticmethod
    def _clear_console() -> None:
        """Clears the console."""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def _print_header(turn_count: int) -> None:
        """Prints the header with the turn number."""
        header = (
            f"=== Turn {turn_count} ===\n"
            if turn_count > 0
            else "=== Start of simulation ==="
        )
        print(header)

    @staticmethod
    def render_map(world_map: "Map") -> None:
        """
        Prints the game map. Column and row numbers are shown if
        config.show_column_and_row_numbers is True.
        """
        show_numbers = config.show_column_and_row_numbers

        if show_numbers:
            col_numbers = "      " + " ".join(
                f"{x:2}" for x in range(world_map.width)
            )
            separator = "    " + "-" * (world_map.width * 3 + 1)
            print(separator)
            print(col_numbers)
            print(separator)

        for y in range(world_map.height):
            row_symbols = [
                world_map.get_entity(Coordinate(x, y)).symbol
                if world_map.get_entity(Coordinate(x, y))
                else config.empty_cell_symbol
                for x in range(world_map.width)
            ]

            if show_numbers:
                row_str = " ".join(row_symbols)
                print(f"{y:2} |  " + row_str)
            else:
                row_str = "".join(row_symbols)
                print(row_str)
