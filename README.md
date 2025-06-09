# 🎮 Kevin's Adventure Game

A text-based adventure game written in Python where players explore different locations, interact with mythical creatures, and manage their inventory in an immersive fantasy world.

## 🌟 Features

- **Multiple Locations**: Explore various environments including:
  - 🏘️ Village - A bustling town with NPCs and shops
  - 🌲 Forest - Lush wilderness with hidden secrets
  - ⛰️ Mountain - Challenging terrain with unique encounters
  
- **Player Management**: 
  - Health and inventory system
  - Gold currency for trading
  - Save/load game functionality
  
- **Dynamic World**:
  - Weather system affecting gameplay
  - Random events and encounters
  - Mythical creature summoning
  - Interactive NPCs and items

- **Game Features**:
  - Persistent save system
  - Help system with available commands
  - Text-based interface with formatted output

## 🚀 Installation

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
2. **Navigation**: Use text commands to move between locations and interact with the world
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Type `quit` to save your progress and exit the game

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py              # Main game loop and entry point
├── game/                # Core game mechanics
│   ├── items.py         # Item management system
│   ├── mythical.py      # Mythical creature interactions
│   ├── player.py        # Player state and actions
│   ├── state.py         # World state management
│   ├── weather.py       # Dynamic weather system
│   └── world.py         # World initialization and management
├── locations/           # Location-specific modules
│   ├── forest.py        # Forest area implementation
│   ├── mountain.py      # Mountain area implementation
│   └── village.py       # Village area implementation
└── utils/               # Utility functions
    ├── random_events.py # Random event generation
    ├── save_load.py     # Save/load game functionality
    └── text_formatting.py # Text display utilities
```

## 🎮 Game Mechanics

- **Health System**: Monitor your character's health throughout the adventure
- **Inventory Management**: Collect and manage items during your journey
- **Gold Economy**: Earn and spend gold for various in-game transactions
- **Location-Based Gameplay**: Each location offers unique experiences and challenges
- **Weather Effects**: Dynamic weather system that affects gameplay
- **Random Events**: Encounter unexpected events that can help or hinder your progress

## 🛠️ Development

This project is structured with modular Python files for easy maintenance and expansion:

- **Game Logic**: Core mechanics are separated into logical modules
- **Location System**: Each location is implemented as a separate module
- **Utility Functions**: Common functionality is abstracted into utility modules
- **Save System**: Persistent game state using JSON serialization

## 🤝 Contributing

Feel free to contribute to Kevin's Adventure Game by:
- Adding new locations
- Implementing new game mechanics
- Improving the user interface
- Adding more random events and encounters

## 📝 License

This project is a test repository for educational and development purposes.

---

**Last Updated**: June 2025  
**Python Version**: 3.x  
**Platform**: Cross-platform (Linux, Windows, macOS)

