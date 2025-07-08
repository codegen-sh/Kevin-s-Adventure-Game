# 🎮 Kevin's Adventure Game

A sophisticated text-based adventure game featuring dynamic weather, mythical creatures, item management, and persistent save/load functionality.

## ✨ Features

- **🌦️ Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **🐉 Mythical Creatures**: Encounter and interact with various mythical beings
- **🎒 Item Management**: Collect, use, and manage items throughout your adventure
- **💾 Save/Load System**: Save your progress and continue your adventure anytime
- **🎲 Random Events**: Experience unexpected events that add excitement to your journey
- **🗺️ Multiple Locations**: Explore different areas in Kevin's world
- **📖 Interactive Storytelling**: Make choices that shape your adventure

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

1. **Starting the Game**: When you first run the game, you'll be asked if you want to load a saved game or start fresh
2. **Game Commands**: 
   - Type your actions in natural language
   - Use `help` to see available commands
   - Use `quit` to save and exit the game
3. **Save System**: Your progress is automatically saved when you quit
4. **Exploration**: Move between different locations and interact with the environment

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py              # Main game loop and entry point
├── game/                # Core game mechanics
│   ├── actions.py       # Action handling system
│   ├── items.py         # Item management and definitions
│   ├── mythical.py      # Mythical creature interactions
│   ├── player.py        # Player character management
│   ├── state.py         # Game state management
│   ├── weather.py       # Dynamic weather system
│   └── world.py         # World and location management
├── locations/           # Location definitions and descriptions
├── utils/               # Utility functions
│   ├── random_events.py # Random event system
│   ├── save_load.py     # Save/load functionality
│   └── text_formatting.py # Text display and formatting
└── README.md           # This file
```

## 🎮 Game Mechanics

- **Weather Effects**: Different weather conditions create unique gameplay scenarios
- **Creature Encounters**: Meet various mythical beings with different behaviors
- **Item System**: Find, collect, and use items strategically
- **Location-Based Gameplay**: Each location offers unique opportunities and challenges
- **Persistent Progress**: Your choices and progress are saved between sessions

## 🤝 Contributing

This is a test repository for exploring text-based adventure game mechanics. Feel free to explore the code and suggest improvements!

## 📝 Requirements

- Python 3.6 or higher
- No additional dependencies required

---

*Last updated: January 2025*  
*A Codegen project for exploring interactive storytelling*

