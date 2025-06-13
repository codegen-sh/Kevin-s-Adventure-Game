# 🎮 Kevin's Adventure Game

A rich text-based adventure game featuring exploration, inventory management, weather systems, and mythical encounters!

## 🌟 Features

- **Dynamic World Exploration**: Navigate through various locations with unique descriptions
- **Inventory System**: Collect, use, and manage items throughout your adventure
- **Weather System**: Experience changing weather conditions that affect gameplay
- **Mythical Encounters**: Meet mysterious creatures and magical beings
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Encounter unexpected situations that add excitement to your journey
- **Player Stats**: Track your health, experience, and other vital statistics

## 🚀 Installation

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

1. **Starting the Game**: When you launch the game, you'll be asked if you want to load a saved game or start fresh
2. **Navigation**: Use directional commands to move between locations
3. **Inventory**: Manage your items using inventory commands
4. **Help**: Type `help` at any time to see available commands
5. **Saving**: Type `quit` to save your progress and exit the game

## 🗂️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game loop and entry point
├── game/                   # Core game mechanics
│   ├── actions.py         # Action handling system
│   ├── items.py           # Item definitions and management
│   ├── mythical.py        # Mythical creatures and encounters
│   ├── player.py          # Player character management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location data and descriptions
├── utils/                 # Utility functions
│   ├── random_events.py   # Random event system
│   ├── save_load.py       # Save/load functionality
│   └── text_formatting.py # Text display utilities
└── README.md              # This file
```

## 🎮 Game Commands

- `help` - Display available commands
- `quit` - Save and exit the game
- `inventory` - View your items
- `look` - Examine your surroundings
- `go [direction]` - Move in a direction
- `take [item]` - Pick up an item
- `use [item]` - Use an item from your inventory

## 🔧 Requirements

- Python 3.6 or higher
- No additional dependencies required - uses only Python standard library

## 🎨 Game Features in Detail

### Weather System
The game features a dynamic weather system that changes as you play, affecting the atmosphere and potentially your gameplay experience.

### Mythical Encounters
Discover magical creatures and beings throughout your adventure, each with unique interactions and stories.

### Save System
Your progress is automatically saved when you quit, allowing you to continue your adventure exactly where you left off.

### Random Events
Unexpected events can occur during your journey, adding variety and excitement to each playthrough.

## 🤝 Contributing

This is a test repository for demonstrating game development concepts. Feel free to explore the code and see how different game systems are implemented!

## 📝 License

This project is for educational and testing purposes.

---

*Last updated: June 2025*  
*Enjoy your adventure, Kevin! 🌈*

