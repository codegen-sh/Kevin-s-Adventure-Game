🌈🌈
# Kevin's Adventure Game

This is a text-based adventure game where you play as Kevin, exploring a fantasy world filled with villages, forests, mountains, and caves.

## Game Overview

Kevin's Adventure Game is a simple yet engaging text-based RPG where players can:
- Explore different locations (Village, Forest, Mountain, Cave)
- Collect and manage inventory items
- Interact with the environment
- Experience random events
- Save and load game progress

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the project directory:
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
- `go [location]` - Travel to a connected location
- `look` - Examine your surroundings
- `inventory` - Check your items
- `take [item]` - Pick up an item
- `drop [item]` - Remove an item from your inventory

### Locations
- **Village**: A peaceful starting area with friendly inhabitants
- **Forest**: A mysterious woodland with resources and potential dangers
- **Mountain**: A challenging terrain with valuable items
- **Cave**: A dark location with hidden treasures

### Game Mechanics
- **Health**: Manage your health points to stay alive
- **Inventory**: Collect useful items throughout your journey
- **Gold**: Currency for trading with villagers

## Development

This repository serves as a test environment for TinySitter, demonstrating basic game architecture and mechanics.

### Project Structure
- `main.py` - Game entry point
- `game/` - Core game mechanics
  - `player.py` - Player state and actions
  - `world.py` - World state and location management
  - `items.py` - Item definitions and interactions
- `locations/` - Location-specific code
- `utils/` - Helper functions

## Contributing

This is a test repository, but feel free to fork it and expand on the adventure!

## License

This project is open source and available for educational purposes.
