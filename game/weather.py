import random


class Weather:
    """
    Represents the weather system in the game.
    
    This class handles weather conditions and their effects on the player.
    """
    
    WEATHER_CONDITIONS = ["clear", "cloudy", "rainy", "stormy", "foggy", "windy"]
    
    def __init__(self, initial_condition="clear"):
        """
        Initialize a new Weather object.
        
        Args:
            initial_condition (str, optional): The initial weather condition
        """
        self.current_condition = initial_condition
    
    def get_current_condition(self):
        """Get the current weather condition."""
        return self.current_condition
    
    def change_condition(self):
        """Change the weather condition randomly."""
        self.current_condition = random.choice(self.WEATHER_CONDITIONS)
        return self.current_condition
    
    def apply_effects(self, player):
        """
        Apply weather effects to the player.
        
        Args:
            player: The player to apply effects to
        """
        if self.current_condition == "rainy":
            print("The rain is making the ground slippery. Be careful!")
            player.agility = max(1, getattr(player, "agility", 10) - 2)
        elif self.current_condition == "stormy":
            print("The storm is making it hard to see and move around.")
            player.agility = max(1, getattr(player, "agility", 10) - 3)
            player.perception = max(1, getattr(player, "perception", 10) - 3)
        elif self.current_condition == "foggy":
            print("The fog is reducing visibility significantly.")
            player.perception = max(1, getattr(player, "perception", 10) - 4)
        elif self.current_condition == "windy":
            print("The strong wind is making it difficult to move quickly.")
            player.agility = max(1, getattr(player, "agility", 10) - 1)
        else:
            print("The weather is clear and doesn't affect your abilities.")
    
    def get_description(self):
        """Get a description of the current weather condition."""
        descriptions = {
            "clear": "The sky is clear and the sun is shining brightly.",
            "cloudy": "Gray clouds cover the sky, blocking out the sun.",
            "rainy": "A steady rain is falling, creating puddles on the ground.",
            "stormy": "Dark clouds loom overhead as thunder rumbles in the distance.",
            "foggy": "A thick fog has settled in, limiting visibility to just a few feet.",
            "windy": "Strong gusts of wind blow through the area, rustling leaves and branches."
        }
        
        return descriptions.get(self.current_condition, "The weather is unremarkable.")
    
    def get_forecast(self):
        """Get a forecast for the weather."""
        future_weather = random.choice(["improve", "worsen", "stay the same"])
        
        if future_weather == "improve":
            return f"The current {self.current_condition} conditions are expected to improve soon."
        elif future_weather == "worsen":
            return f"The {self.current_condition} weather might get worse in the coming hours."
        else:
            return f"The {self.current_condition} weather is likely to persist for a while."


# Legacy functions for backward compatibility
def get_current_weather(world):
    """Get the current weather condition."""
    if hasattr(world, 'weather') and isinstance(world.weather, Weather):
        return world.weather.get_current_condition()
    
    if "weather" not in world:
        world["weather"] = "clear"
    return world["weather"]

def change_weather(world):
    """Change the weather condition randomly."""
    if hasattr(world, 'weather') and isinstance(world.weather, Weather):
        return world.weather.change_condition()
    
    weather_conditions = ["clear", "cloudy", "rainy", "stormy", "foggy", "windy"]
    new_weather = random.choice(weather_conditions)
    world["weather"] = new_weather
    return new_weather

def apply_weather_effects(player, world):
    """Apply weather effects to the player."""
    if hasattr(world, 'weather') and isinstance(world.weather, Weather):
        return world.weather.apply_effects(player)
    
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
    """Get a description of the current weather condition."""
    if hasattr(world, 'weather') and isinstance(world.weather, Weather):
        return world.weather.get_description()
    
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
    """Get a forecast for the weather."""
    if hasattr(world, 'weather') and isinstance(world.weather, Weather):
        return world.weather.get_forecast()
    
    current_weather = get_current_weather(world)
    future_weather = random.choice(["improve", "worsen", "stay the same"])

    if future_weather == "improve":
        return f"The current {current_weather} conditions are expected to improve soon."
    elif future_weather == "worsen":
        return f"The {current_weather} weather might get worse in the coming hours."
    else:
        return f"The {current_weather} weather is likely to persist for a while."
