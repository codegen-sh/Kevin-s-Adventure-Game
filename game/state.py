class GameState:
    """
    A class to manage the game state.
    
    This class centralizes all game state management, including:
    - World state (locations, weather, time)
    - Player state (health, inventory, location)
    - Game flags (quests, discoveries, events)
    
    Attributes:
        world (dict): The game world state
        player (dict): The player's current state
        flags (dict): Game flags and quest progress
        discovered_locations (set): Set of locations the player has discovered
        active_quests (dict): Currently active quests
        completed_quests (set): Completed quests
        game_time (int): In-game time (in minutes)
    """
    
    def __init__(self, player=None, world=None):
        """
        Initialize a new GameState.
        
        Args:
            player (dict, optional): The player's initial state
            world (dict, optional): The world's initial state
        """
        self.world = world if world else {}
        self.player = player if player else {}
        self.flags = {}
        self.discovered_locations = set()
        self.active_quests = {}
        self.completed_quests = set()
        self.game_time = 0
    
    def update_flag(self, flag_name, value=True):
        """
        Update a game flag.
        
        Args:
            flag_name (str): The name of the flag to update
            value (any, optional): The value to set the flag to. Defaults to True.
        """
        self.flags[flag_name] = value
    
    def check_flag(self, flag_name, default=False):
        """
        Check if a game flag is set.
        
        Args:
            flag_name (str): The name of the flag to check
            default (any, optional): The default value if the flag is not set. Defaults to False.
        
        Returns:
            any: The value of the flag, or the default value if not set
        """
        return self.flags.get(flag_name, default)
    
    def discover_location(self, location):
        """
        Mark a location as discovered.
        
        Args:
            location (str): The name of the location to mark as discovered
        """
        self.discovered_locations.add(location)
    
    def is_location_discovered(self, location):
        """
        Check if a location has been discovered.
        
        Args:
            location (str): The name of the location to check
        
        Returns:
            bool: True if the location has been discovered, False otherwise
        """
        return location in self.discovered_locations
    
    def add_quest(self, quest_id, quest_data):
        """
        Add a new quest to the active quests.
        
        Args:
            quest_id (str): The ID of the quest
            quest_data (dict): Quest data including description, objectives, rewards, etc.
        """
        self.active_quests[quest_id] = quest_data
    
    def complete_quest(self, quest_id):
        """
        Mark a quest as completed.
        
        Args:
            quest_id (str): The ID of the quest to mark as completed
        
        Returns:
            bool: True if the quest was active and is now completed, False otherwise
        """
        if quest_id in self.active_quests:
            quest_data = self.active_quests.pop(quest_id)
            self.completed_quests.add(quest_id)
            return True
        return False
    
    def is_quest_active(self, quest_id):
        """
        Check if a quest is active.
        
        Args:
            quest_id (str): The ID of the quest to check
        
        Returns:
            bool: True if the quest is active, False otherwise
        """
        return quest_id in self.active_quests
    
    def is_quest_completed(self, quest_id):
        """
        Check if a quest has been completed.
        
        Args:
            quest_id (str): The ID of the quest to check
        
        Returns:
            bool: True if the quest has been completed, False otherwise
        """
        return quest_id in self.completed_quests
    
    def advance_time(self, minutes):
        """
        Advance the game time.
        
        Args:
            minutes (int): The number of minutes to advance the game time by
        """
        self.game_time += minutes
    
    def get_time_of_day(self):
        """
        Get the current time of day.
        
        Returns:
            str: A string representing the time of day (morning, afternoon, evening, night)
        """
        hours = (self.game_time // 60) % 24
        if 6 <= hours < 12:
            return "morning"
        elif 12 <= hours < 18:
            return "afternoon"
        elif 18 <= hours < 22:
            return "evening"
        else:
            return "night"
    
    def to_dict(self):
        """
        Convert the game state to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the game state
        """
        return {
            "world": self.world,
            "player": self.player,
            "flags": self.flags,
            "discovered_locations": list(self.discovered_locations),
            "active_quests": self.active_quests,
            "completed_quests": list(self.completed_quests),
            "game_time": self.game_time
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a GameState from a dictionary.
        
        Args:
            data (dict): A dictionary representation of the game state
        
        Returns:
            GameState: A new GameState instance
        """
        state = cls(data.get("player", {}), data.get("world", {}))
        state.flags = data.get("flags", {})
        state.discovered_locations = set(data.get("discovered_locations", []))
        state.active_quests = data.get("active_quests", {})
        state.completed_quests = set(data.get("completed_quests", []))
        state.game_time = data.get("game_time", 0)
        return state


def update_world_state(world, event):
    """
    Update the world state based on an event.
    
    Args:
        world (dict): The game world state
        event (str): The event that occurred
    
    Returns:
        None
    """
    if event == "weather_clear":
        world["weather"] = "clear"
    elif event == "weather_rainy":
        world["weather"] = "rainy"
    elif event == "weather_stormy":
        world["weather"] = "stormy"
    elif event == "weather_foggy":
        world["weather"] = "foggy"
    elif event == "weather_windy":
        world["weather"] = "windy"
    elif event == "add_hidden_cave":
        if "hidden_locations" not in world:
            world["hidden_locations"] = []
        if "Hidden Cave" not in world["hidden_locations"]:
            world["hidden_locations"].append("Hidden Cave")
    elif event == "reveal_hidden_path":
        if "Forest" in world["locations"]:
            if "Hidden Path" not in world["locations"]["Forest"]["connections"]:
                world["locations"]["Forest"]["connections"].append("Hidden Path")
    elif event == "reveal_hidden_cave":
        if "Mountain" in world["locations"]:
            if "Hidden Cave" not in world["locations"]["Mountain"]["connections"]:
                world["locations"]["Mountain"]["connections"].append("Hidden Cave")
    elif event == "add_clearing":
        if "Forest" in world["locations"]:
            world["locations"]["Forest"]["description"] += " There is a beautiful clearing with a small pond nearby."
    elif event == "add_underground_lake":
        if "Cave" in world["locations"]:
            world["locations"]["Cave"]["description"] += " There is a beautiful underground lake with crystal-clear water."
    elif event == "reveal_secret_exit":
        if "Cave" in world["locations"]:
            if "Secret Exit" not in world["locations"]["Cave"]["connections"]:
                world["locations"]["Cave"]["connections"].append("Secret Exit")
    elif event == "improve_visibility":
        world["visibility"] = "high"
    elif event == "approaching_storm":
        world["weather"] = "stormy"
    elif event == "reveal_map":
        world["map_revealed"] = True

