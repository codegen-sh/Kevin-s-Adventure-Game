🌈🌈🌈🎮
# Kevin's Adventure Game

A text-based adventure game built with Python, featuring an object-oriented architecture with classes for Player, World, and Location management.

Last updated: July 15, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Features

- **Object-Oriented Design**: Clean class-based architecture for Player, World, and Location entities
- **Rich Command System**: Comprehensive action system with natural language commands
- **Save/Load System**: Persistent game state with backward compatibility
- **Multiple Locations**: Explore Village, Forest, Cave, and Mountain locations
- **Inventory Management**: Collect and use items throughout your adventure
- **Interactive Gameplay**: Dynamic events and location-specific interactions

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

## Usage

### Basic Commands

- **Movement**: `go <location>`, `move <location>`, `travel <location>`
- **Inventory**: `inventory`, `take <item>`, `drop <item>`, `use <item>`
- **Exploration**: `look`, `examine <object>`, `interact`
- **Information**: `status`, `help`, `locations`
- **Game Control**: `quit` (saves automatically)

### Example Gameplay

```
You are in the Village.
Health: 100/100 | Inventory: [] | Gold: 100

What would you like to do? help

=== AVAILABLE COMMANDS ===
Movement:
  go <location>     - Move to a location
  locations         - Show available locations

Inventory:
  inventory         - Show your inventory
  take <item>       - Take an item
  drop <item>       - Drop an item
  use <item>        - Use an item
...

What would you like to do? go forest
You moved to: Forest

A dense, mysterious forest with towering trees and the sound of rustling leaves.
```

## Architecture

### Core Classes

- **Player**: Manages player state, inventory, health, and gold
- **World**: Contains all locations and handles world state
- **Location**: Represents individual game locations with items and connections

### Directory Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Game entry point
├── game/                   # Core game logic
│   ├── actions.py         # Command processing
│   ├── player.py          # Player class and management
│   ├── world.py           # World and location management
│   ├── location.py        # Location class
│   ├── exceptions.py      # Custom game exceptions
│   ├── items.py           # Item definitions
│   ├── mythical.py        # Mythical creature interactions
│   ├── state.py           # Game state management
│   └── weather.py         # Weather system
├── locations/             # Location-specific interactions
│   ├── village.py         # Village interactions
│   ├── forest.py          # Forest interactions
│   ├── mountain.py        # Mountain interactions
│   └── cave.py            # Cave interactions
├── utils/                 # Utility functions
│   ├── save_load.py       # Save/load system
│   ├── text_formatting.py # Text display utilities
│   └── random_events.py   # Random event generation
└── saves/                 # Save game files (created automatically)
```

## Development

### Adding New Locations

1. Create a new location file in `locations/`
2. Add the location to the World class in `game/world.py`
3. Update the interaction handler in `World.interact_with_location()`

### Adding New Items

1. Define item properties in `game/items.py`
2. Add usage logic in `game/actions.py` in the `handle_use_item()` function
3. Place items in locations via the Location class

### Error Handling

The game uses custom exceptions defined in `game/exceptions.py`:
- `GameError`: Base exception for all game errors
- `PlayerError`: Player-related errors
- `LocationError`: Location-related errors
- `SaveLoadError`: Save/load operation errors

## Save System

The game automatically saves when you quit and supports loading previous saves. Save files are stored in JSON format in the `saves/` directory with backward compatibility for older save formats.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes following the existing architecture
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.
