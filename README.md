# Kevin's Adventure Game 🌈🌈

A text-based adventure game built in Python featuring exploration, item management, and interactive storytelling.

## 🎮 Game Features

- **Exploration**: Navigate through diverse locations including villages, forests, mountains, and mysterious caves
- **Item Management**: Collect, use, and trade various items with unique properties and effects
- **Interactive Storytelling**: Engage with NPCs, make choices, and experience random events
- **Save/Load System**: Persistent game state with multiple save slots
- **Weather System**: Dynamic weather that affects gameplay
- **Combat & Health**: Health management with healing items and dangerous encounters

## 🏗️ Architecture

The game follows a modular architecture with clear separation of concerns:

```
Kevin-s-Adventure-Game/
├── config/                 # Configuration management
│   ├── __init__.py         # Configuration loader and manager
│   ├── game_config.py      # Game settings and constants
│   ├── items.json          # Item definitions and categories
│   └── locations.json      # Location data and events
├── game/                   # Core game logic
│   ├── actions.py          # Player action handling
│   ├── items.py            # Item system and usage
│   ├── mythical.py         # Mythical creatures and magic
│   ├── player.py           # Player state management
│   ├── state.py            # Game state management
│   ├── weather.py          # Weather system
│   └── world.py            # World and location management
├── locations/              # Location-specific modules
│   ├── cave.py             # Cave exploration
│   ├── forest.py           # Forest adventures
│   ├── mountain.py         # Mountain climbing
│   └── village.py          # Village interactions
├── utils/                  # Utility modules
│   ├── random_events.py    # Random event system
│   ├── save_load.py        # Save/load functionality
│   ├── text_formatting.py  # Text display utilities
│   └── validation.py       # Input validation and error handling
└── main.py                 # Game entry point
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
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

### Basic Commands

- `move [location]` - Travel to a new location
- `look` - Examine your surroundings
- `inventory` - Check your items
- `pickup [item]` - Pick up an item
- `drop [item]` - Drop an item
- `use [item]` - Use an item from your inventory
- `examine [item]` - Get detailed item information
- `status` - Check your health and stats
- `interact` - Interact with your current location
- `help` - Show all available commands
- `quit` - Save and exit the game

### Locations

- **Village**: A safe starting area with shops, NPCs, and quests
- **Forest**: Dense woodland with wildlife, hidden paths, and foraging opportunities
- **Mountain**: Challenging terrain with climbing, herbs, and a mysterious hermit
- **Cave**: Dark underground chambers requiring torches, containing treasures and dangers

### Items & Inventory

Items fall into several categories:
- **Consumables**: Food and potions that provide healing or other effects
- **Tools**: Equipment like torches, ropes, and weapons
- **Valuables**: Gems, coins, and artifacts that can be traded
- **Quest Items**: Special items with unique magical properties

## 🛠️ Development

### Code Structure

The codebase follows modern Python practices:

- **Type Hints**: All functions include proper type annotations
- **Documentation**: Comprehensive docstrings following Python conventions
- **Error Handling**: Robust error handling with custom validation
- **Configuration Management**: Centralized settings and data management
- **Modular Design**: Clear separation between game logic, UI, and data

### Key Design Patterns

- **Command Pattern**: Action handling system for extensible player commands
- **Configuration Pattern**: Centralized configuration management
- **Module Pattern**: Clear separation of concerns across modules
- **Error Handling Pattern**: Consistent error handling throughout the codebase

### Adding New Features

#### Adding a New Location

1. Create a new file in `locations/` (e.g., `desert.py`)
2. Implement the main exploration function
3. Add location data to `config/locations.json`
4. Update `game/world.py` to include the new location

#### Adding a New Item

1. Add item description to `config/items.json`
2. Add item effects to `config/game_config.py`
3. Implement item handler in `game/items.py`
4. Add item to appropriate location inventories

#### Adding a New Command

1. Add command handler to `game/actions.py`
2. Update help text in `config/game_config.py`
3. Add any necessary validation to `utils/validation.py`

### Testing

Run basic functionality tests:

```bash
# Test game startup and basic commands
echo -e "n\nhelp\nstatus\nlook\nquit" | python main.py

# Test item system
echo -e "n\npickup bread\nuse bread\nquit" | python main.py

# Test movement
echo -e "n\nmove forest\nlook\nquit" | python main.py
```

## 📁 Save Files

Game saves are stored in the `saves/` directory as JSON files. Each save contains:
- Player state (health, inventory, gold, location)
- World state (item locations, discovered areas)
- Game progress and flags

## 🔧 Configuration

Game settings can be modified in `config/game_config.py`:

- Starting health and gold
- Item effects and prices
- Random event probabilities
- Display settings
- Game messages

## 🐛 Troubleshooting

### Common Issues

**Game won't start:**
- Ensure you're using Python 3.7+
- Check that all files are present
- Verify file permissions

**Save/Load errors:**
- Check write permissions in the game directory
- Ensure the `saves/` directory exists
- Verify save file integrity

**Input not working:**
- The game requires interactive terminal input
- Some IDEs may not support interactive input properly
- Try running from command line

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the existing code style
4. Add tests for new functionality
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Style Guidelines

- Follow PEP 8 Python style guidelines
- Include type hints for all functions
- Write comprehensive docstrings
- Add error handling for user inputs
- Keep functions focused and single-purpose

## 📜 License

This project is open source and available under the MIT License.

## 🎉 Acknowledgments

- Built as a learning project for text-based game development
- Inspired by classic adventure games and interactive fiction
- Thanks to the Python community for excellent documentation and tools

## 📈 Version History

### v2.0.0 (Current)
- Complete refactoring with modular architecture
- Added configuration management system
- Improved error handling and input validation
- Added type hints and comprehensive documentation
- Enhanced save/load system
- Expanded item and location systems

### v1.0.0 (Original)
- Basic text adventure functionality
- Simple item and location system
- Basic save/load capability

---

**Last updated**: December 2024  
**Python Version**: 3.7+  
**Platform**: Cross-platform (Windows, macOS, Linux)

