from locations.cave import explore_cave
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village
from config import config


def initialize_world():
    """Initialize the game world using configuration data."""
    world_config = config.get_world_config()
    world_data = world_config["world"]
    
    return {
        "current_location": world_data["starting_location"],
        "locations": world_data["locations"]
    }

def get_current_location(world):
    return world["current_location"]

def get_location_description(world, location):
    return world["locations"][location]["description"]

def get_available_locations(world):
    current_location = get_current_location(world)
    return world["locations"][current_location]["connections"]

def change_location(world, new_location):
    if new_location in get_available_locations(world):
        world["current_location"] = new_location
        return True
    return False

def interact_with_location(world, player):
    current_location = get_current_location(world)

    if current_location == "Forest":
        enter_forest(world, player)
    elif current_location == "Cave":
        explore_cave(world, player)
    elif current_location == "Village":
        visit_village(world, player)
    elif current_location == "Mountain":
        climb_mountain(world, player)
    else:
        print("There's nothing special to interact with here.")

def is_location_accessible(world, location):
    return location in get_available_locations(world)

def get_all_locations(world):
    return list(world["locations"].keys())
