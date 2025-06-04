"""
Weather mechanic plugin - Example game mechanic plugin for Kevin's Adventure Game.
"""

from plugins.base import BaseGameMechanic, PluginMetadata
from game.world import get_current_location
from game.player import damage_player, heal_player
from utils.random_events import generate_random_event
from typing import Dict, Any
import random


class WeatherMechanic(BaseGameMechanic):
    """A weather system mechanic that affects gameplay."""
    
    def __init__(self):
        super().__init__()
        self.current_weather = "clear"
        self.weather_duration = 0
        self.turn_count = 0
    
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="WeatherMechanic",
            version="1.0.0",
            description="Dynamic weather system that affects gameplay and player actions",
            author="Plugin Developer"
        )
    
    def initialize(self) -> bool:
        """Initialize the weather mechanic plugin."""
        self.current_weather = "clear"
        self.weather_duration = random.randint(3, 7)
        return True
    
    def cleanup(self) -> None:
        """Clean up weather mechanic resources."""
        pass
    
    def on_game_start(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called when a new game starts."""
        self.current_weather = "clear"
        self.weather_duration = random.randint(3, 7)
        self.turn_count = 0
        print("The weather system is now active!")
        self._announce_weather()
    
    def on_game_load(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called when a game is loaded."""
        # Restore weather state from world data if available
        weather_data = world.get("weather_mechanic", {})
        self.current_weather = weather_data.get("current_weather", "clear")
        self.weather_duration = weather_data.get("weather_duration", 3)
        self.turn_count = weather_data.get("turn_count", 0)
    
    def on_game_save(self, player: Dict[str, Any], world: Dict[str, Any]) -> Dict[str, Any]:
        """Called when game is saved."""
        return {
            "current_weather": self.current_weather,
            "weather_duration": self.weather_duration,
            "turn_count": self.turn_count
        }
    
    def on_turn_start(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called at the start of each turn."""
        self.turn_count += 1
        
        # Check if weather should change
        self.weather_duration -= 1
        if self.weather_duration <= 0:
            self._change_weather()
        
        # Apply weather effects
        self._apply_weather_effects(player, world)
    
    def on_turn_end(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called at the end of each turn."""
        # Weather effects that happen at turn end
        if self.current_weather == "blizzard":
            current_location = get_current_location(world)
            if current_location == "Mountain":
                print("The blizzard intensifies! You struggle to stay warm.")
                if "winter_cloak" not in player.get("inventory", []):
                    damage_player(player, 8)
    
    def _change_weather(self) -> None:
        """Change the current weather."""
        weather_options = [
            ("clear", 30),
            ("cloudy", 25),
            ("rain", 20),
            ("storm", 10),
            ("fog", 10),
            ("snow", 5)
        ]
        
        # Adjust probabilities based on current weather
        if self.current_weather == "rain":
            # More likely to have storm after rain
            weather_options = [
                ("clear", 20),
                ("cloudy", 20),
                ("rain", 15),
                ("storm", 25),
                ("fog", 15),
                ("snow", 5)
            ]
        elif self.current_weather == "snow":
            # More likely to have blizzard after snow
            weather_options = [
                ("clear", 15),
                ("cloudy", 20),
                ("rain", 5),
                ("storm", 10),
                ("fog", 10),
                ("snow", 20),
                ("blizzard", 20)
            ]
        
        old_weather = self.current_weather
        self.current_weather = generate_random_event(events=weather_options)
        self.weather_duration = random.randint(2, 6)
        
        if self.current_weather != old_weather:
            self._announce_weather_change(old_weather)
    
    def _announce_weather(self) -> None:
        """Announce the current weather."""
        weather_descriptions = {
            "clear": "The sky is clear and bright.",
            "cloudy": "Clouds gather overhead, blocking some sunlight.",
            "rain": "Rain begins to fall steadily.",
            "storm": "A fierce storm rages with thunder and lightning!",
            "fog": "Thick fog rolls in, reducing visibility.",
            "snow": "Snow begins to fall gently from the sky.",
            "blizzard": "A dangerous blizzard sweeps across the land!"
        }
        
        description = weather_descriptions.get(self.current_weather, "The weather is unusual.")
        print(f"Weather: {description}")
    
    def _announce_weather_change(self, old_weather: str) -> None:
        """Announce a weather change."""
        print(f"\\n--- Weather Change ---")
        
        transitions = {
            ("clear", "cloudy"): "Clouds begin to gather in the sky.",
            ("cloudy", "rain"): "The clouds open up and rain begins to fall.",
            ("rain", "storm"): "The rain intensifies into a fierce storm!",
            ("storm", "clear"): "The storm passes and the sky clears.",
            ("fog", "clear"): "The fog lifts, revealing clear skies.",
            ("snow", "blizzard"): "The gentle snow becomes a raging blizzard!",
            ("blizzard", "snow"): "The blizzard calms to gentle snowfall."
        }
        
        transition = transitions.get((old_weather, self.current_weather))
        if transition:
            print(transition)
        else:
            self._announce_weather()
    
    def _apply_weather_effects(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Apply weather effects to the player and world."""
        current_location = get_current_location(world)
        
        if self.current_weather == "rain":
            self._apply_rain_effects(player, world, current_location)
        elif self.current_weather == "storm":
            self._apply_storm_effects(player, world, current_location)
        elif self.current_weather == "fog":
            self._apply_fog_effects(player, world, current_location)
        elif self.current_weather == "snow":
            self._apply_snow_effects(player, world, current_location)
        elif self.current_weather == "blizzard":
            self._apply_blizzard_effects(player, world, current_location)
    
    def _apply_rain_effects(self, player: Dict[str, Any], world: Dict[str, Any], location: str) -> None:
        """Apply rain weather effects."""
        if location == "Forest":
            # Rain makes forest exploration more dangerous
            if random.random() < 0.1:  # 10% chance
                print("You slip on the wet forest floor!")
                damage_player(player, 3)
        elif location == "Desert":
            # Rain in desert is beneficial
            if random.random() < 0.2:  # 20% chance
                print("The rare desert rain refreshes you!")
                heal_player(player, 5)
    
    def _apply_storm_effects(self, player: Dict[str, Any], world: Dict[str, Any], location: str) -> None:
        """Apply storm weather effects."""
        if location in ["Mountain", "Desert"]:
            # Storms are dangerous in exposed areas
            if random.random() < 0.15:  # 15% chance
                print("Lightning strikes nearby! You take cover.")
                damage_player(player, 10)
                if "metal_armor" in player.get("inventory", []):
                    print("Your metal armor attracts lightning!")
                    damage_player(player, 5)
    
    def _apply_fog_effects(self, player: Dict[str, Any], world: Dict[str, Any], location: str) -> None:
        """Apply fog weather effects."""
        # Fog reduces visibility and can cause confusion
        if random.random() < 0.1:  # 10% chance
            print("The thick fog disorients you.")
            if location == "Forest":
                print("You get turned around in the foggy forest.")
            elif location == "Mountain":
                print("The fog makes the mountain paths treacherous.")
                damage_player(player, 5)
    
    def _apply_snow_effects(self, player: Dict[str, Any], world: Dict[str, Any], location: str) -> None:
        """Apply snow weather effects."""
        if location == "Mountain":
            # Snow makes mountain travel slower and colder
            if "warm_clothes" not in player.get("inventory", []):
                if random.random() < 0.1:  # 10% chance
                    print("The cold mountain snow chills you to the bone.")
                    damage_player(player, 5)
        elif location == "Village":
            # Snow in village can be pleasant
            if random.random() < 0.05:  # 5% chance
                print("The peaceful snowfall in the village is beautiful and calming.")
                heal_player(player, 3)
    
    def _apply_blizzard_effects(self, player: Dict[str, Any], world: Dict[str, Any], location: str) -> None:
        """Apply blizzard weather effects."""
        # Blizzards are dangerous everywhere but especially on mountains
        if location == "Mountain":
            print("The blizzard makes mountain travel extremely dangerous!")
            if "winter_gear" not in player.get("inventory", []):
                damage_player(player, 15)
        elif location == "Desert":
            # Blizzard in desert is very unusual
            print("A freak blizzard in the desert! This is highly unusual.")
            damage_player(player, 8)
        else:
            if random.random() < 0.2:  # 20% chance
                print("The blizzard forces you to seek shelter.")
                damage_player(player, 7)
    
    def get_weather_status(self) -> str:
        """Get current weather status for display."""
        weather_names = {
            "clear": "Clear",
            "cloudy": "Cloudy", 
            "rain": "Rainy",
            "storm": "Stormy",
            "fog": "Foggy",
            "snow": "Snowy",
            "blizzard": "Blizzard"
        }
        
        name = weather_names.get(self.current_weather, "Unknown")
        return f"{name} (for {self.weather_duration} more turns)"
    
    def get_weather_advice(self, location: str) -> str:
        """Get weather-specific advice for the current location."""
        advice = {
            ("rain", "Forest"): "Be careful of slippery paths in the forest.",
            ("rain", "Desert"): "Enjoy this rare desert rain while it lasts!",
            ("storm", "Mountain"): "Seek shelter! Lightning is dangerous on the mountain.",
            ("storm", "Desert"): "Take cover from the desert storm.",
            ("fog", "Forest"): "The fog makes it easy to get lost in the forest.",
            ("fog", "Mountain"): "Visibility is poor on the mountain paths.",
            ("snow", "Mountain"): "Dress warmly for the snowy mountain conditions.",
            ("blizzard", "Mountain"): "Extreme danger! Consider waiting out the blizzard.",
            ("blizzard", "Desert"): "A desert blizzard is extremely rare and dangerous."
        }
        
        return advice.get((self.current_weather, location), "")

