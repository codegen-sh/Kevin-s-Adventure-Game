# 🌈 Kevin's Adventure Game

A feature-rich text-based adventure game where players explore different locations, interact with characters, manage inventory, and experience dynamic events in an immersive fantasy world.

## 🎮 Game Features

- **Multiple Locations**: Explore the Village, Forest, Mountain, and mysterious Cave
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect, use, and manage various items throughout your journey
- **Mythical Creatures**: Encounter and summon magical beings to aid your adventure
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected events that add excitement to your journey
- **Player Stats**: Track your health, gold, and inventory as you progress
- **Interactive NPCs**: Talk to villagers and other characters for quests and information

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required (uses only Python standard library)

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

### Starting the Game
- When you start, you'll be prompted to either load a saved game or start fresh
- Your character begins in the Village with 100 health and 100 gold

### Basic Commands
- Type your actions in natural language (e.g., "go to forest", "check inventory")
- Use `help` at any time to see available commands
- Use `quit` to save and exit the game

### Locations You Can Explore

#### 🏘️ Village
- Visit the shop to buy items
- Talk to villagers for information and quests
- Rest at the inn to restore health
- Check for available quests

#### 🌲 Forest
- Explore the wilderness
- Encounter wildlife and find hidden treasures
- Gather natural resources

#### ⛰️ Mountain
- Climb challenging peaks
- Discover rare items and materials
- Face mountain-specific challenges

#### 🕳️ Cave
- Delve into mysterious underground chambers
- Find valuable treasures
- Encounter unique cave creatures

## 🎮 Game Mechanics

### Player Stats
- **Health**: Your life force (starts at 100)
- **Gold**: Currency for purchasing items
- **Inventory**: Items you've collected
- **Location**: Your current position in the world

### Weather System
The game features a dynamic weather system with conditions including:
- Clear skies
- Cloudy weather
- Rain
- Storms
- Fog
- Wind

### Save System
- Your progress is automatically saved when you quit
- Multiple save files are supported
- Save files are stored in the `saves/` directory

## 🗂️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game logic
│   ├── actions.py         # Action handling system
│   ├── items.py           # Item management
│   ├── mythical.py        # Mythical creature system
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific content
│   ├── cave.py           # Cave exploration
│   ├── forest.py         # Forest adventures
│   ├── mountain.py       # Mountain climbing
│   └── village.py        # Village interactions
├── utils/                 # Utility functions
│   ├── random_events.py  # Random event generation
│   ├── save_load.py      # Save/load functionality
│   └── text_formatting.py # Text display utilities
└── README.md             # This file
```

## 🛠️ Development

### Contributing
This is a test repository for demonstrating text-based game development concepts. Feel free to explore the code and understand how the different systems work together.

### Code Organization
- **Modular Design**: Each game system is separated into its own module
- **Clean Architecture**: Clear separation between game logic, data, and presentation
- **Extensible**: Easy to add new locations, items, and features

## 🎲 Game Tips

1. **Explore Thoroughly**: Each location has unique items and experiences
2. **Manage Resources**: Keep an eye on your health and gold
3. **Save Regularly**: Use the quit command to save your progress
4. **Experiment**: Try different actions and see what happens
5. **Read Carefully**: Pay attention to descriptions and hints

## 📝 Version History

- **Current Version**: Enhanced adventure game with multiple systems
- **Last Updated**: May 29, 2025
- **Platform**: Cross-platform (Python 3.6+)

## 🎯 Future Enhancements

Potential areas for expansion:
- Combat system with enemies
- Skill progression and character development
- More complex quest system
- Multiplayer functionality
- Graphical interface

---

**Enjoy your adventure, Kevin!** 🗡️✨

