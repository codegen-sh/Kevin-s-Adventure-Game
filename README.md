# 🌈 Kevin's Adventure Game

A text-based adventure game where players explore a fantasy world filled with mysterious locations, collect items, and embark on quests.

## 🎮 Game Overview

Kevin's Adventure Game is an interactive text-based RPG where you play as Kevin, exploring a world with multiple interconnected locations. Navigate through villages, forests, mountains, and caves while collecting items, completing quests, and managing your health and inventory.

## 🗺️ Game World

The game features several explorable locations:

- **🏘️ Village** - A peaceful starting location with shops, inns, and quest opportunities
- **🌲 Forest** - A mysterious woodland filled with wildlife and hidden treasures
- **⛰️ Mountain** - Treacherous peaks with rare herbs and challenging climbing
- **🕳️ Cave** - Dark underground chambers containing valuable minerals and secrets

## ✨ Features

- **Dynamic Inventory System** - Collect and use various items with unique effects
- **Health Management** - Monitor your health and use items to heal
- **Quest System** - Accept and complete quests from villagers
- **Weather Effects** - Dynamic weather that affects gameplay
- **Save/Load System** - Save your progress and continue later
- **Interactive Locations** - Each location offers unique activities and discoveries
- **Random Events** - Encounter unexpected events that add variety to gameplay

## 🎒 Items & Equipment

The game includes a variety of items you can find and use:

- **🗺️ Map** - Shows available locations to travel to
- **🍞 Bread** - Restores health when consumed
- **🪵 Stick** - A simple tool with various uses
- **🫐 Berries** - Edible fruits with random effects
- **🔦 Torch** - Illuminates dark areas like caves
- **💎 Gemstone** - Valuable item that can be sold
- **🪢 Rope** - Essential for safe mountain climbing
- **⛏️ Pickaxe** - Mining tool for extracting resources
- **🍄 Mushrooms** - Foraged food with unpredictable effects
- **🌿 Mountain Herbs** - Rare medicinal plants
- **🪙 Ancient Coin** - Mysterious currency with magical properties
- **⚔️ Sword** - Weapon for combat and utility

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6 or higher

### Installation Steps

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

1. **Starting the Game:**
   - Run `python main.py`
   - Choose to load a saved game or start fresh
   - You begin in the Village as Kevin

2. **Basic Commands:**
   - Type `help` at any time to see available commands
   - Use action words like "go", "take", "use", "look"
   - Type `quit` to save and exit the game

3. **Navigation:**
   - Move between locations using directional commands
   - Each location has unique activities and items to discover
   - Use the map item to see available destinations

4. **Inventory Management:**
   - Collect items by interacting with your environment
   - Use items from your inventory for various effects
   - Some items are consumable, others are permanent tools

5. **Health & Survival:**
   - Monitor your health status
   - Use food items and rest at inns to restore health
   - Be careful in dangerous areas like mountains without proper equipment

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item definitions and usage
│   ├── mythical.py        # Mythical creature encounters
│   ├── player.py          # Player state management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific modules
│   ├── forest.py          # Forest exploration
│   ├── mountain.py        # Mountain climbing
│   └── village.py         # Village interactions
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Save/load game functionality
    └── text_formatting.py # Text display utilities
```

## 🎲 Game Mechanics

### Random Events
The game features a dynamic random event system that creates unique experiences:
- Finding rare items while exploring
- Encountering friendly or dangerous wildlife
- Weather changes affecting gameplay
- Discovering hidden locations and secrets

### Save System
- Automatic save when quitting the game
- Load previous saves when starting
- Multiple save file support

### Quest System
- Accept quests from village NPCs
- Deliver items to specific locations
- Receive rewards for quest completion

## 🔧 Development Notes

This is a test repository showcasing:
- Modular Python game architecture
- Object-oriented design patterns
- File-based save/load system
- Dynamic content generation
- Interactive storytelling mechanics

## 🤝 Contributing

This is a test repository for educational purposes. Feel free to explore the code and understand the game mechanics!

## 📝 License

This project is for educational and testing purposes.

---

**Last updated:** June 2025  
**Game Version:** 1.0  
**Python Version:** 3.6+

