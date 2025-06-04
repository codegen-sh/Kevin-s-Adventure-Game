# Plugin Development Guide

## Overview

Kevin's Adventure Game supports a plugin system that allows developers to extend the game with custom locations, items, events, and mechanics. This guide explains how to create and integrate plugins into the game.

## Plugin Architecture

### Plugin Types

The game supports several types of plugins:

1. **Location Plugins**: Add new locations with unique events and interactions
2. **Item Plugins**: Create new items with custom effects and behaviors
3. **Event Plugins**: Add new random events and encounters
4. **Mechanic Plugins**: Introduce new game mechanics and systems
5. **UI Plugins**: Customize the user interface and text formatting

### Plugin Structure

A plugin is a Python module that follows specific conventions and interfaces. Plugins are loaded dynamically and integrated into the game's core systems.

```
plugins/
├── __init__.py
├── my_plugin/
│   ├── __init__.py
│   ├── plugin.py          # Main plugin file
│   ├── locations.py       # Location definitions
│   ├── items.py           # Item definitions
│   ├── events.py          # Event definitions
│   └── config.py          # Plugin configuration
```

## Creating a Location Plugin

### Basic Location Plugin

Here's a simple example of a desert location plugin:

```python
# plugins/desert_plugin/plugin.py
"""
Desert Location Plugin for Kevin's Adventure Game.

This plugin adds a desert location with unique events and challenges.
"""

from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event
from utils.text_formatting import print_event
import random

# Plugin metadata
PLUGIN_NAME = "Desert Location"
PLUGIN_VERSION = "1.0.0"
PLUGIN_AUTHOR = "Your Name"
PLUGIN_DESCRIPTION = "Adds a vast desert location with sandstorms and oases"

def get_plugin_info():
    """Return plugin metadata."""
    return {
        "name": PLUGIN_NAME,
        "version": PLUGIN_VERSION,
        "author": PLUGIN_AUTHOR,
        "description": PLUGIN_DESCRIPTION,
        "type": "location"
    }

def explore_desert(player, world):
    """
    Handle desert exploration events and interactions.
    
    Args:
        player (dict): The player object
        world (dict): The world state object
    
    Returns:
        bool: True if exploration was successful
    """
    print("\\nYou enter the vast, scorching desert...")
    print("The sun beats down mercilessly as sand dunes stretch endlessly.")
    print("Mirages shimmer in the distance, and the silence is deafening.")
    
    # Random desert events
    event_chance = random.randint(1, 100)
    
    if event_chance <= 25:
        _desert_sandstorm_event(player)
    elif event_chance <= 40:
        _desert_oasis_event(player)
    elif event_chance <= 55:
        _desert_mirage_event(player, world)
    elif event_chance <= 70:
        _desert_treasure_event(player)
    elif event_chance <= 85:
        _desert_nomad_event(player, world)
    else:
        _desert_peaceful_travel(player)
    
    # Update world state
    update_world_state(world, "desert_visited", True)
    
    # Chance for random event
    if random.randint(1, 100) <= 20:
        generate_random_event(player, world)
    
    return True

def _desert_sandstorm_event(player):
    """Handle sandstorm encounters."""
    print_event("A fierce sandstorm suddenly engulfs you!", "danger")
    print("You struggle to find shelter as sand whips around you.")
    
    if "cloak" in player["inventory"]:
        print("Your cloak protects you from the worst of the storm.")
        damage_player(player, 5)
    else:
        print("Without protection, the sand cuts into your skin.")
        damage_player(player, 15)
    
    # Chance to find something after the storm
    if random.randint(1, 100) <= 30:
        print("After the storm passes, you notice something glinting in the sand.")
        treasure = random.choice(["ancient_coin", "desert_crystal", "buried_relic"])
        add_item_to_inventory(player, treasure)

def _desert_oasis_event(player):
    """Handle oasis discoveries."""
    print_event("You discover a beautiful oasis!", "success")
    print("Palm trees provide shade, and crystal-clear water reflects the sky.")
    print("You drink deeply and rest in the cool shade.")
    
    # Restore health and add water
    heal_player(player, 30)
    add_item_to_inventory(player, "fresh_water")
    
    # Chance to meet other travelers
    if random.randint(1, 100) <= 40:
        print("\\nOther travelers are resting here as well.")
        print("They share stories and trade supplies with you.")
        trade_item = random.choice(["dates", "desert_map", "camel_milk"])
        add_item_to_inventory(player, trade_item)

def _desert_mirage_event(player, world):
    """Handle mirage encounters."""
    mirages = [
        "a magnificent city with golden towers",
        "a cool mountain lake surrounded by trees",
        "a caravan of merchants with exotic goods",
        "an ancient temple rising from the sands"
    ]
    
    mirage = random.choice(mirages)
    print_event(f"You see {mirage} in the distance!", "mystery")
    print("As you approach, the vision wavers and disappears.")
    print("Was it real, or just a trick of the desert heat?")
    
    # Some mirages have real effects
    if "temple" in mirage and random.randint(1, 100) <= 25:
        print("\\nWait... there's something real here after all!")
        print("You find ancient ruins buried in the sand.")
        add_item_to_inventory(player, "ancient_tablet")
        update_world_state(world, "desert_ruins_found", True)

def _desert_treasure_event(player):
    """Handle treasure discoveries."""
    treasures = [
        ("buried_chest", "You find a chest buried in the sand!"),
        ("gem_cache", "A cache of precious gems lies hidden in a rock crevice!"),
        ("lost_caravan", "You discover the remains of a lost caravan!"),
        ("ancient_artifact", "An ancient artifact emerges from the shifting sands!")
    ]
    
    treasure_type, description = random.choice(treasures)
    print_event(description, "success")
    
    if treasure_type == "buried_chest":
        loot = ["gold_coin", "silver_jewelry", "precious_spices"]
        for item in loot:
            add_item_to_inventory(player, item)
    elif treasure_type == "gem_cache":
        gems = random.randint(2, 4)
        for _ in range(gems):
            add_item_to_inventory(player, "desert_gem")
    elif treasure_type == "lost_caravan":
        add_item_to_inventory(player, "trade_goods")
        add_item_to_inventory(player, "water_skin")
    else:  # ancient_artifact
        add_item_to_inventory(player, "desert_relic")

def _desert_nomad_event(player, world):
    """Handle nomad encounters."""
    print_event("You encounter a group of desert nomads!", "info")
    print("They approach cautiously, studying you with curious eyes.")
    
    if player["gold"] >= 20:
        print("\\nThe nomads offer to trade with you.")
        print("They want 20 gold for a special desert survival kit.")
        
        choice = input("Do you want to trade? (y/n): ").lower()
        if choice == 'y':
            player["gold"] -= 20
            add_item_to_inventory(player, "survival_kit")
            add_item_to_inventory(player, "desert_cloak")
            print("The nomads smile and give you their blessing.")
            heal_player(player, 10)
        else:
            print("The nomads nod respectfully and continue on their way.")
    else:
        print("The nomads see that you have little, so they offer you water.")
        print("Their kindness restores your spirit.")
        heal_player(player, 15)
        add_item_to_inventory(player, "blessed_water")

def _desert_peaceful_travel(player):
    """Handle peaceful desert travel."""
    peaceful_events = [
        "You find a comfortable spot in the shade of a large rock.",
        "A gentle breeze provides relief from the desert heat.",
        "You discover edible cactus fruit growing nearby.",
        "The beauty of the desert sunset fills you with wonder.",
        "You find tracks of desert animals in the sand."
    ]
    
    event = random.choice(peaceful_events)
    print_event(event, "info")
    
    if "cactus fruit" in event:
        print("The fruit is sweet and refreshing.")
        heal_player(player, 10)
        add_item_to_inventory(player, "cactus_fruit")
    elif "shade" in event or "breeze" in event:
        print("You rest and recover some energy.")
        heal_player(player, 5)

def get_desert_description():
    """Get a detailed description of the desert location."""
    return ("A vast expanse of golden sand dunes stretching to the horizon. "
            "The desert is both beautiful and dangerous, with scorching heat "
            "during the day and freezing cold at night. Ancient secrets lie "
            "buried beneath the shifting sands, and mirages dance in the "
            "shimmering heat. Nomadic tribes traverse these lands, following "
            "ancient routes between hidden oases.")

def get_desert_items():
    """Get the list of items typically found in the desert."""
    return ["cactus_fruit", "sand_crystal", "desert_flower", "sun_stone"]

def get_desert_connections():
    """Get the list of locations connected to the desert."""
    return ["Village", "Mountain"]  # Desert connects to Village and Mountain

# Plugin registration functions
def register_location(world):
    """Register the desert location with the world."""
    world["locations"]["Desert"] = {
        "description": get_desert_description(),
        "connections": get_desert_connections(),
        "items": get_desert_items(),
        "explore_function": explore_desert
    }
    
    # Add desert to existing location connections
    if "Village" in world["locations"]:
        if "Desert" not in world["locations"]["Village"]["connections"]:
            world["locations"]["Village"]["connections"].append("Desert")
    
    if "Mountain" in world["locations"]:
        if "Desert" not in world["locations"]["Mountain"]["connections"]:
            world["locations"]["Mountain"]["connections"].append("Desert")

def unregister_location(world):
    """Remove the desert location from the world."""
    if "Desert" in world["locations"]:
        del world["locations"]["Desert"]
    
    # Remove desert from other location connections
    for location_data in world["locations"].values():
        if "Desert" in location_data["connections"]:
            location_data["connections"].remove("Desert")

# Plugin lifecycle functions
def initialize_plugin():
    """Initialize the plugin."""
    print(f"Loading {PLUGIN_NAME} v{PLUGIN_VERSION}")
    return True

def cleanup_plugin():
    """Clean up plugin resources."""
    print(f"Unloading {PLUGIN_NAME}")
    return True
```

### Plugin Configuration

Create a configuration file for your plugin:

```python
# plugins/desert_plugin/config.py
"""Configuration for the Desert Location Plugin."""

# Plugin settings
PLUGIN_CONFIG = {
    "enabled": True,
    "debug_mode": False,
    "event_probabilities": {
        "sandstorm": 0.25,
        "oasis": 0.15,
        "mirage": 0.15,
        "treasure": 0.15,
        "nomad": 0.15,
        "peaceful": 0.15
    },
    "item_spawn_rates": {
        "cactus_fruit": 0.3,
        "sand_crystal": 0.2,
        "desert_flower": 0.1,
        "sun_stone": 0.05
    }
}

# Desert-specific settings
DESERT_SETTINGS = {
    "base_damage": 10,
    "oasis_healing": 30,
    "treasure_chance": 0.3,
    "nomad_trade_cost": 20
}

def get_config():
    """Get plugin configuration."""
    return PLUGIN_CONFIG

def get_desert_settings():
    """Get desert-specific settings."""
    return DESERT_SETTINGS
```

## Creating an Item Plugin

### Custom Item Plugin

Here's an example of a magical items plugin:

```python
# plugins/magic_items/plugin.py
"""
Magic Items Plugin for Kevin's Adventure Game.

This plugin adds magical items with special effects.
"""

from game.player import add_item_to_inventory, heal_player, damage_player
from game.world import get_current_location, change_location
from utils.text_formatting import print_event
import random

PLUGIN_NAME = "Magic Items"
PLUGIN_VERSION = "1.0.0"
PLUGIN_AUTHOR = "Your Name"
PLUGIN_DESCRIPTION = "Adds magical items with special powers"

# Magic item definitions
MAGIC_ITEMS = {
    "teleport_scroll": {
        "description": "A mystical scroll that can transport you to any location.",
        "type": "consumable",
        "rarity": "rare",
        "effect": "teleport"
    },
    "healing_potion": {
        "description": "A glowing potion that restores health and vitality.",
        "type": "consumable",
        "rarity": "common",
        "effect": "heal"
    },
    "invisibility_cloak": {
        "description": "A shimmering cloak that makes you invisible to enemies.",
        "type": "equipment",
        "rarity": "legendary",
        "effect": "invisibility"
    },
    "fire_crystal": {
        "description": "A crystal that burns with eternal flame.",
        "type": "tool",
        "rarity": "uncommon",
        "effect": "fire_damage"
    }
}

def get_magic_item_description(item):
    """Get description for a magic item."""
    return MAGIC_ITEMS.get(item, {}).get("description", "A mysterious magical item.")

def use_magic_item(player, item, world):
    """Handle magic item usage."""
    if item not in player["inventory"]:
        print(f"You don't have {item} in your inventory.")
        return False
    
    if item not in MAGIC_ITEMS:
        print(f"{item} is not a magic item.")
        return False
    
    item_data = MAGIC_ITEMS[item]
    effect = item_data["effect"]
    
    if effect == "teleport":
        return _use_teleport_scroll(player, world)
    elif effect == "heal":
        return _use_healing_potion(player)
    elif effect == "invisibility":
        return _use_invisibility_cloak(player, world)
    elif effect == "fire_damage":
        return _use_fire_crystal(player, world)
    
    return False

def _use_teleport_scroll(player, world):
    """Handle teleport scroll usage."""
    print_event("The scroll glows with mystical energy!", "mystery")
    print("You can teleport to any location you've visited before.")
    
    # Show available locations
    locations = list(world["locations"].keys())
    print("\\nAvailable locations:")
    for i, location in enumerate(locations, 1):
        print(f"{i}. {location}")
    
    try:
        choice = int(input("\\nChoose a location (number): ")) - 1
        if 0 <= choice < len(locations):
            target_location = locations[choice]
            player["location"] = target_location
            change_location(world, target_location)
            print_event(f"You teleport to {target_location}!", "success")
            
            # Consume the scroll
            player["inventory"].remove("teleport_scroll")
            return True
        else:
            print("Invalid choice. The scroll fizzles out.")
            return False
    except ValueError:
        print("Invalid input. The scroll remains unused.")
        return False

def _use_healing_potion(player):
    """Handle healing potion usage."""
    print_event("The potion glows with healing light!", "success")
    print("You drink the potion and feel your wounds healing.")
    
    heal_amount = random.randint(40, 60)
    heal_player(player, heal_amount)
    
    # Consume the potion
    player["inventory"].remove("healing_potion")
    return True

def _use_invisibility_cloak(player, world):
    """Handle invisibility cloak usage."""
    print_event("The cloak shimmers and you become invisible!", "mystery")
    print("You are now invisible to enemies for a short time.")
    
    # Add invisibility status (this would need game state support)
    if "status_effects" not in player:
        player["status_effects"] = {}
    
    player["status_effects"]["invisible"] = 3  # 3 turns of invisibility
    print("You feel the magic coursing through you.")
    
    return True

def _use_fire_crystal(player, world):
    """Handle fire crystal usage."""
    current_location = get_current_location(world)
    
    print_event("The crystal erupts in flames!", "danger")
    print("Fire spreads around you, affecting the area.")
    
    if current_location == "Forest":
        print("The forest catches fire! You must flee!")
        damage_player(player, 10)
        # Force move to a safe location
        player["location"] = "Village"
        change_location(world, "Village")
        print("You escape to the Village, singed but alive.")
    elif current_location == "Cave":
        print("The fire illuminates hidden passages in the cave!")
        add_item_to_inventory(player, "hidden_treasure")
        print("You discover a hidden treasure!")
    else:
        print("The fire burns harmlessly in the open area.")
        heal_player(player, 5)  # Warmth provides comfort
    
    return True

# Plugin registration functions
def register_items():
    """Register magic items with the game."""
    # This would integrate with the main item system
    from game import items
    
    # Add magic item descriptions
    for item_name, item_data in MAGIC_ITEMS.items():
        items.item_descriptions[item_name] = item_data["description"]
    
    # Register usage functions
    items.register_item_usage("teleport_scroll", lambda p, w: use_magic_item(p, "teleport_scroll", w))
    items.register_item_usage("healing_potion", lambda p, w: use_magic_item(p, "healing_potion", w))
    items.register_item_usage("invisibility_cloak", lambda p, w: use_magic_item(p, "invisibility_cloak", w))
    items.register_item_usage("fire_crystal", lambda p, w: use_magic_item(p, "fire_crystal", w))

def unregister_items():
    """Remove magic items from the game."""
    from game import items
    
    # Remove magic item descriptions
    for item_name in MAGIC_ITEMS.keys():
        if item_name in items.item_descriptions:
            del items.item_descriptions[item_name]
    
    # Unregister usage functions
    for item_name in MAGIC_ITEMS.keys():
        items.unregister_item_usage(item_name)

def initialize_plugin():
    """Initialize the magic items plugin."""
    print(f"Loading {PLUGIN_NAME} v{PLUGIN_VERSION}")
    register_items()
    return True

def cleanup_plugin():
    """Clean up the magic items plugin."""
    unregister_items()
    print(f"Unloading {PLUGIN_NAME}")
    return True
```

## Plugin Loading System

### Plugin Manager

Create a plugin manager to handle loading and unloading plugins:

```python
# game/plugin_manager.py
"""
Plugin management system for Kevin's Adventure Game.
"""

import os
import sys
import importlib
import traceback
from typing import Dict, List, Any

class PluginManager:
    """Manages game plugins."""
    
    def __init__(self):
        self.loaded_plugins: Dict[str, Any] = {}
        self.plugin_directory = "plugins"
        self.enabled_plugins: List[str] = []
    
    def discover_plugins(self) -> List[str]:
        """Discover available plugins in the plugins directory."""
        if not os.path.exists(self.plugin_directory):
            os.makedirs(self.plugin_directory)
            return []
        
        plugins = []
        for item in os.listdir(self.plugin_directory):
            plugin_path = os.path.join(self.plugin_directory, item)
            if os.path.isdir(plugin_path) and not item.startswith('_'):
                plugin_file = os.path.join(plugin_path, "plugin.py")
                if os.path.exists(plugin_file):
                    plugins.append(item)
        
        return plugins
    
    def load_plugin(self, plugin_name: str) -> bool:
        """Load a specific plugin."""
        try:
            # Add plugin directory to Python path
            plugin_path = os.path.join(self.plugin_directory, plugin_name)
            if plugin_path not in sys.path:
                sys.path.insert(0, plugin_path)
            
            # Import the plugin module
            module_name = f"{self.plugin_directory}.{plugin_name}.plugin"
            plugin_module = importlib.import_module(module_name)
            
            # Initialize the plugin
            if hasattr(plugin_module, 'initialize_plugin'):
                if plugin_module.initialize_plugin():
                    self.loaded_plugins[plugin_name] = plugin_module
                    self.enabled_plugins.append(plugin_name)
                    print(f"Successfully loaded plugin: {plugin_name}")
                    return True
                else:
                    print(f"Failed to initialize plugin: {plugin_name}")
                    return False
            else:
                print(f"Plugin {plugin_name} missing initialize_plugin function")
                return False
                
        except Exception as e:
            print(f"Error loading plugin {plugin_name}: {e}")
            traceback.print_exc()
            return False
    
    def unload_plugin(self, plugin_name: str) -> bool:
        """Unload a specific plugin."""
        if plugin_name not in self.loaded_plugins:
            print(f"Plugin {plugin_name} is not loaded")
            return False
        
        try:
            plugin_module = self.loaded_plugins[plugin_name]
            
            # Clean up the plugin
            if hasattr(plugin_module, 'cleanup_plugin'):
                plugin_module.cleanup_plugin()
            
            # Remove from loaded plugins
            del self.loaded_plugins[plugin_name]
            if plugin_name in self.enabled_plugins:
                self.enabled_plugins.remove(plugin_name)
            
            print(f"Successfully unloaded plugin: {plugin_name}")
            return True
            
        except Exception as e:
            print(f"Error unloading plugin {plugin_name}: {e}")
            traceback.print_exc()
            return False
    
    def load_all_plugins(self) -> None:
        """Load all discovered plugins."""
        plugins = self.discover_plugins()
        for plugin_name in plugins:
            self.load_plugin(plugin_name)
    
    def unload_all_plugins(self) -> None:
        """Unload all loaded plugins."""
        for plugin_name in list(self.loaded_plugins.keys()):
            self.unload_plugin(plugin_name)
    
    def get_plugin_info(self, plugin_name: str) -> Dict[str, Any]:
        """Get information about a plugin."""
        if plugin_name not in self.loaded_plugins:
            return {}
        
        plugin_module = self.loaded_plugins[plugin_name]
        if hasattr(plugin_module, 'get_plugin_info'):
            return plugin_module.get_plugin_info()
        
        return {"name": plugin_name, "status": "loaded"}
    
    def list_plugins(self) -> Dict[str, Dict[str, Any]]:
        """List all available and loaded plugins."""
        available = self.discover_plugins()
        result = {}
        
        for plugin_name in available:
            if plugin_name in self.loaded_plugins:
                result[plugin_name] = self.get_plugin_info(plugin_name)
                result[plugin_name]["status"] = "loaded"
            else:
                result[plugin_name] = {"name": plugin_name, "status": "available"}
        
        return result

# Global plugin manager instance
plugin_manager = PluginManager()
```

## Plugin Integration

### Integrating Plugins with the Main Game

Modify the main game files to support plugins:

```python
# main.py (modified to support plugins)
from game.plugin_manager import plugin_manager
from game.player import create_player, get_player_status
from game.world import get_current_location, initialize_world
from utils.save_load import list_save_files, load_game, save_game
from utils.text_formatting import print_help, print_welcome_message

def main():
    # Load plugins before starting the game
    print("Loading plugins...")
    plugin_manager.load_all_plugins()
    
    print_welcome_message()
    
    # ... rest of the main game loop ...
    
    # Unload plugins when exiting
    plugin_manager.unload_all_plugins()

if __name__ == "__main__":
    main()
```

### Plugin Commands

Add plugin management commands to the game:

```python
# game/actions.py (add plugin commands)
def perform_action(player, world, action):
    """Process and execute a player action."""
    action = action.lower().strip()
    
    # Plugin management commands
    if action == "plugins":
        show_plugins()
        return True
    elif action.startswith("load plugin "):
        plugin_name = action[12:]  # Remove "load plugin " prefix
        return load_plugin_command(plugin_name)
    elif action.startswith("unload plugin "):
        plugin_name = action[14:]  # Remove "unload plugin " prefix
        return unload_plugin_command(plugin_name)
    
    # ... existing action handling ...

def show_plugins():
    """Show available and loaded plugins."""
    from game.plugin_manager import plugin_manager
    
    plugins = plugin_manager.list_plugins()
    if not plugins:
        print("No plugins available.")
        return
    
    print("\\nAvailable Plugins:")
    print("=" * 40)
    for plugin_name, info in plugins.items():
        status = info.get("status", "unknown")
        version = info.get("version", "unknown")
        description = info.get("description", "No description")
        
        print(f"Name: {plugin_name}")
        print(f"Status: {status}")
        print(f"Version: {version}")
        print(f"Description: {description}")
        print("-" * 40)

def load_plugin_command(plugin_name):
    """Load a plugin via command."""
    from game.plugin_manager import plugin_manager
    
    if plugin_manager.load_plugin(plugin_name):
        print(f"Plugin '{plugin_name}' loaded successfully.")
        return True
    else:
        print(f"Failed to load plugin '{plugin_name}'.")
        return False

def unload_plugin_command(plugin_name):
    """Unload a plugin via command."""
    from game.plugin_manager import plugin_manager
    
    if plugin_manager.unload_plugin(plugin_name):
        print(f"Plugin '{plugin_name}' unloaded successfully.")
        return True
    else:
        print(f"Failed to unload plugin '{plugin_name}'.")
        return False
```

## Best Practices

### Plugin Development Guidelines

1. **Follow Naming Conventions**
   - Use descriptive plugin names
   - Follow Python naming conventions
   - Use consistent function naming

2. **Error Handling**
   - Handle errors gracefully
   - Provide meaningful error messages
   - Don't crash the main game

3. **Resource Management**
   - Clean up resources in cleanup_plugin()
   - Don't leave dangling references
   - Manage memory usage

4. **Documentation**
   - Document all plugin functions
   - Provide usage examples
   - Include configuration options

5. **Testing**
   - Test plugin functionality thoroughly
   - Test integration with main game
   - Test loading and unloading

### Plugin Security

1. **Input Validation**
   - Validate all user inputs
   - Sanitize file paths
   - Check data types and ranges

2. **Safe File Operations**
   - Use safe file handling practices
   - Don't execute arbitrary code
   - Validate file contents

3. **Isolation**
   - Keep plugin data separate
   - Don't modify core game files
   - Use proper namespacing

## Advanced Plugin Features

### Event System Integration

Plugins can hook into the game's event system:

```python
def register_event_handlers(event_manager):
    """Register plugin event handlers."""
    event_manager.register("player_move", on_player_move)
    event_manager.register("item_used", on_item_used)
    event_manager.register("location_entered", on_location_entered)

def on_player_move(player, old_location, new_location):
    """Handle player movement events."""
    if new_location == "Desert":
        print("The desert heat hits you immediately!")

def on_item_used(player, item, world):
    """Handle item usage events."""
    if item == "compass" and player["location"] == "Desert":
        print("The compass spins wildly in the desert!")

def on_location_entered(player, location, world):
    """Handle location entry events."""
    if location == "Desert" and "desert_visited" not in world.get("state", {}):
        print("You've never been to a place like this before...")
```

### Configuration System

Plugins can have configurable settings:

```python
# plugins/desert_plugin/config.json
{
    "enabled": true,
    "difficulty": "normal",
    "event_frequency": 0.3,
    "custom_items": ["desert_rose", "sand_dollar"],
    "weather_effects": true
}
```

### Plugin Dependencies

Plugins can depend on other plugins:

```python
def get_plugin_dependencies():
    """Return list of required plugins."""
    return ["base_weather", "extended_items"]

def check_dependencies():
    """Check if all dependencies are loaded."""
    from game.plugin_manager import plugin_manager
    
    dependencies = get_plugin_dependencies()
    for dep in dependencies:
        if dep not in plugin_manager.loaded_plugins:
            return False, f"Missing dependency: {dep}"
    
    return True, "All dependencies satisfied"
```

This plugin system provides a flexible foundation for extending Kevin's Adventure Game with custom content and functionality. Developers can create rich, interactive experiences while maintaining compatibility with the core game systems.

