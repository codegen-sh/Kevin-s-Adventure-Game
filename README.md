🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events.

Last updated: April 30, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players can:
- Explore different locations (Forest, Mountain, Village)
- Collect and use items
- Interact with mythical creatures
- Experience dynamic weather changes
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

1. Start a new game or load a saved game
2. Navigate through locations using directional commands
3. Interact with the environment using action commands
4. Collect items to help you on your journey
5. Save your progress at any time

## Commands

- `help` - Display available commands
- `look` - Examine your current location
- `inventory` - Check your items
- `go [direction]` - Move in a direction (north, south, east, west)
- `take [item]` - Pick up an item
- `use [item]` - Use an item in your inventory
- `talk to [character]` - Interact with characters
- `save` - Save your current progress
- `quit` - Save and exit the game

## Project Structure

- `main.py` - Main game loop and entry point
- `game/` - Core game mechanics
  - `player.py` - Player status and inventory management
  - `world.py` - World state and location management
  - `items.py` - Item definitions and interactions
  - `mythical.py` - Mythical creature encounters
  - `weather.py` - Dynamic weather system
- `locations/` - Different game locations
  - `forest.py` - Forest location and events
  - `mountain.py` - Mountain location and events
  - `village.py` - Village location and events
- `utils/` - Helper functions
  - `save_load.py` - Game saving and loading functionality
  - `text_formatting.py` - Text display utilities
  - `random_events.py` - Random event generation

## Contributing

Contributions to improve the game are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

