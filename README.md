# 🎮 Kevin's Adventure Game

A text-based adventure game where players explore different locations, collect items, encounter mythical creatures, and experience dynamic weather systems.

## 🌟 Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and mysterious caves
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect and use various items throughout your adventure
- **Mythical Creatures**: Encounter and interact with magical beings
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected encounters and events
- **Health & Gold System**: Manage your character's health and resources

## 🎯 Game Locations

- **🏘️ Village**: The starting point with shops and villagers
- **🌲 Forest**: A lush environment filled with wildlife and hidden treasures
- **⛰️ Mountain**: Challenging terrain with unique encounters
- **🕳️ Cave**: Mysterious underground locations to explore

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
2. **Navigation**: Use text commands to interact with the game world
3. **Commands**: Type `help` at any time to see available commands
4. **Saving**: Type `quit` to save your progress and exit the game

## 🗂️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game loop and entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item system and interactions
│   ├── mythical.py        # Mythical creature encounters
│   ├── player.py          # Player state management
│   ├── state.py           # Game state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World initialization and management
├── locations/             # Different game locations
│   ├── forest.py          # Forest location logic
│   ├── mountain.py        # Mountain location logic
│   └── village.py         # Village location logic
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Save/load game functionality
    └── text_formatting.py # Text display utilities
```

## 🎲 Game Mechanics

- **Health System**: Monitor your character's health throughout the adventure
- **Inventory**: Collect and manage items that help in your journey
- **Gold**: Earn and spend gold for various in-game purchases
- **Weather Effects**: Adapt to changing weather conditions
- **Random Events**: Experience unpredictable encounters that add excitement

## 🛠️ Requirements

- Python 3.x
- No external dependencies required - uses only Python standard library

## 🎨 Game Features

- Rich text-based storytelling
- Interactive decision-making
- Persistent game state with save/load functionality
- Modular location system for easy expansion
- Event-driven gameplay with random encounters

## 🤝 Contributing

This is a test repository for demonstrating text-based game development. Feel free to explore the code and understand the game mechanics!

## 📝 License

This project is for educational and testing purposes.

---

*Last updated: June 2025*
*Compatible with: Python 3.x on all platforms*

