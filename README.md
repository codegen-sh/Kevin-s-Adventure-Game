# 🌈 Kevin's Adventure Game

A text-based adventure game where players explore different locations, collect items, battle creatures, and experience dynamic weather and random events.

## 🎮 Game Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and Cave
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect and manage items throughout your adventure
- **Mythical Creatures**: Encounter and summon magical beings
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and discoveries
- **Health & Gold System**: Manage your character's health and resources

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Run the game:
   ```bash
   python main.py
   ```

## 🎯 How to Play

1. **Starting the Game**: When you launch the game, you'll be prompted to either load a saved game or start fresh
2. **Navigation**: Use commands to move between locations and interact with the world
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Type `quit` to save your progress and exit the game

### Available Locations

- **🏘️ Village**: The starting location with shops and NPCs
- **🌲 Forest**: A lush wilderness with hidden treasures and creatures
- **⛰️ Mountain**: Challenging terrain with unique encounters
- **🕳️ Cave**: Dark underground passages with mysterious secrets

### Game Mechanics

- **Health**: Monitor your character's health (starts at 100)
- **Gold**: Collect and spend gold on items and services (starts with 100 gold)
- **Inventory**: Collect items that can help you on your journey
- **Weather**: Dynamic weather affects your adventures
- **Random Events**: Unexpected encounters can help or challenge you

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game loop and entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item system and management
│   ├── mythical.py        # Mythical creature encounters
│   ├── player.py          # Player state and management
│   ├── state.py           # Game state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World state and location management
├── locations/             # Location-specific content
│   ├── forest.py          # Forest location logic
│   ├── mountain.py        # Mountain location logic
│   └── village.py         # Village location logic
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Save/load game functionality
    └── text_formatting.py # Text display and formatting
```

## 🎲 Game Commands

- `help` - Display available commands
- `quit` - Save and exit the game
- `status` - Check your current health and inventory
- `go [location]` - Move to a different location
- `look` - Examine your current surroundings
- `inventory` - View your items

## 💾 Save System

The game automatically creates save files in a `saves/` directory. You can:
- Load previous games when starting
- Multiple save slots supported
- Progress is automatically saved when quitting

## 🔧 Development

### Adding New Features

1. **New Locations**: Add location files in the `locations/` directory
2. **New Items**: Extend the item system in `game/items.py`
3. **New Events**: Add random events in `utils/random_events.py`
4. **New Creatures**: Expand mythical creatures in `game/mythical.py`

### Code Style
- Follow Python PEP 8 conventions
- Use descriptive function and variable names
- Add docstrings for new functions

## 📝 Recent Updates

- Enhanced README with comprehensive game information
- Improved documentation of game features and structure
- Added detailed installation and gameplay instructions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is a test repository for educational and development purposes.

---

**Last Updated**: June 2025  
**Python Version**: 3.6+  
**Platform**: Cross-platform (Linux, Windows, macOS)

Enjoy your adventure! 🗺️✨

