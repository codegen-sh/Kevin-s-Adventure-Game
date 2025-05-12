🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: May 12, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Features

- Explore multiple locations including forests, mountains, and villages
- Interact with various items and mythical creatures
- Experience dynamic weather conditions that affect gameplay
- Save and load game progress
- Random events that create unique gameplay experiences

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

## How to Play

1. When you start the game, you'll be asked if you want to load a saved game or start a new one.
2. Navigate through the world by typing commands like "go north", "examine item", etc.
3. Type 'help' at any time to see available commands.
4. Your progress is automatically saved when you quit the game.

## Commands

- `go [direction]` - Move in a direction (north, south, east, west)
- `examine [item]` - Look at an item more closely
- `take [item]` - Pick up an item
- `use [item]` - Use an item in your inventory
- `inventory` - Check what items you're carrying
- `status` - Check your player status
- `help` - Display available commands
- `quit` - Save and exit the game

## Contributing

This is a test repository. Feel free to fork and experiment with the code!

## License

This project is open source and available for educational purposes.

