# 🎮 Kevin's Adventure Game

A text-based adventure game written in Python featuring an immersive world with multiple locations, dynamic weather, mythical creatures, and a comprehensive save/load system.

## 🌟 Features

- **Multiple Locations**: Explore the Village, Forest, and Mountain regions
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Mythical Creatures**: Encounter various creatures throughout your adventure
- **Inventory Management**: Collect and manage items during your journey
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected events that add excitement to your journey
- **Rich Text Formatting**: Enjoy colorful and formatted text output

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── items.py           # Item definitions and management
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
    └── text_formatting.py # Text formatting and display
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. **Run the game:**
   ```bash
   python main.py
   ```
   or
   ```bash
   python3 main.py
   ```

## 🎯 How to Play

1. **Starting the Game**: Run `python main.py` to begin your adventure
2. **Loading Saves**: Choose to load a previous save file when prompted
3. **Navigation**: Use movement commands to explore different locations
4. **Commands**: Type `help` at any time to see available commands
5. **Saving**: Save your progress at any point during the game

## 🗺️ Game World

### Locations

- **🏘️ Village**: The starting point of your adventure with shops and NPCs
- **🌲 Forest**: A mysterious woodland filled with creatures and hidden treasures
- **⛰️ Mountain**: A challenging terrain with unique encounters and rewards

### Weather System

The game features a dynamic weather system that affects:
- Visibility and exploration
- Creature encounters
- Available actions and events

## 🎮 Game Mechanics

- **Player Stats**: Manage your character's health, inventory, and progress
- **Item Collection**: Discover and collect various items throughout the world
- **Creature Encounters**: Meet mythical beings that can help or hinder your journey
- **Random Events**: Experience unexpected situations that test your decision-making

## 💾 Save System

- Save files are stored locally in JSON format
- Multiple save slots available
- Load any previous save to continue your adventure
- Progress is automatically tracked across all game systems

## 🛠️ Development

This project is structured with modularity in mind:

- **Game Logic**: Separated into logical modules (player, world, items, etc.)
- **Location System**: Each area has its own dedicated module
- **Utility Functions**: Reusable components for saves, formatting, and events
- **Clean Architecture**: Easy to extend with new locations, items, or features

## 🤝 Contributing

This is a test repository for development and experimentation. Feel free to:
- Add new locations
- Implement new game mechanics
- Improve the user interface
- Add new creatures or items

## 📝 License

This project is for educational and testing purposes.

---

**Last Updated**: May 29, 2025  
**Python Version**: 3.7+  
**Platform**: Cross-platform (Linux, Windows, macOS)

*Embark on Kevin's adventure and discover what awaits in this text-based world!* 🌟

