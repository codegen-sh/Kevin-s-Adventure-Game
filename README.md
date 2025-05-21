🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a world of mystery and danger as you navigate through forests, caves, villages, and mountains. Collect items, interact with characters, and uncover the secrets of this magical realm.

## Features

- Explore different locations: Village, Forest, Cave, Mountain
- Interact with NPCs and mythical creatures
- Collect and use items
- Complete quests
- Dynamic weather system
- Random events and encounters
- Save and load game progress

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

- Follow the prompts in the game
- Type 'help' at any time to see available commands
- Use commands like 'move', 'look', 'inventory', 'pickup', 'drop', 'use', etc.
- Explore different locations and interact with the environment
- Complete quests and discover secrets

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

## Project Structure

- `main.py`: Main game loop and initialization
- `game/`: Core game mechanics
  - `actions.py`: Player action handling
  - `items.py`: Item functionality
  - `mythical.py`: Mythical creature interactions
  - `player.py`: Player state and actions
  - `state.py`: Game state management
  - `weather.py`: Weather system
  - `world.py`: World structure and navigation
- `locations/`: Location-specific interactions
  - `cave.py`: Cave location
  - `forest.py`: Forest location
  - `mountain.py`: Mountain location
  - `village.py`: Village location
- `utils/`: Utility functions
  - `random_events.py`: Random event generation
  - `save_load.py`: Save/load game functionality
  - `text_formatting.py`: Text formatting utilities

## License

This project is open source and available for educational purposes.

Last updated: May 21, 2025
