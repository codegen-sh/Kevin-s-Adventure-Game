"""
Weather module for Kevin's Adventure Game.
Contains the Weather class that manages weather conditions.
"""
import random
from typing import Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.player import Player
    from src.game.world import World


class Weather:
    """
    Manages weather conditions in the game world.
    """

    # Weather conditions and their descriptions
    WEATHER_DESCRIPTIONS = {
        "clear": "The sky is clear and the sun is shining brightly.",
        "cloudy": "Gray clouds cover the sky, blocking out the sun.",
        "rainy": "A steady rain is falling, creating puddles on the ground.",
        "stormy": "Dark clouds loom overhead as thunder rumbles in the distance.",
        "foggy": "A thick fog has settled in, limiting visibility to just a few feet.",
        "windy": "Strong gusts of wind blow through the area, rustling leaves and branches."
    }

    # Weather effects on player attributes
    WEATHER_EFFECTS = {
        "clear": {},
        "cloudy": {},
        "rainy": {"agility": -2},
        "stormy": {"agility": -3, "perception": -3},
        "foggy": {"perception": -4},
        "windy": {"agility": -1}
    }

    def __init__(self):
        """Initialize the weather system."""
        self.current_weather = "clear"
        self.weather_conditions = list(self.WEATHER_DESCRIPTIONS.keys())

    def get_current_weather(self) -> str:
        """
        Get the current weather condition.

        Returns:
            The current weather condition
        """
        return self.current_weather

    def change_weather(self) -> str:
        """
        Change the weather to a random condition.

        Returns:
            The new weather condition
        """
        self.current_weather = random.choice(self.weather_conditions)
        return self.current_weather

    def apply_weather_effects(self, player: 'Player') -> None:
        """
        Apply weather effects to the player.

        Args:
            player: The player to apply effects to
        """
        effects = self.WEATHER_EFFECTS.get(self.current_weather, {})
        
        # Reset attributes to default values
        player.agility = 10
        player.perception = 10
        
        # Apply weather-specific effects
        for attribute, modifier in effects.items():
            if attribute == "agility":
                player.agility = max(1, player.agility + modifier)
            elif attribute == "perception":
                player.perception = max(1, player.perception + modifier)
        
        # Describe the effects to the player
        if effects:
            effect_desc = self._get_weather_effect_description()
            print(effect_desc)
        else:
            print("The weather is clear and doesn't affect your abilities.")

    def _get_weather_effect_description(self) -> str:
        """
        Get a description of the current weather effects.

        Returns:
            A description of the weather effects
        """
        if self.current_weather == "rainy":
            return "The rain is making the ground slippery. Be careful!"
        elif self.current_weather == "stormy":
            return "The storm is making it hard to see and move around."
        elif self.current_weather == "foggy":
            return "The fog is reducing visibility significantly."
        elif self.current_weather == "windy":
            return "The strong wind is making it difficult to move quickly."
        return "The weather doesn't seem to be affecting you."

    def describe_weather(self) -> str:
        """
        Get a description of the current weather.

        Returns:
            A description of the current weather
        """
        return self.WEATHER_DESCRIPTIONS.get(
            self.current_weather, 
            "The weather is unremarkable."
        )

    def forecast(self) -> str:
        """
        Get a weather forecast.

        Returns:
            A weather forecast message
        """
        future_weather = random.choice(["improve", "worsen", "stay the same"])

        if future_weather == "improve":
            return f"The current {self.current_weather} conditions are expected to improve soon."
        elif future_weather == "worsen":
            return f"The {self.current_weather} weather might get worse in the coming hours."
        else:
            return f"The {self.current_weather} weather is likely to persist for a while."

