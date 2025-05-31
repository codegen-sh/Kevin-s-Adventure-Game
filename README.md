# 🌈 Kevin's Adventure Game

A text-based adventure game written in Python where players explore a magical world filled with mystery, danger, and treasure. Navigate through diverse locations, collect items, interact with characters, and uncover the secrets of this enchanted realm.

## 🎮 About the Game

Kevin's Adventure Game is an immersive text-based RPG that takes you on an epic journey through various locations including villages, forests, mountains, and mysterious caves. The game features:

- **Dynamic World**: Explore multiple interconnected locations with unique characteristics
- **Inventory System**: Collect and manage items throughout your adventure
- **Player Progression**: Track your health, gold, and inventory as you progress
- **Save/Load System**: Save your progress and continue your adventure later
- **Weather System**: Experience dynamic weather that affects your journey
- **Random Events**: Encounter unexpected events that add excitement to your adventure
- **Mythical Encounters**: Meet legendary creatures and characters

## 🚀 Quick Start

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

That's it! The game will start immediately and guide you through the setup process.

## 🎯 How to Play

### Starting the Game

When you launch the game, you'll be presented with options to:
- Start a new adventure
- Load a previously saved game

### Basic Commands

The game responds to text commands. Here are the essential commands:

- `help` - Display available commands and game information
- `status` - Check your current health, inventory, and gold
- `inventory` - View items in your possession
- `look` - Examine your current location
- `go [direction]` - Move to a different location
- `take [item]` - Pick up an item
- `use [item]` - Use an item from your inventory
- `save` - Save your current progress
- `quit` - Exit the game

### Game Mechanics

- **Health**: Your life force - avoid letting it reach zero!
- **Gold**: Currency for trading and purchasing items
- **Inventory**: Stores items you collect during your adventure
- **Locations**: Each area has unique features, items, and challenges

## 🗂️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── README.md              # This documentation file
├── .gitignore            # Git ignore rules
├── game/                 # Core game logic
│   ├── items.py         # Item management and interactions
│   ├── mythical.py      # Mythical creatures and encounters
│   ├── player.py        # Player character management
│   ├── state.py         # Game state management
│   ├── weather.py       # Weather system
│   └── world.py         # World and location management
├── locations/           # Location-specific modules
│   ├── forest.py       # Forest area implementation
│   ├── mountain.py     # Mountain area implementation
│   └── village.py      # Village area implementation
└── utils/              # Utility functions
    ├── random_events.py # Random event generation
    ├── save_load.py    # Save/load game functionality
    └── text_formatting.py # Text display utilities
```

### Module Descriptions

#### Core Game Modules (`game/`)

- **`items.py`**: Manages all item-related functionality including item interactions, inventory management, and item effects
- **`mythical.py`**: Handles encounters with mythical creatures and special characters
- **`player.py`**: Contains player character creation, status tracking, and basic player actions
- **`state.py`**: Manages overall game state and progression
- **`weather.py`**: Implements dynamic weather system that affects gameplay
- **`world.py`**: Controls world navigation and location management

#### Location Modules (`locations/`)

- **`forest.py`**: Implements the forest location with its unique features and challenges
- **`mountain.py`**: Handles mountain area exploration and mountain-specific events
- **`village.py`**: Manages village interactions, NPCs, and trading

#### Utility Modules (`utils/`)

- **`random_events.py`**: Generates random events to enhance gameplay variety
- **`save_load.py`**: Provides save and load functionality for game persistence
- **`text_formatting.py`**: Handles text display, formatting, and user interface elements

## 💾 Save System

The game includes a robust save/load system:

- **Automatic Save Directory**: Saves are stored in a `saves/` directory (automatically created)
- **Multiple Save Slots**: Save multiple game states with different names
- **Complete State Preservation**: All player progress, inventory, and location data is preserved

### Save File Location

Save files are stored in the `saves/` directory in the game folder. This directory is automatically created when you first save a game.

## 🛠️ Development

### Code Style

The project follows Python best practices:
- Clear, descriptive function and variable names
- Modular design with separation of concerns
- Comprehensive docstrings for major functions
- Consistent code formatting

### Adding New Features

To extend the game:

1. **New Locations**: Add new location modules in the `locations/` directory
2. **New Items**: Extend the item system in `game/items.py`
3. **New Events**: Add random events in `utils/random_events.py`
4. **New Mechanics**: Create new modules in the appropriate directory

### Testing Your Changes

1. Run the game with `python main.py`
2. Test all new features thoroughly
3. Verify save/load functionality works with new features
4. Ensure existing functionality remains intact

## 🤝 Contributing

We welcome contributions to Kevin's Adventure Game! Here's how you can help:

### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/Kevin-s-Adventure-Game.git
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Making Changes

1. **Follow the existing code style** and structure
2. **Test your changes** thoroughly
3. **Add comments** for complex logic
4. **Update documentation** if needed

### Submitting Changes

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```
2. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
3. **Create a Pull Request** on GitHub

### Contribution Guidelines

- **Bug Reports**: Use GitHub Issues to report bugs with detailed descriptions
- **Feature Requests**: Propose new features through GitHub Issues
- **Code Quality**: Ensure your code is clean, commented, and follows Python conventions
- **Testing**: Test all changes thoroughly before submitting

## 📋 System Requirements

- **Python Version**: 3.6 or higher
- **Operating System**: Cross-platform (Windows, macOS, Linux)
- **Dependencies**: None (uses only Python standard library)
- **Storage**: Minimal disk space required (< 1MB for game files)

## 🐛 Troubleshooting

### Common Issues

**Game won't start:**
- Ensure Python 3.6+ is installed: `python --version`
- Check that you're in the correct directory
- Verify all game files are present

**Save/Load issues:**
- Ensure the `saves/` directory has write permissions
- Check available disk space
- Verify save file isn't corrupted

**Import errors:**
- Ensure all Python files are in their correct directories
- Check that no files are missing from the repository

### Getting Help

If you encounter issues:
1. Check the troubleshooting section above
2. Review the [GitHub Issues](https://github.com/codegen-sh/Kevin-s-Adventure-Game/issues) page
3. Create a new issue with detailed information about your problem

## 📝 License

This project is open source. Please check the repository for license information.

## 🎉 Acknowledgments

- Created as a demonstration of text-based game development in Python
- Inspired by classic adventure games and interactive fiction
- Built with modularity and extensibility in mind

---

**Last Updated**: May 31, 2025  
**Version**: 1.0  
**Compatibility**: Python 3.6+

Ready to begin your adventure? Run `python main.py` and let the journey begin! 🚀

