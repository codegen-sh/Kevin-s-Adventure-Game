# 🎮 Kevin's Adventure Game

A text-based adventure game where players explore different locations, collect items, battle creatures, and experience random events in an immersive fantasy world.

## 🌟 Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and mysterious Cave
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect and manage items throughout your adventure
- **Mythical Creatures**: Encounter and summon magical beings to aid your journey
- **Random Events**: Experience unpredictable events that keep the game exciting
- **Save/Load System**: Save your progress and continue your adventure later
- **Health & Gold System**: Manage your character's health and collect gold
- **Interactive Combat**: Battle creatures and make strategic decisions

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required (uses only Python standard library)

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

1. **Starting the Game**: When you run the game, you'll be prompted to either load a saved game or start fresh
2. **Navigation**: Use commands to move between locations and interact with the world
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Type `quit` to save your progress and exit the game

### Available Commands

- `help` - Display available commands
- `quit` - Save and exit the game
- `go [location]` - Move to a different location
- `inventory` - Check your current items
- `status` - View your character's health and gold
- Location-specific commands vary by area

## 🗺️ Game World

### Locations

- **🏘️ Village**: The starting point with shops and friendly NPCs
- **🌲 Forest**: A lush woodland filled with creatures and hidden treasures
- **⛰️ Mountain**: Challenging terrain with rare items and dangerous encounters
- **🕳️ Cave**: A mysterious underground location with ancient secrets

### Game Mechanics

- **Health System**: Monitor your health and heal when necessary
- **Gold Economy**: Earn and spend gold on items and services
- **Weather Effects**: Dynamic weather that influences gameplay
- **Random Events**: Unexpected encounters that can help or hinder your progress

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item management system
│   ├── mythical.py        # Mythical creature interactions
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific modules
│   ├── cave.py           # Cave exploration
│   ├── forest.py         # Forest adventures
│   ├── mountain.py       # Mountain climbing
│   └── village.py        # Village interactions
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Save/load game functionality
    └── text_formatting.py # Text display utilities
```

## 🎮 Gameplay Tips

- Explore all locations to discover unique items and events
- Manage your health carefully - some areas are more dangerous than others
- Save frequently to preserve your progress
- Experiment with different commands in each location
- Pay attention to weather changes as they may affect available actions

## 🔧 Development

This game is built using pure Python with a modular architecture that makes it easy to:
- Add new locations
- Implement new items and creatures
- Extend the random event system
- Modify game mechanics

## 📝 Contributing

Feel free to contribute to Kevin's Adventure Game by:
- Adding new locations or events
- Improving the user interface
- Fixing bugs or enhancing existing features
- Expanding the item and creature systems

## 📄 License

This project is open source and available under the MIT License.

---

**Last Updated**: May 29, 2025  
**Version**: 1.0  
**Platform**: Cross-platform (Python 3.6+)

Enjoy your adventure! 🗡️✨

