"""
State management module for Kevin's Adventure Game.
Contains functions for updating and managing the game state.
"""

def update_world_state(world, event):
    """
    Update the world state based on an event.
    
    Args:
        world (dict): The world state
        event (str): The event that occurred
    
    Returns:
        bool: True if the state was updated successfully, False otherwise
    """
    if event == "add_clearing":
        if "special_locations" not in world:
            world["special_locations"] = []
        if "forest_clearing" not in world["special_locations"]:
            world["special_locations"].append("forest_clearing")
            print("You've discovered a beautiful clearing in the forest!")
            return True
    
    elif event == "add_river":
        if "special_locations" not in world:
            world["special_locations"] = []
        if "forest_river" not in world["special_locations"]:
            world["special_locations"].append("forest_river")
            print("You've discovered a river flowing through the forest!")
            return True
    
    elif event == "add_hidden_cave":
        if "special_locations" not in world:
            world["special_locations"] = []
        if "hidden_cave" not in world["special_locations"]:
            world["special_locations"].append("hidden_cave")
            print("You've discovered a hidden cave!")
            return True
    
    elif event == "reveal_hidden_path":
        if "hidden_paths" not in world:
            world["hidden_paths"] = []
        if "forest_secret_path" not in world["hidden_paths"]:
            world["hidden_paths"].append("forest_secret_path")
            print("You've discovered a hidden path in the forest!")
            return True
    
    elif event == "reveal_map":
        world["map_revealed"] = True
        print("The entire map has been revealed to you!")
        return True
    
    elif event == "improve_visibility":
        world["visibility"] = "high"
        print("The clear weather improves visibility across the land.")
        return True
    
    elif event == "approaching_storm":
        world["weather"] = "stormy"
        print("A storm is approaching. Be careful!")
        return True
    
    elif event.startswith("weather_"):
        weather_type = event.split("_")[1]
        world["weather"] = weather_type
        print(f"The weather has changed to {weather_type}.")
        return True
    
    return False

def get_world_state(world, state_key):
    """
    Get a specific state value from the world.
    
    Args:
        world (dict): The world state
        state_key (str): The key of the state to get
    
    Returns:
        The value of the state, or None if it doesn't exist
    """
    return world.get(state_key, None)

def set_world_state(world, state_key, value):
    """
    Set a specific state value in the world.
    
    Args:
        world (dict): The world state
        state_key (str): The key of the state to set
        value: The value to set
    """
    world[state_key] = value
    return True
