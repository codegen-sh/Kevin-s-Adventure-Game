🌈🌈🌈🎮
# Kevin's Adventure Game

![Kevin the Beet](kevin-the-beet.png)

A text-based adventure game featuring Kevin, our adorable pink and green beet mascot! This game has been completely refactored with modern Python architecture, improved error handling, and extensible design patterns.

## 🚀 Features

- **Object-Oriented Design**: Clean class-based architecture for players, locations, and game state
- **Robust Error Handling**: Comprehensive input validation and error recovery
- **Save/Load System**: Persistent game state with multiple save slots
- **Extensible Location System**: Easy to add new locations with consistent interfaces
- **Type Safety**: Full type hints for better code maintainability
- **Interactive Locations**: Rich location-specific interactions and events
- **Inventory Management**: Comprehensive item system with usage effects
- **Game Statistics**: Track your progress and achievements

## 📋 Requirements

- Python 3.7 or higher
- No external dependencies required!

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Run the game:
   ```bash
   python main.py
   ```

## 🎮 How to Play

### Basic Commands

- **Movement**: `go [location]`, `move [location]`, `travel [location]`
- **Exploration**: `look`, `examine`, `explore`, `search`
- **Inventory**: `inventory`, `inv`, `take [item]`, `drop [item]`, `use [item]`
- **Information**: `status`, `stats`, `map`, `help`
- **Game Control**: `save`, `quit`, `wait`, `rest`

### Game Locations

- **Village**: Starting location with shops and friendly NPCs
- **Forest**: Dense woodland with hidden treasures and dangers
- **Mountain**: Treacherous peaks with rare herbs and hermits
- **Cave**: Dark underground chambers with ancient secrets

### Tips for New Players

1. Start by typing `help` to see all available commands
2. Use `look` to examine your surroundings thoroughly
3. Collect items - they often have useful effects
4. Save your game regularly with the `save` command
5. Talk to NPCs and explore thoroughly for hidden content

## 🏗️ Architecture

The game follows modern software engineering principles:

### Core Components

- **`game/player.py`**: Player class with inventory and status management
- **`game/world.py`**: World state and location management
- **`game/actions.py`**: Command processing and action handling
- **`game/game_state.py`**: Centralized game state management
- **`game/game.py`**: Main game loop and coordination
- **`game/location_base.py`**: Base classes for location implementations

### Utilities

- **`utils/input_handler.py`**: Robust input validation and error handling
- **`utils/save_load.py`**: Game persistence system
- **`utils/text_formatting.py`**: Display formatting and messaging
- **`utils/random_events.py`**: Dynamic event generation

### Locations

- **`locations/village.py`**: Village-specific interactions
- **`locations/forest.py`**: Forest exploration and events
- **`locations/mountain.py`**: Mountain climbing and challenges
- **`locations/cave.py`**: Cave exploration and treasure hunting

## 🔧 Development

### Adding New Locations

1. Create a new file in the `locations/` directory
2. Implement the location-specific exploration function
3. Add the location to the world initialization in `game/world.py`
4. Update location connections as needed

### Adding New Items

1. Add item descriptions to `game/items.py`
2. Implement item usage effects in the `use_item` function
3. Place items in appropriate locations

### Extending the Game

The modular architecture makes it easy to:
- Add new player abilities or stats
- Implement combat systems
- Create quest systems
- Add multiplayer functionality
- Integrate with external APIs

## 🐛 Troubleshooting

### Common Issues

**Game won't start**: Ensure you're using Python 3.7+
```bash
python --version
```

**Save files not loading**: Check that the `saves/` directory exists and has proper permissions

**Input errors**: The game includes robust error handling, but if you encounter persistent issues, try the legacy mode:
```python
# In main.py, change the last line to:
legacy_main()
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes with proper type hints and documentation
4. Add tests if applicable
5. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions
- Add docstrings for classes and methods
- Keep functions focused and modular

## 📝 Changelog

### Version 2.0.0 (Current)
- Complete architectural refactor
- Added comprehensive error handling
- Implemented type safety
- Created extensible location system
- Added game statistics tracking
- Improved save/load functionality

### Version 1.0.0 (Legacy)
- Basic text adventure functionality
- Simple save/load system
- Core locations and items

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Kevin the Beet mascot design
- Community feedback and testing
- Open source Python community

---

**Last updated**: September 25, 2025  
**Python Version**: 3.7+  
**Status**: Active Development
