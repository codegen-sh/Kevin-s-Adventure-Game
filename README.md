🌈🌈
# Kevin's Adventure Game

This is a text-based adventure game where you navigate through different locations, interact with items, and experience dynamic weather conditions.

Last updated: April 18, 2025

## Game Features

- Multiple locations to explore (Forest, Village, Mountain)
- Dynamic weather system that affects gameplay
- Inventory management
- Save and load game functionality
- Random events and encounters
- Mythical creatures to discover

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/kevin-s-github/kevins-adventure-game.git
   ```

2. Run the game:
   ```
   python main.py
   ```

## Usage

1. Follow the prompts in the game.
2. Type 'help' at any time to see available commands.
3. Use 'save' to save your progress and 'quit' to exit the game.

## Game Structure

- `main.py`: Entry point for the game
- `game/`: Core game mechanics
  - `player.py`: Player character management
  - `world.py`: World state and location management
  - `items.py`: Game items and inventory
  - `weather.py`: Dynamic weather system
  - `mythical.py`: Mythical creatures
- `locations/`: Different game locations
  - `forest.py`: Forest location and events
  - `mountain.py`: Mountain location and events
  - `village.py`: Village location and events
- `utils/`: Utility functions
  - `text_formatting.py`: Text display utilities
  - `random_events.py`: Random event generation
  - `save_load.py`: Game save/load functionality
