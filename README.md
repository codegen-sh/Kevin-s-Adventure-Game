🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, collect items, and encounter mythical creatures.

Last updated: May 9, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players explore various locations including forests, mountains, and villages. Players can collect items, interact with mythical creatures, and experience random events influenced by weather conditions.

## Features

- Multiple locations to explore (Forest, Mountain, Village)
- Inventory system for collecting and using items
- Dynamic weather system that affects gameplay
- Encounter mythical creatures
- Save and load game progress
- Random events that create unique experiences

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

1. Start a new game or load a saved game
2. Navigate through locations using commands like "go forest", "go mountain", "go village"
3. Collect items with "take [item]"
4. Check your inventory with "inventory"
5. Save your progress with "save"
6. Type 'help' at any time to see all available commands

## Game Commands

- `go [location]` - Travel to a different location
- `look` - Examine your surroundings
- `take [item]` - Pick up an item
- `use [item]` - Use an item from your inventory
- `inventory` - Check what items you're carrying
- `status` - Check your player status
- `save` - Save your current game
- `load` - Load a previously saved game
- `help` - Display available commands
- `quit` - Save and exit the game

## Project Structure

- `main.py` - Main game loop and entry point
- `game/` - Core game mechanics
  - `player.py` - Player status and inventory
  - `world.py` - Game world and location management
  - `items.py` - Item definitions and interactions
  - `mythical.py` - Mythical creature encounters
  - `weather.py` - Weather system affecting gameplay
- `locations/` - Different game locations
  - `forest.py` - Forest location and events
  - `mountain.py` - Mountain location and events
  - `village.py` - Village location and events
- `utils/` - Utility functions
  - `save_load.py` - Game saving and loading
  - `text_formatting.py` - Text display formatting
  - `random_events.py` - Random event generation

## Contributing

Contributions to Kevin's Adventure Game are welcome! Feel free to submit pull requests with new features, locations, or bug fixes.

## License

This project is open source and available for educational purposes.

