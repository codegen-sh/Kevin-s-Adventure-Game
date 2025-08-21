"""
State module for Kevin's Adventure Game.

This module contains functions for managing the game state.
"""
from game.weather import change_weather, get_current_weather


def update_world_state(world, event):
    """
    Update the world state based on an event.

    Args:
        world (dict): The game world state
        event (str): The event that occurred

    Returns:
        None
    """
    # Initialize world state if it doesn't exist
    if "state" not in world:
        world["state"] = {
            "discovered_locations": set(),
            "active_quests": [],
            "completed_quests": [],
            "time_of_day": "day",
            "days_passed": 0,
            "special_discoveries": set()
        }
    
    # Handle weather-related events
    if event.startswith("weather_"):
        weather_type = event.replace("weather_", "")
        world["weather"] = weather_type
        print(f"The weather has changed to {weather_type}.")
    
    # Handle location discoveries
    elif event.startswith("discover_") or event.startswith("add_"):
        location = event.replace("discover_", "").replace("add_", "")
        if location not in world["state"]["discovered_locations"]:
            world["state"]["discovered_locations"].add(location)
            print(f"You've discovered {location.replace('_', ' ')}!")
            
            # Add new location to the world if it doesn't exist
            if location == "clearing" and "Clearing" not in world["locations"]:
                world["locations"]["Clearing"] = {
                    "description": "A beautiful forest clearing with wildflowers and a small pond.",
                    "connections": ["Forest"],
                    "items": ["flower", "clear_water"]
                }
                world["locations"]["Forest"]["connections"].append("Clearing")
            
            elif location == "underground_lake" and "Underground Lake" not in world["locations"]:
                world["locations"]["Underground Lake"] = {
                    "description": "A vast underground lake with crystal-clear water that glows faintly.",
                    "connections": ["Cave"],
                    "items": ["glowing_fish", "pure_water"]
                }
                world["locations"]["Cave"]["connections"].append("Underground Lake")
            
            elif location == "hidden_cave" and "Hidden Cave" not in world["locations"]:
                world["locations"]["Hidden Cave"] = {
                    "description": "A small, hidden cave that seems to have been used as a shelter in the past.",
                    "connections": ["Mountain"],
                    "items": ["old_journal", "flint"]
                }
                world["locations"]["Mountain"]["connections"].append("Hidden Cave")
    
    # Handle revealing hidden paths or features
    elif event.startswith("reveal_"):
        feature = event.replace("reveal_", "")
        if feature == "hidden_path":
            print("You've discovered a hidden path!")
            # Logic for revealing a hidden path
        elif feature == "hidden_cave":
            print("You've discovered a hidden cave!")
            # Logic for revealing a hidden cave
        elif feature == "map":
            print("You can now see all locations on your map!")
            world["state"]["map_revealed"] = True
    
    # Handle quest-related events
    elif event.startswith("quest_"):
        quest_action, quest_name = event.replace("quest_", "").split("_", 1)
        
        if quest_action == "start":
            if quest_name not in world["state"]["active_quests"]:
                world["state"]["active_quests"].append(quest_name)
                print(f"You've started the quest: {quest_name.replace('_', ' ').title()}")
        
        elif quest_action == "complete":
            if quest_name in world["state"]["active_quests"]:
                world["state"]["active_quests"].remove(quest_name)
                world["state"]["completed_quests"].append(quest_name)
                print(f"You've completed the quest: {quest_name.replace('_', ' ').title()}")
                # Add rewards based on the quest
                if quest_name == "deliver_package":
                    print("You receive 50 gold as a reward!")
                    # Logic to add gold to player would go here
    
    # Handle time progression
    elif event == "advance_time":
        if world["state"]["time_of_day"] == "day":
            world["state"]["time_of_day"] = "night"
            print("The sun sets and night falls.")
        else:
            world["state"]["time_of_day"] = "day"
            world["state"]["days_passed"] += 1
            print("The sun rises on a new day.")
        
        # Weather has a chance to change with time
        if get_current_weather(world) != "stormy":  # Storms last longer
            new_weather = change_weather(world)
            print(f"The weather changes to {new_weather}.")
    
    # Handle creature-related events
    elif event.startswith("creature_"):
        creature_event = event.replace("creature_", "")
        print(f"A creature event has occurred: {creature_event}")
        # Logic for creature events would go here
    
    # Handle special discoveries
    elif event in ["ancient_ruins", "magical_spring", "abandoned_camp"]:
        if event not in world["state"]["special_discoveries"]:
            world["state"]["special_discoveries"].add(event)
            print(f"You've discovered {event.replace('_', ' ')}!")
    
    # Handle other events
    else:
        print(f"World state updated: {event}")


def get_world_state(world, key=None):
    """
    Get the current world state or a specific state value.

    Args:
        world (dict): The game world state
        key (str, optional): The specific state key to get. Defaults to None.

    Returns:
        The world state or a specific state value
    """
    if "state" not in world:
        world["state"] = {
            "discovered_locations": set(),
            "active_quests": [],
            "completed_quests": [],
            "time_of_day": "day",
            "days_passed": 0,
            "special_discoveries": set()
        }
    
    if key:
        return world["state"].get(key)
    return world["state"]


def set_world_state(world, key, value):
    """
    Set a specific world state value.

    Args:
        world (dict): The game world state
        key (str): The state key to set
        value: The value to set

    Returns:
        None
    """
    if "state" not in world:
        world["state"] = {
            "discovered_locations": set(),
            "active_quests": [],
            "completed_quests": [],
            "time_of_day": "day",
            "days_passed": 0,
            "special_discoveries": set()
        }
    
    world["state"][key] = value

