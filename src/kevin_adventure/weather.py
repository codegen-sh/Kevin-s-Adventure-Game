"""
Weather module for Kevin's Adventure Game.
"""
import random
from typing import Dict, Optional

from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World


def get_current_weather(world: World) -> str:
    """
    Get the current weather in the world.

    Args:
        world: The game world

    Returns:
        The current weather
    """
    return world.weather


def change_weather(world: World) -> str:
    """
    Change the weather in the world.

    Args:
        world: The game world

    Returns:
        The new weather
    """
    weather_conditions = ["clear", "cloudy", "rainy", "stormy", "foggy", "windy"]
    new_weather = random.choice(weather_conditions)
    world.weather = new_weather
    return new_weather


def apply_weather_effects(player: Player, world: World) -> None:
    """
    Apply weather effects to the player.

    Args:
        player: The player to apply effects to
        world: The game world
    """
    current_weather = get_current_weather(world)

    if current_weather == "rainy":
        print("The rain is making the ground slippery. Be careful!")
        player.agility = max(1, player.agility - 2)
    elif current_weather == "stormy":
        print("The storm is making it hard to see and move around.")
        player.agility = max(1, player.agility - 3)
        player.perception = max(1, player.perception - 3)
    elif current_weather == "foggy":
        print("The fog is reducing visibility significantly.")
        player.perception = max(1, player.perception - 4)
    elif current_weather == "windy":
        print("The strong wind is making it difficult to move quickly.")
        player.agility = max(1, player.agility - 1)
    else:
        print("The weather is clear and doesn't affect your abilities.")


def describe_weather(world: World) -> str:
    """
    Get a description of the current weather.

    Args:
        world: The game world

    Returns:
        A description of the current weather
    """
    current_weather = get_current_weather(world)

    descriptions = {
        "clear": "The sky is clear and the sun is shining brightly.",
        "cloudy": "Gray clouds cover the sky, blocking out the sun.",
        "rainy": "A steady rain is falling, creating puddles on the ground.",
        "stormy": "Dark clouds loom overhead as thunder rumbles in the distance.",
        "foggy": "A thick fog has settled in, limiting visibility to just a few feet.",
        "windy": "Strong gusts of wind blow through the area, rustling leaves and branches."
    }

    return descriptions.get(current_weather, "The weather is unremarkable.")


def weather_forecast(world: World) -> str:
    """
    Get a forecast of the future weather.

    Args:
        world: The game world

    Returns:
        A forecast of the future weather
    """
    current_weather = get_current_weather(world)
    future_weather = random.choice(["improve", "worsen", "stay the same"])

    if future_weather == "improve":
        return f"The current {current_weather} conditions are expected to improve soon."
    elif future_weather == "worsen":
        return f"The {current_weather} weather might get worse in the coming hours."
    else:
        return f"The {current_weather} weather is likely to persist for a while."

