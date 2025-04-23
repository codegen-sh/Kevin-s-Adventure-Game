🌈🌈
# Kevin's Adventure Game

This is a text-based adventure game where you navigate through different locations, interact with items, and experience random events.

Last updated: April 23, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Features

- Explore multiple locations including forests, mountains, and villages
- Interact with various items and mythical creatures
- Experience dynamic weather changes
- Save and load game progress
- Random events that affect gameplay

## Project Structure

```
.
├── game/               # Core game mechanics
│   ├── items.py        # Item definitions and interactions
│   ├── mythical.py     # Mythical creatures and encounters
│   ├── player.py       # Player character management
│   ├── state.py        # Game state tracking
│   ├── weather.py      # Weather system
│   └── world.py        # World map and navigation
├── locations/          # Game locations
│   ├── forest.py       # Forest location and events
│   ├── mountain.py     # Mountain location and events
│   └── village.py      # Village location and events
├── utils/              # Utility functions
│   ├── random_events.py    # Random event generation
│   ├── save_load.py        # Game saving/loading functionality
│   └── text_formatting.py  # Text display utilities
└── main.py             # Main game entry point
```

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

## Gameplay

1. When you start the game, you'll be asked if you want to load a saved game or start a new one.
2. Navigate through the world by typing commands like "go north", "go south", etc.
3. Interact with items using commands like "take sword", "use potion", etc.
4. Type 'help' at any time to see available commands.
5. Type 'quit' to save your progress and exit the game.

## Available Commands

- `go [direction]` - Move in a direction (north, south, east, west)
- `look` - Examine your surroundings
- `take [item]` - Pick up an item
- `use [item]` - Use an item in your inventory
- `inventory` - Check your inventory
- `status` - Check your player status
- `help` - Display available commands
- `quit` - Save and exit the game

## Contributing

This is a test repository. Feel free to fork and experiment with the code!

## License

This project is open source and available for educational purposes.
