🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with villages, forests, caves, and mountains. Collect items, interact with your environment, and uncover the secrets of this enchanting realm.

Last updated: May 6, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Features

- **Explore Different Locations**: Travel between the village, forest, cave, and mountain
- **Inventory Management**: Collect, use, and drop items throughout your journey
- **Health System**: Manage your health as you face challenges and dangers
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience dynamic events that make each playthrough unique

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

1. When you start the game, you'll be asked if you want to load a saved game or start a new one.
2. Use text commands to navigate and interact with the world.
3. Type 'help' at any time to see all available commands.

### Available Commands

- `move [location]`: Move to a new location (e.g., `move Forest`)
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

## Game Structure

The game is organized into the following directories:

- `game/`: Core game mechanics and objects
- `locations/`: Different locations you can explore
- `utils/`: Utility functions for game operations

## Contributing

Feel free to fork this repository and make your own additions to Kevin's adventure! Pull requests are welcome.

