# 🌈 Kevin's Adventure Game

A comprehensive text-based adventure game featuring exploration, combat, inventory management, and dynamic weather systems.

## 🎮 Game Features

- **Multiple Locations**: Explore diverse environments including villages, forests, mountains, and mysterious caves
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect, use, and manage various items throughout your journey
- **Mythical Creatures**: Encounter and summon magical beings to aid your adventure
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and events during exploration
- **Health & Gold System**: Manage your character's health and collect gold for trading

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

1. **Starting the Game**: When you launch the game, you'll be prompted to either start a new adventure or load a previously saved game.

2. **Basic Commands**: 
   - Type `help` at any time to see available commands
   - Use directional commands to move between locations
   - Interact with the environment using action commands

3. **Exploration**: Visit different locations each with unique features:
   - **Village**: Trade with merchants and interact with villagers
   - **Forest**: Discover hidden treasures and encounter wildlife
   - **Mountain**: Face challenging climbs and find rare items
   - **Cave**: Explore mysterious underground chambers

4. **Inventory**: Manage your items and use them strategically during your adventure

5. **Save Your Progress**: Use the save feature to preserve your adventure and continue later

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── game/                    # Core game logic
│   ├── actions.py          # Player action handling
│   ├── items.py            # Item management system
│   ├── mythical.py         # Mythical creature interactions
│   ├── player.py           # Player character management
│   ├── state.py            # Game state management
│   ├── weather.py          # Dynamic weather system
│   └── world.py            # World and location management
├── locations/              # Location-specific modules
│   ├── cave.py            # Cave exploration
│   ├── forest.py          # Forest adventures
│   ├── mountain.py        # Mountain climbing
│   └── village.py         # Village interactions
├── utils/                  # Utility functions
│   ├── random_events.py   # Random event generation
│   ├── save_load.py       # Save/load game functionality
│   └── text_formatting.py # Text display utilities
└── main.py                # Game entry point
```

## 🎲 Game Mechanics

- **Health System**: Monitor your character's health and use healing items when needed
- **Gold Economy**: Earn and spend gold for items and services
- **Weather Effects**: Adapt to changing weather conditions that impact gameplay
- **Random Events**: Encounter unexpected situations that can help or hinder your progress
- **Location-Based Actions**: Each location offers unique interactions and opportunities

## 💾 Save System

The game features an automatic save system that allows you to:
- Save your current progress at any time
- Load previously saved games
- Multiple save slots for different playthroughs

## 🤝 Contributing

This is a test repository for demonstrating text-based game development. Feel free to explore the code and understand the game mechanics!

## 📝 Technical Details

- **Language**: Python 3.6+
- **Architecture**: Modular design with separated concerns
- **Save Format**: JSON-based save files
- **Text Interface**: Console-based user interaction

---

*Last updated: May 29, 2025*  
*Repository: codegen-sh/Kevin-s-Adventure-Game*

