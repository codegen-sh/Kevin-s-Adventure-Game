🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, collect items, and encounter mythical creatures.

Last updated: May 1, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Features

- Explore multiple locations including forests, mountains, and villages
- Collect and use items throughout your journey
- Encounter mythical creatures and weather events
- Save and load game progress
- Simple text-based interface

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the project directory:
   ```
   cd Kevin-s-Adventure-Game
   ```

3. Make sure you have Python installed (Python 3.6+ recommended)

## Usage

1. Run the game:
   ```
   python main.py
   ```

2. Follow the on-screen prompts to play the game
3. Type 'help' at any time to see available commands
4. Type 'quit' to save your progress and exit the game

## Game Structure

- `game/` - Core game mechanics
  - `items.py` - Item definitions and interactions
  - `mythical.py` - Mythical creature encounters
  - `player.py` - Player state and actions
  - `state.py` - Game state management
  - `weather.py` - Weather events and effects
  - `world.py` - World initialization and management

- `locations/` - Different game locations
  - `forest.py` - Forest location and events
  - `mountain.py` - Mountain location and events
  - `village.py` - Village location and events

- `utils/` - Utility functions
  - `random_events.py` - Random event generation
  - `save_load.py` - Game saving and loading functionality
  - `text_formatting.py` - Text display formatting

## Commands

- `go [direction]` - Move in a direction (north, south, east, west)
- `look` - Examine your surroundings
- `inventory` - Check your inventory
- `take [item]` - Pick up an item
- `use [item]` - Use an item
- `talk` - Talk to nearby characters
- `help` - Display available commands
- `save` - Save your current progress
- `load` - Load a previously saved game
- `quit` - Save and exit the game

## Contributing

This is a test repository. Feel free to fork and experiment with the code!

## License

This project is open source and available for educational purposes.

