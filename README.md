🌈🌈
# Kevin's Adventure Game

A text-based adventure game where players explore a fantasy world filled with challenges, items, and mythical creatures.

Last updated: May 12, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Overview

Kevin's Adventure Game is an interactive text-based adventure where players navigate through different locations, collect items, interact with mythical creatures, and experience random events influenced by weather conditions.

## Features

- Explore multiple locations (forest, mountain, village)
- Collect and use various items
- Encounter mythical creatures
- Experience dynamic weather effects
- Save and load game progress
- Random events that change gameplay

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

## Game Structure

- `game/` - Core game mechanics
  - `items.py` - Item definitions and interactions
  - `mythical.py` - Mythical creature encounters
  - `player.py` - Player character attributes and actions
  - `state.py` - Game state management
  - `weather.py` - Weather system affecting gameplay
  - `world.py` - World map and navigation

- `locations/` - Game world locations
  - `forest.py` - Forest area with unique encounters
  - `mountain.py` - Mountain area with challenges
  - `village.py` - Village for trading and quests

- `utils/` - Helper utilities
  - `random_events.py` - Random event generation
  - `save_load.py` - Game save/load functionality
  - `text_formatting.py` - Text display formatting

## How to Play

1. Start the game by running `python main.py`
2. Follow the on-screen prompts to navigate the world
3. Type commands to interact with the environment:
   - `go [direction]` - Move in a direction (north, south, east, west)
   - `look` - Examine your surroundings
   - `inventory` - Check your items
   - `take [item]` - Pick up an item
   - `use [item]` - Use an item in your inventory
   - `talk [character]` - Speak with a character
   - `save` - Save your game progress
   - `load` - Load a saved game
   - `help` - Display available commands
   - `quit` - Exit the game

## Contributing

This is a test repository. Feel free to fork and experiment with the code!

## License

This project is for testing purposes only.

