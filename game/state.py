"""
Module for managing game state changes and updates.
"""

def update_world_state(world, state_change):
    """
    Update the world state based on a state change event.
    
    Args:
        world (dict): The world state dictionary
        state_change (str): The state change to apply
    
    Returns:
        bool: True if the state was updated successfully, False otherwise
    """
    # Initialize state tracking if it doesn't exist
    if "state" not in world:
        world["state"] = {
            "discovered_locations": [],
            "weather": "clear",
            "time_of_day": "day",
            "special_events": []
        }
    
    # Handle different state changes
    if state_change == "add_clearing":
        if "clearing" not in world["locations"]:
            world["locations"]["Clearing"] = {
                "description": "A beautiful forest clearing with a small pond and wildflowers.",
                "connections": ["Forest"],
                "items": ["flower", "water_flask"]
            }
            world["state"]["discovered_locations"].append("Clearing")
            return True
    
    elif state_change == "add_river":
        if "river" not in world["locations"]:
            world["locations"]["River"] = {
                "description": "A flowing river with clear water. Fish can be seen swimming beneath the surface.",
                "connections": ["Forest", "Village"],
                "items": ["fishing_rod", "water_flask"]
            }
            world["state"]["discovered_locations"].append("River")
            return True
    
    elif state_change == "discovered_underground_lake":
        if "Underground Lake" not in world["locations"]:
            world["locations"]["Underground Lake"] = {
                "description": "A serene underground lake with crystal-clear water that seems to glow with a faint blue light.",
                "connections": ["Cave"],
                "items": ["glowing_crystal", "healing_herb"]
            }
            world["state"]["discovered_locations"].append("Underground Lake")
            return True
    
    elif state_change.startswith("weather_"):
        weather = state_change.split("_")[1]
        world["state"]["weather"] = weather
        return True
    
    # Handle special events
    elif state_change == "dragon_awakened":
        world["state"]["special_events"].append("dragon_awakened")
        return True
    
    elif state_change == "village_festival":
        world["state"]["special_events"].append("village_festival")
        return True
    
    # If we reach here, the state change wasn't handled
    return False


def get_world_state(world, state_key=None):
    """
    Get the current world state or a specific state value.
    
    Args:
        world (dict): The world state dictionary
        state_key (str, optional): Specific state key to retrieve
    
    Returns:
        The requested state information or the entire state dict if no key is provided
    """
    # Initialize state if it doesn't exist
    if "state" not in world:
        world["state"] = {
            "discovered_locations": [],
            "weather": "clear",
            "time_of_day": "day",
            "special_events": []
        }
    
    if state_key:
        return world["state"].get(state_key)
    else:
        return world["state"]


def has_event_occurred(world, event_name):
    """
    Check if a specific event has occurred in the world.
    
    Args:
        world (dict): The world state dictionary
        event_name (str): The name of the event to check
    
    Returns:
        bool: True if the event has occurred, False otherwise
    """
    return event_name in get_world_state(world, "special_events")

