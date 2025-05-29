# 🌈 Kevin's Adventure Game

A text-based adventure game where players explore different locations, interact with mythical creatures, manage inventory, and experience dynamic weather systems.

## 🎮 Game Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and mysterious Caves
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Mythical Creatures**: Encounter and summon magical beings to aid your journey
- **Inventory Management**: Collect items, manage gold, and track your possessions
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and events
- **Health System**: Monitor your health and heal when needed

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Ensure you have Python 3.6+ installed:
   ```bash
   python --version
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 🎯 How to Play

1. **Starting the Game**: Run `python main.py` and choose whether to load a saved game or start fresh
2. **Navigation**: Use commands to move between locations and interact with the world
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Type `quit` to save your progress and exit the game

### Available Commands
- `help` - Display available commands
- `quit` - Save and exit the game
- `status` - Check your current health, inventory, and location
- `move [location]` - Travel to different locations
- `inventory` - View your current items and gold

## 🗺️ Game World

### Locations
- **Village** 🏘️ - The starting point with shops and friendly NPCs
- **Forest** 🌲 - A lush wilderness with hidden treasures and creatures
- **Mountain** ⛰️ - Challenging terrain with rare items and dangers
- **Cave** 🕳️ - Mysterious underground chambers with ancient secrets

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game logic
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item management system
│   ├── mythical.py        # Mythical creature interactions
│   ├── player.py          # Player state and management
│   ├── state.py           # Game state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific modules
│   ├── cave.py           # Cave exploration logic
│   ├── forest.py         # Forest area interactions
│   ├── mountain.py       # Mountain climbing mechanics
│   └── village.py        # Village activities and NPCs
├── utils/                 # Utility functions
│   ├── random_events.py  # Random event generation
│   ├── save_load.py      # Game save/load functionality
│   └── text_formatting.py # Text display and formatting
└── README.md             # This file
```

## 🎲 Game Mechanics

- **Health System**: Start with 100 health points, manage through healing items and rest
- **Inventory**: Collect items, manage gold, and use tools to progress
- **Weather Effects**: Different weather conditions affect gameplay and events
- **Random Events**: Encounter unexpected situations that can help or hinder progress
- **Save System**: Automatic saving when quitting, with multiple save slot support

## 🛠️ Development

This project is built with Python and uses a modular architecture for easy expansion and maintenance.

### Adding New Features
- **New Locations**: Add modules to the `locations/` directory
- **New Items**: Extend the `game/items.py` module
- **New Events**: Add to `utils/random_events.py`
- **New Creatures**: Expand `game/mythical.py`

## 📝 Requirements

- Python 3.6 or higher
- No external dependencies required - uses only Python standard library

## 🤝 Contributing

This is a test repository for development and experimentation. Feel free to explore the code and suggest improvements!

## 📄 License

This project is for educational and testing purposes.

---

**Last Updated**: May 29, 2025  
**Version**: 1.0  
**Platform**: Cross-platform (Python)

