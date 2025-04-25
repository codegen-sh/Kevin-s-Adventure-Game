🌈🌈
# Kevin's Adventure Game

This is a text-based adventure game where you play as Kevin, exploring a world filled with villages, forests, mountains, and caves.

Last updated: April 25, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

In this adventure game, you can:
- Explore different locations (Village, Forest, Mountain, Cave)
- Collect and use items
- Interact with your environment
- Experience random events and weather changes
- Manage your health and inventory

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

## How to Play

1. Follow the prompts in the game.
2. Type 'help' at any time to see available commands.

### Available Commands:
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

- **Dynamic Weather System**: Experience different weather conditions that affect gameplay
- **Item Interactions**: Different items have unique effects based on where and how they're used
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Encounter unexpected situations during your journey

## Project Structure

- `main.py`: Entry point of the game
- `game/`: Core game mechanics and objects
- `locations/`: Different locations in the game world
- `utils/`: Utility functions for game operations

## Known Issues

- The actions.py file is referenced but missing
- The cave.py location file is referenced but missing

## Future Enhancements

- Add more locations to explore
- Implement a combat system
- Add more NPCs and quests
- Expand the item system with crafting
