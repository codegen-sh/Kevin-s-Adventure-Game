# 🎮 Kevin's Adventure Game

A text-based adventure game where players explore different locations, encounter random events, and embark on exciting quests!

## 🌟 Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and mysterious Caves
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect items, manage gold, and use tools strategically
- **Random Events**: Encounter unexpected situations and mythical creatures
- **Save/Load System**: Save your progress and continue your adventure later
- **Health & Status Tracking**: Monitor your character's health and status
- **Interactive Gameplay**: Make choices that impact your journey

## 🎯 Game Locations

- **🏘️ Village**: The starting point with shops and villagers
- **🌲 Forest**: A lush wilderness full of wildlife and hidden treasures
- **⛰️ Mountain**: Challenging terrain with unique encounters
- **🕳️ Cave**: Dark and mysterious underground passages

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required (uses only Python standard library)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the game directory:
   ```bash
   cd Kevin-s-Adventure-Game
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Starting the Game**: When you run the game, you'll be prompted to either load a saved game or start fresh
2. **Navigation**: Use location names to move between areas (e.g., "forest", "village", "mountain", "cave")
3. **Commands**: 
   - Type `help` to see available commands
   - Type `quit` to save and exit the game
   - Type `status` to check your current health and inventory
4. **Exploration**: Each location offers unique events and opportunities
5. **Inventory**: Collect items and manage your resources wisely

## 🗂️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item management system
│   ├── mythical.py        # Mythical creature encounters
│   ├── player.py          # Player state and management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World state and locations
├── locations/             # Location-specific modules
│   ├── cave.py           # Cave exploration
│   ├── forest.py         # Forest adventures
│   ├── mountain.py       # Mountain climbing
│   └── village.py        # Village interactions
├── utils/                 # Utility functions
│   ├── random_events.py  # Random event generation
│   ├── save_load.py      # Save/load game functionality
│   └── text_formatting.py # Text display utilities
└── README.md             # This file
```

## 🎲 Game Mechanics

- **Health System**: Monitor your health and find ways to heal
- **Weather Effects**: Different weather conditions affect your adventures
- **Random Events**: Encounter unexpected situations based on probability
- **Mythical Creatures**: Summon or encounter magical beings
- **Item Collection**: Gather useful items throughout your journey
- **Gold Management**: Earn and spend gold wisely

## 💾 Save System

The game automatically creates a `saves/` directory to store your progress. You can:
- Save your game by typing `quit`
- Load previous saves when starting the game
- Multiple save files are supported

## 🤝 Contributing

This is a test repository for learning and experimentation. Feel free to:
- Report bugs or issues
- Suggest new features or locations
- Submit pull requests with improvements

## 📝 License

This project is open source and available under the MIT License.

## 🎯 Future Enhancements

- Combat system
- Character progression/leveling
- More diverse random events
- Additional locations and quests
- Multiplayer support
- GUI interface

---

**Last Updated**: May 29, 2025  
**Version**: 1.0  
**Platform**: Cross-platform (Python)

Happy adventuring! 🗺️✨

