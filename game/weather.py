"""
Weather module for Kevin's Adventure Game.

This module contains functions for managing weather in the game.
"""
import random
from typing import Dict, Union


def get_current_weather(world: Dict[str, Union[str, Dict]]) -> str:
    """
    Get the current weather.
    
    Args:
        world (dict): The game world state
        
    Returns:
        str: The current weather
    """
    if "weather" not in world:
        world["weather"] = "clear"
    return world["weather"]


def change_weather(world: Dict[str, Union[str, Dict]]) -> str:
    """
    Change the weather randomly.
    
    Args:
        world (dict): The game world state
        
    Returns:
        str: The new weather
    """
    weather_conditions = ["clear", "cloudy", "rainy", "stormy", "foggy", "windy"]
    # Weighted random choice - current weather has a higher chance to persist
    current_weather = get_current_weather(world)
    weights = [2 if w == current_weather else 1 for w in weather_conditions]
    new_weather = random.choices(weather_conditions, weights=weights, k=1)[0]
    world["weather"] = new_weather
    return new_weather


def apply_weather_effects(player, world: Dict[str, Union[str, Dict]]) -> None:
    """
    Apply weather effects to the player.
    
    Args:
        player: The player
        world (dict): The game world state
    """
    current_weather = get_current_weather(world)
    
    # Initialize or reset player stats if they don't exist
    if isinstance(player, dict):
        if "stats" not in player:
            player["stats"] = {
                "strength": 10,
                "agility": 10,
                "perception": 10
            }
        stats = player["stats"]
    else:
        stats = player.stats
    
    # Reset stats to base values
    stats["strength"] = 10
    stats["agility"] = 10
    stats["perception"] = 10
    
    # Apply weather effects
    if current_weather == "rainy":
        print("The rain is making the ground slippery. Be careful!")
        stats["agility"] = max(1, stats["agility"] - 2)
    elif current_weather == "stormy":
        print("The storm is making it hard to see and move around.")
        stats["agility"] = max(1, stats["agility"] - 3)
        stats["perception"] = max(1, stats["perception"] - 3)
    elif current_weather == "foggy":
        print("The fog is reducing visibility significantly.")
        stats["perception"] = max(1, stats["perception"] - 4)
    elif current_weather == "windy":
        print("The strong wind is making it difficult to move quickly.")
        stats["agility"] = max(1, stats["agility"] - 1)
    else:  # clear or cloudy
        print("The weather is pleasant and doesn't affect your abilities.")


def describe_weather(world: Dict[str, Union[str, Dict]]) -> str:
    """
    Get a description of the current weather.
    
    Args:
        world (dict): The game world state
        
    Returns:
        str: A description of the current weather
    """
    current_weather = get_current_weather(world)
    time_of_day = world.get("state", {}).get("time_of_day", "day")
    
    descriptions = {
        "clear": {
            "day": "The sky is clear and the sun is shining brightly.",
            "night": "The sky is clear, revealing a beautiful starry night."
        },
        "cloudy": {
            "day": "Gray clouds cover the sky, blocking out the sun.",
            "night": "Thick clouds obscure the stars, making the night darker."
        },
        "rainy": {
            "day": "A steady rain is falling, creating puddles on the ground.",
            "night": "Rain falls steadily through the dark night."
        },
        "stormy": {
            "day": "Dark clouds loom overhead as thunder rumbles and lightning flashes.",
            "night": "Lightning illuminates the night sky as thunder crashes around you."
        },
        "foggy": {
            "day": "A thick fog has settled in, limiting visibility to just a few feet.",
            "night": "A dense fog makes the night even darker and more mysterious."
        },
        "windy": {
            "day": "Strong gusts of wind blow through the area, rustling leaves and branches.",
            "night": "The wind howls through the darkness, creating eerie sounds."
        }
    }
    
    return descriptions.get(current_weather, {}).get(time_of_day, "The weather is unremarkable.")


def weather_forecast(world: Dict[str, Union[str, Dict]]) -> str:
    """
    Get a forecast of the weather.
    
    Args:
        world (dict): The game world state
        
    Returns:
        str: A forecast of the weather
    """
    current_weather = get_current_weather(world)
    future_weather = random.choice(["improve", "worsen", "stay the same"])
    
    if future_weather == "improve":
        return f"The current {current_weather} conditions are expected to improve soon."
    elif future_weather == "worsen":
        return f"The {current_weather} weather might get worse in the coming hours."
    else:
        return f"The {current_weather} weather is likely to persist for a while."


def get_weather_effects(weather: str) -> Dict[str, int]:
    """
    Get the effects of a weather condition.
    
    Args:
        weather (str): The weather condition
        
    Returns:
        Dict[str, int]: The effects of the weather
    """
    effects = {
        "clear": {"visibility": 10, "movement": 10, "comfort": 10},
        "cloudy": {"visibility": 8, "movement": 9, "comfort": 8},
        "rainy": {"visibility": 6, "movement": 7, "comfort": 5},
        "stormy": {"visibility": 3, "movement": 4, "comfort": 2},
        "foggy": {"visibility": 2, "movement": 8, "comfort": 6},
        "windy": {"visibility": 7, "movement": 6, "comfort": 4}
    }
    
    return effects.get(weather, {"visibility": 10, "movement": 10, "comfort": 10})

