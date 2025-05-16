🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events.

Last updated: May 16, 2025

## Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players can:
- Explore different locations (village, forest, mountain)
- Collect and use items
- Encounter mythical creatures
- Experience dynamic weather conditions
- Save and load game progress

## Project Structure

```
Kevin-s-Adventure-Game/
├── game/                  # Core game mechanics
│   ├── items.py           # Item definitions and interactions
│   ├── mythical.py        # Mythical creatures
│   ├── player.py          # Player state and actions
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Game locations
│   ├── forest.py          # Forest location and events
│   ├── mountain.py        # Mountain location and events
│   └── village.py         # Village location and events
├── utils/                 # Utility functions
│   ├── random_events.py   # Random event generation
│   ├── save_load.py       # Save/load game functionality
│   └── text_formatting.py # Text display utilities
└── main.py                # Main game entry point
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

### Basic Commands
- `look` - Examine your surroundings
- `go [direction]` - Move in a direction (north, south, east, west)
- `take [item]` - Pick up an item
- `use [item]` - Use an item in your inventory
- `inventory` - Check your inventory
- `status` - Check your player status
- `save [filename]` - Save your game
- `load [filename]` - Load a saved game
- `help` - Display available commands
- `quit` - Exit the game

### Game Features
- **Dynamic Weather**: Weather conditions change and affect gameplay
- **Random Events**: Unexpected events occur during your adventure
- **Inventory System**: Collect and manage items
- **Save/Load**: Save your progress and continue later

## Development

### Adding New Features
- New locations can be added in the `locations/` directory
- New items can be defined in `game/items.py`
- New mythical creatures can be added to `game/mythical.py`

### Testing
Run the game and test new features by exploring different game paths and interactions.

## License

This project is for demonstration purposes only.

## Credits

Created as a test repository for Codegen.

