🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you play as Kevin, exploring a world filled with mysteries, challenges, and adventures.

Last updated: May 18, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players navigate through different locations, interact with items, encounter mythical creatures, and experience random events influenced by weather conditions. The game features a save/load system to continue your adventure at any time.

## Features

- **Multiple Locations**: Explore forests, mountains, villages, and more
- **Inventory System**: Collect and use items throughout your journey
- **Weather Effects**: Dynamic weather system that affects gameplay
- **Mythical Encounters**: Meet and interact with mythical creatures
- **Save/Load System**: Save your progress and continue your adventure later

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
3. Interact with your environment using commands like "look", "take [item]", "use [item]", etc.
4. Type "help" at any time to see a list of available commands.
5. Type "quit" to save your progress and exit the game.

## Game Commands

- `go [direction]` - Move in a specified direction (north, south, east, west)
- `look` - Examine your current surroundings
- `take [item]` - Pick up an item
- `use [item]` - Use an item in your inventory
- `inventory` or `inv` - Check your inventory
- `status` - Check your player status
- `help` - Display available commands
- `quit` - Save and exit the game

## Game Structure

- `main.py` - The main game loop and entry point
- `game/` - Core game mechanics and objects
  - `player.py` - Player character functionality
  - `world.py` - World map and location management
  - `items.py` - Item definitions and interactions
  - `mythical.py` - Mythical creature encounters
  - `weather.py` - Weather system and effects
- `locations/` - Different game locations
  - `forest.py` - Forest location and events
  - `mountain.py` - Mountain location and events
  - `village.py` - Village location and events
- `utils/` - Utility functions
  - `save_load.py` - Game save/load functionality
  - `text_formatting.py` - Text display utilities
  - `random_events.py` - Random event generation

## Contributing

Contributions to Kevin's Adventure Game are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License

This project is open source and available under the MIT License.

