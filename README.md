# Kevin's Adventure Game

A text-based adventure game where you explore a world of mystery and danger as you navigate through forests, caves, villages, and mountains. Collect items, interact with characters, and uncover the secrets of this magical realm.

## Features

- Explore different locations (Village, Forest, Cave, Mountain)
- Collect and use items
- Interact with NPCs
- Random events and encounters
- Save and load game progress
- Weather system
- Configurable game settings

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Run the game:
   ```
   python main.py
   ```

### Command Line Arguments

- `--name`: Set the player name (default: Kevin)

Example:
```
python main.py --name Alice
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

The game is structured using an object-oriented approach:

- `game/`: Core game mechanics
  - `actions.py`: Game actions (move, look, etc.)
  - `base.py`: Base classes for game objects
  - `config.py`: Game configuration
  - `game.py`: Main game class
  - `items.py`: Item definitions
  - `mythical.py`: Mythical creatures and objects
  - `player.py`: Player class and functions
  - `state.py`: Game state management
  - `weather.py`: Weather system
  - `world.py`: World class and functions
- `locations/`: Location-specific code
  - `cave.py`: Cave location
  - `forest.py`: Forest location
  - `mountain.py`: Mountain location
  - `village.py`: Village location
- `utils/`: Utility functions
  - `random_events.py`: Random event generation
  - `save_load.py`: Save and load game functions
  - `text_formatting.py`: Text formatting utilities
- `main.py`: Entry point for the game

## Customization

You can customize the game by editing the `config.json` file. If the file doesn't exist, the game will create one with default values.

Example configuration:
```json
{
  "default_player_name": "Kevin",
  "max_health": 100,
  "starting_gold": 100,
  "starting_location": "Village",
  "save_directory": "saves",
  "random_event_chance": 0.2,
  "debug_mode": false
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors who have helped with the development of this game.
- Special thanks to Kevin for the inspiration!

