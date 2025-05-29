# 🎮 Kevin's Adventure Game

A text-based adventure game written in Python where players embark on an epic journey through various locations, encounter mythical creatures, and experience dynamic weather systems.

## 🌟 Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and Cave
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Mythical Creatures**: Encounter and interact with magical beings
- **Inventory Management**: Collect and manage items throughout your adventure
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected events that add excitement to your journey
- **Player Stats**: Track your health, gold, and inventory
- **Interactive NPCs**: Talk to villagers and other characters

## 🚀 Quick Start

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

1. **Starting the Game**: When you run the game, you'll be prompted to either load a saved game or start fresh
2. **Navigation**: Use text commands to interact with the game world
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Type `quit` to save your progress and exit the game

### Available Locations

- **🏘️ Village**: Visit shops, talk to villagers, rest at the inn, and find quests
- **🌲 Forest**: Explore the wilderness and encounter forest creatures
- **⛰️ Mountain**: Climb treacherous peaks and discover mountain secrets
- **🕳️ Cave**: Venture into dark caves filled with mysteries

### Game Mechanics

- **Health System**: Monitor your health and heal when necessary
- **Inventory**: Collect items, weapons, and treasures
- **Gold**: Earn and spend gold at village shops
- **Weather**: Adapt to changing weather conditions
- **Random Events**: Stay alert for unexpected encounters

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── items.py           # Item management system
│   ├── mythical.py        # Mythical creature interactions
│   ├── player.py          # Player stats and actions
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific modules
│   ├── village.py         # Village interactions
│   ├── forest.py          # Forest exploration
│   └── mountain.py        # Mountain climbing
├── utils/                 # Utility functions
│   ├── random_events.py   # Random event generation
│   ├── save_load.py       # Save/load game functionality
│   └── text_formatting.py # Text display utilities
└── saves/                 # Save game files (created automatically)
```

## 🎮 Gameplay Tips

- **Explore Thoroughly**: Each location has multiple activities and hidden secrets
- **Manage Resources**: Keep track of your health and gold
- **Save Regularly**: Use the quit command to save your progress
- **Experiment**: Try different actions and see what happens
- **Read Carefully**: Pay attention to descriptions and hints

## 🛠️ Development

This game is built using pure Python with no external dependencies, making it easy to run and modify. The modular structure allows for easy expansion of locations, items, and game mechanics.

### Adding New Features

- **New Locations**: Add new location files in the `locations/` directory
- **New Items**: Extend the item system in `game/items.py`
- **New Events**: Add random events in `utils/random_events.py`

## 🐛 Troubleshooting

- **Import Errors**: Ensure you're running the game from the root directory
- **Save Issues**: The game will automatically create a `saves/` directory if it doesn't exist
- **Python Version**: Make sure you're using Python 3.6 or higher

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements, bug fixes, or new features!

---

*Last updated: May 29, 2025*  
*Compatible with: Python 3.6+*  
*Platform: Cross-platform (Windows, macOS, Linux)*

