# 🎮 Kevin's Adventure Game

A text-based adventure game where players explore different locations, collect items, battle mythical creatures, and experience dynamic weather and random events.

## 🌟 Features

- **Multiple Locations**: Explore the village, forest, mountain, and mysterious caves
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Item Collection**: Discover and collect various items throughout your journey
- **Mythical Creatures**: Encounter and battle legendary beings
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected events that add excitement to your journey
- **Player Status Tracking**: Monitor your health, inventory, and progress

## 🚀 Getting Started

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

1. **Starting the Game**: Run `python main.py` to begin your adventure
2. **Loading Saves**: Choose to load a previous save file when prompted
3. **Navigation**: Use location commands to move between areas
4. **Commands**: Type `help` at any time to see available commands
5. **Saving**: Save your progress at any point during the game

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Game action handlers
│   ├── items.py           # Item system and inventory management
│   ├── mythical.py        # Mythical creatures and battles
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific content
│   ├── forest.py          # Forest area implementation
│   ├── mountain.py        # Mountain area implementation
│   └── village.py         # Village area implementation
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Save/load game functionality
    └── text_formatting.py # Text display and formatting
```

## 🎮 Game Mechanics

- **Health System**: Monitor your character's health throughout the adventure
- **Inventory Management**: Collect and manage items you find during exploration
- **Location-Based Gameplay**: Each location offers unique experiences and challenges
- **Weather Effects**: Dynamic weather that influences your adventure
- **Save System**: Persistent game saves allow you to continue your journey

## 🤝 Contributing

This is a test repository for demonstrating text-based game development. Feel free to explore the code and suggest improvements!

## 📝 License

This project is for educational and testing purposes.

---

*Last updated: June 2025*

