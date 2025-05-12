"""
Module for managing weather effects in the game.
"""
import random

from game.player import damage_player, heal_player
from game.state import get_world_state, update_world_state
from utils.text_formatting import print_event


def initialize_weather(world):
    """
    Initialize the weather system in the world.
    
    Args:
        world (dict): The world state dictionary
    """
    weather_types = ["clear", "cloudy", "rainy", "foggy", "stormy", "windy"]
    initial_weather = random.choice(weather_types)
    update_world_state(world, f"weather_{initial_weather}")
    print_event(f"The weather is {initial_weather}.")


def get_current_weather(world):
    """
    Get the current weather in the world.
    
    Args:
        world (dict): The world state dictionary
    
    Returns:
        str: The current weather condition
    """
    return get_world_state(world, "weather") or "clear"


def change_weather(world, new_weather=None):
    """
    Change the weather in the world.
    
    Args:
        world (dict): The world state dictionary
        new_weather (str, optional): The new weather to set. If None, a random weather is chosen.
    
    Returns:
        str: The new weather condition
    """
    weather_types = ["clear", "cloudy", "rainy", "foggy", "stormy", "windy"]
    
    if new_weather is None:
        current_weather = get_current_weather(world)
        # Exclude the current weather to ensure a change
        possible_weathers = [w for w in weather_types if w != current_weather]
        new_weather = random.choice(possible_weathers)
    
    update_world_state(world, f"weather_{new_weather}")
    print_event(f"The weather changes to {new_weather}.")
    return new_weather


def apply_weather_effects(world, player):
    """
    Apply effects of the current weather to the player.
    
    Args:
        world (dict): The world state dictionary
        player (dict): The player's state
    """
    current_weather = get_current_weather(world)
    current_location = player["location"]
    
    # Different weather effects based on location and weather type
    if current_location in ["Forest", "Mountain", "Village"]:
        # These locations are affected by weather
        if current_weather == "rainy":
            print("The rain makes the ground slippery.")
            if random.random() < 0.2:  # 20% chance
                print("You slip and fall, taking minor damage.")
                damage_player(player, 5)
        
        elif current_weather == "stormy":
            print("The storm is fierce, with lightning and strong winds.")
            if random.random() < 0.3:  # 30% chance
                print("Lightning strikes nearby, startling you!")
                damage_player(player, 10)
        
        elif current_weather == "foggy":
            print("The thick fog makes it difficult to see far ahead.")
            # No direct damage, but could affect other game mechanics
        
        elif current_weather == "clear":
            print("The clear weather lifts your spirits.")
            if random.random() < 0.2:  # 20% chance
                print("The pleasant weather makes you feel better.")
                heal_player(player, 5)
    
    elif current_location == "Cave":
        # Cave is mostly sheltered from weather
        if current_weather in ["rainy", "stormy"]:
            print("You can hear the sound of rain and thunder outside, but you're safe in the cave.")
        else:
            print("The weather outside doesn't affect you much in the cave.")


def get_weather_description(weather):
    """
    Get a detailed description of a weather condition.
    
    Args:
        weather (str): The weather condition
    
    Returns:
        str: A detailed description of the weather
    """
    descriptions = {
        "clear": "The sky is clear and blue, with the sun shining brightly. It's a perfect day for exploration.",
        "cloudy": "Gray clouds cover the sky, blocking the sun and casting a dull light over the land.",
        "rainy": "Rain falls steadily from dark clouds, creating puddles and making the ground muddy and slippery.",
        "foggy": "A thick fog has settled, limiting visibility and giving the surroundings a mysterious atmosphere.",
        "stormy": "Dark storm clouds fill the sky, with lightning flashing and thunder rumbling. The wind howls fiercely.",
        "windy": "Strong winds blow through the area, bending trees and carrying leaves and debris through the air."
    }
    
    return descriptions.get(weather, f"The weather is {weather}.")

