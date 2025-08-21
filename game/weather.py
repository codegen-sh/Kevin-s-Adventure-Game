"""
Module for handling weather in the game.
"""

import random
from enum import Enum, auto


class WeatherType(Enum):
    """Enum for weather types."""
    CLEAR = auto()
    CLOUDY = auto()
    RAINY = auto()
    STORMY = auto()
    FOGGY = auto()
    WINDY = auto()


class Weather:
    """
    A class to handle weather in the game.
    
    Attributes:
        current_weather (WeatherType): The current weather
        weather_descriptions (dict): Descriptions for each weather type
        weather_effects (dict): Effects for each weather type
    """
    
    def __init__(self, initial_weather=None):
        """
        Initialize a new Weather instance.
        
        Args:
            initial_weather (WeatherType, optional): The initial weather. Defaults to None.
        """
        self.current_weather = initial_weather if initial_weather else WeatherType.CLEAR
        self.weather_descriptions = {
            WeatherType.CLEAR: "The sky is clear and the sun is shining brightly.",
            WeatherType.CLOUDY: "Gray clouds cover the sky, blocking out the sun.",
            WeatherType.RAINY: "A steady rain is falling, creating puddles on the ground.",
            WeatherType.STORMY: "Dark clouds loom overhead as thunder rumbles in the distance.",
            WeatherType.FOGGY: "A thick fog has settled in, limiting visibility to just a few feet.",
            WeatherType.WINDY: "Strong gusts of wind blow through the area, rustling leaves and branches."
        }
        self.weather_effects = {
            WeatherType.CLEAR: {},
            WeatherType.CLOUDY: {},
            WeatherType.RAINY: {"agility": -2},
            WeatherType.STORMY: {"agility": -3, "perception": -3},
            WeatherType.FOGGY: {"perception": -4},
            WeatherType.WINDY: {"agility": -1}
        }
    
    def get_current_weather(self):
        """
        Get the current weather.
        
        Returns:
            WeatherType: The current weather
        """
        return self.current_weather
    
    def change_weather(self):
        """
        Change the weather randomly.
        
        Returns:
            WeatherType: The new weather
        """
        weather_types = list(WeatherType)
        new_weather = random.choice(weather_types)
        self.current_weather = new_weather
        return new_weather
    
    def set_weather(self, weather_type):
        """
        Set the weather to a specific type.
        
        Args:
            weather_type (WeatherType): The weather type to set
        """
        self.current_weather = weather_type
    
    def get_weather_description(self):
        """
        Get the description of the current weather.
        
        Returns:
            str: The weather description
        """
        return self.weather_descriptions.get(self.current_weather, "The weather is unremarkable.")
    
    def get_weather_effects(self):
        """
        Get the effects of the current weather.
        
        Returns:
            dict: The weather effects
        """
        return self.weather_effects.get(self.current_weather, {})
    
    def apply_weather_effects(self, player):
        """
        Apply the effects of the current weather to the player.
        
        Args:
            player: The player to apply the effects to
        """
        effects = self.get_weather_effects()
        
        for stat, modifier in effects.items():
            if hasattr(player, stat):
                original_value = getattr(player, stat)
                setattr(player, stat, max(1, original_value + modifier))
            elif isinstance(player, dict) and stat in player:
                player[stat] = max(1, player[stat] + modifier)
    
    def weather_forecast(self):
        """
        Get a forecast for the weather.
        
        Returns:
            str: A weather forecast
        """
        current_weather_name = self.current_weather.name.lower()
        future_weather = random.choice(["improve", "worsen", "stay the same"])
        
        if future_weather == "improve":
            return f"The current {current_weather_name} conditions are expected to improve soon."
        elif future_weather == "worsen":
            return f"The {current_weather_name} weather might get worse in the coming hours."
        else:
            return f"The {current_weather_name} weather is likely to persist for a while."
    
    def to_dict(self):
        """
        Convert the weather to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the weather
        """
        return {
            "current_weather": self.current_weather.name
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Weather instance from a dictionary.
        
        Args:
            data (dict): A dictionary representation of weather
        
        Returns:
            Weather: A new Weather instance
        """
        weather = cls()
        if "current_weather" in data:
            try:
                weather.current_weather = WeatherType[data["current_weather"]]
            except (KeyError, ValueError):
                weather.current_weather = WeatherType.CLEAR
        return weather


# Legacy functions for backward compatibility
def get_current_weather(world):
    """
    Get the current weather from the world.
    
    Args:
        world (dict): The world state
    
    Returns:
        str: The current weather
    """
    if hasattr(world, 'weather') and isinstance(world.weather, Weather):
        return world.weather.get_current_weather().name.lower()
    elif isinstance(world, dict):
        if "weather" not in world:
            world["weather"] = "clear"
        return world["weather"]
    return "clear"

def change_weather(world):
    """
    Change the weather in the world.
    
    Args:
        world (dict): The world state
    
    Returns:
        str: The new weather
    """
    if hasattr(world, 'weather') and isinstance(world.weather, Weather):
        new_weather = world.weather.change_weather()
        return new_weather.name.lower()
    elif isinstance(world, dict):
        weather_conditions = ["clear", "cloudy", "rainy", "stormy", "foggy", "windy"]
        new_weather = random.choice(weather_conditions)
        world["weather"] = new_weather
        return new_weather
    return "clear"

def apply_weather_effects(player, world):
    """
    Apply weather effects to the player.
    
    Args:
        player (dict): The player state
        world (dict): The world state
    """
    if hasattr(world, 'weather') and isinstance(world.weather, Weather):
        world.weather.apply_weather_effects(player)
        return
    
    current_weather = get_current_weather(world)
    
    if current_weather == "rainy":
        print("The rain is making the ground slippery. Be careful!")
        player["agility"] = max(1, player.get("agility", 10) - 2)
    elif current_weather == "stormy":
        print("The storm is making it hard to see and move around.")
        player["agility"] = max(1, player.get("agility", 10) - 3)
        player["perception"] = max(1, player.get("perception", 10) - 3)
    elif current_weather == "foggy":
        print("The fog is reducing visibility significantly.")
        player["perception"] = max(1, player.get("perception", 10) - 4)
    elif current_weather == "windy":
        print("The strong wind is making it difficult to move quickly.")
        player["agility"] = max(1, player.get("agility", 10) - 1)
    else:
        print("The weather is clear and doesn't affect your abilities.")

def describe_weather(world):
    """
    Get a description of the current weather.
    
    Args:
        world (dict): The world state
    
    Returns:
        str: A description of the current weather
    """
    if hasattr(world, 'weather') and isinstance(world.weather, Weather):
        return world.weather.get_weather_description()
    
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

def weather_forecast(world):
    """
    Get a forecast for the weather.
    
    Args:
        world (dict): The world state
    
    Returns:
        str: A weather forecast
    """
    if hasattr(world, 'weather') and isinstance(world.weather, Weather):
        return world.weather.weather_forecast()
    
    current_weather = get_current_weather(world)
    future_weather = random.choice(["improve", "worsen", "stay the same"])
    
    if future_weather == "improve":
        return f"The current {current_weather} conditions are expected to improve soon."
    elif future_weather == "worsen":
        return f"The {current_weather} weather might get worse in the coming hours."
    else:
        return f"The {current_weather} weather is likely to persist for a while."

