# 🎮 Kevin's Adventure Game

A rich, text-based adventure game featuring exploration, combat, inventory management, and dynamic weather systems.

## 🌟 Features

- **🗺️ Multiple Locations**: Explore diverse environments including forests, villages, mountains, and mysterious caves
- **⚔️ Combat System**: Engage with various creatures and mythical beings
- **🎒 Inventory Management**: Collect, use, and manage items throughout your journey
- **🌤️ Dynamic Weather**: Experience changing weather conditions that affect gameplay
- **💾 Save/Load System**: Save your progress and continue your adventure later
- **🎲 Random Events**: Encounter unexpected events that add excitement to your journey
- **🐉 Mythical Creatures**: Summon and interact with legendary beings

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

1. **Starting the Game**: Run `python main.py` and choose to start a new game or load a saved one
2. **Navigation**: Use commands to move between locations and interact with the environment
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Save your progress at any point to continue later

### Available Locations
- 🌲 **Forest**: Hunt for resources and encounter wildlife
- 🏘️ **Village**: Trade with merchants and interact with NPCs
- ⛰️ **Mountain**: Face challenging terrain and discover hidden treasures
- 🕳️ **Cave**: Explore dark depths and uncover secrets

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item definitions and management
│   ├── mythical.py        # Mythical creature system
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
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

## 🎮 Game Mechanics

### Player System
- Health and status tracking
- Inventory management with various item types
- Character progression through adventures

### Combat & Interaction
- Turn-based encounters with creatures
- Strategic item usage during combat
- Peaceful interaction options with NPCs

### Weather System
- Dynamic weather changes affecting gameplay
- Weather-dependent events and encounters
- Seasonal variations in different locations

### Save System
- Multiple save slots available
- Automatic progress tracking
- Resume adventures from any saved point

## 🤝 Contributing

This is a test repository for demonstrating text-based game development concepts. Feel free to explore the code and suggest improvements!

## 📝 License

This project is for educational and testing purposes.

---

**Last Updated**: May 30, 2025  
**Version**: 2.0  
**Platform**: Cross-platform (Python 3.6+)

