🌈🌈
# Kevin's Adventure Game

A comprehensive text-based adventure game featuring dynamic weather, mythical creatures, item management, and save/load functionality.

## Features

🎮 **Core Gameplay**
- Interactive text-based adventure with multiple locations
- Dynamic player stats and inventory management
- Save and load game functionality
- Help system with available commands

🌦️ **Dynamic Weather System**
- Real-time weather changes affecting gameplay
- Weather impacts on player actions and environment

🐉 **Mythical Creatures**
- Encounter various mythical beings during your adventure
- Unique interactions and challenges

🎒 **Item Management**
- Comprehensive inventory system
- Various items with different properties and uses
- Item interactions and combinations

🗺️ **World Exploration**
- Multiple interconnected locations
- Rich descriptions and environmental storytelling
- Location-based events and interactions

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Run the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Starting the Game**: Run `python main.py` to begin your adventure
2. **Loading Saves**: Choose to load a previous save file when prompted
3. **Commands**: Type 'help' at any time to see available commands
4. **Navigation**: Use directional commands to move between locations
5. **Inventory**: Manage your items and check your status
6. **Saving**: Save your progress at any time during the game

## Game Structure

```
Kevin-s-Adventure-Game/
├── main.py              # Main game entry point
├── game/                # Core game modules
│   ├── actions.py       # Game action handlers
│   ├── items.py         # Item definitions and management
│   ├── mythical.py      # Mythical creature encounters
│   ├── player.py        # Player character management
│   ├── state.py         # Game state management
│   ├── weather.py       # Dynamic weather system
│   └── world.py         # World and location definitions
├── locations/           # Location-specific content
├── utils/               # Utility modules
│   ├── random_events.py # Random event system
│   ├── save_load.py     # Save/load functionality
│   └── text_formatting.py # Text display utilities
└── README.md           # This file
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Contributing

This is a test repository for educational purposes. Feel free to explore the code and suggest improvements!

---

*Last updated: June 2025*
*Platform: Linux x86_64*

