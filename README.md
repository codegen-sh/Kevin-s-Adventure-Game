# Kevin's Adventure Game

A text-based adventure game where you explore a world of mystery and danger as you navigate through forests, caves, villages, and mountains.

## Game Overview

In Kevin's Adventure Game, you play as a character named Kevin (or a name of your choice) who explores various locations, collects items, interacts with the environment, and encounters random events. The game features:

- Multiple locations to explore (Village, Forest, Cave, Mountain)
- Inventory management
- Health and gold systems
- Random events and encounters
- Save/load functionality

## How to Play

1. Run the game:
   ```
   python main.py
   ```

2. Choose to load a saved game or start a new one.

3. Enter commands to interact with the game world. Type `help` at any time to see available commands.

### Available Commands

- `move [location]`: Move to a new location
- `look`: Examine your surroundings
- `inventory`: Check your inventory
- `pickup [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message
- `quit`: Save and exit the game

## Game Structure

The game is organized into several modules:

- `main.py`: Entry point for the game
- `game/`: Core game mechanics
  - `actions.py`: Handles player actions
  - `config.py`: Game configuration
  - `engine.py`: Main game engine
  - `items.py`: Item definitions
  - `mythical.py`: Mythical creature encounters
  - `player.py`: Player management
  - `state.py`: Game state tracking
  - `weather.py`: Weather system
  - `world.py`: World and location management
- `locations/`: Location-specific interactions
  - `base.py`: Base location class
  - `cave.py`: Cave location
  - `forest.py`: Forest location
  - `mountain.py`: Mountain location
  - `village.py`: Village location
- `utils/`: Utility functions
  - `random_events.py`: Random event generation
  - `save_load.py`: Save/load functionality
  - `text_formatting.py`: Text formatting utilities

## Extending the Game

### Adding New Locations

To add a new location:

1. Create a new file in the `locations/` directory (e.g., `locations/beach.py`)
2. Create a new location class that inherits from `BaseLocation`
3. Implement the location's interactions
4. Add the location to the world initialization in `game/world.py`

### Adding New Items

To add new items:

1. Add the item to the `ITEMS` dictionary in `game/config.py`
2. Implement any special item behavior in `game/actions.py` (in the `handle_use` function)

### Adding New Random Events

To add new random events:

1. Add the event to the appropriate location or to `utils/random_events.py`
2. Implement the event's effects

## License

This project is open source and available under the MIT License.

