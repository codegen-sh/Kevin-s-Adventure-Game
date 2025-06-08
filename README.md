# 🎮 Kevin's Adventure Game

A text-based adventure game where you explore a mystical world filled with mystery, danger, and magical encounters. Navigate through diverse locations, collect items, interact with characters, and uncover the secrets of this enchanted realm.

## 🌟 Features

- **Rich World Exploration**: Travel through forests, villages, mountains, and more
- **Interactive Gameplay**: Use various commands to interact with your environment
- **Inventory System**: Collect, use, and manage items throughout your journey
- **Save/Load System**: Save your progress and continue your adventure later
- **Dynamic Events**: Experience random events and encounters
- **Weather System**: Dynamic weather affects your adventure
- **Mythical Encounters**: Meet magical creatures and characters
- **Player Status Tracking**: Monitor your health, inventory, and progress

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

### Starting the Game
- When you start, you'll be asked if you want to load a saved game
- If no save files exist, a new adventure begins automatically
- You start as Kevin in a mysterious world ready to be explored

### Available Commands
- `move [location]` - Travel to a new location
- `look` - Examine your current surroundings
- `inventory` - Check what items you're carrying
- `pickup [item]` - Pick up an item from your location
- `drop [item]` - Drop an item from your inventory
- `use [item]` - Use an item from your inventory
- `examine [item]` - Get detailed information about an item
- `status` - Check your current health and status
- `interact` - Interact with your current location
- `help` - Display all available commands
- `quit` - Save your progress and exit the game

### Game Locations
- **Forest** - A mysterious woodland with hidden secrets
- **Village** - A peaceful settlement with friendly inhabitants
- **Mountain** - Treacherous peaks with breathtaking views

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── game/
│   ├── actions.py      # Game action handlers
│   ├── items.py        # Item definitions and management
│   ├── mythical.py     # Mythical creatures and encounters
│   ├── player.py       # Player character management
│   ├── state.py        # Game state management
│   ├── weather.py      # Weather system
│   └── world.py        # World and location management
├── locations/
│   ├── forest.py       # Forest location logic
│   ├── mountain.py     # Mountain location logic
│   └── village.py      # Village location logic
├── utils/
│   ├── random_events.py    # Random event system
│   ├── save_load.py        # Save/load functionality
│   └── text_formatting.py # Text display utilities
└── main.py             # Main game entry point
```

## 💾 Save System

The game automatically saves your progress when you quit. Save files are stored locally and can be loaded when you restart the game. You can have multiple save files for different playthroughs.

## 🎨 Game Features

### Dynamic World
- Weather changes affect gameplay
- Random events keep each playthrough unique
- Interactive environments with discoverable secrets

### Character Development
- Track your status and progress
- Manage inventory strategically
- Make choices that affect your journey

### Exploration
- Multiple interconnected locations
- Hidden items and secrets to discover
- Rich descriptions and atmospheric text

## 🛠️ Requirements

- Python 3.6 or higher
- No additional dependencies required - uses only Python standard library

## 🤝 Contributing

This is a test repository for demonstrating text-based game development. Feel free to explore the code and see how different game systems are implemented!

## 📝 License

This project is for educational and demonstration purposes.

---

**Last updated:** June 8, 2025  
**Repository:** [codegen-sh/Kevin-s-Adventure-Game](https://github.com/codegen-sh/Kevin-s-Adventure-Game)

*Embark on your adventure today! 🗺️✨*

