🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world, collect items, and embark on quests.

Last updated: May 18, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

In Kevin's Adventure Game, you play as Kevin, an adventurer exploring a world filled with:
- Multiple locations (Village, Forest, Mountain)
- Items to collect and use
- Health and inventory management
- Gold currency system
- Random events and weather effects
- Save/load game functionality

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
- `move [location]`: Travel to a different location
- `look`: Examine your surroundings
- `inventory`: Check your current items
- `pickup [item]`: Add an item to your inventory
- `drop [item]`: Remove an item from your inventory
- `use [item]`: Use an item from your inventory
- `examine [item]`: Get details about an item
- `status`: Check your health, gold, and inventory
- `interact`: Interact with your current location
- `help`: Display available commands
- `quit`: Save and exit the game

### Game World
The game features several locations to explore:
- **Village**: The starting point with shops and NPCs
- **Forest**: Find rare items and encounter mythical creatures
- **Mountain**: Dangerous terrain with valuable treasures

### Game Features
- **Health System**: Manage your health points (max 100)
- **Inventory Management**: Collect and use various items
- **Gold Economy**: Earn and spend gold coins
- **Save/Load System**: Continue your adventure later

## Project Structure
```
.
├── game/               # Core game mechanics
│   ├── items.py        # Item definitions and functions
│   ├── mythical.py     # Mythical creatures and events
│   ├── player.py       # Player stats and actions
│   ├── state.py        # Game state management
│   ├── weather.py      # Weather system
│   └── world.py        # World map and locations
├── locations/          # Location-specific content
│   ├── forest.py       # Forest location
│   ├── mountain.py     # Mountain location
│   └── village.py      # Village location
├── utils/              # Utility functions
│   ├── random_events.py    # Random event generation
│   ├── save_load.py        # Save/load game functionality
│   └── text_formatting.py  # Text display formatting
└── main.py             # Main game loop
```

## Contributing
This is a test repository for TinySitter. Feel free to fork and experiment with the code!

## License
This project is open source and available for educational purposes.

