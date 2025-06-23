🌈 # Kevin's Adventure Game 🌈

A feature-rich text-based adventure game where players explore different locations, collect items, battle mythical creatures, and experience dynamic weather and random events.

## 🎮 Features

- **Multiple Locations**: Explore the Village, Forest, and Mountain regions
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Item Collection**: Discover and collect various items throughout your journey
- **Mythical Creatures**: Encounter and battle legendary beings
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and events
- **Player Status Tracking**: Monitor your health, inventory, and progress

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

1. **Starting the Game**: Choose to load a saved game or start fresh
2. **Navigation**: Move between different locations (Village, Forest, Mountain)
3. **Commands**: Type commands to interact with the world
4. **Help**: Type `help` at any time to see available commands
5. **Saving**: Type `quit` to save your progress and exit

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py              # Main game loop and entry point
├── game/                # Core game mechanics
│   ├── actions.py       # Game action handlers
│   ├── items.py         # Item definitions and management
│   ├── mythical.py      # Mythical creature encounters
│   ├── player.py        # Player character management
│   ├── state.py         # Game state management
│   ├── weather.py       # Weather system
│   └── world.py         # World and location management
├── locations/           # Location-specific content
│   ├── forest.py        # Forest area content
│   ├── mountain.py      # Mountain area content
│   └── village.py       # Village area content
└── utils/               # Utility functions
    ├── random_events.py # Random event system
    ├── save_load.py     # Save/load functionality
    └── text_formatting.py # Text display utilities
```

## 🎲 Game Mechanics

- **Weather Effects**: Different weather conditions affect your adventure
- **Item System**: Collect, use, and manage various items
- **Location-Based Events**: Each area has unique encounters and opportunities
- **Persistent Progress**: Your game state is automatically saved when you quit

## 🛠️ Requirements

- Python 3.x
- No additional dependencies required

## 🎪 Contributing

This is a test repository for demonstrating text-based game development concepts. Feel free to explore the code and see how different game systems are implemented!

---

*Last updated: June 2025*
