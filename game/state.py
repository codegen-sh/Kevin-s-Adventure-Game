class GameState:
    """
    Manages the overall state of the game.
    
    This class handles game events, quests, and other state-related functionality.
    """
    
    def __init__(self):
        """Initialize a new GameState."""
        self.events = []
        self.quests = {}
        self.discovered_locations = ["Village"]
        self.game_time = 0  # Time in game hours
    
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
            event (str): The event to check
            
        Returns:
            bool: True if the event has occurred, False otherwise
        """
        return event in self.events
    
    def add_quest(self, quest_id, quest_data):
        """
        Add a quest to the game state.
        
        Args:
            quest_id (str): The ID of the quest
            quest_data (dict): The quest data
        """
        self.quests[quest_id] = quest_data
    
    def complete_quest(self, quest_id):
        """
        Mark a quest as completed.
        
        Args:
            quest_id (str): The ID of the quest
            
        Returns:
            bool: True if the quest was completed, False otherwise
        """
        if quest_id in self.quests:
            self.quests[quest_id]["completed"] = True
            return True
        return False
    
    def is_quest_completed(self, quest_id):
        """
        Check if a quest is completed.
        
        Args:
            quest_id (str): The ID of the quest
            
        Returns:
            bool: True if the quest is completed, False otherwise
        """
        return quest_id in self.quests and self.quests[quest_id].get("completed", False)
    
    def discover_location(self, location):
        """
        Mark a location as discovered.
        
        Args:
            location (str): The location to discover
        """
        if location not in self.discovered_locations:
            self.discovered_locations.append(location)
    
    def is_location_discovered(self, location):
        """
        Check if a location is discovered.
        
        Args:
            location (str): The location to check
            
        Returns:
            bool: True if the location is discovered, False otherwise
        """
        return location in self.discovered_locations
    
    def advance_time(self, hours=1):
        """
        Advance the game time.
        
        Args:
            hours (int, optional): The number of hours to advance
        """
        self.game_time += hours
    
    def get_time_of_day(self):
        """
        Get the current time of day.
        
        Returns:
            str: The current time of day (morning, afternoon, evening, night)
        """
        hour = self.game_time % 24
        if 6 <= hour < 12:
            return "morning"
        elif 12 <= hour < 18:
            return "afternoon"
        elif 18 <= hour < 22:
            return "evening"
        else:
            return "night"


# Legacy function for backward compatibility
def update_world_state(world, event):
    """
    Update the world state based on an event.
    
    Args:
        world: The game world
        event: The event to process
    """
    if hasattr(world, 'game_state'):
        world.game_state.add_event(event)
    # TODO: Implement this function
    pass
