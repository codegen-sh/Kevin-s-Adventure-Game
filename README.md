🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: May 14, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

In Kevin's Adventure Game, you play as Kevin, exploring a world with various locations including:
- Villages
- Forests
- Mountains

The game features:
- Item collection and management
- Weather effects that impact gameplay
- Mythical creatures to encounter
- Random events that can help or hinder your journey
- Save/load functionality to continue your adventure

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
2. Navigate through the world by typing commands like "go north", "go south", etc.
3. Interact with your environment using commands like "look", "take [item]", "use [item]".
4. Check your status at any time to see your inventory and health.
5. Save your game by typing "quit" - your progress will be automatically saved.

## Commands

- `help` - Display available commands
- `look` - Examine your current location
- `go [direction]` - Move in a direction (north, south, east, west)
- `take [item]` - Pick up an item
- `use [item]` - Use an item in your inventory
- `inventory` - Check what items you're carrying
- `status` - Check your player status
- `save` - Save your current game
- `quit` - Save and exit the game

## Game Structure

The game is organized into several modules:
- `game/` - Core game mechanics (player, world, items, etc.)
- `locations/` - Different areas you can explore
- `utils/` - Helper functions for game functionality

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

