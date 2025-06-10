"""
World module for the game.
"""
from locations.cave import explore_cave
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village


class World:
    """Class representing the game world."""
    
    def __init__(self):
        """Initialize the game world."""
        self.current_location = "Village"
        self.weather = "sunny"
        self.locations = {
            "Village": {
                "description": "A small, peaceful village with thatched-roof houses and friendly inhabitants.",
                "connections": ["Forest", "Mountain"],
                "items": ["map", "bread"]
            },
            "Forest": {
                "description": "A dense, mysterious forest with towering trees and the sound of rustling leaves.",
                "connections": ["Village", "Cave"],
                "items": ["stick", "berries"]
            },
            "Cave": {
                "description": "A dark, damp cave with echoing sounds and glittering minerals on the walls.",
                "connections": ["Forest"],
                "items": ["torch", "gemstone"]
            },
            "Mountain": {
                "description": "A tall, snow-capped mountain with treacherous paths and breathtaking views.",
                "connections": ["Village"],
                "items": ["rope", "pickaxe"]
            }
        }
    
    def get_current_location(self):
        """Get the current location."""
        return self.current_location
    
    def get_location_description(self, location):
        """Get the description of a location."""
        return self.locations[location]["description"]
    
    def get_available_locations(self):
        """Get the available locations from the current location."""
        return self.locations[self.current_location]["connections"]
    
    def change_location(self, new_location):
        """Change the current location."""
        if new_location in self.get_available_locations():
            self.current_location = new_location
            return True
        return False
    
    def interact_with_location(self, player):
        """Interact with the current location."""
        if self.current_location == "Forest":
            enter_forest(self, player)
        elif self.current_location == "Cave":
            explore_cave(self, player)
        elif self.current_location == "Village":
            visit_village(self, player)
        elif self.current_location == "Mountain":
            climb_mountain(self, player)
        else:
            print("There's nothing special to interact with here.")
    
    def is_location_accessible(self, location):
        """Check if a location is accessible from the current location."""
        return location in self.get_available_locations()
    
    def get_all_locations(self):
        """Get all locations in the world."""
        return list(self.locations.keys())
    
    def change_weather(self, new_weather):
        """Change the current weather."""
        self.weather = new_weather
        print(f"The weather changes to {new_weather}.")
    
    def get_weather(self):
        """Get the current weather."""
        return self.weather
    
    def update_world_state(self, state_change):
        """Update the world state based on a state change."""
        if state_change.startswith("weather_"):
            new_weather = state_change[8:]  # Remove "weather_" prefix
            self.change_weather(new_weather)
        elif state_change == "add_hidden_cave":
            if "Hidden Cave" not in self.locations:
                self.locations["Hidden Cave"] = {
                    "description": "A hidden cave with ancient artifacts and mysterious symbols.",
                    "connections": ["Forest"],
                    "items": ["ancient_scroll", "magic_crystal"]
                }
                self.locations["Forest"]["connections"].append("Hidden Cave")
                print("A new location has been discovered: Hidden Cave")


# Compatibility functions for legacy code
def initialize_world():
    """Initialize the game world."""
    return {
        "current_location": "Village",
        "weather": "sunny",
        "locations": {
            "Village": {
                "description": "A small, peaceful village with thatched-roof houses and friendly inhabitants.",
                "connections": ["Forest", "Mountain"],
                "items": ["map", "bread"]
            },
            "Forest": {
                "description": "A dense, mysterious forest with towering trees and the sound of rustling leaves.",
                "connections": ["Village", "Cave"],
                "items": ["stick", "berries"]
            },
            "Cave": {
                "description": "A dark, damp cave with echoing sounds and glittering minerals on the walls.",
                "connections": ["Forest"],
                "items": ["torch", "gemstone"]
            },
            "Mountain": {
                "description": "A tall, snow-capped mountain with treacherous paths and breathtaking views.",
                "connections": ["Village"],
                "items": ["rope", "pickaxe"]
            }
        }
    }


def get_current_location(world):
    """Get the current location."""
    if isinstance(world, World):
        return world.get_current_location()
    else:
        # Legacy support for dictionary-based world
        return world["current_location"]


def get_location_description(world, location):
    """Get the description of a location."""
    if isinstance(world, World):
        return world.get_location_description(location)
    else:
        # Legacy support for dictionary-based world
        return world["locations"][location]["description"]


def get_available_locations(world):
    """Get the available locations from the current location."""
    if isinstance(world, World):
        return world.get_available_locations()
    else:
        # Legacy support for dictionary-based world
        current_location = get_current_location(world)
        return world["locations"][current_location]["connections"]


def change_location(world, new_location):
    """Change the current location."""
    if isinstance(world, World):
        return world.change_location(new_location)
    else:
        # Legacy support for dictionary-based world
        if new_location in get_available_locations(world):
            world["current_location"] = new_location
            return True
        return False


def interact_with_location(world, player):
    """Interact with the current location."""
    if isinstance(world, World):
        world.interact_with_location(player)
    else:
        # Legacy support for dictionary-based world
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
    """Check if a location is accessible from the current location."""
    if isinstance(world, World):
        return world.is_location_accessible(location)
    else:
        # Legacy support for dictionary-based world
        return location in get_available_locations(world)


def get_all_locations(world):
    """Get all locations in the world."""
    if isinstance(world, World):
        return world.get_all_locations()
    else:
        # Legacy support for dictionary-based world
        return list(world["locations"].keys())


def change_weather(world, new_weather):
    """Change the current weather."""
    if isinstance(world, World):
        world.change_weather(new_weather)
    else:
        # Legacy support for dictionary-based world
        world["weather"] = new_weather
        print(f"The weather changes to {new_weather}.")


def get_weather(world):
    """Get the current weather."""
    if isinstance(world, World):
        return world.get_weather()
    else:
        # Legacy support for dictionary-based world
        return world.get("weather", "sunny")


def update_world_state(world, state_change):
    """Update the world state based on a state change."""
    if isinstance(world, World):
        world.update_world_state(state_change)
    else:
        # Legacy support for dictionary-based world
        if state_change.startswith("weather_"):
            new_weather = state_change[8:]  # Remove "weather_" prefix
            change_weather(world, new_weather)
        elif state_change == "add_hidden_cave":
            if "Hidden Cave" not in world["locations"]:
                world["locations"]["Hidden Cave"] = {
                    "description": "A hidden cave with ancient artifacts and mysterious symbols.",
                    "connections": ["Forest"],
                    "items": ["ancient_scroll", "magic_crystal"]
                }
                world["locations"]["Forest"]["connections"].append("Hidden Cave")
                print("A new location has been discovered: Hidden Cave")

