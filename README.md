# 🎮 Kevin's Adventure Game

A text-based adventure game where players explore different locations, collect items, battle creatures, and experience random events in an immersive fantasy world.

## 🌟 Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and mysterious Cave
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect and manage items throughout your adventure
- **Mythical Creatures**: Encounter and summon magical beings to aid your journey
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and events
- **Health & Gold System**: Manage your character's health and resources

## 🎯 Game Components

### Locations
- **Village**: The starting hub with shops and NPCs
- **Forest**: A lush wilderness with hidden treasures and dangers
- **Mountain**: Challenging terrain with unique encounters
- **Cave**: Mysterious underground passages

### Game Systems
- **Player Management**: Health, inventory, gold, and location tracking
- **Weather System**: Dynamic weather affecting gameplay
- **Item System**: Collectible items with various effects
- **Combat & Events**: Random encounters and mythical creature interactions

## 🚀 Installation & Setup

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

1. **Starting the Game**: Run `python main.py` and choose to start a new game or load a saved game
2. **Navigation**: Use text commands to move between locations and interact with the world
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Type `quit` to save your progress and exit the game

### Basic Commands
- `help` - Display available commands
- `quit` - Save and exit the game
- `status` - Check your current health, inventory, and location
- Location-specific commands will be shown when you enter each area

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game logic
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item management system
│   ├── mythical.py        # Mythical creature interactions
│   ├── player.py          # Player state management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World state and location management
├── locations/             # Location-specific modules
│   ├── cave.py           # Cave exploration
│   ├── forest.py         # Forest adventures
│   ├── mountain.py       # Mountain climbing
│   └── village.py        # Village interactions
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Save/load game functionality
    └── text_formatting.py # Text display utilities
```

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies required - uses only Python standard library

## 🎨 Game Features in Detail

### Save System
The game automatically creates a `saves/` directory and allows you to:
- Save your progress when quitting
- Load previous games on startup
- Multiple save file support

### Weather System
Dynamic weather affects your adventure:
- Clear, cloudy, rainy, stormy, foggy, and windy conditions
- Weather impacts certain events and interactions

### Inventory & Items
- Collect various items throughout your journey
- Items can heal, provide gold, or have special effects
- Inventory management with item descriptions

## 🤝 Contributing

This is a test repository for learning and experimentation. Feel free to:
- Add new locations
- Create new items and creatures
- Implement additional game mechanics
- Improve the user interface

## 📝 License

This project is for educational and testing purposes.

---

**Last Updated**: May 29, 2025  
**Version**: 1.0  
**Platform**: Cross-platform (Python)

Happy adventuring! 🗡️✨

