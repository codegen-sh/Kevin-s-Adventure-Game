# Data Structures Documentation

## Overview

This document describes the key data structures used throughout Kevin's Adventure Game. Understanding these structures is essential for developers working on the game or creating extensions.

## Core Data Structures

### Player Object

The player object is a dictionary that contains all player-related information:

```python
player = {
    "name": str,           # Player's name
    "health": int,         # Current health points (0-100)
    "inventory": list,     # List of item names (strings)
    "location": str,       # Current location name
    "gold": int           # Amount of gold coins
}
```

#### Example:
```python
{
    "name": "Kevin",
    "health": 85,
    "inventory": ["sword", "potion", "map"],
    "location": "Forest",
    "gold": 150
}
```

#### Validation Rules:
- `health`: Must be between 0 and 100
- `inventory`: Can contain duplicate items
- `location`: Must be a valid location name
- `gold`: Must be non-negative

### World Object

The world object contains the game world state and location definitions:

```python
world = {
    "current_location": str,    # Current location name
    "locations": dict,          # Dictionary of location data
    "state": dict              # Global world state variables
}
```

#### Location Structure:
```python
location = {
    "description": str,        # Text description of the location
    "connections": list,       # List of connected location names
    "items": list,            # List of available items
    "visited": bool,          # Whether player has visited (optional)
    "properties": dict        # Location-specific properties (optional)
}
```

#### Example:
```python
{
    "current_location": "Village",
    "locations": {
        "Village": {
            "description": "A peaceful village with friendly inhabitants.",
            "connections": ["Forest", "Mountain"],
            "items": ["map", "bread"],
            "visited": True,
            "properties": {
                "safe_zone": True,
                "has_shop": True
            }
        },
        "Forest": {
            "description": "A dense, mysterious forest.",
            "connections": ["Village", "Cave"],
            "items": ["stick", "berries"],
            "visited": False,
            "properties": {
                "danger_level": 2,
                "resource_rich": True
            }
        }
    },
    "state": {
        "day_count": 5,
        "weather": "sunny",
        "global_events": []
    }
}
```

### Item Definitions

Items are defined by their names (strings) and have associated metadata:

```python
# Item descriptions (in items.py)
item_descriptions = {
    "item_name": str,          # Description text
    # ...
}

# Item effects (various functions)
item_effects = {
    "item_name": function,     # Function to execute when used
    # ...
}
```

#### Item Categories:
1. **Consumables**: Items that are consumed when used (potions, food)
2. **Tools**: Items that provide functionality (map, torch, pickaxe)
3. **Weapons**: Items for combat (sword, stick)
4. **Treasures**: Valuable items (gemstone, gold_coin)
5. **Quest Items**: Special items for storylines (ancient_artifact)

#### Example Item Definitions:
```python
{
    "bread": "A fresh loaf of bread. Restores 20 health.",
    "map": "Shows available locations you can travel to.",
    "sword": "A sharp blade useful for combat and defense.",
    "gemstone": "A valuable sparkling gem worth good money."
}
```

### Save File Structure

Save files are JSON documents with the following structure:

```python
save_data = {
    "player": dict,           # Complete player object
    "world": dict,            # Complete world object
    "timestamp": str,         # ISO format timestamp
    "version": str,           # Game version
    "metadata": dict          # Additional save metadata
}
```

#### Example:
```python
{
    "player": {
        "name": "Kevin",
        "health": 75,
        "inventory": ["sword", "map"],
        "location": "Cave",
        "gold": 200
    },
    "world": {
        "current_location": "Cave",
        "locations": { /* ... */ },
        "state": {
            "cave_visited": True,
            "dragon_defeated": False
        }
    },
    "timestamp": "2024-06-04T21:13:28.123456",
    "version": "1.0",
    "metadata": {
        "play_time": 3600,
        "save_count": 5
    }
}
```

## Event Data Structures

### Random Events

Random events are defined as dictionaries with event data:

```python
event = {
    "type": str,              # Event type identifier
    "description": str,       # Event description text
    "effects": dict,          # Effects on player/world
    "probability": float,     # Occurrence probability (0.0-1.0)
    "conditions": dict        # Conditions for event to trigger
}
```

#### Example:
```python
{
    "type": "treasure_find",
    "description": "You discover a hidden treasure chest!",
    "effects": {
        "add_item": "gold_coin",
        "add_gold": 50
    },
    "probability": 0.15,
    "conditions": {
        "location": ["Forest", "Cave"],
        "has_item": "map"
    }
}
```

### Creature Encounters

Mythical creatures are represented as dictionaries:

```python
creature = {
    "name": str,              # Creature name
    "description": str,       # Creature description
    "health": int,            # Creature health
    "attack": int,            # Attack damage
    "defense": int,           # Defense rating
    "loot": list,            # Possible loot items
    "behavior": str          # Behavior type (friendly, hostile, neutral)
}
```

#### Example:
```python
{
    "name": "Forest Dragon",
    "description": "A majestic dragon with emerald scales.",
    "health": 200,
    "attack": 30,
    "defense": 15,
    "loot": ["dragon_scale", "gold_coin", "magic_ring"],
    "behavior": "hostile"
}
```

## Configuration Structures

### Game Configuration

Game settings and balance parameters:

```python
config = {
    "player": {
        "starting_health": 100,
        "max_health": 100,
        "starting_gold": 100,
        "starting_location": "Village"
    },
    "world": {
        "random_event_chance": 0.3,
        "weather_change_chance": 0.2,
        "creature_encounter_chance": 0.25
    },
    "items": {
        "max_inventory_size": None,  # None = unlimited
        "item_stack_limit": 1        # Items per stack
    }
}
```

### Location Templates

Templates for creating new locations:

```python
location_template = {
    "name": str,              # Location name
    "description": str,       # Location description
    "connections": list,      # Connected locations
    "items": list,           # Available items
    "events": list,          # Possible events
    "properties": {
        "danger_level": int,  # 1-5 danger rating
        "resource_type": str, # Type of resources available
        "safe_zone": bool,    # Whether it's a safe area
        "weather_affected": bool  # Whether weather affects this location
    }
}
```

## Data Validation

### Player Validation

```python
def validate_player(player):
    """Validate player object structure and values."""
    required_keys = ["name", "health", "inventory", "location", "gold"]
    
    # Check required keys exist
    for key in required_keys:
        if key not in player:
            return False, f"Missing required key: {key}"
    
    # Validate data types and ranges
    if not isinstance(player["health"], int) or not 0 <= player["health"] <= 100:
        return False, "Health must be integer between 0 and 100"
    
    if not isinstance(player["inventory"], list):
        return False, "Inventory must be a list"
    
    if not isinstance(player["gold"], int) or player["gold"] < 0:
        return False, "Gold must be non-negative integer"
    
    return True, "Valid"
```

### World Validation

```python
def validate_world(world):
    """Validate world object structure."""
    required_keys = ["current_location", "locations"]
    
    for key in required_keys:
        if key not in world:
            return False, f"Missing required key: {key}"
    
    # Validate current location exists
    if world["current_location"] not in world["locations"]:
        return False, "Current location not found in locations"
    
    # Validate location connections
    for location_name, location_data in world["locations"].items():
        for connection in location_data.get("connections", []):
            if connection not in world["locations"]:
                return False, f"Invalid connection: {connection} from {location_name}"
    
    return True, "Valid"
```

## Data Migration

### Version Compatibility

When updating data structures, maintain backward compatibility:

```python
def migrate_save_data(save_data):
    """Migrate save data to current version."""
    version = save_data.get("version", "0.1")
    
    if version == "0.1":
        # Add new fields with defaults
        save_data["metadata"] = {}
        save_data["version"] = "1.0"
    
    # Add future migrations here
    
    return save_data
```

### Default Values

Provide sensible defaults for missing data:

```python
DEFAULT_PLAYER = {
    "name": "Adventurer",
    "health": 100,
    "inventory": [],
    "location": "Village",
    "gold": 100
}

DEFAULT_LOCATION = {
    "description": "A mysterious place.",
    "connections": [],
    "items": [],
    "visited": False,
    "properties": {}
}
```

## Performance Considerations

### Memory Usage

- Keep data structures minimal and focused
- Use appropriate data types (int vs float)
- Avoid deep nesting where possible
- Clean up temporary data structures

### Serialization

- JSON is human-readable but larger than binary formats
- Consider compression for large save files
- Validate data on load to prevent corruption

### Access Patterns

- Frequently accessed data should be easily retrievable
- Consider caching for expensive calculations
- Use appropriate data structures for access patterns (dict vs list)

## Best Practices

### Naming Conventions

- Use descriptive names for dictionary keys
- Follow consistent naming patterns
- Use snake_case for keys and variables
- Avoid abbreviations unless widely understood

### Documentation

- Document all data structure fields
- Provide examples for complex structures
- Explain validation rules and constraints
- Keep documentation updated with code changes

### Error Handling

- Validate data structure integrity
- Provide meaningful error messages
- Handle missing or corrupted data gracefully
- Log data validation errors for debugging

This documentation should be updated whenever data structures are modified to ensure accuracy and completeness.

