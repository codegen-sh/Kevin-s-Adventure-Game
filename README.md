# Kevin's Adventure Game

A text-based adventure game built with Python, featuring an immersive world of exploration, mystery, and discovery.

## 🎮 Game Overview

Kevin's Adventure Game is a classic text-based adventure where players explore a rich fantasy world, collect items, interact with mythical creatures, and uncover hidden secrets. The game features multiple locations, a dynamic weather system, random events, and an engaging storyline.

### Key Features

- **🗺️ Multiple Locations**: Explore villages, forests, caves, and mountains
- **🎒 Inventory System**: Collect and use various items and tools
- **🌦️ Dynamic Weather**: Weather affects gameplay and events
- **🐉 Mythical Creatures**: Encounter and interact with magical beings
- **💾 Save/Load System**: Save your progress and continue later
- **🎲 Random Events**: Dynamic events keep gameplay fresh and exciting
- **🏆 Achievement System**: Track your progress and accomplishments

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Git (for development)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. **Set up virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the game**:
   ```bash
   python main.py
   ```

## 🎯 How to Play

### Basic Commands

- **Movement**: `go [location]`, `move [location]`, or just type the location name
- **Inventory**: `inventory` or `inv` to see your items
- **Items**: `use [item]`, `take [item]`, `examine [item]`
- **Information**: `status`, `look around`, `locations`
- **Help**: `help` for command list
- **Save/Quit**: `save`, `quit`

### Game Mechanics

1. **Exploration**: Move between connected locations to discover new areas
2. **Item Collection**: Find and collect useful items throughout your journey
3. **Health Management**: Monitor your health and use healing items when needed
4. **Gold System**: Earn and spend gold on useful items and services
5. **Random Events**: Experience unique events that can help or challenge you

### Tips for New Players

- Start by exploring the Village to get familiar with the game
- Always check your status and inventory regularly
- Save your game frequently to preserve progress
- Experiment with different items to discover their effects
- Pay attention to location descriptions for hidden clues

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── game/                   # Core game logic
│   ├── actions.py         # Action processing system
│   ├── items.py           # Item definitions and usage
│   ├── mythical.py        # Mythical creature encounters
│   ├── player.py          # Player management
│   ├── state.py           # Game state management
│   ├── weather.py         # Weather system
│   └── world.py           # World and location management
├── locations/             # Location-specific modules
│   ├── cave.py           # Cave exploration
│   ├── forest.py         # Forest adventures
│   ├── mountain.py       # Mountain climbing
│   └── village.py        # Village interactions
├── utils/                 # Utility functions
│   ├── random_events.py  # Random event generation
│   ├── save_load.py      # Save/load functionality
│   └── text_formatting.py # Text display utilities
├── docs/                  # Documentation
├── scripts/               # Development scripts
├── tools/                 # Development tools
├── tests/                 # Test files
└── main.py               # Game entry point
```

## 🛠️ Development

### Setting Up Development Environment

1. **Clone and setup**:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements-dev.txt
   ```

2. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

3. **Run tests**:
   ```bash
   python -m pytest
   ```

### Development Tools

- **Code Formatting**: `./scripts/format.sh` - Format code with Black
- **Linting**: `./scripts/lint.sh` - Run flake8, mypy, and pylint
- **Testing**: `./scripts/test.sh` - Run tests with coverage
- **Content Validation**: `python tools/validate_content.py`
- **Performance Profiling**: `python tools/profile_game.py`

### Code Quality Standards

- **Style**: Follow PEP 8 with Black formatting (88 char line limit)
- **Documentation**: Google-style docstrings for all functions
- **Type Hints**: Add type hints to new code
- **Testing**: Aim for 80%+ test coverage
- **Linting**: Code must pass flake8 and mypy checks

## 📚 Documentation

Comprehensive documentation is available in the `docs/` directory:

- **[Architecture Guide](docs/architecture.md)**: System design and module structure
- **[Developer Guide](docs/developer-guide.md)**: Setup and development workflow
- **[Contributing Guide](docs/contributing.md)**: How to contribute to the project
- **[Plugin Development](docs/plugin-development.md)**: Creating game plugins
- **[Content Creation](docs/content-creation.md)**: Adding new game content
- **[Data Structures](docs/data-structures.md)**: Core data structure documentation

## 🔌 Plugin System

Kevin's Adventure Game supports a flexible plugin system for extending functionality:

### Plugin Types

- **Location Plugins**: Add new explorable areas
- **Item Plugins**: Create custom items with unique effects
- **Event Plugins**: Add new random events and encounters
- **Mechanic Plugins**: Introduce new game systems

### Creating Plugins

See the [Plugin Development Guide](docs/plugin-development.md) for detailed instructions on creating and integrating plugins.

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=game --cov=utils --cov=locations

# Run specific test file
python -m pytest tests/test_player.py
```

### Test Coverage

Current test coverage goals:
- Core modules: 80%+ coverage
- Utility functions: 90%+ coverage
- Critical paths: 100% coverage

## 🚀 Performance

### Optimization Features

- Efficient data structures for game state
- Lazy loading of location modules
- Optimized save/load operations
- Memory-conscious event handling

### Profiling Tools

Use the built-in profiling tools to analyze performance:

```bash
python tools/profile_game.py
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/contributing.md) for details.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Run quality checks: `./scripts/lint.sh && ./scripts/test.sh`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to your fork: `git push origin feature/amazing-feature`
7. Submit a pull request

### Areas for Contribution

- 🗺️ New locations and areas to explore
- 🎒 Additional items and tools
- 🎲 More random events and encounters
- 🐛 Bug fixes and performance improvements
- 📖 Documentation improvements
- 🧪 Test coverage expansion

## 📋 Roadmap

### Version 1.1 (Planned)
- [ ] Combat system with turn-based battles
- [ ] NPC dialogue system
- [ ] Quest and mission framework
- [ ] Achievement system
- [ ] Sound effects and music support

### Version 1.2 (Future)
- [ ] Multiplayer support
- [ ] Graphical user interface option
- [ ] Mobile app version
- [ ] Mod support and community content
- [ ] Localization for multiple languages

## 🐛 Known Issues

- Save files from very old versions may not be compatible
- Some random events may have low probability of occurrence
- Performance may degrade with very large inventory sizes

See [GitHub Issues](https://github.com/codegen-sh/Kevin-s-Adventure-Game/issues) for the complete list.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic text-based adventure games
- Built with Python and love for retro gaming
- Community contributors and testers
- Open source libraries and tools

## 📞 Support

- **Documentation**: Check the `docs/` directory
- **Issues**: [GitHub Issues](https://github.com/codegen-sh/Kevin-s-Adventure-Game/issues)
- **Discussions**: [GitHub Discussions](https://github.com/codegen-sh/Kevin-s-Adventure-Game/discussions)

## 🎉 Fun Facts

- The game world contains over 15 different item types
- There are more than 20 unique random events
- The codebase includes comprehensive type hints and documentation
- All game content is easily moddable through the plugin system

---

**Happy adventuring! 🗡️⚔️🏰**

