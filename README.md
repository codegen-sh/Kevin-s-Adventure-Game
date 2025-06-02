# 🎮 Kevin's Adventure Game

A text-based adventure game written in Python featuring exploration, inventory management, and dynamic gameplay elements.

## 🌟 Features

- **Interactive World**: Explore multiple locations including Village, Forest, Mountain, and Cave
- **Player Management**: Health, inventory, and gold tracking system
- **Dynamic Weather**: Weather system that affects gameplay
- **Mythical Elements**: Encounter mythical creatures and events
- **Save/Load System**: Save your progress and continue later
- **Random Events**: Unpredictable events to keep gameplay exciting
- **Item System**: Collect, use, and manage various items
- **Location-based Interactions**: Each location offers unique experiences and challenges

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game logic
│   ├── actions.py         # Game action handlers
│   ├── items.py           # Item management system
│   ├── mythical.py        # Mythical creatures and events
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific modules
│   ├── forest.py          # Forest location logic
│   ├── mountain.py        # Mountain location logic
│   └── village.py         # Village location logic
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Save/load game functionality
    └── text_formatting.py # Text display and formatting
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

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

1. **Starting the Game**: Run `python main.py` to begin your adventure
2. **Loading Saves**: Choose to load a previous save file when prompted
3. **Navigation**: Use location names to move between areas
4. **Commands**: Type `help` at any time to see available commands
5. **Inventory**: Manage items you collect during your journey
6. **Saving**: Save your progress at any time to continue later

### Available Locations
- **Village**: The starting point with shops and NPCs
- **Forest**: A mysterious woodland with hidden treasures
- **Mountain**: Challenging terrain with unique encounters
- **Cave**: Dark depths with rare items and dangers

## 🎮 Gameplay Elements

- **Health System**: Monitor your character's health throughout the adventure
- **Gold Economy**: Earn and spend gold on items and services
- **Weather Effects**: Dynamic weather that influences your journey
- **Random Encounters**: Unexpected events that add excitement
- **Item Collection**: Discover and use various items to aid your quest

## 🛠️ Development

This project serves as a test repository for TinySitter and demonstrates:
- Modular Python game architecture
- File-based save/load systems
- Object-oriented game design patterns
- Text-based user interface design

## 📝 Game Commands

- `help` - Display available commands
- `status` - Check player status
- `inventory` - View your items
- `save` - Save current game
- `quit` - Exit the game

## 🤝 Contributing

This is a test repository, but feel free to explore the code and suggest improvements!

## 📄 License

This project is for educational and testing purposes.

---

**Last Updated**: June 2, 2025  
**Repository**: [Kevin-s-Adventure-Game](https://github.com/codegen-sh/Kevin-s-Adventure-Game)  
**Status**: Active Development

