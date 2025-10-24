# Configuration System for Kevin's Adventure Game

This directory contains the centralized configuration management system for Kevin's Adventure Game. The configuration system allows for easy modification of game content without changing code, supports environment-specific settings, and provides a foundation for modding.

## Directory Structure

```
config/
├── README.md                    # This file
├── __init__.py                  # Configuration module initialization
├── config_manager.py            # Core configuration management class
├── game_settings/               # Core game settings
│   └── base.json               # Base game configuration
├── items/                       # Item definitions and shop inventories
│   ├── items.json              # All item definitions
│   └── shop_inventory.json     # Shop configurations
├── locations/                   # Location and world data
│   ├── world.json              # World structure and location connections
│   ├── forest.json             # Forest-specific configuration
│   ├── village.json            # Village-specific configuration
│   ├── mountain.json           # Mountain-specific configuration
│   └── cave.json               # Cave-specific configuration (if exists)
├── events/                      # Random events and encounters
│   ├── random_events.json      # Global random events
│   └── location_events.json    # Location-specific events (if exists)
├── schemas/                     # JSON schemas for validation
│   ├── items.schema.json       # Items configuration schema
│   ├── locations.schema.json   # Locations configuration schema
│   ├── events.schema.json      # Events configuration schema
│   └── game_settings.schema.json # Game settings schema
└── environments/                # Environment-specific overrides
    ├── development.json        # Development environment settings
    └── production.json         # Production environment settings
```

## Usage

### Basic Usage

```python
from config import config

# Load game settings
game_settings = config.get_game_settings()
starting_health = game_settings["player"]["starting_health"]

# Load item data
item_data = config.get_item_data("sword")
item_description = item_data["description"]

# Load location data
location_data = config.get_location_data("Forest")
location_description = location_data["description"]

# Load shop configuration
shop_config = config.get_shop_config("village_shop")
bread_price = shop_config["inventory"]["bread"]["price"]
```

### Environment-Specific Configuration

Set the `GAME_ENVIRONMENT` environment variable to load different configurations:

```bash
# Development mode (higher starting gold, easier gameplay)
export GAME_ENVIRONMENT=development
python main.py

# Production mode (default settings)
export GAME_ENVIRONMENT=production
python main.py
```

### Configuration Manager API

The `ConfigManager` class provides the following methods:

- `get_game_settings()` - Load base game settings
- `get_items_config()` - Load all item definitions
- `get_item_data(item_name)` - Get specific item data
- `get_world_config()` - Load world and location structure
- `get_location_config(location_name)` - Load location-specific configuration
- `get_location_data(location_name)` - Get location data from world config
- `get_shop_config(shop_name)` - Load shop configuration
- `get_events_config()` - Load random events configuration
- `reload_config(config_path)` - Reload specific or all configurations
- `validate_configuration()` - Validate all loaded configurations

## Configuration File Formats

### Game Settings (`game_settings/base.json`)

Contains core game parameters:

```json
{
  "player": {
    "starting_health": 100,
    "max_health": 100,
    "starting_gold": 100,
    "starting_location": "Village",
    "starting_inventory": []
  },
  "game": {
    "save_file_extension": ".sav",
    "max_inventory_size": null,
    "auto_save": false,
    "difficulty": "normal"
  }
}
```

### Items Configuration (`items/items.json`)

Defines all game items with their properties and effects:

```json
{
  "items": {
    "bread": {
      "name": "Bread",
      "description": "A fresh loaf of bread...",
      "type": "consumable",
      "consumable": true,
      "effects": {
        "heal": 20,
        "message": "You eat the bread..."
      }
    }
  }
}
```

### Locations Configuration (`locations/world.json`)

Defines the game world structure:

```json
{
  "world": {
    "starting_location": "Village",
    "locations": {
      "Village": {
        "name": "Village",
        "description": "A small, peaceful village...",
        "connections": ["Forest", "Mountain"],
        "starting_items": ["map", "bread"],
        "location_type": "settlement",
        "safe_zone": true
      }
    }
  }
}
```

### Location-Specific Configuration (`locations/forest.json`)

Defines location-specific interactions and events:

```json
{
  "forest": {
    "entrance_message": "You enter the lush, green forest...",
    "actions": {
      "explore_deeper": {
        "name": "Explore deeper",
        "description": "Venture further into the forest",
        "events": [
          {
            "name": "find_berries",
            "probability": 40,
            "message": "You stumble upon a bush full of ripe berries!",
            "reward": "berries"
          }
        ]
      }
    }
  }
}
```

## Modding Support

The configuration system is designed to support easy modding:

1. **Override Configurations**: Create custom configuration files and load them using the ConfigManager
2. **Environment Overrides**: Use environment-specific files to modify game behavior
3. **Schema Validation**: All configurations are validated against JSON schemas
4. **Hot Reloading**: Configurations can be reloaded without restarting the game

### Creating a Mod

1. Create a new environment configuration file (e.g., `environments/my_mod.json`)
2. Override specific values you want to change
3. Set `GAME_ENVIRONMENT=my_mod` when running the game

Example mod configuration:

```json
{
  "base": {
    "player": {
      "starting_gold": 500
    }
  },
  "items": {
    "items": {
      "bread": {
        "effects": {
          "heal": 50
        }
      }
    }
  }
}
```

## Validation

All configuration files are validated against JSON schemas located in the `schemas/` directory. This ensures:

- Required fields are present
- Data types are correct
- Values are within acceptable ranges
- Configuration structure is consistent

To validate configurations manually:

```python
from config import config
config.validate_configuration()
```

## Migration from Hardcoded Values

The configuration system replaces hardcoded values throughout the game:

- **Player stats** (health, gold) → `game_settings/base.json`
- **Item properties** → `items/items.json`
- **Shop inventories** → `items/shop_inventory.json`
- **Location data** → `locations/world.json` and location-specific files
- **Random event probabilities** → `events/random_events.json`

## Best Practices

1. **Use descriptive names** for configuration keys
2. **Include comments** in JSON files where helpful (though JSON doesn't support comments, use descriptive keys)
3. **Validate configurations** after making changes
4. **Use environment overrides** for testing and development
5. **Keep related configurations together** in the same file
6. **Use schemas** to ensure configuration validity
7. **Document custom configurations** for mods

## Troubleshooting

### Common Issues

1. **Configuration file not found**: Check file paths and ensure files exist
2. **JSON parsing errors**: Validate JSON syntax using a JSON validator
3. **Schema validation failures**: Check that all required fields are present and have correct types
4. **Environment overrides not working**: Ensure `GAME_ENVIRONMENT` is set correctly

### Debugging

Enable debug logging to see configuration loading details:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

### Error Messages

The ConfigManager provides detailed error messages for common issues:

- Missing configuration files
- Invalid JSON syntax
- Schema validation failures
- Missing required fields

