🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: May 8, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

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
  - `player.py` - Player character attributes and actions
  - `state.py` - Game state management
  - `weather.py` - Dynamic weather system
  - `world.py` - World map and navigation

- `locations/` - Game locations
  - `forest.py` - Forest location and events
  - `mountain.py` - Mountain location and events
  - `village.py` - Village location and events

- `utils/` - Utility functions
  - `random_events.py` - Random event generation
  - `save_load.py` - Game save/load functionality
  - `text_formatting.py` - Text formatting utilities

## How to Play

1. Start the game by running `python main.py`
2. Navigate through the world using commands like `go north`, `go south`, etc.
3. Interact with objects using commands like `take item`, `use item`, etc.
4. Type `help` at any time to see available commands
5. Use `save` to save your progress and `load` to continue a saved game

## Commands

- `help` - Display available commands
- `look` - Look around your current location
- `inventory` - Check your inventory
- `go [direction]` - Move in a direction (north, south, east, west)
- `take [item]` - Pick up an item
- `use [item]` - Use an item
- `talk to [character]` - Talk to a character
- `save` - Save your game
- `load` - Load a saved game
- `quit` - Exit the game

## Contributing

This is a test repository. Feel free to fork and experiment with your own features!

