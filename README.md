🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, collect items, and encounter mythical creatures.

Last updated: May 9, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

Kevin's Adventure Game is an interactive text-based adventure where you play as Kevin, exploring a world filled with:
- Multiple locations (village, forest, mountain)
- Collectible items and inventory management
- Dynamic weather system
- Random events
- Mythical creatures to encounter
- Save/load game functionality

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

1. When you start the game, you'll be asked if you want to load a saved game or start a new one.
2. Navigate through the world by typing commands like "go north", "go to forest", etc.
3. Interact with the environment using commands like "look", "take [item]", "use [item]".
4. Check your status with "status" or "inventory".
5. Save your progress at any time by typing "quit".

## Available Commands

- `help` - Display available commands
- `look` - Examine your surroundings
- `go [direction/location]` - Move to a different location
- `take [item]` - Pick up an item
- `drop [item]` - Drop an item from your inventory
- `use [item]` - Use an item in your inventory
- `inventory` or `items` - Check your inventory
- `status` - Check your player status
- `save` - Save your current game
- `quit` - Save and exit the game

## Game Structure

The game is organized into several modules:
- `game/` - Core game mechanics (player, items, world, etc.)
- `locations/` - Different locations you can explore
- `utils/` - Utility functions for saving/loading and text formatting

## Contributing

This is a test repository. Feel free to fork and experiment with your own features!

## License

This project is open source and available for educational purposes.

