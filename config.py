from dataclasses import dataclass


@dataclass(frozen=True)
class SimulationConfig:
    """Configuration for the simulation."""

    map_width: int = 15
    map_height: int = 10

    # Initial number of creatures
    initial_herbivores: int = 6
    initial_predators: int = 3

    base_herbivore_hp: float = 100.0
    base_predator_hp: float = 100.0
    grass_recovery_hp: float = 25.0
    predator_hp_gain_on_kill: float = 50.0

    hunger_hp_loss_per_turn: float = 5.0

    predator_attack_damage: float = 50.0

    herbivore_speed: int = 1
    predator_speed: int = 2

    # Object generation parameters (0.1 = 10%)
    initial_grass_percent: float = 0.1
    initial_rock_percent: float = 0.1
    initial_tree_percent: float = 0.1
    initial_grass_regrowth_rate: float = 0.01

    herbivore_symbol: str = "🐰"
    predator_symbol: str = "🐺"
    grass_symbol: str = "🌿"
    rock_symbol: str = "🗿"
    tree_symbol: str = "🌳"
    empty_cell_symbol: str = "🟫"
    attack_symbol: str = "⚔️"
    health_symbol: str = "❤️"
    damage_symbol: str = "💥"
    death_symbol: str = "💀"

    # Simulation delay (seconds)
    turn_delay: float = 1.8

    show_column_and_row_numbers: bool = False

    # Maximum number of logs of one type in one line
    max_logs_per_line: int = 5


config = SimulationConfig()
