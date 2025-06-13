# 🎮 Kevin's Adventure Game

A rich text-based adventure game featuring exploration, inventory management, weather systems, and mythical encounters!

## ✨ Features

- **🗺️ World Exploration**: Navigate through different locations with unique descriptions
- **🎒 Inventory System**: Collect, use, and manage various items throughout your journey
- **🌦️ Dynamic Weather**: Experience changing weather conditions that affect gameplay
- **🐉 Mythical Encounters**: Meet mysterious creatures and magical beings
- **💾 Save/Load System**: Save your progress and continue your adventure later
- **🎲 Random Events**: Encounter unexpected situations that keep the game exciting
- **📊 Player Stats**: Track your health, inventory, and progress

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation

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

1. **Starting the Game**: When you first run the game, you'll be asked if you want to load a saved game or start fresh
2. **Navigation**: Use directional commands to move between locations
3. **Inventory**: Manage your items and use them strategically
4. **Commands**: Type `help` at any time to see available commands
5. **Saving**: Type `quit` to save your progress and exit the game

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game loop and entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Action handling system
│   ├── items.py           # Item definitions and management
│   ├── mythical.py        # Mythical creatures and encounters
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location definitions
├── locations/             # Location-specific content
├── utils/                 # Utility functions
│   ├── random_events.py   # Random event system
│   ├── save_load.py       # Save/load functionality
│   └── text_formatting.py # Text display utilities
└── README.md              # This file
```

## 🎮 Game Commands

- `help` - Display available commands
- `quit` - Save and exit the game
- `inventory` - View your current items
- `look` - Examine your surroundings
- `go [direction]` - Move in a direction (north, south, east, west)
- `take [item]` - Pick up an item
- `use [item]` - Use an item from your inventory

## 🔧 Development

This game is built with a modular architecture:

- **Game Engine**: Core mechanics in the `game/` directory
- **Utilities**: Helper functions for save/load, formatting, and events
- **Extensible Design**: Easy to add new locations, items, and features

## 🤝 Contributing

Feel free to contribute by:
- Adding new locations and descriptions
- Creating new items and their interactions
- Implementing additional game mechanics
- Improving the user interface
- Adding new random events

## 📝 License

This project is open source and available under the MIT License.

## 🎉 Have Fun!

Embark on Kevin's adventure and explore the mysterious world that awaits! Remember to save your progress regularly and don't hesitate to experiment with different strategies.

---

*Last updated: June 2025*

