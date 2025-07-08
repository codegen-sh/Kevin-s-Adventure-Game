# 🌈 Kevin's Adventure Game

A sophisticated text-based adventure game featuring dynamic weather, mythical creatures, item management, and persistent save/load functionality.

## 🎮 Game Features

### Core Gameplay
- **Immersive World**: Explore diverse locations including villages, forests, caves, and mountains
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Mythical Encounters**: Discover and interact with magical creatures and elements
- **Item Management**: Collect, use, and manage various items throughout your adventure
- **Player Progression**: Track health, gold, and inventory as you progress

### Advanced Features
- **Save/Load System**: Persistent game state with multiple save slots
- **Random Events**: Encounter unexpected events that add variety to gameplay
- **Interactive Commands**: Rich command system for exploring and interacting with the world
- **Status Tracking**: Real-time display of player health, inventory, and gold
- **Text Formatting**: Enhanced visual presentation with formatted text output

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required (uses only Python standard library)

### Setup
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

### Starting the Game
When you launch the game, you'll be prompted to either:
- Start a new adventure as Kevin
- Load a previously saved game from available save files

### Basic Commands
- `help` - Display all available commands
- `look` - Examine your current surroundings
- `move [location]` - Travel to a new location
- `inventory` - Check your current items
- `pickup [item]` - Collect items you find
- `quit` - Save your progress and exit the game

### Game Mechanics
- **Health**: Monitor your health status - avoid dangerous situations
- **Gold**: Collect and manage gold for trading and purchases
- **Inventory**: Carry useful items that can help in your adventure
- **Weather**: Adapt to changing weather conditions that affect your journey

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game loop and entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item system and definitions
│   ├── mythical.py        # Mythical creatures and magic
│   ├── player.py          # Player state management
│   ├── state.py           # Game state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World generation and management
├── locations/             # Location definitions and descriptions
├── utils/                 # Utility functions
│   ├── random_events.py   # Random event system
│   ├── save_load.py       # Save/load functionality
│   └── text_formatting.py # Text display utilities
└── README.md              # This file
```

## 🎲 Game Features in Detail

### Weather System
The game features a dynamic weather system that affects gameplay:
- Different weather patterns influence available actions
- Weather changes can create new opportunities or challenges
- Atmospheric effects enhance immersion

### Save/Load System
- Multiple save slots available
- Automatic save on quit
- Load any previous save to continue your adventure
- Persistent world state and player progress

### Item System
- Diverse items with different properties and uses
- Inventory management with capacity considerations
- Items can affect player abilities and story progression

## 🤝 Contributing

This is a test repository for educational and demonstration purposes. Feel free to explore the code and understand how a text-based adventure game can be structured in Python.

## 📝 License

This project is for educational and testing purposes.

---

**Last Updated**: January 2025  
**Version**: 2.0  
**Platform**: Cross-platform (Python 3.6+)

