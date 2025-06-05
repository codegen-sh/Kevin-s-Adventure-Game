🌈🌈
# Kevin's Adventure Game

A text-based adventure game built with Python, featuring an improved modular architecture for better maintainability and extensibility.

## 🎮 Features

- **Immersive Text-Based Adventure**: Explore different locations including forests, villages, and mountains
- **Rich Item System**: Collect, use, and trade various items with unique effects
- **Dynamic Events**: Random encounters, weather changes, and special discoveries
- **Save/Load System**: Save your progress and continue your adventure later
- **Modular Architecture**: Clean, maintainable code structure with proper separation of concerns
- **Type Safety**: Full type hints for better code quality and IDE support
- **Comprehensive Testing**: Unit tests ensure reliability and stability

## 🏗️ Architecture

The game follows a clean, modular architecture:

```
├── game/                   # Core game logic
│   ├── actions.py         # Action handling system
│   ├── constants.py       # Game constants and configuration
│   ├── engine.py          # Central game engine
│   ├── exceptions.py      # Custom exception classes
│   ├── item_handlers.py   # Item system using Strategy pattern
│   ├── items.py           # Item management
│   ├── player.py          # Player state and operations
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific logic
│   ├── forest.py          # Forest location
│   ├── mountain.py        # Mountain location
│   └── village.py         # Village location
├── ui/                    # User interface layer
│   ├── display.py         # Display and formatting
│   └── input_handler.py   # Input processing and validation
├── utils/                 # Utility modules
│   ├── random_events.py   # Random event system
│   ├── save_load.py       # Save/load functionality
│   └── text_formatting.py # Legacy text formatting (deprecated)
├── tests/                 # Unit tests
└── main.py               # Main entry point
```

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. **Ensure you have Python 3.7+ installed:**
   ```bash
   python --version
   ```

3. **Run the game:**
   ```bash
   python main.py
   ```

## 🎯 How to Play

### Basic Commands

- **Movement**: `go village`, `move forest`, `travel mountain`
- **Inventory**: `inventory`, `use bread`, `take map`, `drop stick`
- **Exploration**: `look`, `examine sword`, `explore`, `search`
- **Interaction**: `interact`, `talk`
- **Status**: `status`, `health`, `location`
- **Game**: `save`, `help`, `quit`

### Game Mechanics

1. **Health System**: Monitor your health and use healing items when needed
2. **Inventory Management**: Collect and use items strategically
3. **Location Exploration**: Each location offers unique items and events
4. **Random Events**: Encounter travelers, find treasure, or face challenges
5. **Weather Effects**: Weather changes can affect your adventure

### Tips for New Players

- Start by typing `help` to see all available commands
- Explore thoroughly - each location has hidden secrets
- Manage your inventory wisely - some items are consumable
- Save your game regularly to preserve progress
- Experiment with different item combinations

## 🛠️ Development

### Running Tests

```bash
python -m pytest tests/
```

Or run individual test files:

```bash
python -m unittest tests.test_player
```

### Code Quality

The codebase follows Python best practices:

- **Type Hints**: All functions include proper type annotations
- **Documentation**: Comprehensive docstrings and comments
- **Error Handling**: Custom exceptions for different error types
- **Separation of Concerns**: Clear boundaries between game logic, UI, and data
- **Extensibility**: Easy to add new items, locations, and features

### Adding New Features

#### Adding a New Item

1. Add the item to `game/constants.py`
2. Create a handler in `game/item_handlers.py`
3. Register the handler in the `ItemHandlerRegistry`

#### Adding a New Location

1. Create a new file in `locations/`
2. Add location constants to `game/constants.py`
3. Update world initialization in `game/world.py`
4. Add location-specific logic to `game/actions.py`

## 📋 System Requirements

- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimal requirements (< 50MB)
- **Storage**: < 10MB for game files and saves

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure you're running from the project root directory
2. **Save File Issues**: Check that the `saves/` directory exists and is writable
3. **Display Issues**: Some terminals may not support all Unicode characters

### Getting Help

- Check the in-game `help` command for available actions
- Review the game logs in `game.log` for error details
- Ensure all dependencies are properly installed

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Add tests** for new functionality
4. **Ensure all tests pass**: `python -m pytest`
5. **Follow the existing code style** and type hints
6. **Submit a pull request** with a clear description

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/Kevin-s-Adventure-Game.git
cd Kevin-s-Adventure-Game

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run tests to ensure everything works
python -m pytest tests/
```

## 📜 License

This project is open source and available under the MIT License.

## 🎉 Acknowledgments

- Built with ❤️ for adventure game enthusiasts
- Inspired by classic text-based adventure games
- Thanks to all contributors and testers

---

**Last updated**: December 2024  
**Version**: 2.0.0 (Refactored)  
**Python Version**: 3.7+

Happy adventuring! 🗺️⚔️✨

