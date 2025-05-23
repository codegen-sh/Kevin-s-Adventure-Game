# 🎮 Kevin's Adventure Game

A comprehensive text-based adventure game featuring dynamic weather, mythical creatures, and an immersive world to explore!

## 🌟 Features

- **Rich World Exploration**: Navigate through diverse locations including villages, forests, and mountains
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Mythical Creatures**: Encounter and interact with various mythical beings
- **Inventory Management**: Collect, use, and manage items throughout your adventure
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and events during your journey
- **Player Progression**: Track your status and progress through the game

## 🗺️ Game Locations

- **Village**: The starting point of your adventure with shops and NPCs
- **Forest**: A mysterious woodland filled with creatures and hidden treasures
- **Mountain**: Challenging terrain with unique encounters and rewards

## 🎯 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. **Run the game**:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Starting the Game**: Run `python main.py` to begin your adventure
2. **Loading Saves**: Choose to load a previous save file when prompted
3. **Navigation**: Use directional commands to move between locations
4. **Inventory**: Manage your items and equipment
5. **Help**: Type `help` at any time to see available commands
6. **Saving**: Save your progress at any point during the game

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── items.py           # Item system and inventory management
│   ├── mythical.py        # Mythical creatures and encounters
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World and location management
├── locations/             # Specific location implementations
│   ├── forest.py          # Forest area logic
│   ├── mountain.py        # Mountain area logic
│   └── village.py         # Village area logic
└── utils/                 # Utility functions
    ├── random_events.py   # Random event system
    ├── save_load.py       # Save/load functionality
    └── text_formatting.py # Text display and formatting
```

## 🎲 Game Mechanics

- **Weather Effects**: Weather conditions influence gameplay and available actions
- **Item System**: Comprehensive inventory with various item types and effects
- **Random Events**: Procedurally generated encounters keep each playthrough unique
- **Location-Based Gameplay**: Each area offers unique challenges and opportunities

## 🔧 Requirements

- Python 3.x
- No external dependencies required - uses only Python standard library

## 🎨 Game Features

- **Interactive Storytelling**: Rich narrative with player choices affecting outcomes
- **Persistent World**: Your actions and progress are saved between sessions
- **Modular Design**: Easy to extend with new locations, items, and features

## 🚀 Getting Started

1. Start the game with `python main.py`
2. Choose whether to load an existing save or start fresh
3. Follow the on-screen prompts to navigate and interact
4. Use the `help` command to learn about available actions
5. Explore different locations and discover what Kevin's world has to offer!

## 📝 Last Updated

May 23, 2025

---

*Embark on Kevin's adventure and discover the mysteries that await! 🌟*

