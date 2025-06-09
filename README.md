# 🎮 Kevin's Adventure Game

A text-based adventure game featuring exploration, item collection, weather systems, and mythical creatures!

## 🌟 Features

- **Dynamic World**: Explore multiple locations including villages, forests, and mountains
- **Weather System**: Experience changing weather conditions that affect gameplay
- **Item Collection**: Discover and collect various items throughout your adventure
- **Mythical Creatures**: Encounter magical beings in your journey
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and events

## 🗺️ Game World

The game features several interconnected locations:

- **🏘️ Village**: The starting point of your adventure
- **🌲 Forest**: A mysterious woodland with hidden secrets
- **⛰️ Mountain**: Challenging terrain with unique encounters

## 🎯 Game Components

### Core Systems
- **Player Management**: Character creation and status tracking
- **World System**: Location management and navigation
- **Weather Engine**: Dynamic weather affecting gameplay
- **Item System**: Comprehensive item collection and management
- **Save/Load**: Persistent game state management

### Utilities
- **Random Events**: Unpredictable encounters and scenarios
- **Text Formatting**: Enhanced display and user interface
- **Save Management**: Multiple save file support

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

## 🎮 How to Play

1. **Starting the Game**: Run `python main.py` to begin your adventure
2. **Loading Saves**: Choose to load a previous save file when prompted
3. **Commands**: Type 'help' at any time to see available commands
4. **Exploration**: Navigate between different locations
5. **Interaction**: Collect items, interact with creatures, and experience events
6. **Saving**: Save your progress to continue later

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game logic
│   ├── items.py           # Item system and definitions
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
    └── text_formatting.py # UI and text display
```

## 🛠️ Development Status

**Current Version**: Development Build  
**Last Updated**: June 9, 2025  
**Platform**: Linux/Unix compatible  

### Known Issues
- Some game modules may need additional integration
- Game balance and feature completion in progress

## 🤝 Contributing

This is a test repository for development and experimentation. Feel free to explore the code and suggest improvements!

## 📝 License

This project is for educational and testing purposes.

---

*Embark on Kevin's adventure and discover what awaits in this magical world!* ✨

