🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with mystery and danger.

Last updated: May 8, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Overview

Kevin's Adventure Game is an interactive text-based adventure where players navigate through different locations, collect items, interact with characters, and uncover the secrets of a magical realm. The game features:

- Multiple locations to explore (Village, Forest, Mountain)
- Inventory management system
- Health and gold tracking
- Save and load game functionality
- Random events and encounters
- Weather system that affects gameplay

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

The game is organized into several modules:

- `game/`: Core game mechanics
  - `player.py`: Player creation and management
  - `world.py`: World initialization and location management
  - `items.py`: Item definitions and interactions
  - `state.py`: Game state management
  - `weather.py`: Weather system affecting gameplay
  - `mythical.py`: Mythical creatures and encounters

- `locations/`: Different game locations
  - `village.py`: Village location and interactions
  - `forest.py`: Forest location and interactions
  - `mountain.py`: Mountain location and interactions

- `utils/`: Utility functions
  - `text_formatting.py`: Text display formatting
  - `save_load.py`: Game save and load functionality
  - `random_events.py`: Random event generation

## How to Play

1. Start the game by running `python main.py`
2. Choose to start a new game or load a saved game
3. Navigate through the world using text commands
4. Collect items, interact with the environment, and manage your resources
5. Type 'help' at any time to see available commands

### Available Commands

- `move [location]`: Move to a new location
- `look`: Examine your surroundings
- `inventory`: Check your inventory
- `pickup [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message
- `quit`: Save and exit the game

## Game Features

- **Player Status**: Track your health, inventory, and gold
- **Inventory Management**: Collect, use, and drop items
- **Multiple Locations**: Explore different areas with unique challenges
- **Save/Load System**: Save your progress and continue later
- **Random Events**: Encounter unexpected situations during your adventure
- **Weather System**: Experience different weather conditions that affect gameplay

## Contributing

Contributions to Kevin's Adventure Game are welcome! Feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is open source and available for educational and personal use.

