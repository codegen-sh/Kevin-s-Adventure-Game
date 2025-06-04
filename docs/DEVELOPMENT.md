# Development Guide

## Architecture Overview

Kevin's Adventure Game follows a modular architecture designed for maintainability and extensibility.

### Core Principles

1. **Separation of Concerns**: Each module has a specific responsibility
2. **Configuration-Driven**: Game data is externalized to JSON files
3. **Type Safety**: All functions include type hints
4. **Error Resilience**: Comprehensive error handling throughout
5. **Extensibility**: Easy to add new features without breaking existing code

### Module Responsibilities

#### `config/`
- **Purpose**: Centralized configuration management
- **Key Files**:
  - `game_config.py`: Game constants and settings
  - `items.json`: Item definitions and metadata
  - `locations.json`: Location data and events
  - `__init__.py`: Configuration loader and manager

#### `game/`
- **Purpose**: Core game logic and state management
- **Key Files**:
  - `actions.py`: Command processing and action handling
  - `items.py`: Item system and usage mechanics
  - `player.py`: Player state and operations
  - `world.py`: World state and location management

#### `locations/`
- **Purpose**: Location-specific gameplay mechanics
- **Pattern**: Each location has its own module with exploration functions

#### `utils/`
- **Purpose**: Shared utilities and helper functions
- **Key Files**:
  - `validation.py`: Input validation and error handling
  - `save_load.py`: Game persistence
  - `text_formatting.py`: Display utilities
  - `random_events.py`: Random event system

## Adding New Features

### Adding a New Location

1. **Create the location module**:
   ```python
   # locations/desert.py
   def explore_desert(player, world):
       """Main exploration function for the desert."""
       print("You find yourself in a vast, sandy desert...")
       # Implementation here
   ```

2. **Add location data**:
   ```json
   // config/locations.json
   "Desert": {
     "description": "A vast expanse of golden sand dunes.",
     "items": ["cactus_fruit", "sand_dollar"],
     "connections": ["Village", "Oasis"],
     "features": ["mirages", "sandstorms", "ancient_ruins"]
   }
   ```

3. **Update world connections**:
   ```python
   # game/world.py - add to location connections
   ```

### Adding a New Item

1. **Define item properties**:
   ```json
   // config/items.json
   "magic_lamp": "An ancient brass lamp with mysterious engravings."
   ```

2. **Add item effects**:
   ```python
   # config/game_config.py
   ITEM_EFFECTS = {
       "magic_lamp": {"special": "grant_wish", "consumable": False}
   }
   ```

3. **Implement item handler**:
   ```python
   # game/items.py
   def _use_magic_lamp(player, world):
       """Use magic lamp to grant a wish."""
       print("You rub the lamp and a genie appears!")
       # Implementation here
   ```

### Adding a New Command

1. **Add command handler**:
   ```python
   # game/actions.py
   def handle_cast_spell(player, world, args):
       """Handle spell casting command."""
       if not args:
           print("Cast which spell?")
           return
       # Implementation here
   ```

2. **Register command**:
   ```python
   # game/actions.py - add to COMMAND_HANDLERS
   "cast": handle_cast_spell,
   ```

3. **Update help text**:
   ```python
   # config/game_config.py
   HELP_TEXT += "\n- cast [spell]: Cast a magical spell"
   ```

## Code Style Guidelines

### Type Hints

All functions must include proper type hints:

```python
def process_action(player: Dict[str, Any], action: str) -> bool:
    """Process a player action."""
    pass
```

### Documentation

Use comprehensive docstrings:

```python
def heal_player(player: Dict[str, Any], amount: int) -> None:
    """
    Heal the player by a specified amount.
    
    Args:
        player (Dict[str, Any]): Player state dictionary
        amount (int): Amount of health to restore
        
    Raises:
        ValueError: If amount is negative
    """
    pass
```

### Error Handling

Use proper error handling patterns:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    return default_value
```

### Configuration Usage

Access configuration through the config manager:

```python
from config import config, GAME_SETTINGS

# Get item description
description = config.get_item_description("sword")

# Get game setting
max_health = GAME_SETTINGS["max_health"]
```

## Testing Guidelines

### Manual Testing

Test basic functionality:

```bash
# Test game flow
echo -e "n\nhelp\nstatus\nlook\nquit" | python main.py

# Test item system
echo -e "n\npickup bread\nuse bread\ninventory\nquit" | python main.py

# Test movement
echo -e "n\nmove forest\nlook\nmove village\nquit" | python main.py
```

### Integration Testing

Test save/load functionality:

```bash
# Create a save
echo -e "n\npickup bread\nmove forest\nquit" | python main.py

# Load the save
echo -e "y\n1\nstatus\nquit" | python main.py
```

## Performance Considerations

### Memory Management

- Use `copy()` for list/dict defaults to prevent shared state
- Clear large data structures when no longer needed
- Avoid circular references in game state

### File I/O

- Use context managers for file operations
- Handle file errors gracefully
- Consider file locking for concurrent access

### Configuration Loading

- Cache configuration data after first load
- Use lazy loading for large datasets
- Validate configuration on startup

## Debugging Tips

### Common Issues

1. **Import Errors**: Check module paths and circular imports
2. **Configuration Errors**: Validate JSON syntax and required fields
3. **State Corruption**: Ensure proper state management in save/load
4. **Input Validation**: Test edge cases and invalid inputs

### Debugging Tools

```python
# Add debug prints
print(f"DEBUG: Player state: {player}")

# Use pdb for interactive debugging
import pdb; pdb.set_trace()

# Log important events
import logging
logging.info(f"Player moved to {location}")
```

## Release Process

1. **Code Review**: Ensure all changes follow guidelines
2. **Testing**: Run comprehensive manual tests
3. **Documentation**: Update README and docs as needed
4. **Version Bump**: Update version in README
5. **Changelog**: Document changes and new features

## Future Enhancements

### Planned Features

- **Combat System**: Turn-based combat with enemies
- **Quest System**: Structured quests with objectives
- **Character Classes**: Different player types with unique abilities
- **Multiplayer**: Basic multiplayer support
- **GUI Interface**: Optional graphical interface

### Technical Improvements

- **Unit Tests**: Comprehensive test suite
- **Logging System**: Structured logging throughout
- **Plugin System**: Support for game modifications
- **Performance Optimization**: Profiling and optimization
- **Database Backend**: Optional database for game state

