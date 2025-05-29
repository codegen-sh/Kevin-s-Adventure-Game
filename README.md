# 🎮 Kevin's Adventure Game

A text-based adventure game featuring exploration, combat, and mythical creatures in a dynamic world.

## 🌟 Features

- **Dynamic World**: Explore multiple locations including villages, forests, and mountains
- **Weather System**: Experience changing weather conditions that affect gameplay
- **Mythical Creatures**: Encounter and interact with various mythical beings
- **Inventory Management**: Collect and manage items throughout your adventure
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and events
- **Player Progression**: Develop your character as you explore

## 🗺️ Game Locations

- **Village**: A safe haven with shops and friendly NPCs
- **Forest**: A mysterious woodland filled with creatures and hidden treasures
- **Mountain**: Treacherous peaks with challenging encounters

## 🚀 Installation & Setup

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

1. **Starting the Game**: Run `python main.py` to begin your adventure
2. **Loading Saves**: Choose to load a previous save file when prompted
3. **Commands**: Type `help` at any time to see available commands
4. **Navigation**: Move between locations using directional commands
5. **Interaction**: Interact with NPCs, items, and the environment
6. **Saving**: Save your progress at any time to continue later

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player actions and interactions
│   ├── items.py           # Item definitions and management
│   ├── mythical.py        # Mythical creatures and encounters
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific content
│   ├── forest.py          # Forest area implementation
│   ├── mountain.py        # Mountain area implementation
│   └── village.py         # Village area implementation
└── utils/                 # Utility functions
    ├── random_events.py   # Random event system
    ├── save_load.py       # Save/load functionality
    └── text_formatting.py # Text display utilities
```

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies required

## 🎲 Game Features

### Weather System
Experience dynamic weather that affects your adventure:
- Sunny, rainy, cloudy, and stormy conditions
- Weather impacts visibility and encounters

### Mythical Creatures
Encounter various mythical beings throughout your journey:
- Each creature has unique behaviors and interactions
- Some are friendly, others may be hostile

### Item System
Discover and collect various items:
- Weapons and tools
- Consumables and treasures
- Quest items and collectibles

## 🔧 Development

This project serves as a test repository for text-based adventure game mechanics and is built with modularity in mind for easy expansion and modification.

## 📝 License

This project is a test repository for educational and development purposes.

---

**Last Updated**: May 29, 2025  
**Repository**: [codegen-sh/Kevin-s-Adventure-Game](https://github.com/codegen-sh/Kevin-s-Adventure-Game)

