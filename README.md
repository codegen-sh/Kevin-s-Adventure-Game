🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you play as Kevin, exploring a world filled with villages, forests, mountains, and mythical creatures.

Last updated: May 12, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Features

- **Multiple Locations**: Explore the Village, Forest, and Mountain areas
- **Inventory System**: Collect and use items throughout your journey
- **Mythical Creatures**: Encounter and summon magical beings like phoenixes, unicorns, and dragons
- **Health System**: Manage your health as you face challenges
- **Save/Load**: Save your progress and continue your adventure later

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

## How to Play

1. Follow the prompts in the game
2. Type commands to interact with the world:
   - `move [location]` - Travel to a new location (village, forest, mountain)
   - `look` - Examine your surroundings
   - `inventory` - Check your items
   - `pickup [item]` - Add an item to your inventory
   - `drop [item]` - Remove an item from your inventory
   - `summon [creature]` - Call a mythical creature (phoenix, unicorn, dragon)
   - `help` - Display available commands
   - `quit` - Save and exit the game

## Game Structure

- `main.py` - The main game loop and entry point
- `game/` - Core game mechanics
  - `player.py` - Player status, inventory, and health management
  - `world.py` - Game world and location management
  - `mythical.py` - Mythical creature interactions
  - `items.py` - Item definitions and interactions
- `locations/` - Different areas to explore
  - `village.py` - The starting village area
  - `forest.py` - The mysterious forest
  - `mountain.py` - The dangerous mountain
- `utils/` - Helper functions
  - `save_load.py` - Game saving and loading functionality
  - `text_formatting.py` - Text display utilities
  - `random_events.py` - Random encounter generation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

