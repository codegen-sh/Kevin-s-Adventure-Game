# 🎮 Kevin's Adventure Game

A text-based adventure game where players explore a mystical world filled with locations, items, weather systems, and mythical creatures.

## 🌟 Features

- **🗺️ Multiple Locations**: Explore the Village, Forest, and Mountain regions
- **🎒 Inventory System**: Collect and manage items throughout your journey
- **💰 Gold Economy**: Earn and spend gold on your adventures
- **🌤️ Dynamic Weather**: Experience changing weather conditions that affect gameplay
- **🐉 Mythical Creatures**: Encounter magical beings in your travels
- **💾 Save/Load System**: Save your progress and continue your adventure later
- **🎲 Random Events**: Experience unexpected encounters and events
- **❤️ Health System**: Manage your character's health throughout the game

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required (uses only Python standard library)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. **Run the game:**
   ```bash
   python main.py
   ```

## 🎯 How to Play

1. **Starting the Game**: When you run the game, you'll be prompted to either load a saved game or start fresh
2. **Navigation**: Use text commands to move between locations and interact with the world
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Save your progress at any point to continue later

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── items.py           # Item system and definitions
│   ├── mythical.py        # Mythical creatures and encounters
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific content
│   ├── forest.py          # Forest area content
│   ├── mountain.py        # Mountain area content
│   └── village.py         # Village area content
├── utils/                 # Utility functions
│   ├── random_events.py   # Random event system
│   ├── save_load.py       # Save/load functionality
│   └── text_formatting.py # Text display utilities
└── README.md              # This file
```

## 🎮 Game Mechanics

### Character System
- **Health**: Monitor your character's wellbeing
- **Inventory**: Collect and use various items
- **Gold**: Currency for trading and purchases
- **Location**: Track your current position in the world

### World Exploration
- **Village**: The starting hub with shops and NPCs
- **Forest**: A mysterious woodland with hidden treasures
- **Mountain**: Challenging terrain with unique encounters

### Weather Effects
The game features a dynamic weather system that can affect:
- Visibility and exploration
- Random event probability
- Character interactions

## 🛠️ Development

This is a modular Python project designed for easy extension:

- **Adding Locations**: Create new location files in the `locations/` directory
- **New Items**: Extend the item system in `game/items.py`
- **Custom Events**: Add random events in `utils/random_events.py`
- **Mythical Creatures**: Expand creature encounters in `game/mythical.py`

## 📝 Contributing

Feel free to contribute to Kevin's Adventure Game by:
1. Forking the repository
2. Creating a feature branch
3. Making your changes
4. Submitting a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🎯 Future Enhancements

- Combat system
- Character progression/leveling
- More diverse locations
- Multiplayer support
- GUI interface option

---

**Last Updated**: May 28, 2025  
**Version**: 1.0  
**Platform**: Cross-platform (Python 3.6+)

🌈 Happy adventuring! 🌈

