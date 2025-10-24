# Kevin's Adventure Game - Class-Based Architecture

This document describes the new class-based architecture implemented for Kevin's Adventure Game, which provides better code organization, type safety, and extensibility while maintaining backward compatibility.

## Overview

The game has been refactored from a function-based approach to a proper object-oriented architecture with the following core components:

- **Player Class**: Encapsulates player data and behavior
- **World Class**: Manages game state and locations
- **GameEngine Class**: Handles the main game loop and command processing
- **BaseLocation Abstract Class**: Provides consistent interface for all locations

## Core Classes

### Player Class (`game/player_class.py`)

The `Player` class encapsulates all player-related data and methods:

```python
class Player:
    def __init__(self, name: str, health: int = 100, max_health: int = 100, 
                 location: str = "Village", gold: int = 100) -> None
```

**Key Features:**
- Type hints throughout
- Data validation in constructors and methods
- Property-based access to computed values (`is_alive`, `is_at_max_health`)
- Comprehensive inventory management
- Health and gold management with bounds checking
- Serialization support (`to_dict()`, `from_dict()`)

**Key Methods:**
- `add_item(item: str)` - Add item to inventory
- `remove_item(item: str)` - Remove item from inventory
- `heal(amount: int)` - Heal player with validation
- `take_damage(amount: int)` - Apply damage with bounds checking
- `move_to(location: str)` - Move to new location
- `get_status()` - Get formatted status string

### World Class (`game/world_class.py`)

The `World` class manages the game world state and locations:

```python
class World:
    def __init__(self) -> None
```

**Key Features:**
- Location management with BaseLocation objects
- Weather and time systems
- Global state tracking
- Event system for world state changes
- Serialization support

**Key Methods:**
- `add_location(location: BaseLocation)` - Add location to world
- `change_location(new_location: str, player: Player)` - Handle location changes
- `get_available_locations()` - Get accessible locations
- `update_world_state(event: str, data: Any)` - Handle world events
- `interact_with_current_location(player: Player)` - Trigger location interactions

### GameEngine Class (`game/game_engine.py`)

The `GameEngine` class coordinates all game systems and handles the main game loop:

```python
class GameEngine:
    def __init__(self, player: Optional[Player] = None, world: Optional[World] = None) -> None
```

**Key Features:**
- Command system with extensible command handlers
- Save/load game functionality
- Debug mode support
- Error handling and recovery
- Backward compatibility with function-based approach

**Key Methods:**
- `start_game()` - Start the main game loop
- `_process_command(action: str)` - Process player commands
- Command handlers for all game actions (`_handle_go`, `_handle_take`, etc.)

### BaseLocation Abstract Class (`game/base_location.py`)

The `BaseLocation` class provides a consistent interface for all game locations:

```python
class BaseLocation(ABC):
    def __init__(self, location_data: LocationData) -> None
```

**Key Features:**
- Abstract methods that must be implemented by subclasses
- Common location functionality (items, connections, properties)
- Type-safe location data management
- Extensible special properties system

**Abstract Methods:**
- `enter(player: Player, world: World)` - Handle player entering location
- `get_available_actions(player: Player, world: World)` - Get available actions
- `perform_action(action: str, player: Player, world: World)` - Handle actions

**Concrete Methods:**
- `add_item(item: str)` - Add item to location
- `remove_item(item: str)` - Remove item from location
- `get_full_description()` - Get complete location description

## Location Implementation Example

Here's how to create a new location using the class-based architecture:

```python
from game.base_location import BaseLocation, LocationData

class MyLocation(BaseLocation):
    def __init__(self):
        location_data = LocationData(
            name="My Location",
            description="A custom location for the game.",
            connections=["Village"],
            items=["special_item"]
        )
        super().__init__(location_data)
    
    def enter(self, player: Player, world: World) -> None:
        print(f"Welcome to {self.name}!")
        if not self.visited:
            print("This is your first time here.")
            self.mark_visited()
    
    def get_available_actions(self, player: Player, world: World) -> List[str]:
        return ["look", "take", "special_action"]
    
    def perform_action(self, action: str, player: Player, world: World) -> bool:
        if action == "special_action":
            print("You perform a special action!")
            return True
        return super().perform_action(action, player, world)
```

## Backward Compatibility

The new architecture maintains full backward compatibility with the existing function-based code:

### Compatibility Functions

Each new class provides compatibility functions that maintain the old interface:

```python
# Old way (still works)
player_data = create_player("Kevin")
world_data = initialize_world()
perform_action(player_data, world_data, "look")

# New way (recommended)
player = Player("Kevin")
world = World()
engine = GameEngine(player, world)
engine.start_game()
```

### Migration Strategy

1. **Phase 1**: New classes implemented alongside old functions
2. **Phase 2**: Old functions redirect to new classes internally
3. **Phase 3**: Gradual migration of calling code to use new classes
4. **Phase 4**: Optional removal of compatibility functions

## Type Safety

The new architecture includes comprehensive type hints:

```python
from typing import List, Dict, Any, Optional

def change_location(self, new_location: str, player: Player) -> bool:
    """
    Change the current location.
    
    Args:
        new_location: Name of the new location
        player: The player object
        
    Returns:
        True if location change was successful, False otherwise
    """
```

## Error Handling

Robust error handling and validation throughout:

```python
def add_item(self, item: str) -> bool:
    if not isinstance(item, str) or not item.strip():
        raise ValueError("Item must be a non-empty string")
    
    self.inventory.append(item.strip())
    print(f"You picked up: {item}")
    return True
```

## Testing

The class-based architecture is designed to be easily testable:

```python
def test_player_health():
    player = Player("Test")
    assert player.health == 100
    
    player.take_damage(30)
    assert player.health == 70
    
    player.heal(20)
    assert player.health == 90
```

## Benefits

### Code Organization
- Clear separation of concerns
- Logical grouping of related functionality
- Easier to navigate and understand

### Type Safety
- Comprehensive type hints
- Better IDE support and error detection
- Reduced runtime errors

### Extensibility
- Easy to add new locations, items, and features
- Plugin-like architecture for locations
- Event system for game state changes

### Maintainability
- Encapsulated data and behavior
- Consistent interfaces
- Better error handling and validation

### Testing
- Isolated components for unit testing
- Mockable dependencies
- Predictable behavior

## Usage Examples

### Creating a Custom Game

```python
from game.player_class import Player
from game.world_class import World
from game.game_engine import GameEngine

# Create custom player
player = Player("Hero", health=150, gold=200)
player.add_item("magic_sword")

# Create custom world
world = World()
# Add custom locations...

# Start game
engine = GameEngine(player, world)
engine.start_game()
```

### Adding Custom Commands

```python
class CustomGameEngine(GameEngine):
    def _initialize_commands(self):
        commands = super()._initialize_commands()
        commands["custom_command"] = self._handle_custom_command
        return commands
    
    def _handle_custom_command(self, args: List[str]) -> None:
        print("Custom command executed!")
```

## File Structure

```
game/
├── player_class.py      # Player class implementation
├── world_class.py       # World class implementation
├── game_engine.py       # GameEngine class implementation
├── base_location.py     # BaseLocation abstract class
├── actions.py           # Backward compatibility for actions
├── player.py            # Original player functions (compatibility)
├── world.py             # Original world functions (compatibility)
└── ...

locations/
├── village_class.py     # Example class-based village location
├── village.py           # Original village functions
└── ...

main_new.py              # New main entry point with architecture choice
main.py                  # Original main entry point (unchanged)
```

## Migration Guide

To migrate existing code to use the new architecture:

1. **Replace function calls with class methods:**
   ```python
   # Old
   player = create_player("Kevin")
   add_item_to_inventory(player, "sword")
   
   # New
   player = Player("Kevin")
   player.add_item("sword")
   ```

2. **Use GameEngine for game loop:**
   ```python
   # Old
   while True:
       action = input("What to do? ")
       perform_action(player, world, action)
   
   # New
   engine = GameEngine(player, world)
   engine.start_game()
   ```

3. **Create custom locations:**
   ```python
   # Old
   def my_location_function(world, player):
       # location logic
   
   # New
   class MyLocation(BaseLocation):
       def enter(self, player, world):
           # location logic
   ```

## Future Enhancements

The new architecture enables several future enhancements:

- **Plugin System**: Easy addition of new locations and features
- **Multiplayer Support**: Multiple Player objects in shared World
- **Advanced AI**: NPCs as Player-like objects
- **Scripting**: Location behavior defined in external scripts
- **Save System**: Rich save data with full object state
- **Modding Support**: External modules can extend base classes

## Conclusion

The new class-based architecture provides a solid foundation for the game's future development while maintaining full compatibility with existing code. It offers better organization, type safety, and extensibility, making the codebase more maintainable and easier to enhance.

