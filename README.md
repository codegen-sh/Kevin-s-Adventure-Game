# 🌈 Kevin's Adventure Game

A text-based adventure game where players embark on an epic journey as Kevin, exploring mystical locations, encountering mythical creatures, and collecting items in a dynamic world.

## 🎮 Features

- **Dynamic World**: Explore multiple locations including villages, forests, and mountains
- **Weather System**: Experience changing weather conditions that affect gameplay
- **Mythical Creatures**: Encounter and interact with various mythical beings
- **Inventory Management**: Collect and manage items throughout your adventure
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected events that add excitement to your journey
- **Interactive Gameplay**: Use various commands to navigate and interact with the world

## 🗂️ Project Structure

```
Kevin-s-Adventure-Game/
├── game/                    # Core game mechanics
│   ├── actions.py          # Game action handlers
│   ├── items.py            # Item system and inventory
│   ├── mythical.py         # Mythical creatures and encounters
│   ├── player.py           # Player character management
│   ├── state.py            # Game state management
│   ├── weather.py          # Weather system
│   └── world.py            # World and location management
├── locations/              # Location-specific modules
│   ├── forest.py           # Forest location
│   ├── mountain.py         # Mountain location
│   └── village.py          # Village location
├── utils/                  # Utility functions
│   ├── random_events.py    # Random event system
│   ├── save_load.py        # Save/load functionality
│   └── text_formatting.py # Text display utilities
└── main.py                 # Main game entry point
```

## 🚀 Installation & Setup

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
2. **Loading Saves**: Choose to load a previous save file or start a new game
3. **Commands**: Type `help` at any time to see available commands
4. **Navigation**: Move between locations and interact with the environment
5. **Inventory**: Collect items and manage your inventory
6. **Saving**: Save your progress at any time to continue later

## 🎲 Game Commands

- `help` - Display available commands
- `status` - Check your current status
- `inventory` - View your items
- `save` - Save your current progress
- `quit` - Exit the game

## 🌟 Game Elements

- **Locations**: Village, Forest, Mountain (each with unique features)
- **Weather**: Dynamic weather system affecting gameplay
- **Items**: Collectible items with various properties
- **Mythical Creatures**: Encounter legendary beings
- **Random Events**: Unexpected occurrences during your journey

## 🛠️ Technical Details

- **Language**: Python 3.x
- **Architecture**: Modular design with separate components for game logic
- **Save System**: JSON-based save/load functionality
- **Text Interface**: Rich text formatting for enhanced user experience

## 🤝 Contributing

This is a test repository for demonstrating text-based game development. Feel free to explore the code and suggest improvements!

## 📝 License

This project is for educational and testing purposes.

---

*Last updated: May 23, 2025*  
*Environment: Linux x86_64*

