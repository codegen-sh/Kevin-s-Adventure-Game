# 🎮 Kevin's Adventure Game

A text-based adventure game where you explore a mystical world filled with danger, treasure, and magical encounters!

## 🌟 Features

- **🗺️ Multiple Locations**: Explore the Village, Forest, Mountain, and mysterious Cave
- **⚔️ Combat System**: Battle mythical creatures and monsters
- **🎒 Inventory Management**: Collect items, weapons, and treasures
- **💰 Economy System**: Earn and spend gold throughout your adventure
- **🌤️ Dynamic Weather**: Experience changing weather conditions that affect gameplay
- **🎲 Random Events**: Encounter unexpected events and challenges
- **💾 Save/Load System**: Save your progress and continue your adventure later
- **🏥 Health System**: Manage your health as you face dangers

## 🚀 Getting Started

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

1. **Starting the Game**: When you launch the game, you can choose to start a new adventure or load a previously saved game.

2. **Basic Commands**: 
   - Type `help` at any time to see available commands
   - Use directional commands to move between locations
   - Interact with items and characters you encounter

3. **Game Mechanics**:
   - **Health**: Keep track of your health points (starts at 100)
   - **Inventory**: Collect and manage items in your inventory
   - **Gold**: Earn gold through adventures and use it for purchases
   - **Locations**: Travel between Village, Forest, Mountain, and Cave

4. **Saving Progress**: Use the save feature to preserve your adventure progress

## 🗺️ Game World

### Locations

- **🏘️ Village**: Your starting point - a peaceful settlement with shops and friendly NPCs
- **🌲 Forest**: A mysterious woodland filled with creatures and hidden treasures
- **⛰️ Mountain**: Treacherous peaks with challenging encounters and valuable rewards
- **🕳️ Cave**: Dark underground passages with ancient secrets

## 🎮 Game Systems

### Combat
Engage in turn-based combat with various mythical creatures and monsters throughout your journey.

### Weather System
Dynamic weather conditions affect your adventure:
- Sunny weather may boost your mood
- Rain might make travel more difficult
- Storms could lead to unexpected encounters

### Random Events
Experience unpredictable events that can help or hinder your progress, keeping each playthrough unique.

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py              # Main game entry point
├── game/                # Core game mechanics
│   ├── actions.py       # Player actions and commands
│   ├── items.py         # Item definitions and management
│   ├── mythical.py      # Mythical creatures and encounters
│   ├── player.py        # Player character management
│   ├── state.py         # Game state management
│   ├── weather.py       # Weather system
│   └── world.py         # World initialization and management
├── locations/           # Location-specific content
│   ├── forest.py        # Forest area implementation
│   ├── mountain.py      # Mountain area implementation
│   └── village.py       # Village area implementation
└── utils/               # Utility functions
    ├── random_events.py # Random event system
    ├── save_load.py     # Save/load functionality
    └── text_formatting.py # Text display utilities
```

## 🤝 Contributing

This is a test repository for demonstrating text-based game development. Feel free to explore the code and suggest improvements!

## 📝 License

This project is created for educational and testing purposes.

---

**Last Updated**: December 2024  
**Python Version**: 3.6+  
**Platform**: Cross-platform (Linux, Windows, macOS)

*Embark on Kevin's adventure and discover what mysteries await! 🗡️✨*

