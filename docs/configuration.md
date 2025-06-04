# Configuration Management System

## Overview

Kevin's Adventure Game now features a centralized configuration management system that allows for easy modification of game content without changing code. This system supports environment-specific configurations, provides validation, and enables modding capabilities.

## Key Benefits

- **Easy Content Modification**: Change game parameters without touching code
- **Environment Support**: Different settings for development, testing, and production
- **Modding Support**: Easy creation of game modifications
- **Validation**: JSON schemas ensure configuration integrity
- **Hot Reloading**: Configurations can be reloaded without restarting the game

## Migration Summary

The following hardcoded values have been extracted to configuration files:

### Player Settings
- **Before**: Hardcoded in `game/player.py`
  ```python
  "health": 100,
  "gold": 100,
  "location": "Village"
  ```
- **After**: Configurable in `config/game_settings/base.json`
  ```json
  {
    "player": {
      "starting_health": 100,
      "starting_gold": 100,
      "starting_location": "Village"
    }
  }
  ```

### Item Definitions
- **Before**: Hardcoded dictionary in `game/items.py`
- **After**: Comprehensive configuration in `config/items/items.json`
- **Benefits**: Easy to add new items, modify effects, and balance gameplay

### Shop Inventories
- **Before**: Hardcoded prices in `locations/village.py`
- **After**: Configurable shop data in `config/items/shop_inventory.json`
- **Benefits**: Easy price adjustments and inventory management

### World Structure
- **Before**: Hardcoded world data in `game/world.py`
- **After**: Configurable world structure in `config/locations/world.json`
- **Benefits**: Easy to add new locations and modify connections

### Location Interactions
- **Before**: Hardcoded probabilities and messages in location files
- **After**: Configurable interactions in location-specific JSON files
- **Benefits**: Easy to balance random events and modify content

### Random Events
- **Before**: Hardcoded in `utils/random_events.py`
- **After**: Configurable in `config/events/random_events.json`
- **Benefits**: Easy to adjust probabilities and add new events

## Usage Examples

### Basic Configuration Loading
```python
from config import config

# Get player starting values
game_settings = config.get_game_settings()
starting_health = game_settings["player"]["starting_health"]

# Get item information
sword_data = config.get_item_data("sword")
sword_description = sword_data["description"]

# Get location data
village_data = config.get_location_data("Village")
village_connections = village_data["connections"]
```

### Environment-Specific Configuration
```bash
# Development mode (easier gameplay for testing)
export GAME_ENVIRONMENT=development
python main.py

# Production mode (normal difficulty)
export GAME_ENVIRONMENT=production
python main.py
```

### Creating a Mod
1. Create `config/environments/my_mod.json`:
```json
{
  "base": {
    "player": {
      "starting_gold": 500,
      "starting_health": 150
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

2. Run with mod:
```bash
export GAME_ENVIRONMENT=my_mod
python main.py
```

## Configuration Files Structure

```
config/
├── game_settings/base.json      # Core game parameters
├── items/
│   ├── items.json              # All item definitions
│   └── shop_inventory.json     # Shop configurations
├── locations/
│   ├── world.json              # World structure
│   ├── forest.json             # Forest-specific config
│   ├── village.json            # Village-specific config
│   └── mountain.json           # Mountain-specific config
├── events/
│   └── random_events.json      # Random events and encounters
├── schemas/                     # JSON validation schemas
└── environments/                # Environment-specific overrides
    ├── development.json        # Development settings
    └── production.json         # Production settings
```

## Validation and Error Handling

The configuration system includes:

- **JSON Schema Validation**: Ensures all configurations are properly structured
- **Graceful Fallbacks**: Falls back to hardcoded values if configuration fails
- **Detailed Error Messages**: Clear error reporting for configuration issues
- **Type Checking**: Validates data types and value ranges

## Backward Compatibility

The system maintains backward compatibility by:

- Providing fallback mechanisms for missing configurations
- Preserving existing save file formats
- Maintaining the same game behavior with default configurations
- Gradual migration path for existing content

## Performance Considerations

- **Caching**: Configurations are cached after first load
- **Lazy Loading**: Configurations are loaded only when needed
- **Hot Reloading**: Configurations can be reloaded without restart
- **Minimal Overhead**: Configuration access is optimized for game performance

## Future Enhancements

The configuration system is designed to support:

- **Visual Configuration Editor**: GUI tool for modifying configurations
- **Plugin System**: Support for loadable game plugins
- **Dynamic Content**: Runtime modification of game content
- **Multiplayer Configurations**: Server-side configuration management
- **Localization**: Multi-language content support

## Best Practices for Modders

1. **Use Environment Overrides**: Create environment-specific files rather than modifying base configurations
2. **Validate Configurations**: Use the provided schemas to validate custom configurations
3. **Test Thoroughly**: Test mods with different game scenarios
4. **Document Changes**: Clearly document what your mod changes
5. **Preserve Balance**: Consider game balance when modifying values
6. **Use Descriptive Names**: Use clear, descriptive names for custom content

## Troubleshooting

### Common Issues

1. **Configuration Not Loading**
   - Check file paths and JSON syntax
   - Verify environment variable is set correctly
   - Check console for error messages

2. **Schema Validation Errors**
   - Ensure all required fields are present
   - Check data types match schema requirements
   - Validate JSON syntax

3. **Game Behavior Changes**
   - Compare with base configuration values
   - Check environment overrides
   - Verify configuration cache is cleared

### Debug Mode

Enable debug logging to see configuration loading details:
```python
import logging
logging.basicConfig(level=logging.INFO)
```

This will show which configurations are being loaded and any errors encountered.

