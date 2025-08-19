# Kevin's Adventure Game

A text-based adventure game where you explore a world of mystery and danger as you navigate through forests, caves, villages, and mountains.

## Features

- Explore different locations in a fantasy world
- Collect and use items
- Interact with the environment
- Save and load game progress
- Random events and encounters

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Install the game:
   ```
   pip install -e .
   ```

## How to Play

Run the game:
```
python main.py
```

Or if you installed the package:
```
kevins-adventure
```

### Commands

- `move [location]`: Move to a new location
- `look`: Examine your surroundings
- `inventory`: Check your inventory
- `pickup [item]` or `take [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message
- `quit`: Save and exit the game

## Game Structure

The game is organized into several modules:

- `game/`: Core game logic and state management
  - `actions.py`: Handles player actions
  - `engine.py`: Manages the game loop and state
  - `items.py`: Defines items and their effects
  - `player.py`: Manages player state
  - `world.py`: Manages the game world and locations
  - `mythical.py`: Handles mythical creatures and events
  - `state.py`: Manages game state

- `locations/`: Different locations in the game
  - `cave.py`: Cave location and events
  - `forest.py`: Forest location and events
  - `mountain.py`: Mountain location and events
  - `village.py`: Village location and events

- `utils/`: Utility functions
  - `random_events.py`: Generates random events
  - `save_load.py`: Handles saving and loading games
  - `text_formatting.py`: Formats text output

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

