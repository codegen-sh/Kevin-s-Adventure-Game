🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you play as Kevin, exploring a world filled with mysteries, challenges, and adventures.

Last updated: May 18, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players navigate through different locations, interact with items, encounter mythical creatures, and experience random events. The game features:

- Multiple locations to explore (Village, Forest, Mountain)
- Dynamic weather system that affects gameplay
- Inventory management
- Save/load game functionality
- Random events to keep gameplay interesting

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

1. Start a new game or load a saved game
2. Navigate through the world using text commands
3. Collect items, interact with the environment, and overcome challenges
4. Save your progress at any time by typing "quit"

## Commands

- `help` - Display available commands
- `look` - Examine your surroundings
- `go [direction]` - Move in a direction (north, south, east, west)
- `take [item]` - Pick up an item
- `use [item]` - Use an item in your inventory
- `inventory` - Check your current inventory
- `status` - Check your player status
- `save` - Save your current game
- `quit` - Save and exit the game

## Game Structure

- `main.py` - Main game loop and entry point
- `game/` - Core game mechanics and objects
  - Player management
  - World state
  - Items and inventory
  - Weather system
  - Mythical creatures
- `locations/` - Different game locations
  - Village
  - Forest
  - Mountain
- `utils/` - Helper functions
  - Save/load functionality
  - Text formatting
  - Random events

## Contributing

Feel free to fork this repository and contribute to the game by adding:
- New locations
- Items and creatures
- Game mechanics
- Bug fixes and improvements

## License

This project is open source and available for educational purposes.

