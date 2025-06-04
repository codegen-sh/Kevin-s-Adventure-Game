# Plugin Development Guide for Kevin's Adventure Game

This guide explains how to create plugins for Kevin's Adventure Game using the extensible plugin system.

## Table of Contents

1. [Overview](#overview)
2. [Plugin Types](#plugin-types)
3. [Getting Started](#getting-started)
4. [Location Plugins](#location-plugins)
5. [Action Plugins](#action-plugins)
6. [Game Mechanic Plugins](#game-mechanic-plugins)
7. [Plugin Metadata](#plugin-metadata)
8. [Hot Reloading](#hot-reloading)
9. [Best Practices](#best-practices)
10. [Examples](#examples)

## Overview

The plugin system allows developers to extend Kevin's Adventure Game with new locations, actions, and game mechanics without modifying the core game code. Plugins are Python modules that inherit from base classes and implement specific interfaces.

### Key Features

- **Automatic Discovery**: Plugins are automatically discovered and loaded from plugin directories
- **Hot Reloading**: Plugins can be reloaded during development without restarting the game
- **Validation**: Built-in validation ensures plugins meet requirements before loading
- **Metadata System**: Rich metadata support with versioning and dependencies
- **Error Handling**: Robust error handling prevents plugin failures from crashing the game

## Plugin Types

The system supports three main types of plugins:

1. **Location Plugins** (`BaseLocation`): Add new areas for players to explore
2. **Action Plugins** (`BaseAction`): Add new commands and interactions
3. **Game Mechanic Plugins** (`BaseGameMechanic`): Add new game systems and features

## Getting Started

### 1. Plugin Directory Structure

```
plugins/
├── __init__.py
├── config.json
├── examples/
│   ├── __init__.py
│   ├── desert_location.py
│   ├── inspect_action.py
│   └── weather_mechanic.py
└── custom/
    └── your_plugin.py
```

### 2. Basic Plugin Template

All plugins must inherit from one of the base classes and implement required methods:

```python
from plugins.base import BaseLocation, PluginMetadata
from typing import Dict, Any, List

class MyLocation(BaseLocation):
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="MyLocation",
            version="1.0.0",
            description="A custom location",
            author="Your Name"
        )
    
    def initialize(self) -> bool:
        return True
    
    def cleanup(self) -> None:
        pass
    
    # Implement other required methods...
```

### 3. Creating a Plugin

Use the plugin manager to create templates:

```python
from plugins.manager import get_plugin_manager

manager = get_plugin_manager()
file_path = manager.create_plugin("My Location", "location", "plugins/custom")
```

## Location Plugins

Location plugins add new areas to the game world that players can visit and explore.

### Required Methods

```python
class MyLocation(BaseLocation):
    def get_description(self) -> str:
        """Return the location description shown to players."""
        return "A mysterious location with secrets to discover."
    
    def get_connections(self) -> List[str]:
        """Return list of connected location names."""
        return ["Village", "Forest"]
    
    def get_items(self) -> List[str]:
        """Return list of items available in this location."""
        return ["mysterious_key", "ancient_scroll"]
    
    def enter_location(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """Handle player entering this location."""
        print(f"You enter {self.metadata.name}...")
        
        while True:
            print("\\nWhat would you like to do?")
            print("1. Explore")
            print("2. Leave")
            
            choice = input("Enter choice: ")
            if choice == "1":
                self._explore(world, player)
            elif choice == "2":
                break
    
    def _explore(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """Custom exploration logic."""
        print("You discover something interesting...")
```

### Location Integration

Locations are automatically added to the game world when the plugin system initializes. The location data structure includes:

- `description`: Text shown when entering the location
- `connections`: List of locations the player can travel to
- `items`: List of items that can be found here

## Action Plugins

Action plugins add new commands that players can use throughout the game.

### Required Methods

```python
class MyAction(BaseAction):
    def get_triggers(self) -> List[str]:
        """Return command words that trigger this action."""
        return ["mycommand", "mc", "custom"]
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], 
                command: str, args: List[str]) -> bool:
        """Execute the action."""
        print(f"Executing {command} with args: {args}")
        
        # Perform action logic here
        # Return True if action was handled, False otherwise
        return True
    
    def get_help_text(self) -> str:
        """Return help text for this action."""
        return "mycommand - Perform a custom action"
    
    def can_execute(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        """Check if action can be executed in current context."""
        # Add any conditions here
        return True
```

### Action Processing

Actions are processed in this order:
1. Plugin actions (highest priority)
2. Built-in movement commands
3. Built-in interaction commands
4. Default "unknown command" response

## Game Mechanic Plugins

Game mechanic plugins add new systems that affect gameplay throughout the game.

### Required Methods

```python
class MyMechanic(BaseGameMechanic):
    def on_game_start(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called when a new game starts."""
        print("My mechanic is now active!")
    
    def on_game_load(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called when a game is loaded."""
        # Restore mechanic state from saved data
        pass
    
    def on_game_save(self, player: Dict[str, Any], world: Dict[str, Any]) -> Dict[str, Any]:
        """Called when game is saved."""
        return {"my_data": "value"}  # Return data to save
    
    def on_turn_start(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called at the start of each turn."""
        # Apply turn-based effects
        pass
    
    def on_turn_end(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called at the end of each turn."""
        # Clean up turn effects
        pass
```

### Game Events

Mechanics can respond to these game events:
- `start`: New game started
- `load`: Game loaded from save
- `save`: Game being saved (return data to include)
- `turn_start`: Beginning of player turn
- `turn_end`: End of player turn

## Plugin Metadata

All plugins must provide metadata describing the plugin:

```python
@property
def metadata(self) -> PluginMetadata:
    return PluginMetadata(
        name="PluginName",           # Unique plugin identifier
        version="1.0.0",             # Semantic version
        description="What it does",   # Brief description
        author="Your Name",           # Plugin author
        dependencies=["OtherPlugin"], # Required plugins (optional)
        min_game_version="1.0.0"     # Minimum game version (optional)
    )
```

### Versioning

Use semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

## Hot Reloading

Hot reloading allows you to modify plugins during development without restarting the game.

### Enabling Hot Reload

```python
from plugins.manager import get_plugin_manager

manager = get_plugin_manager()
manager.loader.enable_hot_reload()
```

Or set in `plugins/config.json`:
```json
{
  "hot_reload": true
}
```

### How It Works

1. File system watcher monitors plugin directories
2. When a `.py` file changes, the plugin is automatically reloaded
3. Old plugin instances are cleaned up
4. New plugin instances are created and registered
5. Game continues with updated plugin

### Development Workflow

1. Create your plugin file
2. Enable hot reload
3. Start the game
4. Edit your plugin file
5. Changes are automatically applied
6. Test in the running game

## Best Practices

### Code Organization

- Keep plugin files focused on a single responsibility
- Use descriptive names for classes and methods
- Include docstrings for all public methods
- Handle errors gracefully

### Error Handling

```python
def execute(self, player, world, command, args):
    try:
        # Your action logic here
        return True
    except Exception as e:
        print(f"Error in {self.metadata.name}: {e}")
        return False
```

### Player Interaction

- Provide clear feedback for all actions
- Use consistent input prompts
- Validate user input
- Offer help and guidance

### Game Integration

- Respect existing game mechanics
- Don't modify core game state unexpectedly
- Use the provided utility functions
- Follow the game's tone and style

### Performance

- Avoid expensive operations in frequently called methods
- Cache computed values when appropriate
- Clean up resources in the `cleanup()` method
- Use efficient algorithms for game logic

## Examples

### Simple Location Plugin

```python
from plugins.base import BaseLocation, PluginMetadata
from game.player import add_item_to_inventory, heal_player

class Garden(BaseLocation):
    @property
    def metadata(self):
        return PluginMetadata(
            name="Garden",
            version="1.0.0",
            description="A peaceful garden location"
        )
    
    def initialize(self):
        return True
    
    def cleanup(self):
        pass
    
    def get_description(self):
        return "A beautiful garden with colorful flowers and fruit trees."
    
    def get_connections(self):
        return ["Village"]
    
    def get_items(self):
        return ["apple", "flower"]
    
    def enter_location(self, world, player):
        print("You enter the peaceful garden.")
        print("The scent of flowers fills the air.")
        
        while True:
            print("\\n1. Pick fruit")
            print("2. Rest among flowers")
            print("3. Leave")
            
            choice = input("Choice: ")
            if choice == "1":
                add_item_to_inventory(player, "apple")
                print("You pick a fresh apple.")
            elif choice == "2":
                heal_player(player, 10)
                print("You rest peacefully among the flowers.")
            elif choice == "3":
                break
```

### Simple Action Plugin

```python
from plugins.base import BaseAction, PluginMetadata

class DanceAction(BaseAction):
    @property
    def metadata(self):
        return PluginMetadata(
            name="DanceAction",
            version="1.0.0",
            description="Allows the player to dance"
        )
    
    def initialize(self):
        return True
    
    def cleanup(self):
        pass
    
    def get_triggers(self):
        return ["dance", "boogie"]
    
    def execute(self, player, world, command, args):
        print("You break into a spontaneous dance!")
        print("Your spirits are lifted!")
        
        # Small health boost for dancing
        player["health"] = min(100, player["health"] + 5)
        return True
    
    def get_help_text(self):
        return "dance - Break into a joyful dance"
```

### Simple Mechanic Plugin

```python
from plugins.base import BaseGameMechanic, PluginMetadata
import random

class LuckMechanic(BaseGameMechanic):
    def __init__(self):
        super().__init__()
        self.luck_points = 0
    
    @property
    def metadata(self):
        return PluginMetadata(
            name="LuckMechanic",
            version="1.0.0",
            description="Adds a luck system to the game"
        )
    
    def initialize(self):
        return True
    
    def cleanup(self):
        pass
    
    def on_game_start(self, player, world):
        self.luck_points = 50  # Start with neutral luck
        print("The luck system is active!")
    
    def on_turn_start(self, player, world):
        # Random luck events
        if random.random() < 0.1:  # 10% chance
            if random.random() < 0.5:
                self.luck_points += 10
                print("You feel lucky today!")
            else:
                self.luck_points -= 10
                print("You feel a bit unlucky...")
    
    def on_game_save(self, player, world):
        return {"luck_points": self.luck_points}
    
    def get_luck_modifier(self):
        """Other plugins can call this to get luck bonuses."""
        if self.luck_points > 70:
            return 1.2  # 20% bonus
        elif self.luck_points < 30:
            return 0.8  # 20% penalty
        return 1.0  # No modifier
```

## Testing Your Plugins

### Manual Testing

1. Create your plugin
2. Start the game
3. Test all plugin functionality
4. Verify error handling
5. Check integration with other systems

### Validation

The plugin system automatically validates:
- Required methods are implemented
- Metadata is complete and valid
- Plugin can be instantiated
- No critical errors during initialization

### Debugging

- Use print statements for debugging
- Check the console for error messages
- Use the plugin status command: `plugins`
- Enable hot reload for faster iteration

## Troubleshooting

### Common Issues

**Plugin not loading:**
- Check file is in correct directory
- Verify class inherits from correct base class
- Check for syntax errors
- Ensure all required methods are implemented

**Hot reload not working:**
- Verify hot reload is enabled
- Check file permissions
- Ensure watchdog is installed
- Look for error messages in console

**Plugin conflicts:**
- Check for duplicate trigger words
- Verify location names don't conflict
- Review plugin dependencies
- Check load order

### Getting Help

1. Check this documentation
2. Look at example plugins
3. Review error messages carefully
4. Test with minimal plugin first
5. Ask for help with specific error messages

## Advanced Topics

### Plugin Dependencies

Specify dependencies in metadata:
```python
dependencies=["WeatherMechanic", "BaseInventory"]
```

### Custom Settings

Plugins can read settings from config:
```python
def apply_settings(self, settings):
    self.difficulty = settings.get("difficulty", "normal")
```

### Inter-Plugin Communication

Plugins can interact through the plugin manager:
```python
weather_plugin = plugin_manager.mechanics.get("WeatherMechanic")
if weather_plugin:
    current_weather = weather_plugin.current_weather
```

### Save Data Integration

Game mechanics can save custom data:
```python
def on_game_save(self, player, world):
    return {
        "custom_state": self.state,
        "player_data": self.player_specific_data
    }
```

This data is automatically included in save files and restored on load.

