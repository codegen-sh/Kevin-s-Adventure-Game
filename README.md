🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world, collect items, and embark on quests.

Last updated: April 30, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Overview

Kevin's Adventure Game is an interactive text-based adventure where players navigate through different locations, collect items, interact with characters, and uncover the secrets of a magical realm. The game features:

- Multiple locations to explore (Village, Forest, Mountain)
- Inventory management system
- Health and gold tracking
- Save/load game functionality
- Random events and encounters
- Weather system that affects gameplay

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

### Commands

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

### Locations

- **Village**: The starting point with shops and friendly NPCs
- **Forest**: A mysterious area with valuable resources and potential dangers
- **Mountain**: A challenging terrain with rare items and difficult encounters

### Game Mechanics

- **Health**: Starts at 100. If it reaches 0, the game ends
- **Inventory**: Collect and manage items throughout your journey
- **Gold**: Currency for purchasing items and services
- **Save/Load**: Save your progress and continue your adventure later

## Project Structure

```
Kevin-s-Adventure-Game/
├── game/               # Core game mechanics
│   ├── items.py        # Item definitions and interactions
│   ├── mythical.py     # Mythical creatures and events
│   ├── player.py       # Player state and actions
│   ├── state.py        # Game state management
│   ├── weather.py      # Weather system
│   └── world.py        # World structure and navigation
├── locations/          # Game locations
│   ├── forest.py       # Forest location logic
│   ├── mountain.py     # Mountain location logic
│   └── village.py      # Village location logic
├── utils/              # Utility functions
│   ├── random_events.py    # Random event generation
│   ├── save_load.py        # Save/load game functionality
│   └── text_formatting.py  # Text display utilities
└── main.py             # Main game loop and entry point
```

## Contributing

Contributions to Kevin's Adventure Game are welcome! Feel free to submit pull requests with new features, bug fixes, or improvements.

## License

This project is open source and available for educational purposes.

