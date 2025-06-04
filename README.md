# 🌈 Kevin's Adventure Game

A text-based adventure game where you explore a mystical world filled with forests, mountains, villages, and caves. Collect items, encounter mythical creatures, and experience dynamic weather as you embark on your journey!

## 🎮 Features

- **Multiple Locations**: Explore diverse environments including forests, mountains, villages, and caves
- **Dynamic Weather System**: Experience changing weather conditions that affect your adventure
- **Inventory Management**: Collect, use, and manage various items throughout your journey
- **Mythical Creatures**: Encounter and interact with magical beings
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and events
- **Interactive Gameplay**: Make choices that affect your adventure

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

1. **Starting the Game**: Run `python main.py` to begin your adventure
2. **Loading Saves**: Choose to load a previous save file when prompted
3. **Navigation**: Use commands to move between locations and interact with the world
4. **Inventory**: Manage your items and use them strategically
5. **Saving**: Save your progress at any time to continue later

### Available Commands

- `move [location]` - Move to a new location
- `look` - Examine your surroundings
- `inventory` - Check your inventory
- `pickup [item]` - Pick up an item
- `drop [item]` - Drop an item from your inventory
- `use [item]` - Use an item from your inventory
- `save` - Save your current game progress
- `help` - Display available commands
- `quit` - Exit the game

## 🗺️ Game World

The adventure takes place across several interconnected locations:

- **🌲 Forest**: A mysterious woodland with hidden treasures and creatures
- **🏔️ Mountain**: Treacherous peaks with challenging terrain and rare items
- **🏘️ Village**: A peaceful settlement where you can interact with NPCs
- **🕳️ Cave**: Dark underground passages filled with secrets

## 🎲 Game Mechanics

- **Health System**: Monitor your health and heal when necessary
- **Weather Effects**: Adapt to changing weather conditions
- **Random Events**: Encounter unexpected situations that can help or hinder your progress
- **Item System**: Discover and utilize various items with different properties
- **Character Progression**: Develop your character through exploration and interaction

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── items.py           # Item definitions and management
│   ├── mythical.py        # Mythical creature encounters
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific modules
│   ├── forest.py          # Forest location logic
│   ├── mountain.py        # Mountain location logic
│   └── village.py         # Village location logic
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Save/load functionality
    └── text_formatting.py # Text display utilities
```

## 💾 Save System

The game features an automatic save system that allows you to:
- Save your progress at any time
- Load from multiple save files
- Continue your adventure from where you left off

Save files are stored locally and contain your character's progress, inventory, and current location.

## 🤝 Contributing

This is a test repository for TinySitter! Feel free to explore the code and suggest improvements.

## 📝 License

This project is a test repository and is available for educational purposes.

---

**Last updated**: June 4, 2025  
**Repository**: [codegen-sh/Kevin-s-Adventure-Game](https://github.com/codegen-sh/Kevin-s-Adventure-Game)

