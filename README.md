# 🌈 Kevin's Adventure Game

A text-based adventure game where players explore different locations, collect items, battle creatures, and experience random events in a dynamic world.

## 🎮 Game Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and mysterious Cave
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect and use various items throughout your adventure
- **Mythical Creatures**: Encounter and summon magical beings to aid your journey
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and discoveries
- **Health & Gold System**: Manage your resources as you explore

## 🚀 Installation

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
2. **Navigation**: Use commands to move between locations and interact with the world
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Type `quit` to save your progress and exit the game

## 🗂️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game loop and entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item management system
│   ├── mythical.py        # Mythical creature interactions
│   ├── player.py          # Player state and management
│   ├── state.py           # World state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World initialization and location management
├── locations/             # Location-specific content
│   ├── cave.py           # Cave exploration
│   ├── forest.py         # Forest adventures
│   ├── mountain.py       # Mountain climbing
│   └── village.py        # Village interactions
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Game save/load functionality
    └── text_formatting.py # Text display and formatting
```

## 🎲 Game Mechanics

- **Health System**: Monitor your health as you face challenges
- **Gold Economy**: Earn and spend gold in the village
- **Weather Effects**: Different weather conditions affect your adventures
- **Location-Based Events**: Each location offers unique experiences and challenges
- **Persistent Progress**: Your game state is automatically saved when you quit

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies required - uses only Python standard library

## 🎨 Game Locations

- **🏘️ Village**: The starting point with shops and friendly NPCs
- **🌲 Forest**: A lush wilderness full of mysteries and creatures
- **⛰️ Mountain**: Challenging terrain with valuable rewards
- **🕳️ Cave**: Dark depths hiding ancient secrets

## 🎪 Contributing

This is a test repository for exploring text-based game development. Feel free to fork and experiment with new features!

## 📝 License

This project is for educational and testing purposes.

---

*Last updated: May 29, 2025*  
*Platform: Linux x86_64*

