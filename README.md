🌈🎮🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: May 17, 2025

## Overview

Kevin's Adventure Game is an interactive text-based adventure where players can:
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

2. Navigate to the project directory:
   ```
   cd Kevin-s-Adventure-Game
   ```

3. Run the game:
   ```
   python main.py
   ```

## Game Structure

- `game/` - Core game mechanics
  - `items.py` - Item definitions and interactions
  - `mythical.py` - Mythical creatures and encounters
  - `player.py` - Player character attributes and inventory
  - `state.py` - Game state management
  - `weather.py` - Dynamic weather system
  - `world.py` - World map and navigation

- `locations/` - Game world locations
  - `forest.py` - Forest area events and interactions
  - `mountain.py` - Mountain area events and interactions
  - `village.py` - Village area events and interactions

- `utils/` - Helper utilities
  - `random_events.py` - Random event generation
  - `save_load.py` - Game save/load functionality
  - `text_formatting.py` - Text display formatting

## Gameplay Commands

- `go [direction]` - Move in a direction (north, south, east, west)
- `look` - Examine your surroundings
- `take [item]` - Pick up an item
- `use [item]` - Use an item in your inventory
- `inventory` - Check your inventory
- `status` - Check your player status
- `save` - Save your game
- `load` - Load a saved game
- `help` - Display available commands
- `quit` - Exit the game

## Contributing

This is a test repository. Feel free to fork and experiment with your own features!

## License

This project is for demonstration purposes only.

