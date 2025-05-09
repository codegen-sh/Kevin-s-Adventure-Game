🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, collect items, and encounter mythical creatures.

Last updated: May 9, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Description

Kevin's Adventure Game is an interactive text-based adventure where players explore a world with forests, mountains, and villages. Players can collect items, interact with mythical creatures, and experience random events influenced by weather conditions.

## Features

- Multiple locations to explore (Forest, Mountain, Village)
- Inventory system for collecting and using items
- Dynamic weather system that affects gameplay
- Encounter mythical creatures
- Save and load game progress
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

4. Run the game:
   ```
   python main.py
   ```

## How to Play

1. Start a new game or load a saved game
2. Navigate through the world using commands like:
   - `go [direction]` (north, south, east, west)
   - `look` to examine your surroundings
   - `inventory` to check your items
   - `take [item]` to collect items
   - `use [item]` to use items in your inventory
   - `talk` to interact with characters
   - `save` to save your progress
   - `help` to see all available commands
   - `quit` to save and exit the game

## Game Structure

- `main.py`: Entry point of the game
- `game/`: Core game mechanics
  - Player status and inventory
  - World initialization
  - Weather system
  - Mythical creatures
- `locations/`: Different areas to explore
  - Forest
  - Mountain
  - Village
- `utils/`: Helper functions
  - Save/load functionality
  - Text formatting
  - Random events

## Contributing

This is a test repository. Feel free to fork and experiment with your own features!

## License

This project is open source and available for educational purposes.

