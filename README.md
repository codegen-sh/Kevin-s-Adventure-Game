🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, collect items, and encounter mythical creatures.

Last updated: May 8, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Description

Kevin's Adventure Game is an interactive text-based adventure where players explore a world filled with forests, mountains, and villages. Players can collect items, interact with mythical creatures, and experience random events influenced by weather conditions.

## Features

- Multiple locations to explore (Forest, Mountain, Village)
- Inventory system for collecting and using items
- Dynamic weather system that affects gameplay
- Mythical creatures to encounter
- Save and load game functionality
- Random events that create unique experiences

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the project directory:
   ```
   cd Kevin-s-Adventure-Game
   ```

3. Make sure you have Python installed (Python 3.6 or higher recommended)

## Usage

1. Run the game:
   ```
   python main.py
   ```

2. Follow the on-screen prompts to play the game
3. Type 'help' at any time to see available commands
4. Type 'quit' to save your progress and exit the game

## Game Commands

- `go [direction]` - Move in a specified direction (north, south, east, west)
- `look` - Examine your surroundings
- `inventory` - Check your current items
- `take [item]` - Pick up an item
- `use [item]` - Use an item from your inventory
- `talk` - Interact with characters if present
- `help` - Display available commands
- `quit` - Save and exit the game

## Project Structure

- `game/` - Core game mechanics and objects
  - `actions.py` - Handles player actions
  - `items.py` - Defines collectible items
  - `mythical.py` - Mythical creature encounters
  - `player.py` - Player character functionality
  - `weather.py` - Dynamic weather system
  - `world.py` - World state and location management
  
- `locations/` - Different areas to explore
  - `forest.py` - Forest location and events
  - `mountain.py` - Mountain location and events
  - `village.py` - Village location and events
  
- `utils/` - Helper functions
  - `random_events.py` - Generates random encounters
  - `save_load.py` - Game save/load functionality
  - `text_formatting.py` - Text display utilities

## Contributing

This is a test repository. Feel free to fork and experiment with your own features!

## License

This project is open source and available for educational purposes.

