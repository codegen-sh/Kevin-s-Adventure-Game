🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with challenges, treasures, and mythical creatures.

Last updated: May 8, 2025

## Overview

Kevin's Adventure Game is an interactive text-based adventure where players navigate through different locations, interact with characters, collect items, and face various challenges. The game features dynamic weather, random events, and a save/load system to continue your adventure later.

## Features

- **Multiple Locations**: Explore the village, forest, and mountain areas
- **Item Collection**: Find and use various items throughout your journey
- **Weather System**: Dynamic weather that affects gameplay
- **Mythical Creatures**: Encounter and interact with various mythical beings
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected events that make each playthrough unique

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

1. Follow the text prompts that appear on the screen
2. Type commands to interact with the game world:
   - `go [direction]` - Move in a specific direction (north, south, east, west)
   - `look` - Examine your surroundings
   - `inventory` or `i` - Check your inventory
   - `take [item]` - Pick up an item
   - `use [item]` - Use an item in your inventory
   - `talk [character]` - Speak with a character
   - `save` - Save your current game
   - `load` - Load a previously saved game
   - `help` - Display available commands
   - `quit` - Exit the game

## Game Structure

- **game/**: Core game mechanics
  - `items.py` - Item definitions and functionality
  - `mythical.py` - Mythical creatures and interactions
  - `player.py` - Player character attributes and actions
  - `state.py` - Game state management
  - `weather.py` - Weather system and effects
  - `world.py` - World building and environment
- **locations/**: Different areas to explore
  - `forest.py` - Forest location and events
  - `mountain.py` - Mountain location and events
  - `village.py` - Village location and events
- **utils/**: Helper functions
  - `random_events.py` - Random event generation
  - `save_load.py` - Game saving and loading functionality
  - `text_formatting.py` - Text display formatting

## Contributing

Contributions to improve the game are welcome! Feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available for educational purposes.

