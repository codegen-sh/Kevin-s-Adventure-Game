🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you play as Kevin, exploring a fantasy world filled with villages, forests, mountains, and caves.

## Features

- Explore different locations including a village, forest, cave, and mountain
- Collect and use items
- Interact with the environment
- Save and load game progress
- Random events and encounters
- Health and inventory management

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Run the game:
   ```
   python main.py
   ```

## Game Structure

- `game/` - Core game mechanics
  - `player.py` - Player character management
  - `world.py` - Game world and locations
  - `items.py` - Item definitions and interactions
  - `mythical.py` - Mythical creatures and encounters
  - `state.py` - Game state management
  - `weather.py` - Weather system
- `locations/` - Location-specific interactions
  - `forest.py` - Forest location events
  - `mountain.py` - Mountain location events
  - `village.py` - Village location events
- `utils/` - Utility functions
  - `random_events.py` - Random event generation
  - `save_load.py` - Game saving and loading
  - `text_formatting.py` - Text display formatting

## Usage

1. Follow the prompts in the game.
2. Type 'help' at any time to see available commands.
3. Type 'quit' to save and exit the game.

## Commands

- `go [location]` - Travel to a connected location
- `look` - Examine your surroundings
- `inventory` - Check your inventory
- `take [item]` - Pick up an item
- `drop [item]` - Drop an item from your inventory
- `use [item]` - Use an item from your inventory
- `talk` - Talk to nearby characters
- `help` - Display available commands
- `quit` - Save and exit the game
