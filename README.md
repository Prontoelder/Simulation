# Ecosystem Simulation

This is a console-based ecosystem simulation in Python, where herbivores (🐰) eat grass (🌿), predators (🐺) hunt herbivores, and static objects (rocks 🗿, trees 🌳) block movement. The simulation runs on a grid (map) with mechanics for movement (BFS pathfinding), attacks, eating, hunger, and grass regeneration.

## Features

- **Modular Structure**: OOP with abstract classes, entity factory, and separate modules for actions, entities, rendering, etc.
- **Simulation Logic**:
  - Entities move, eat/attack, and suffer hunger.
  - Pathfinding using BFS to find nearest targets.
  - Grass regenerates with probability.
- **Modes**: Automatic (with pause via Ctrl+C) and step-by-step.
- **Configuration**: Customizable parameters (map size, HP, speed, etc.) in `simulation/config.py`.
- **Logging**: Events (movements, attacks, deaths) are printed to the console.
- **Rendering**: ASCII-art map with emojis, updated each turn.

## Requirements

- Python 3.8+ (tested on 3.12).
- No external dependencies (standard library: `random`, `time`, `os`, `collections`, `abc`, `typing`).

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Prontoelder/simulation.git
   cd simulation
   ```
2. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Running

Run the main script:

```
python simulation/main.py
```

- **Menu**:
  - 1: Start automatic simulation (pause with Ctrl+C).
  - 2: Start step-by-step simulation (Enter for next turn).
  - 0: Exit.
- The simulation ends when either herbivores or predators are extinct.

## Example Output
```
MOVE: 🐰 at (14, 0) -> (14, 1)
ATTACK: 🐺 at (11, 8) ⚔️  🐰 at (10, 8) and dealt 50 damage
MOVE: 🐺 at (5, 3) -> (5, 2)
MOVE: 🐺 at (2, 6) -> (3, 7)
ADD: 🌿 added to (4, 4)
🟫🌿🟫🟫🟫🟫🗿🌿🟫🌿🗿🟫🟫🌳🟫
🟫🟫🟫🌿🟫🌳🌳🗿🌿🌳🟫🟫🐰🌿🐰
🟫🟫🗿🌿🟫🐺🐰🟫🗿🟫🟫🟫🌳🐰🗿
🌿🟫🟫🟫🟫🟫🌳🗿🟫🟫🟫🟫🟫🟫🟫
🟫🟫🟫🟫🌿🌳🟫🟫🟫🟫🟫🟫🟫🟫🟫
🗿🟫🗿🟫🟫🗿🟫🟫🟫🟫🌳🌳🌳🟫🟫
🟫🌳🟫🌳🟫🟫🟫🟫🐰🌳🟫🟫🟫🟫🗿
🟫🌿🟫🐺🟫🟫🟫🟫🟫🟫🟫🗿🌳🌳🟫
🗿🌿🟫🟫🌿🟫🟫🌿🟫🟫🐰🐺🟫🟫🟫
🌿🟫🌿🟫🟫🗿🟫🟫🗿🟫🟫🟫🌿🟫🟫
```
## Project Structure
```
simulation/
├── actions/                # Game actions organized by phase
│   ├── init/               # Initialization actions
│   └── turn/               # Turn-based actions
├── entities/               # All game entities
│   ├── actions/            # Entity actions
│   ├── base/               # Base entity classes
│   ├── static/             # Static entities (grass, rocks, trees)
│   └── entity_factory.py   # Entity creation factory
├── logging/                # Game logging system
├── pathfinding/            # Pathfinding algorithms
├── rendering/              # Map rendering
├── utils/                  # Utility functions and enums
├── world/                  # Map and coordinate system
├── config.py               # Simulation configuration
├── simulation.py           # Main simulation controller
└── main.py                 # Entry point
```
## Configuration

Edit `simulation/config.py` for experiments:

- `map_width`, `map_height`: Map size (default: 15x10).
- `initial_herbivores`, `initial_predators`: Starting counts (default: 6 herbivores, 3 predators).
- `base_herbivore_hp`, `base_predator_hp`: Initial health (default: 100.0 each).
- `grass_recovery_hp`: HP gained by herbivores eating grass (default: 25.0).
- `predator_hp_gain_on_kill`: HP gained by predators on kill (default: 50.0).
- `hunger_hp_loss_per_turn`: HP lost per turn due to hunger (default: 5.0).
- `predator_attack_damage`: Damage dealt by predators (default: 50.0).
- `herbivore_speed`, `predator_speed`: Movement speed (default: 1 for herbivores, 2 for predators).
- `initial_grass_percent`, `initial_rock_percent`, `initial_tree_percent`: Initial map coverage (default: 10% each).
- `initial_grass_regrowth_rate`: Grass regrowth probability per empty cell (default: 1%).
- `herbivore_symbol`, `predator_symbol`, `grass_symbol`, `rock_symbol`, `tree_symbol`, `empty_cell_symbol`, `attack_symbol`: Map symbols (default: 🐰, 🐺, 🌿, 🗿, 🌳, 🟫, ⚔️).
- `turn_delay`: Delay in auto mode (default: 1.8 seconds).
- `show_column_and_row_numbers`: Show map grid numbers (default: False).
