# 🎮 Kevin's Adventure Game

A text-based adventure game where players explore different locations, collect items, battle creatures, and experience random events in an immersive fantasy world.

## 🌟 Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and more
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect and manage items throughout your adventure
- **Mythical Creatures**: Encounter and summon magical beings to aid your journey
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and discoveries
- **Health & Gold System**: Manage your character's health and wealth
- **Interactive Combat**: Battle creatures and make strategic decisions

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

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
2. **Navigation**: Use commands to move between locations and interact with the environment
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Save your progress at any point to continue later

### Available Locations
- **Village**: The starting point with shops and villagers
- **Forest**: A lush wilderness with hidden treasures and creatures
- **Mountain**: Challenging terrain with unique encounters

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── game/                   # Core game logic
│   ├── actions.py         # Player actions and interactions
│   ├── items.py           # Item management system
│   ├── mythical.py        # Mythical creature encounters
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific modules
│   ├── forest.py          # Forest location logic
│   ├── mountain.py        # Mountain location logic
│   └── village.py         # Village location logic
├── utils/                 # Utility functions
│   ├── random_events.py   # Random event generation
│   ├── save_load.py       # Save/load game functionality
│   └── text_formatting.py # Text display utilities
├── main.py               # Main game entry point
└── README.md             # This file
```

## 🎮 Game Mechanics

### Player Stats
- **Health**: Your character's life force (starts at 100)
- **Gold**: Currency for purchasing items and services (starts at 100)
- **Inventory**: Items collected during your adventure
- **Location**: Current position in the game world

### Weather System
The game features a dynamic weather system with conditions including:
- Clear, Cloudy, Rainy, Stormy, Foggy, Windy

Weather affects gameplay and can influence random events and encounters.

## 💾 Save System

The game automatically creates a `saves/` directory where your progress is stored. You can:
- Save your game at any point
- Load previous saves when starting the game
- Manage multiple save files

## 🤝 Contributing

This is a test repository for demonstrating text-based game development. Feel free to explore the code and suggest improvements!

## 📝 License

This project is for educational and testing purposes.

---

**Last Updated**: May 29, 2025  
**Environment**: Linux x86_64 GNU/Linux  
**Python Version**: 3.6+

