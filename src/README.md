# Kevin's Adventure Game

A text-based adventure game where you explore a world of mystery and danger as you navigate through forests, caves, villages, and mountains. Collect items, interact with characters, and uncover the secrets of this magical realm.

## Features

- Explore different locations: Village, Forest, Cave, Mountain
- Collect and use items
- Interact with NPCs and mythical creatures
- Random events and encounters
- Weather system
- Save and load game progress

## Code Structure

The game has been refactored to use an object-oriented approach with the following structure:

```
kevin_adventure/
├── core/
│   ├── actions.py      # Game actions
│   ├── entity.py       # Base entity class
│   ├── game.py         # Main game loop
│   ├── player.py       # Player class
│   └── world.py        # World class
├── creatures/
│   └── mythical.py     # Mythical creatures
├── items/
│   └── item_manager.py # Item management
├── locations/
│   ├── cave.py         # Cave location
│   ├── forest.py       # Forest location
│   ├── location.py     # Base location class
│   ├── mountain.py     # Mountain location
│   └── village.py      # Village location
├── utils/
│   ├── random_events.py    # Random event generation
│   ├── save_load.py        # Save/load functionality
│   └── text_formatting.py  # Text formatting utilities
├── weather.py          # Weather system
└── __init__.py         # Package initialization
```

## How to Play

1. Run `python src/main.py` to start the game
2. Follow the on-screen instructions
3. Type `help` at any time to see available commands

## Commands

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

## Improvements from Original Code

1. **Object-Oriented Design**: Replaced dictionary-based data structures with proper classes
2. **Code Organization**: Better organized code with clear separation of concerns
3. **Type Hints**: Added type hints for better code readability and IDE support
4. **Error Handling**: Improved error handling throughout the codebase
5. **Documentation**: Added docstrings and comments to explain the code
6. **Missing Files**: Created previously missing files (actions.py, cave.py)
7. **Completed TODOs**: Implemented functionality that was previously marked as TODO
8. **Consistent Style**: Applied consistent coding style throughout the codebase

