# 🎮 Kevin's Adventure Game

A text-based adventure game where players explore different locations, collect items, battle creatures, and experience dynamic weather and random events.

## 🌟 Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and mysterious Cave
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect and manage items throughout your adventure
- **Mythical Creatures**: Encounter and summon magical beings to aid your journey
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and events
- **Health & Gold System**: Manage your character's health and collect gold
- **Interactive Combat**: Battle creatures and make strategic decisions

## 🎯 Game Locations

- **🏘️ Village**: The starting point with shops, NPCs, and safe haven
- **🌲 Forest**: A lush wilderness filled with creatures and hidden treasures
- **⛰️ Mountain**: Challenging terrain with unique encounters and rewards
- **🕳️ Cave**: Mysterious underground location with ancient secrets

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required (uses only Python standard library)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. **Run the game:**
   ```bash
   python main.py
   ```

## 🎮 How to Play

### Basic Commands
- **Movement**: Use location names to travel (e.g., "forest", "village", "mountain", "cave")
- **Actions**: Type actions like "explore", "rest", "shop", "inventory"
- **Help**: Type `help` at any time to see available commands
- **Save & Quit**: Type `quit` to save your progress and exit

### Game Mechanics
- **Health**: Monitor your health and rest when needed
- **Inventory**: Collect items and manage your belongings
- **Gold**: Earn and spend gold on items and services
- **Weather**: Adapt to changing weather conditions
- **Random Events**: Stay alert for unexpected encounters

### Save System
- The game automatically saves when you quit
- Load previous saves when starting a new session
- Multiple save files supported

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item management system
│   ├── mythical.py        # Mythical creature interactions
│   ├── player.py          # Player state and actions
│   ├── state.py           # Game state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World state and locations
├── locations/             # Location-specific content
│   ├── cave.py           # Cave exploration
│   ├── forest.py         # Forest adventures
│   ├── mountain.py       # Mountain climbing
│   └── village.py        # Village interactions
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Save/load functionality
    └── text_formatting.py # Text display utilities
```

## 🎨 Game Features in Detail

### 🌤️ Weather System
The game features a dynamic weather system that affects gameplay:
- Clear, cloudy, rainy, stormy, foggy, and windy conditions
- Weather impacts certain actions and events
- Adds immersion and strategic depth

### 🎲 Random Events
Experience unexpected encounters:
- Treasure discoveries
- Creature encounters
- Environmental challenges
- Beneficial or challenging situations

### 🧙‍♂️ Mythical Creatures
Summon and interact with magical beings:
- Various creature types with unique abilities
- Strategic summoning system
- Creatures can aid in your adventures

## 🤝 Contributing

This is a test repository for learning and experimentation. Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Fork and create your own adventures

## 📝 Development Notes

- **Language**: Python 3.6+
- **Dependencies**: None (uses Python standard library only)
- **Architecture**: Modular design with separate concerns
- **Save Format**: JSON-based save files

## 🎯 Future Enhancements

Potential areas for expansion:
- Additional locations and quests
- More complex combat system
- Character progression and skills
- Multiplayer functionality
- GUI interface
- Sound effects and music

## 📄 License

This project is open source and available for educational purposes.

---

**Last Updated**: May 29, 2025  
**Version**: 1.0  
**Platform**: Cross-platform (Python)

Happy adventuring! 🗺️✨

