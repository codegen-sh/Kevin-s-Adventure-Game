🌈🌈
# Kevin's Adventure Game

This is a text-based adventure game where you explore a magical world, collect items, and interact with different locations.

Last updated: May 12, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Features

- Explore multiple locations: Village, Forest, Mountain, and Cave
- Collect and use items to solve challenges
- Interact with your environment
- Save and load game progress
- Dynamic weather system
- Random events during exploration

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

## Game Commands

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

## Game Structure

The game is organized into the following modules:

- `game/`: Core game mechanics
  - `items.py`: Item definitions and interactions
  - `player.py`: Player creation and management
  - `world.py`: World initialization and location management
  - `weather.py`: Dynamic weather system
  - `mythical.py`: Mythical creatures and events
  - `state.py`: Game state management

- `locations/`: Different game locations
  - `village.py`: Village location and interactions
  - `forest.py`: Forest location and interactions
  - `mountain.py`: Mountain location and interactions

- `utils/`: Utility functions
  - `save_load.py`: Game saving and loading functionality
  - `text_formatting.py`: Text formatting and display
  - `random_events.py`: Random event generation

## Saving and Loading

The game automatically saves your progress when you quit. You can also load a previous save when starting the game.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

