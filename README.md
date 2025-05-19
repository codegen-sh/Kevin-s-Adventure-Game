🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you play as Kevin, exploring a world filled with villages, forests, mountains, and mythical creatures.

Last updated: May 19, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players can:
- Explore different locations (Village, Forest, Mountain)
- Collect and manage inventory items
- Interact with the game world through text commands
- Experience random events and weather changes
- Encounter mythical creatures
- Save and load game progress

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the game directory:
   ```
   cd Kevin-s-Adventure-Game
   ```

3. Run the game:
   ```
   python main.py
   ```

## Gameplay

### Basic Commands
- `help` - Display available commands
- `quit` - Save and exit the game
- `move [location]` - Move to a different location (Village, Forest, Mountain)
- `pickup [item]` - Add an item to your inventory
- `drop [item]` - Remove an item from your inventory
- `use [item]` - Use an item from your inventory

### Player Stats
- **Health**: Starts at 100. Decreases when taking damage, increases when healing.
- **Inventory**: Items you've collected during your adventure.
- **Gold**: Currency for purchasing items and services.
- **Location**: Your current position in the game world.

### Game World
The game features multiple locations to explore:
- **Village**: A safe starting area with shops and NPCs
- **Forest**: Contains valuable resources and potential dangers
- **Mountain**: Challenging terrain with rare items and mythical creatures

## Save/Load System

The game automatically saves your progress when you quit. You can load a previous save when starting the game.

## Development

The game is structured into several modules:
- `game/`: Core game mechanics and objects
- `locations/`: Different areas in the game world
- `utils/`: Helper functions for game functionality

## Contributing

Contributions to expand the game world, add new features, or fix bugs are welcome! Please feel free to submit pull requests.

## License

This project is open source and available for educational and entertainment purposes.

