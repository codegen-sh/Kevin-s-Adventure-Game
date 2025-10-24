# Kevin's Adventure Game Plugin System

An extensible plugin architecture that allows easy addition of new locations, actions, and game mechanics to Kevin's Adventure Game.

## Quick Start

### 1. Installation

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Enable Plugins

Plugins are automatically loaded when the game starts. The plugin system will discover and load all plugins from:
- `plugins/examples/` - Example plugins included with the game
- `plugins/custom/` - Your custom plugins

### 3. Create Your First Plugin

Use the plugin manager to create a template:

```python
from plugins.manager import get_plugin_manager

manager = get_plugin_manager()
manager.initialize()

# Create a new location plugin
file_path = manager.create_plugin("My Location", "location", "plugins/custom")
print(f"Created plugin template at: {file_path}")
```

### 4. Enable Hot Reloading (Development)

For development, enable hot reloading to see changes immediately:

```python
manager.loader.enable_hot_reload()
```

Or set in `plugins/config.json`:
```json
{
  "hot_reload": true
}
```

## Plugin Types

### Location Plugins
Add new areas for players to explore:
- Define location description, connections, and items
- Handle player interactions within the location
- Integrate seamlessly with the game world

### Action Plugins  
Add new commands and interactions:
- Define trigger words that activate the action
- Implement custom command logic
- Provide help text for players

### Game Mechanic Plugins
Add new systems and features:
- Respond to game events (start, load, save, turns)
- Modify gameplay mechanics
- Persist state across game sessions

## Example Plugins Included

### Desert Location (`plugins/examples/desert_location.py`)
A vast desert location with:
- Multiple exploration options
- Weather-dependent events
- Hidden treasures and dangers
- Dynamic encounters

### Inspect Action (`plugins/examples/inspect_action.py`)
Enhanced examination system:
- Detailed item descriptions
- Location analysis
- Inventory inspection
- Player status review

### Weather Mechanic (`plugins/examples/weather_mechanic.py`)
Dynamic weather system:
- Changing weather conditions
- Location-specific effects
- Player impact and adaptation
- Atmospheric enhancement

## Plugin System Features

### Automatic Discovery
- Plugins are automatically found and loaded
- No manual registration required
- Supports nested directory structures

### Hot Reloading
- Modify plugins during development
- Changes applied without restarting game
- File system monitoring for instant updates

### Validation & Error Handling
- Built-in plugin validation
- Graceful error handling
- Detailed error reporting
- Plugin isolation (failures don't crash game)

### Metadata System
- Rich plugin information
- Version management
- Dependency tracking
- Author attribution

### Configuration Management
- JSON-based configuration
- Plugin-specific settings
- Enable/disable plugins
- Runtime configuration changes

## Plugin Status Commands

Use these in-game commands to manage plugins:

- `plugins` - Show plugin system status
- `help` - Shows both game and plugin help

## Configuration

Edit `plugins/config.json` to configure the plugin system:

```json
{
  "hot_reload": false,
  "enabled_plugins": [],
  "disabled_plugins": [],
  "plugin_settings": {
    "PluginName": {
      "setting1": "value1",
      "setting2": "value2"
    }
  }
}
```

## Directory Structure

```
plugins/
├── __init__.py              # Plugin system package
├── README.md               # This file
├── config.json             # Plugin configuration
├── base.py                 # Base plugin classes
├── registry.py             # Plugin registries
├── loader.py               # Plugin loading and discovery
├── manager.py              # High-level plugin management
├── examples/               # Example plugins
│   ├── __init__.py
│   ├── desert_location.py  # Desert location plugin
│   ├── inspect_action.py   # Inspect action plugin
│   └── weather_mechanic.py # Weather system plugin
└── custom/                 # Your custom plugins
    └── (your plugins here)
```

## Development Workflow

1. **Create Plugin Template**
   ```python
   manager.create_plugin("Plugin Name", "type", "output_dir")
   ```

2. **Enable Hot Reload**
   ```python
   manager.loader.enable_hot_reload()
   ```

3. **Edit Plugin File**
   - Implement required methods
   - Add custom logic
   - Test functionality

4. **Test in Game**
   - Changes are automatically applied
   - Test all plugin features
   - Verify error handling

5. **Deploy**
   - Disable hot reload for production
   - Add to version control
   - Share with other developers

## API Reference

### Plugin Manager
```python
from plugins.manager import get_plugin_manager

manager = get_plugin_manager()
manager.initialize()                    # Initialize plugin system
manager.create_plugin(name, type, dir)  # Create plugin template
manager.enable_plugin(name)             # Enable specific plugin
manager.disable_plugin(name)            # Disable specific plugin
manager.get_status()                    # Get system status
manager.shutdown()                      # Clean shutdown
```

### Base Classes
```python
from plugins.base import BaseLocation, BaseAction, BaseGameMechanic

class MyPlugin(BaseLocation):  # or BaseAction, BaseGameMechanic
    # Implement required methods
    pass
```

## Best Practices

### Plugin Development
- Keep plugins focused and single-purpose
- Handle errors gracefully
- Provide clear user feedback
- Follow game's tone and style
- Use descriptive names and documentation

### Performance
- Avoid expensive operations in frequently called methods
- Cache computed values when appropriate
- Clean up resources properly
- Use efficient algorithms

### Integration
- Respect existing game mechanics
- Don't modify core game state unexpectedly
- Use provided utility functions
- Test with other plugins

## Troubleshooting

### Plugin Not Loading
- Check file is in correct directory (`plugins/examples/` or `plugins/custom/`)
- Verify class inherits from correct base class
- Check for syntax errors in Python code
- Ensure all required methods are implemented

### Hot Reload Not Working
- Verify hot reload is enabled in config or code
- Check that `watchdog` package is installed
- Ensure file permissions allow monitoring
- Look for error messages in console

### Plugin Conflicts
- Check for duplicate trigger words in actions
- Verify location names don't conflict
- Review plugin dependencies
- Check plugin load order

### Getting Help
1. Read the full documentation in `docs/PLUGIN_DEVELOPMENT.md`
2. Examine example plugins for reference
3. Check console for detailed error messages
4. Test with minimal plugin first
5. Use the plugin status command: `plugins`

## Contributing

To contribute to the plugin system:

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Include tests and documentation
5. Submit a pull request

### Areas for Contribution
- Additional example plugins
- Enhanced error handling
- Performance optimizations
- Documentation improvements
- Testing framework
- Plugin marketplace/sharing system

## License

This plugin system is part of Kevin's Adventure Game and follows the same license terms.

