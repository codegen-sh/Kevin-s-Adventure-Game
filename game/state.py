"""
State module for Kevin's Adventure Game.
Contains the GameState class and related functions.
"""


class GameState:
    """
    GameState class representing the overall game state.
    
    Attributes:
        player: The player instance
        world: The world instance
        weather (str): The current weather
        time_of_day (str): The current time of day
        events (list): List of events that have occurred
        quests (dict): Dictionary of active quests
        discovered_locations (set): Set of discovered location names
    """
    
    def __init__(self, player, world, weather="sunny", time_of_day="day", events=None, quests=None, discovered_locations=None):
        """
        Initialize a new GameState instance.
        
        Args:
            player: The player instance
            world: The world instance
            weather (str, optional): The current weather. Defaults to "sunny".
            time_of_day (str, optional): The current time of day. Defaults to "day".
            events (list, optional): List of events that have occurred. Defaults to empty list.
            quests (dict, optional): Dictionary of active quests. Defaults to empty dict.
            discovered_locations (set, optional): Set of discovered location names. Defaults to empty set.
        """
        self.player = player
        self.world = world
        self.weather = weather
        self.time_of_day = time_of_day
        self.events = events or []
        self.quests = quests or {}
        self.discovered_locations = discovered_locations or set()
    
    def add_event(self, event):
        """
        Add an event to the game state.
        
        Args:
            event (str): The event to add
        """
        self.events.append(event)
    
    def has_event_occurred(self, event):
        """
        Check if an event has occurred.
        
        Args:
            event (str): The event to check for
            
        Returns:
            bool: True if the event has occurred, False otherwise
        """
        return event in self.events
    
    def add_quest(self, quest_id, quest_data):
        """
        Add a quest to the game state.
        
        Args:
            quest_id (str): The quest ID
            quest_data (dict): The quest data
        """
        self.quests[quest_id] = quest_data
    
    def complete_quest(self, quest_id):
        """
        Mark a quest as completed.
        
        Args:
            quest_id (str): The quest ID
            
        Returns:
            bool: True if the quest was completed, False otherwise
        """
        if quest_id in self.quests:
            self.quests[quest_id]["completed"] = True
            return True
        return False
    
    def is_quest_active(self, quest_id):
        """
        Check if a quest is active.
        
        Args:
            quest_id (str): The quest ID
            
        Returns:
            bool: True if the quest is active, False otherwise
        """
        return quest_id in self.quests and not self.quests[quest_id].get("completed", False)
    
    def is_quest_completed(self, quest_id):
        """
        Check if a quest is completed.
        
        Args:
            quest_id (str): The quest ID
            
        Returns:
            bool: True if the quest is completed, False otherwise
        """
        return quest_id in self.quests and self.quests[quest_id].get("completed", False)
    
    def discover_location(self, location_name):
        """
        Mark a location as discovered.
        
        Args:
            location_name (str): The name of the location
        """
        self.discovered_locations.add(location_name)
    
    def is_location_discovered(self, location_name):
        """
        Check if a location has been discovered.
        
        Args:
            location_name (str): The name of the location
            
        Returns:
            bool: True if the location has been discovered, False otherwise
        """
        return location_name in self.discovered_locations
    
    def set_weather(self, weather):
        """
        Set the current weather.
        
        Args:
            weather (str): The new weather
        """
        self.weather = weather
    
    def set_time_of_day(self, time_of_day):
        """
        Set the current time of day.
        
        Args:
            time_of_day (str): The new time of day
        """
        self.time_of_day = time_of_day
    
    def to_dict(self):
        """
        Convert the GameState instance to a dictionary.
        
        Returns:
            dict: A dictionary representation of the game state
        """
        return {
            "player": self.player.to_dict() if hasattr(self.player, "to_dict") else self.player,
            "world": self.world.to_dict() if hasattr(self.world, "to_dict") else self.world,
            "weather": self.weather,
            "time_of_day": self.time_of_day,
            "events": self.events.copy(),
            "quests": {k: v.copy() for k, v in self.quests.items()},
            "discovered_locations": list(self.discovered_locations)
        }
    
    @classmethod
    def from_dict(cls, state_dict):
        """
        Create a GameState instance from a dictionary.
        
        Args:
            state_dict (dict): A dictionary representation of a game state
            
        Returns:
            GameState: A new GameState instance
        """
        from game.player import Player
        from game.world import World
        
        player = Player.from_dict(state_dict["player"]) if "player" in state_dict else None
        world = World.from_dict(state_dict["world"]) if "world" in state_dict else None
        
        return cls(
            player=player,
            world=world,
            weather=state_dict.get("weather", "sunny"),
            time_of_day=state_dict.get("time_of_day", "day"),
            events=state_dict.get("events", []).copy(),
            quests={k: v.copy() for k, v in state_dict.get("quests", {}).items()},
            discovered_locations=set(state_dict.get("discovered_locations", []))
        )


# Legacy function for backward compatibility
def update_world_state(world, event):
    """
    Update the world state based on an event.
    
    Args:
        world (dict): The game world state
        event (str): The event to process
    """
    # Handle different events
    if event == "add_clearing":
        # Add a clearing to the forest
        if "Forest" in world["locations"]:
            if "Clearing" not in world["locations"]["Forest"]["connections"]:
                world["locations"]["Forest"]["connections"].append("Clearing")
            
            if "Clearing" not in world["locations"]:
                world["locations"]["Clearing"] = {
                    "description": "A beautiful clearing with a small pond and wildflowers.",
                    "connections": ["Forest"],
                    "items": ["wildflowers"]
                }
    elif event == "add_river":
        # Add a river to the forest
        if "Forest" in world["locations"]:
            if "River" not in world["locations"]["Forest"]["connections"]:
                world["locations"]["Forest"]["connections"].append("River")
            
            if "River" not in world["locations"]:
                world["locations"]["River"] = {
                    "description": "A clear, flowing river with fish swimming in it.",
                    "connections": ["Forest"],
                    "items": ["fishing_rod"]
                }
    elif event == "add_hidden_cave":
        # Add a hidden cave to the mountain
        if "Mountain" in world["locations"]:
            if "Hidden Cave" not in world["locations"]["Mountain"]["connections"]:
                world["locations"]["Mountain"]["connections"].append("Hidden Cave")
            
            if "Hidden Cave" not in world["locations"]:
                world["locations"]["Hidden Cave"] = {
                    "description": "A hidden cave with ancient drawings on the walls.",
                    "connections": ["Mountain"],
                    "items": ["ancient_artifact"]
                }
    elif event.startswith("weather_"):
        # Change the weather
        weather = event.split("_")[1]
        world["weather"] = weather

