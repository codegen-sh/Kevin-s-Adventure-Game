# 🎮 Kevin's Adventure Game

A text-based adventure game where players explore different locations, collect items, battle creatures, and experience random events in a dynamic world.

## 🌟 Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and Cave
- **Dynamic Weather System**: Weather conditions that affect gameplay
- **Inventory Management**: Collect and use various items throughout your journey
- **Mythical Creatures**: Encounter and summon magical beings to aid your quest
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters that keep the game exciting
- **Health & Gold System**: Manage your resources as you explore

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

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

1. **Starting the Game**: When you launch the game, you'll be prompted to either start a new game or load a saved game.

2. **Basic Commands**:
   - Type `help` to see available commands
   - Type `quit` to save and exit the game
   - Use action words like `explore`, `search`, `fight`, `heal`, etc.

3. **Locations**: Navigate between different areas:
   - **Village**: The starting location with shops and NPCs
   - **Forest**: A lush area with wildlife and hidden treasures
   - **Mountain**: A challenging terrain with unique encounters
   - **Cave**: A mysterious underground location

4. **Game Mechanics**:
   - Monitor your health and gold
   - Collect items to aid your journey
   - Weather affects your adventures
   - Random events can help or hinder your progress

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game loop and entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Action handling system
│   ├── items.py           # Item management
│   ├── mythical.py        # Mythical creature interactions
│   ├── player.py          # Player state and actions
│   ├── state.py           # World state management
│   ├── weather.py         # Weather system
│   └── world.py           # World initialization and location management
├── locations/             # Location-specific modules
│   ├── forest.py          # Forest location logic
│   ├── mountain.py        # Mountain location logic
│   └── village.py         # Village location logic
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Save/load game functionality
    └── text_formatting.py # Text display utilities
```

## 🎮 Game Commands

- `help` - Display available commands
- `status` - Check your current health, gold, and inventory
- `explore` - Explore your current location
- `move [location]` - Travel to a different location
- `inventory` - View your items
- `use [item]` - Use an item from your inventory
- `quit` - Save and exit the game

## 💾 Save System

The game automatically creates save files when you quit. Save files are stored in a `saves/` directory and include:
- Player status (health, gold, inventory)
- Current location
- World state
- Timestamp of the save

## 🔧 Development

This is a modular Python project that's easy to extend:

- **Adding New Locations**: Create new files in the `locations/` directory
- **Adding Items**: Extend the item system in `game/items.py`
- **New Events**: Add random events in `utils/random_events.py`
- **Game Mechanics**: Modify core mechanics in the `game/` directory

## 🤝 Contributing

This is a test repository for development purposes. Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests for improvements

## 📝 License

This project is for educational and testing purposes.

---

**Last Updated**: December 2024  
**Python Version**: 3.6+  
**Platform**: Cross-platform (Linux, Windows, macOS)

Enjoy your adventure! 🗺️✨

