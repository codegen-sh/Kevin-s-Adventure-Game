# Kevin's Adventure Game

A text-based adventure game where you play as Kevin, exploring a world of mystery and danger.

## Overview

Kevin's Adventure Game is a simple text-based adventure game where you can:

- Explore different locations (Village, Forest, Cave, Mountain)
- Collect and use items
- Interact with characters
- Complete quests
- Discover secrets

## Game Structure

The game has been refactored to use a proper object-oriented architecture:

```
src/
├── kevin_adventure/
│   ├── core/
│   │   ├── game.py             # Main game class
│   │   └── command_processor.py # Processes player commands
│   ├── entities/
│   │   ├── player.py           # Player class
│   │   ├── item.py             # Item class
│   │   ├── item_registry.py    # Registry for item handlers
│   │   ├── world.py            # World class
│   │   └── location.py         # Location class
│   ├── locations/
│   │   ├── village.py          # Village location handler
│   │   ├── forest.py           # Forest location handler
│   │   ├── cave.py             # Cave location handler
│   │   ├── mountain.py         # Mountain location handler
│   │   └── location_registry.py # Registry for location handlers
│   ├── ui/
│   │   └── text_ui.py          # Text-based user interface
│   └── utils/
│       ├── random_events.py    # Random event generation
│       └── save_load.py        # Save/load functionality
└── main.py                     # Entry point
```

## How to Play

1. Run the game:
   ```
   python src/main.py
   ```

2. Follow the on-screen instructions to navigate the game world.

3. Use the following commands:
   - `move [location]` or `go [location]`: Move to a new location
   - `look`: Examine your surroundings
   - `inventory`: Check your inventory
   - `pickup [item]` or `take [item]`: Pick up an item
   - `drop [item]`: Drop an item from your inventory
   - `use [item]`: Use an item
   - `examine [item]`: Get a description of an item
   - `status`: Check your current status
   - `interact`: Interact with your current location
   - `help`: Show help message
   - `quit`: Save and exit the game

## Features

- **Object-Oriented Design**: Proper class structure for better organization and maintainability
- **Command Processing**: Flexible command system for player input
- **Save/Load System**: Save your progress and load it later
- **Random Events**: Encounter random events during your adventure
- **Item System**: Collect, use, and manage items
- **Location Interactions**: Each location has unique interactions
- **Quest System**: Complete quests for rewards

## Development

The game has been refactored from a procedural style to an object-oriented architecture to improve:

- Code organization and readability
- Maintainability and extensibility
- Separation of concerns
- Error handling

## Future Enhancements

- Combat system
- Character progression
- More locations and quests
- Enhanced item interactions
- Graphical user interface

