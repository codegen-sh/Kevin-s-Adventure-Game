# 🌟 Kevin's Adventure Game

A text-based adventure game where players explore a fantasy world filled with mystical creatures, treasures, and exciting challenges!

## 🎮 Game Overview

Kevin's Adventure Game is an interactive text-based RPG where you play as an adventurer exploring different locations, collecting items, battling creatures, and uncovering secrets. The game features:

- **Multiple Locations**: Explore the Village, Forest, Mountain, and mysterious Cave
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect and use various items including weapons, potions, and magical artifacts
- **Mythical Creatures**: Encounter and interact with magical beings
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and discoveries

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation & Running

1. **Clone the repository:**
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. **Run the game:**
   ```bash
   python main.py
   ```

3. **Follow the on-screen prompts** to create your character and begin your adventure!

## 🎯 How to Play

### Basic Commands
- Type `help` at any time to see available commands
- Use numbered options to make choices
- Navigate between locations using the travel system
- Manage your inventory and use items strategically

### Game Features

#### 🗺️ Locations
- **Village**: The starting point with shops, NPCs, and rumors of treasure
- **Forest**: A lush wilderness with hidden paths and wildlife
- **Mountain**: Treacherous peaks with caves and valuable resources
- **Cave**: Dark underground chambers requiring torches to explore

#### 🎒 Items & Inventory
- **Weapons**: Swords, bows, and magical weapons for combat
- **Potions**: Health potions, magic potions, and special elixirs
- **Tools**: Torches for cave exploration, maps, and utility items
- **Treasures**: Gold, gems, and rare artifacts

#### 🌤️ Weather System
The game features dynamic weather that affects your adventure:
- Clear, cloudy, rainy, stormy, foggy, and windy conditions
- Weather impacts visibility and available actions

#### 💾 Save System
- Save your game progress at any time
- Load previous saves to continue your adventure
- Multiple save slots available

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item system and interactions
│   ├── mythical.py        # Mythical creature encounters
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific content
│   ├── village.py         # Village interactions
│   ├── forest.py          # Forest exploration
│   └── mountain.py        # Mountain adventures
├── utils/                 # Utility functions
│   ├── random_events.py   # Random event generation
│   ├── save_load.py       # Save/load functionality
│   └── text_formatting.py # Text display utilities
└── README.md              # This file
```

## 🎲 Game Mechanics

### Character Stats
- **Health**: Your life points (starts at 100)
- **Gold**: Currency for purchasing items
- **Inventory**: Items you've collected
- **Location**: Your current position in the world

### Combat & Encounters
- Face various creatures and challenges
- Use weapons and magic to overcome obstacles
- Strategic item usage can turn the tide of battle

### Exploration
- Discover hidden paths and secret areas
- Random events add unpredictability to your journey
- Environmental interactions based on current weather

## 🛠️ Development

This project is structured with modular Python files for easy maintenance and expansion. Key components:

- **Modular Design**: Separate files for different game systems
- **Event-Driven**: Random events and player choices drive the narrative
- **Extensible**: Easy to add new locations, items, and features

## 🤝 Contributing

This is a test repository for development and experimentation. Feel free to explore the code and suggest improvements!

## 📝 Notes

- The game includes references to a Cave location that may need additional implementation
- Weather system affects gameplay dynamics
- Save files are stored in a local `saves/` directory

---

**Last Updated**: May 29, 2025  
**Repository**: [codegen-sh/Kevin-s-Adventure-Game](https://github.com/codegen-sh/Kevin-s-Adventure-Game)

Enjoy your adventure! 🗡️✨

