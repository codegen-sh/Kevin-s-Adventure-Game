🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: May 12, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Features

- Explore multiple locations including forests, mountains, and villages
- Interact with various items and mythical creatures
- Experience dynamic weather conditions
- Save and load game progress
- Random events that affect gameplay

## Project Structure

```
.
├── game/           # Core game mechanics
│   ├── items.py    # Item definitions and interactions
│   ├── mythical.py # Mythical creatures and encounters
│   ├── player.py   # Player character management
│   ├── state.py    # Game state tracking
│   ├── weather.py  # Weather system
│   └── world.py    # World initialization and management
├── locations/      # Game world locations
│   ├── forest.py   # Forest location and events
│   ├── mountain.py # Mountain location and events
│   └── village.py  # Village location and events
├── utils/          # Utility functions
│   ├── random_events.py  # Random event generation
│   ├── save_load.py      # Game saving/loading functionality
│   └── text_formatting.py # Text display utilities
└── main.py         # Main game entry point
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

1. Start a new game or load a saved game
2. Navigate through different locations using commands like "go north", "go south", etc.
3. Interact with items using commands like "take sword", "use potion", etc.
4. Type 'help' at any time to see available commands
5. Type 'quit' to save your progress and exit the game

## Available Commands

- `help` - Display available commands
- `go [direction]` - Move in a direction (north, south, east, west)
- `look` - Examine your surroundings
- `take [item]` - Pick up an item
- `drop [item]` - Drop an item from your inventory
- `use [item]` - Use an item from your inventory
- `inventory` - Check your inventory
- `status` - Check your player status
- `save` - Save your current game
- `quit` - Save and exit the game

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

