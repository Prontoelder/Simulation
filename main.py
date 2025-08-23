import sys

from simulation import Simulation
from utils.menu import show_main_menu
from world import Map


def main() -> None:
    while True:
        choice = show_main_menu()

        if choice in ("1", "2"):
            run_simulation(choice)
        elif choice == "0":
            print("Exit.")
            break
        else:
            print("Invalid choice. Please try again.")


def run_simulation(choice: str) -> None:
    """Runs simulation in the selected mode."""
    mode = "auto" if choice == "1" else "step"
    world_map = Map()
    sim = Simulation(world_map)
    sim.start_simulation(mode=mode)
    print("Return to main menu.")


def handle_keyboard_interrupt() -> None:
    """Handles keyboard interrupt."""
    print("\nGame interrupted by user. Goodbye!")
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        handle_keyboard_interrupt()
