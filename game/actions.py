"""
Enhanced action system for Kevin's Adventure Game with plugin support.
This integrates with the plugin system for extensible actions.
"""

from game.world import (
    change_location, 
    get_available_locations, 
    interact_with_location,
    get_current_location
)
from game.player import add_item_to_inventory
from plugins.manager import get_plugin_manager


def perform_action(player, world, action):
    """
    Perform an action in the game.
    Enhanced with plugin system support for extensible actions.
    """
    action = action.lower().strip()
    
    # Try plugin actions first
    plugin_manager = get_plugin_manager()
    if plugin_manager._initialized:
        if plugin_manager.handle_action(action, player, world):
            return
    
    # Movement actions
    if action in ["go", "move", "travel"]:
        print("Where would you like to go?")
        available = get_available_locations(world)
        print(f"Available locations: {', '.join(available)}")
        return
    
    # Check if action is a location name for movement
    available_locations = get_available_locations(world)
    for location in available_locations:
        if action == location.lower():
            if change_location(world, location):
                print(f"You travel to the {location}.")
                
                # Check if plugin handles this location
                if plugin_manager._initialized:
                    if plugin_manager.handle_location_entry(location, player, world):
                        return
                
                # Fall back to original location handling
                interact_with_location(world, player)
                return
            else:
                print(f"You cannot go to {location} from here.")
                return
    
    # Interaction actions
    if action in ["explore", "interact", "look"]:
        current_location = get_current_location(world)
        
        # Check if plugin handles this location
        if plugin_manager._initialized:
            if plugin_manager.handle_location_entry(current_location, player, world):
                return
        
        # Fall back to original interaction
        interact_with_location(world, player)
        return
    
    # Inventory actions
    if action in ["inventory", "inv", "items"]:
        print(f"Inventory: {', '.join(player['inventory']) if player['inventory'] else 'Empty'}")
        return
    
    # Status action
    if action in ["status", "stats"]:
        print(f"Name: {player['name']}")
        print(f"Health: {player['health']}")
        print(f"Gold: {player['gold']}")
        print(f"Location: {get_current_location(world)}")
        return
    
    # Plugin help
    if action in ["plugin", "plugins"]:
        if plugin_manager._initialized:
            status = plugin_manager.get_status()
            print("=== Plugin System Status ===")
            print(f"Locations: {status['plugin_counts']['locations']}")
            print(f"Actions: {status['plugin_counts']['actions']}")
            print(f"Mechanics: {status['plugin_counts']['mechanics']}")
            print(f"Hot-reload: {'Enabled' if status['hot_reload_enabled'] else 'Disabled'}")
        else:
            print("Plugin system not initialized.")
        return
    
    # Default response for unknown actions
    print(f"I don't understand '{action}'. Type 'help' for available commands.")

