🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: May 18, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

Kevin's Adventure Game is a text-based RPG where you play as Kevin, exploring a world with various locations including:
- Villages
- Forests
- Mountains

The game features:
- Dynamic weather system
- Inventory management
- Character progression
- Mythical creatures
- Random events
- Save/load functionality

## Project Structure

```
.
├── game/               # Core game mechanics
│   ├── items.py        # Item definitions and interactions
│   ├── mythical.py     # Mythical creatures and encounters
│   ├── player.py       # Player character functionality
│   ├── state.py        # Game state management
│   ├── weather.py      # Weather system
│   └── world.py        # World map and location management
├── locations/          # Location-specific content
│   ├── forest.py       # Forest location events and items
│   ├── mountain.py     # Mountain location events and items
│   └── village.py      # Village location events and items
├── utils/              # Utility functions
│   ├── random_events.py    # Random event generation
│   ├── save_load.py        # Game saving and loading
│   └── text_formatting.py  # Text display formatting
└── main.py             # Main game loop and entry point
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
4. Encounter mythical creatures and decide how to interact with them
5. Experience random events based on your location and the weather
6. Save your progress at any time by typing "quit"

## Commands

- `help` - Display available commands
- `go [direction]` - Move in a direction (north, south, east, west)
- `look` - Examine your surroundings
- `inventory` - Check your inventory
- `take [item]` - Pick up an item
- `drop [item]` - Drop an item
- `use [item]` - Use an item
- `talk to [character]` - Interact with a character
- `quit` - Save and exit the game

## Development

This is a test repository for demonstrating game development concepts. Feel free to fork and extend with your own features!

## Known Issues

- The actions.py file is referenced in main.py but is currently missing
- Some weather effects may not be properly implemented yet
- Mountain location has limited interaction options

## License

This project is open source and available for educational purposes.

