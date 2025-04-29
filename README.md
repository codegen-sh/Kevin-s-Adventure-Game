🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: April 29, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

Kevin's Adventure Game is a simple text-based adventure where players can:
- Explore different locations (forest, mountain, village)
- Collect and use items
- Encounter mythical creatures
- Experience dynamic weather conditions
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

## Game Commands

- `go [direction]` - Move in a specific direction (north, south, east, west)
- `look` - Examine your surroundings
- `take [item]` - Pick up an item
- `use [item]` - Use an item in your inventory
- `inventory` - Check your current inventory
- `status` - Check your player status
- `save` - Save your current game
- `load` - Load a previously saved game
- `help` - Display available commands
- `quit` - Save and exit the game

## Game Structure

The game is organized into several modules:
- `game/` - Core game mechanics and objects
  - `player.py` - Player character management
  - `world.py` - World and location management
  - `items.py` - Game items and interactions
  - `mythical.py` - Mythical creatures
  - `weather.py` - Dynamic weather system
  - `state.py` - Game state management
- `locations/` - Different game locations
  - `forest.py` - Forest location and events
  - `mountain.py` - Mountain location and events
  - `village.py` - Village location and events
- `utils/` - Utility functions
  - `save_load.py` - Game saving and loading
  - `text_formatting.py` - Text display utilities
  - `random_events.py` - Random event generation

## Contributing

This is a test repository. Feel free to fork and experiment with the code!

## License

This project is for demonstration purposes only.

