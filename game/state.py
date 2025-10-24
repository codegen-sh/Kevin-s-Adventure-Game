"""
Module for handling game state changes.
"""

def update_world_state(world, state_change):
    """
    Update the world state based on a state change event.
    
    Args:
        world (dict): The world state
        state_change (str): The state change to apply
    """
    if state_change.startswith("weather_"):
        # Update weather
        weather = state_change.split("_")[1]
        world["weather"] = weather
        print(f"The weather has changed to {weather}.")
    
    elif state_change == "add_hidden_cave":
        # Add a hidden cave to special locations if not already there
        if "hidden_cave" not in world.get("special_locations", []):
            if "special_locations" not in world:
                world["special_locations"] = []
            world["special_locations"].append("hidden_cave")
            
            # Add the hidden cave as a connection from the current location
            from game.world import get_current_location
            current_location = get_current_location(world)
            if "Hidden Cave" not in world["locations"][current_location]["connections"]:
                world["locations"][current_location]["connections"].append("Hidden Cave")
            
            # Add the hidden cave as a new location if it doesn't exist
            if "Hidden Cave" not in world["locations"]:
                world["locations"]["Hidden Cave"] = {
                    "description": "A mysterious cave hidden behind dense foliage. Strange glowing crystals illuminate the interior.",
                    "connections": [current_location],
                    "items": ["crystal", "ancient_scroll"]
                }
    
    elif state_change == "unlock_mountain_path":
        # Unlock a new path on the mountain
        if "Mountain Peak" not in world["locations"]:
            world["locations"]["Mountain Peak"] = {
                "description": "The breathtaking peak of the mountain, offering a panoramic view of the entire region.",
                "connections": ["Mountain"],
                "items": ["binoculars", "rare_herb"]
            }
            world["locations"]["Mountain"]["connections"].append("Mountain Peak")
            print("You've discovered a path to the Mountain Peak!")

