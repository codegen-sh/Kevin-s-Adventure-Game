🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a fantasy world, collect items, and embark on quests.

Last updated: April 25, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

In Kevin's Adventure Game, you play as Kevin, a brave adventurer exploring a world filled with:

- A peaceful village where you can rest and trade
- A mysterious forest with hidden treasures and dangers
- Treacherous mountains with valuable resources
- A dark cave system waiting to be discovered

Manage your health, inventory, and gold as you navigate through different locations and face various challenges.

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

- `go [location]` - Travel to a connected location (e.g., `go Forest`)
- `look` - Examine your current surroundings
- `inventory` or `i` - Check your inventory
- `take [item]` - Pick up an item
- `drop [item]` - Remove an item from your inventory
- `use [item]` - Use an item from your inventory
- `help` - Display available commands
- `save` - Save your current game progress
- `quit` - Save and exit the game

### Game Features

- **Health System**: Manage your health points (HP) through combat and healing
- **Inventory Management**: Collect and use various items throughout your journey
- **Gold Economy**: Earn and spend gold on items and services
- **Dynamic Weather**: Experience changing weather conditions that affect gameplay
- **Random Events**: Encounter unexpected situations during your adventure

## Development

The game is structured with the following components:

- `main.py` - Game entry point and main loop
- `game/` - Core game mechanics and objects
- `locations/` - Different areas in the game world
- `utils/` - Helper functions and utilities

## Contributing

Contributions to Kevin's Adventure Game are welcome! Feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
