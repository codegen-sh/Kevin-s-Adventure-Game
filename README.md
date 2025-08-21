# Kevin's Adventure Game

A text-based adventure game where you explore a world of mystery and danger as you navigate through forests, caves, villages, and mountains.

## Game Overview

In Kevin's Adventure Game, you play as Kevin, an adventurer exploring a fantasy world. You can:

- Explore different locations (Village, Forest, Cave, Mountain)
- Collect and use items
- Interact with the environment
- Complete quests
- Encounter mythical creatures
- Experience different weather conditions

## How to Play

1. Run the game:
   ```
   python main.py
   ```

2. Choose to load a saved game or start a new one.

3. Use text commands to navigate and interact with the world:

### Basic Commands

- `move [location]` or `go [location]`: Move to a new location
- `look`: Examine your surroundings
- `inventory` or `inv`: Check your inventory
- `pickup [item]` or `take [item]` or `get [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]` or `inspect [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message
- `quit`: Save and exit the game

## Game Mechanics

### Locations

- **Village**: A peaceful starting location with shops and villagers
- **Forest**: A mysterious forest with wildlife and hidden paths
- **Cave**: A dark cave with minerals and potential treasures
- **Mountain**: A challenging mountain with a hermit and great views

### Items

The game features various items you can collect and use:

- Food items (bread, berries, mushrooms)
- Tools (torch, rope, pickaxe)
- Valuable items (gemstone, ancient coin)
- Magical items (mythical creature artifacts)

### Weather System

The game includes a dynamic weather system that affects gameplay:

- Clear: No effects
- Cloudy: Slight visibility reduction
- Rainy: Reduced agility
- Stormy: Reduced agility and perception
- Foggy: Significantly reduced perception
- Windy: Slightly reduced agility

### Health System

- Your health ranges from 0 to 100
- You can heal by eating food, resting, or using healing items
- You can take damage from various hazards
- If your health reaches 0, you are defeated

### Save/Load System

- The game automatically saves when you quit
- You can load a saved game when starting the game
- Save files are stored in the `saves` directory

## Developer Documentation

### Code Structure

The game is organized into several modules:

- `main.py`: Main game loop and entry point
- `game/`: Core game mechanics
  - `actions.py`: Player action handling
  - `items.py`: Item definitions and functionality
  - `mythical.py`: Mythical creature system
  - `player.py`: Player state and actions
  - `state.py`: World state management
  - `weather.py`: Weather system
  - `world.py`: World structure and navigation
- `locations/`: Location-specific interactions
  - `cave.py`: Cave location
  - `forest.py`: Forest location
  - `mountain.py`: Mountain location
  - `village.py`: Village location
- `utils/`: Utility functions
  - `random_events.py`: Random event generation
  - `save_load.py`: Save/load functionality
  - `text_formatting.py`: Text formatting utilities

### Class Structure

The game uses both object-oriented and functional approaches:

- `Player`: Represents the player character
- `World`: Represents the game world

Legacy dictionary-based functions are maintained for backward compatibility.

### Adding New Features

#### Adding a New Location

1. Create a new file in the `locations/` directory
2. Implement the location's interaction function
3. Add the location to the `World` class in `world.py`
4. Add connections to existing locations

#### Adding a New Item

1. Add the item to the `get_item_description` function in `items.py`
2. Implement the item's functionality in the `use_item` function
3. Add the item to a location in the world

#### Adding a New Command

1. Add a new handler function in `actions.py`
2. Add the command to the `perform_action` function

### Save File Format

Save files are JSON files with the following structure:

```json
{
  "version": 2,
  "timestamp": "2023-01-01T12:00:00",
  "player": {
    "name": "Kevin",
    "health": 100,
    "inventory": ["map", "bread"],
    "location": "Village",
    "gold": 100,
    "stats": {
      "strength": 10,
      "agility": 10,
      "perception": 10
    }
  },
  "world": {
    "current_location": "Village",
    "locations": {
      "Village": {
        "description": "A small, peaceful village...",
        "connections": ["Forest", "Mountain"],
        "items": ["map", "bread"]
      },
      // Other locations...
    },
    "weather": "clear",
    "state": {
      "discovered_locations": [],
      "active_quests": [],
      "completed_quests": [],
      "time_of_day": "day",
      "days_passed": 0,
      "special_discoveries": []
    }
  }
}
```

## Future Enhancements

- Combat system
- More locations to explore
- More quests and storylines
- Character progression and skills
- More mythical creatures
- Day/night cycle effects
- Crafting system

## License

This project is open source and available under the MIT License.

