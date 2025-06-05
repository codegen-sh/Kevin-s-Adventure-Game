from typing import Dict, Any, List
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village
from game.constants import Locations


def initialize_world() -> Dict[str, Any]:
    """Initialize the game world with all locations and their properties."""
    world = {
        "current_location": Locations.VILLAGE,
        "weather": "sunny",
        "locations": {
            Locations.VILLAGE: {
                "description": "A peaceful village with friendly inhabitants. You can see a shop, an inn, and villagers going about their daily business.",
                "items": ["bread", "map"],
                "accessible_from": [Locations.FOREST, Locations.MOUNTAIN],
                "connections": [Locations.FOREST, Locations.MOUNTAIN]
            },
            Locations.FOREST: {
                "description": "A dense, mysterious forest filled with tall trees and hidden paths. Sunlight filters through the canopy above.",
                "items": ["stick", "berries"],
                "accessible_from": [Locations.VILLAGE, Locations.MOUNTAIN],
                "connections": [Locations.VILLAGE, Locations.MOUNTAIN]
            },
            Locations.MOUNTAIN: {
                "description": "A towering mountain with rocky paths and breathtaking views. The air is thin and crisp here.",
                "items": ["rope", "mountain_herbs"],
                "accessible_from": [Locations.VILLAGE, Locations.FOREST],
                "connections": [Locations.VILLAGE, Locations.FOREST]
            }
        }
    }
    return world

def get_current_location(world: Dict[str, Any]) -> str:
    return world["current_location"]

def get_location_description(world: Dict[str, Any], location: str) -> str:
    return world["locations"][location]["description"]

def get_available_locations(world: Dict[str, Any]) -> List[str]:
    current_location = get_current_location(world)
    return world["locations"][current_location]["connections"]

def change_location(world: Dict[str, Any], new_location: str) -> bool:
    if new_location in get_available_locations(world):
        world["current_location"] = new_location
        return True
    return False

def interact_with_location(world: Dict[str, Any], player: Any) -> None:
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

def is_location_accessible(world: Dict[str, Any], location: str) -> bool:
    return location in get_available_locations(world)

def get_all_locations(world: Dict[str, Any]) -> List[str]:
    return list(world["locations"].keys())
