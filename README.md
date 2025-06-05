# 🎮 Kevin's Adventure Game

A text-based adventure game featuring exploration, combat, inventory management, and dynamic weather systems.

## 🌟 Features

- **Immersive World**: Explore multiple locations including villages, forests, and mountains
- **Dynamic Weather**: Experience changing weather conditions that affect gameplay
- **Inventory System**: Collect and manage various items throughout your adventure
- **Save/Load System**: Save your progress and continue your adventure later
- **Mythical Encounters**: Discover magical creatures and legendary items
- **Interactive Combat**: Engage in strategic battles with various enemies
- **Random Events**: Experience unexpected encounters and discoveries

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

1. **Starting the Game**: Run `python main.py` and choose whether to start a new game or load a saved one
2. **Navigation**: Use directional commands to move between locations
3. **Inventory**: Manage your items and equipment
4. **Combat**: Engage enemies using various combat commands
5. **Saving**: Save your progress at any time using the save command
6. **Help**: Type `help` at any time to see available commands

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py              # Main game entry point
├── game/                # Core game mechanics
│   ├── actions.py       # Player actions and commands
│   ├── items.py         # Item definitions and management
│   ├── mythical.py      # Mythical creatures and encounters
│   ├── player.py        # Player character management
│   ├── state.py         # Game state management
│   ├── weather.py       # Weather system
│   └── world.py         # World and location management
├── locations/           # Location-specific content
│   ├── forest.py        # Forest area implementation
│   ├── mountain.py      # Mountain area implementation
│   └── village.py       # Village area implementation
└── utils/               # Utility functions
    ├── random_events.py # Random event system
    ├── save_load.py     # Save/load functionality
    └── text_formatting.py # Text display utilities
```

## 🎮 Game Commands

- **Movement**: `north`, `south`, `east`, `west`
- **Inventory**: `inventory`, `use [item]`, `drop [item]`
- **Combat**: `attack`, `defend`, `flee`
- **System**: `save`, `load`, `help`, `quit`
- **Exploration**: `look`, `search`, `examine [object]`

## 🌦️ Weather System

The game features a dynamic weather system that affects:
- Visibility and exploration
- Combat effectiveness
- Item discovery rates
- NPC behavior

## 💾 Save System

- Save your game progress at any time
- Multiple save slots available
- Automatic backup of game state
- Load any saved game from the main menu

## 🧙‍♂️ Mythical Elements

Discover and interact with:
- Legendary weapons and artifacts
- Mythical creatures with unique abilities
- Ancient locations with hidden secrets
- Magical events and encounters

## 🤝 Contributing

This is a test repository for demonstrating text-based game development. Feel free to explore the code and suggest improvements!

## 📝 License

This project is for educational and testing purposes.

---

*Last updated: June 2025*
*Compatible with: Python 3.6+*

