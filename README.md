🌈🌈
# Kevin's Adventure Game

A text-based adventure game with improved architecture and rich gameplay features.

**Latest Update:** Comprehensive refactoring with improved architecture, new action system, and enhanced gameplay features.

## Features

🎮 **Rich Gameplay**
- Explore multiple locations: Village, Forest, Mountain, Cave
- Dynamic weather system affecting gameplay
- Comprehensive inventory and item system
- Mythical creature encounters
- Random events and discoveries
- Save/load game functionality

🏗️ **Improved Architecture**
- Clean separation of concerns with modular design
- Command pattern for action handling
- Game Controller pattern for centralized management
- Object-oriented design principles
- Comprehensive error handling

🌟 **Enhanced User Experience**
- Intuitive command system with helpful suggestions
- Rich descriptions and atmospheric text
- Status tracking and health management
- Multiple ways to interact with the world

## Installation

1. Clone the repository:
```bash
git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
cd Kevin-s-Adventure-Game
```

2. Run the game:
```bash
python main.py
```

## How to Play

### Basic Commands
- **Movement:** `go <location>`, `enter`, `explore`
- **Items:** `inventory`, `use <item>`, `take <item>`, `drop <item>`
- **Actions:** `look`, `examine <target>`, `search`, `talk`, `shop`
- **Status:** `status`, `health`, `weather`, `forecast`
- **Game:** `save`, `help`, `quit`

### Locations
- **Village:** Safe haven with shops, NPCs, and rest areas
- **Forest:** Mysterious woodland with creatures and hidden treasures
- **Mountain:** Challenging terrain with climbing opportunities
- **Cave:** Dark depths with ancient secrets and dangers

### Tips
- Type `help` at any time to see available commands
- Rest in the village to recover health safely
- Weather affects your abilities - plan accordingly
- Search areas thoroughly to find hidden items
- Save your game regularly to preserve progress

## Architecture

The game uses a clean, modular architecture:

```
game/
├── controller.py    # Central game management
├── actions.py       # Command handling system
├── player.py        # Player state and actions
├── world.py         # World state and locations
├── items.py         # Item system and interactions
├── weather.py       # Dynamic weather system
├── mythical.py      # Mythical creature encounters
└── state.py         # World state management

locations/
├── village.py       # Village-specific interactions
├── forest.py        # Forest exploration and events
├── mountain.py      # Mountain climbing and challenges
└── cave.py          # Cave exploration and mysteries

utils/
├── save_load.py     # Game persistence
├── text_formatting.py  # Display utilities
└── random_events.py    # Random event generation
```

## Testing

Run the test suite to verify game functionality:

```bash
python test_game.py
```

## Development

The game is designed with extensibility in mind:
- Add new locations by creating modules in `locations/`
- Extend the action system by adding commands to `game/actions.py`
- Create new items and their behaviors in `game/items.py`
- Add weather effects in `game/weather.py`

## Contributing

Feel free to contribute improvements, bug fixes, or new features!

## License

This project is open source and available under the MIT License.
