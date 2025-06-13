# 🎮 Kevin's Adventure Game

A rich text-based adventure game featuring dynamic weather, mythical creatures, and an immersive world to explore!

## ✨ Features

- **Dynamic World**: Explore different locations with unique descriptions and interactions
- **Weather System**: Experience changing weather conditions that affect gameplay
- **Mythical Creatures**: Encounter and interact with various mythical beings
- **Inventory Management**: Collect, use, and manage items throughout your adventure
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected events that add excitement to your journey
- **Player Stats**: Track your health, experience, and other character attributes

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher

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

1. **Starting the Game**: When you first run the game, you'll be asked if you want to load a saved game or start fresh
2. **Commands**: Type commands to interact with the world (e.g., "look around", "go north", "take item")
3. **Help**: Type `help` at any time to see available commands
4. **Saving**: Type `quit` to save your progress and exit the game

### Basic Commands
- `help` - Display available commands
- `quit` - Save and exit the game
- `look` - Examine your surroundings
- `inventory` - Check your items
- `status` - View your character stats

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py              # Main game loop and entry point
├── game/                # Core game mechanics
│   ├── actions.py       # Action handling system
│   ├── items.py         # Item definitions and management
│   ├── mythical.py      # Mythical creature interactions
│   ├── player.py        # Player character management
│   ├── state.py         # Game state management
│   ├── weather.py       # Dynamic weather system
│   └── world.py         # World and location definitions
├── locations/           # Location-specific content
├── utils/               # Utility functions
│   ├── random_events.py # Random event system
│   ├── save_load.py     # Save/load functionality
│   └── text_formatting.py # Text display utilities
└── README.md           # This file
```

## 🎨 Game Features in Detail

### Weather System
The game features a dynamic weather system that changes as you play, affecting the atmosphere and potentially your actions.

### Mythical Creatures
Encounter various mythical beings throughout your adventure, each with unique interactions and behaviors.

### Item System
Discover and collect items that can help you on your journey. Manage your inventory wisely!

### Save System
Your progress is automatically saved when you quit, and you can load previous saves to continue your adventure.

## 🤝 Contributing

This is a test repository for demonstrating game development concepts. Feel free to explore the code and see how different game systems are implemented!

## 📝 License

This project is for educational and testing purposes.

---

*Last updated: June 2025*
*Enjoy your adventure! 🌟*

