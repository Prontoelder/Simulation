from time import sleep
from typing import TYPE_CHECKING

from actions.init import PopulateMapAction
from actions.turn import (
    ApplyHungerAction,
    MoveCreaturesAction,
    SpawnGrassAction,
)
from config import config
from rendering import MapRenderer
from utils import EntityType
from utils.menu import (
    show_pause_menu,
    show_step_menu,
)

if TYPE_CHECKING:
    from world import Map


class Simulation:
    def __init__(self, world_map: "Map") -> None:
        self.world_map = world_map
        self.init_actions = [PopulateMapAction()]
        self.turn_actions = [
            MoveCreaturesAction(),
            ApplyHungerAction(),
            SpawnGrassAction(),
        ]
        self.turn_count = 0
        self._is_stopped = False
        self._is_paused = False

    def start_simulation(self, mode: str) -> None:
        """
        Start the simulation in the specified mode.

        Args:
            mode: Simulation mode - "step" for step-by-step,
            "auto" for automatic
        """
        for action in self.init_actions:
            action.execute(self.world_map)

        MapRenderer.render_frame(self.world_map, self.turn_count)

        if mode == "step":
            self._run_step_mode()
        elif mode == "auto":
            self._run_auto_mode()

        print("\n=== Simulation completed ===")
        if self._is_stopped:
            print("Simulation stopped by user.")
        else:
            print(self._get_simulation_end_message())

    def next_turn(self, with_delay: bool = True) -> None:
        """
        Execute the next turn of the simulation.

        Args:
            with_delay: Whether to wait for a delay before the next turn
        """
        self.turn_count += 1
        if with_delay:
            sleep(config.turn_delay)

        for action in self.turn_actions:
            action.execute(self.world_map)

        MapRenderer.render_frame(self.world_map, self.turn_count)

    def stop(self) -> None:
        """Stop the simulation."""
        self._is_stopped = True

    def _run_step_mode(self) -> None:
        """Run simulation in step-by-step mode with user control."""
        while self._is_running():
            choice = self._show_step_menu()

            if choice in {"1", ""}:
                self.next_turn(with_delay=False)
            elif choice == "2":
                self.stop()
                break
            else:
                print("Invalid choice. Please try again.")

    def _show_step_menu(self) -> str:
        """Show the step mode menu and get user choice."""
        return show_step_menu()

    def _run_auto_mode(self) -> None:
        """Run simulation in automatic mode with pause capability."""
        print("\n[AUTOMATIC MODE] Simulation started.")
        print("Press Ctrl+C to pause and control.")
        self._run_simulation_loop()

    def _run_simulation_loop(self) -> None:
        """
        Run the main simulation loop
        with keyboard interrupt handling for pausing.
        """
        try:
            while self._is_running():
                self.next_turn(with_delay=True)
        except KeyboardInterrupt:
            self._handle_pause_menu()

    def _handle_pause_menu(self) -> None:
        """Handle the pause menu and user choices."""
        while True:
            choice = self._show_pause_menu()

            if choice == "1":
                print("\n[CONTINUE] Simulation resumed.")
                print("Press Ctrl+C to pause and control.")
                self._run_simulation_loop()
                break
            elif choice == "2":
                print("\n[STOP] Simulation stopped.")
                self.stop()
                break
            else:
                print("Invalid choice. Please try again.")

    def _show_pause_menu(self) -> str:
        """Show the pause menu and get user choice."""
        return show_pause_menu()

    def _is_running(self) -> bool:
        """Check if the simulation should continue running."""
        return not self._is_stopped and self._is_simulation_running()

    def _is_simulation_running(self) -> bool:
        """
        Check if simulation conditions are met to continue.

        Returns:
            True if both herbivores and predators exist, False otherwise
        """
        herbivore_count = len(
            self.world_map.get_entity_by_type(EntityType.HERBIVORE)
        )
        predator_count = len(
            self.world_map.get_entity_by_type(EntityType.PREDATOR)
        )
        return herbivore_count > 0 and predator_count > 0

    def _get_simulation_end_message(self) -> str:
        """Get appropriate simulation end message based on final state."""
        herbivore_count = len(
            self.world_map.get_entity_by_type(EntityType.HERBIVORE)
        )
        predator_count = len(
            self.world_map.get_entity_by_type(EntityType.PREDATOR)
        )

        if herbivore_count == 0:
            return "All herbivores were eaten. Predators won!"
        if predator_count == 0:
            return "All predators died. Herbivores survived!"
        return "Simulation completed."
