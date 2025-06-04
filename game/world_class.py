"""
World class for Kevin's Adventure Game.
Manages game state and location handling with proper encapsulation.
"""
from typing import Dict, List, Any, Optional, Type
import random
from game.base_location import BaseLocation, LocationData, GenericLocation


class World:
    """
    Manages the game world state, locations, and global game properties.
    
    Attributes:
        current_location (str): Name of the player's current location
        locations (Dict[str, BaseLocation]): Dictionary of all game locations
        weather (str): Current weather condition
        time_of_day (str): Current time of day
        global_state (Dict[str, Any]): Global game state variables
    """
    
    def __init__(self) -> None:
        """Initialize a new game world."""
        self.current_location = "Village"
        self.locations: Dict[str, BaseLocation] = {}
        self.weather = "clear"
        self.time_of_day = "day"
        self.global_state: Dict[str, Any] = {}
        
        # Initialize default locations
        self._initialize_default_locations()
    
    def _initialize_default_locations(self) -> None:
        """Initialize the default game locations."""
        # Village
        village_data = LocationData(
            name="Village",
            description="A small, peaceful village with thatched-roof houses and friendly inhabitants.",
            connections=["Forest", "Mountain"],
            items=["map", "bread"]
        )
        self.add_location(GenericLocation(village_data))
        
        # Forest
        forest_data = LocationData(
            name="Forest",
            description="A dense, mysterious forest with towering trees and the sound of rustling leaves.",
            connections=["Village", "Cave"],
            items=["stick", "berries"]
        )
        self.add_location(GenericLocation(forest_data))
        
        # Cave
        cave_data = LocationData(
            name="Cave",
            description="A dark, damp cave with echoing sounds and glittering minerals on the walls.",
            connections=["Forest"],
            items=["torch", "gemstone"]
        )
        self.add_location(GenericLocation(cave_data))
        
        # Mountain
        mountain_data = LocationData(
            name="Mountain",
            description="A tall, snow-capped mountain with treacherous paths and breathtaking views.",
            connections=["Village"],
            items=["rope", "pickaxe"]
        )
        self.add_location(GenericLocation(mountain_data))
    
    def add_location(self, location: BaseLocation) -> bool:
        """
        Add a location to the world.
        
        Args:
            location: The location to add
            
        Returns:
            True if location was added, False if it already exists
            
        Raises:
            ValueError: If location is not a BaseLocation instance
        """
        if not isinstance(location, BaseLocation):
            raise ValueError("location must be a BaseLocation instance")
        
        if location.name not in self.locations:
            self.locations[location.name] = location
            return True
        return False
    
    def remove_location(self, location_name: str) -> bool:
        """
        Remove a location from the world.
        
        Args:
            location_name: Name of the location to remove
            
        Returns:
            True if location was removed, False if not found
        """
        if not isinstance(location_name, str):
            return False
        
        location_name = location_name.strip()
        if location_name in self.locations:
            # Don't allow removing the current location
            if location_name == self.current_location:
                return False
            
            # Remove connections to this location from other locations
            for loc in self.locations.values():
                loc.remove_connection(location_name)
            
            del self.locations[location_name]
            return True
        return False
    
    def get_location(self, location_name: str) -> Optional[BaseLocation]:
        """
        Get a location by name.
        
        Args:
            location_name: Name of the location
            
        Returns:
            The location object, or None if not found
        """
        if not isinstance(location_name, str):
            return None
        return self.locations.get(location_name.strip())
    
    def get_current_location_obj(self) -> Optional[BaseLocation]:
        """
        Get the current location object.
        
        Returns:
            Current location object, or None if not found
        """
        return self.get_location(self.current_location)
    
    def get_current_location_name(self) -> str:
        """
        Get the name of the current location.
        
        Returns:
            Name of the current location
        """
        return self.current_location
    
    def get_location_description(self, location_name: str) -> str:
        """
        Get the description of a location.
        
        Args:
            location_name: Name of the location
            
        Returns:
            Location description, or error message if not found
        """
        location = self.get_location(location_name)
        if location:
            return location.get_full_description()
        return f"Unknown location: {location_name}"
    
    def get_available_locations(self) -> List[str]:
        """
        Get list of locations accessible from current location.
        
        Returns:
            List of accessible location names
        """
        current_loc = self.get_current_location_obj()
        if current_loc:
            return current_loc.connections
        return []
    
    def get_all_location_names(self) -> List[str]:
        """
        Get list of all location names in the world.
        
        Returns:
            List of all location names
        """
        return list(self.locations.keys())
    
    def is_location_accessible(self, location_name: str) -> bool:
        """
        Check if a location is accessible from the current location.
        
        Args:
            location_name: Name of the location to check
            
        Returns:
            True if accessible, False otherwise
        """
        return location_name in self.get_available_locations()
    
    def change_location(self, new_location: str, player: 'Player') -> bool:
        """
        Change the current location.
        
        Args:
            new_location: Name of the new location
            player: The player object
            
        Returns:
            True if location change was successful, False otherwise
        """
        if not isinstance(new_location, str):
            return False
        
        new_location = new_location.strip()
        
        # Check if location exists
        if new_location not in self.locations:
            print(f"Location '{new_location}' does not exist.")
            return False
        
        # Check if location is accessible
        if not self.is_location_accessible(new_location):
            print(f"You cannot reach '{new_location}' from here.")
            return False
        
        # Change location
        self.current_location = new_location
        
        # Update player location
        if hasattr(player, 'move_to'):
            player.move_to(new_location)
        elif isinstance(player, dict):
            player['location'] = new_location
        
        # Trigger location enter event
        location_obj = self.get_location(new_location)
        if location_obj:
            location_obj.enter(player, self)
        
        return True
    
    def interact_with_current_location(self, player: 'Player') -> None:
        """
        Interact with the current location.
        
        Args:
            player: The player object
        """
        current_loc = self.get_current_location_obj()
        if current_loc:
            current_loc.enter(player, self)
        else:
            print("You are in an unknown location.")
    
    def perform_location_action(self, action: str, player: 'Player') -> bool:
        """
        Perform an action at the current location.
        
        Args:
            action: The action to perform
            player: The player object
            
        Returns:
            True if action was successful, False otherwise
        """
        current_loc = self.get_current_location_obj()
        if current_loc:
            return current_loc.perform_action(action, player, self)
        return False
    
    def get_available_actions(self, player: 'Player') -> List[str]:
        """
        Get available actions at the current location.
        
        Args:
            player: The player object
            
        Returns:
            List of available actions
        """
        current_loc = self.get_current_location_obj()
        if current_loc:
            return current_loc.get_available_actions(player, self)
        return []
    
    def get_current_weather(self) -> str:
        """
        Get the current weather condition.
        
        Returns:
            Current weather condition
        """
        return self.weather
    
    def change_weather(self) -> str:
        """
        Change the weather to a random condition.
        
        Returns:
            New weather condition
        """
        weather_conditions = ["clear", "cloudy", "rainy", "stormy", "foggy", "windy"]
        self.weather = random.choice(weather_conditions)
        return self.weather
    
    def set_weather(self, weather: str) -> None:
        """
        Set the weather to a specific condition.
        
        Args:
            weather: The weather condition to set
            
        Raises:
            ValueError: If weather is not a valid string
        """
        if not isinstance(weather, str) or not weather.strip():
            raise ValueError("Weather must be a non-empty string")
        self.weather = weather.strip()
    
    def get_time_of_day(self) -> str:
        """
        Get the current time of day.
        
        Returns:
            Current time of day
        """
        return self.time_of_day
    
    def advance_time(self) -> str:
        """
        Advance the time of day.
        
        Returns:
            New time of day
        """
        time_progression = {
            "dawn": "morning",
            "morning": "noon",
            "noon": "afternoon",
            "afternoon": "evening",
            "evening": "night",
            "night": "dawn"
        }
        self.time_of_day = time_progression.get(self.time_of_day, "day")
        return self.time_of_day
    
    def set_time_of_day(self, time: str) -> None:
        """
        Set the time of day.
        
        Args:
            time: The time of day to set
            
        Raises:
            ValueError: If time is not a valid string
        """
        if not isinstance(time, str) or not time.strip():
            raise ValueError("Time must be a non-empty string")
        self.time_of_day = time.strip()
    
    def get_global_state(self, key: str, default: Any = None) -> Any:
        """
        Get a global state value.
        
        Args:
            key: The state key
            default: Default value if key not found
            
        Returns:
            State value or default
        """
        if not isinstance(key, str):
            return default
        return self.global_state.get(key.strip(), default)
    
    def set_global_state(self, key: str, value: Any) -> None:
        """
        Set a global state value.
        
        Args:
            key: The state key
            value: The value to set
            
        Raises:
            ValueError: If key is not a valid string
        """
        if not isinstance(key, str) or not key.strip():
            raise ValueError("State key must be a non-empty string")
        self.global_state[key.strip()] = value
    
    def update_world_state(self, event: str, data: Any = None) -> None:
        """
        Update the world state based on an event.
        
        Args:
            event: The event that occurred
            data: Additional event data
        """
        if not isinstance(event, str):
            return
        
        event = event.strip().lower()
        
        # Handle common world state updates
        if event == "time_advance":
            self.advance_time()
        elif event == "weather_change":
            self.change_weather()
        elif event.startswith("reveal_"):
            # Handle reveal events (e.g., "reveal_hidden_path")
            self.set_global_state(event, True)
        elif event.startswith("complete_"):
            # Handle completion events (e.g., "complete_quest")
            self.set_global_state(event, True)
        
        # Store the event in global state for tracking
        events_key = "events_occurred"
        events = self.get_global_state(events_key, [])
        if not isinstance(events, list):
            events = []
        events.append({"event": event, "data": data, "time": self.time_of_day})
        self.set_global_state(events_key, events)
    
    def add_item_to_location(self, location_name: str, item: str) -> bool:
        """
        Add an item to a specific location.
        
        Args:
            location_name: Name of the location
            item: Item to add
            
        Returns:
            True if item was added, False otherwise
        """
        location = self.get_location(location_name)
        if location:
            return location.add_item(item)
        return False
    
    def remove_item_from_location(self, location_name: str, item: str) -> bool:
        """
        Remove an item from a specific location.
        
        Args:
            location_name: Name of the location
            item: Item to remove
            
        Returns:
            True if item was removed, False otherwise
        """
        location = self.get_location(location_name)
        if location:
            return location.remove_item(item)
        return False
    
    def get_location_items(self, location_name: str) -> List[str]:
        """
        Get items at a specific location.
        
        Args:
            location_name: Name of the location
            
        Returns:
            List of items at the location
        """
        location = self.get_location(location_name)
        if location:
            return location.items
        return []
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert world to dictionary for saving.
        
        Returns:
            Dictionary representation of the world
        """
        locations_dict = {}
        for name, location in self.locations.items():
            locations_dict[name] = location.to_dict()
        
        return {
            "current_location": self.current_location,
            "locations": locations_dict,
            "weather": self.weather,
            "time_of_day": self.time_of_day,
            "global_state": self.global_state.copy()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'World':
        """
        Create a world from dictionary data.
        
        Args:
            data: Dictionary containing world data
            
        Returns:
            New World instance
            
        Raises:
            ValueError: If data is invalid or missing required fields
        """
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        
        world = cls()
        
        # Clear default locations if we're loading from save
        world.locations.clear()
        
        # Load locations
        if "locations" in data and isinstance(data["locations"], dict):
            for name, loc_data in data["locations"].items():
                if isinstance(loc_data, dict):
                    location_data = LocationData(
                        name=loc_data.get("name", name),
                        description=loc_data.get("description", ""),
                        connections=loc_data.get("connections", []).copy() if isinstance(loc_data.get("connections"), list) else [],
                        items=loc_data.get("items", []).copy() if isinstance(loc_data.get("items"), list) else [],
                        visited=loc_data.get("visited", False),
                        special_properties=loc_data.get("special_properties", {}).copy() if isinstance(loc_data.get("special_properties"), dict) else {}
                    )
                    world.add_location(GenericLocation(location_data))
        
        # Load other properties
        if "current_location" in data:
            world.current_location = data["current_location"]
        if "weather" in data:
            world.weather = data["weather"]
        if "time_of_day" in data:
            world.time_of_day = data["time_of_day"]
        if "global_state" in data and isinstance(data["global_state"], dict):
            world.global_state = data["global_state"].copy()
        
        return world


# Backward compatibility functions
def initialize_world() -> Dict[str, Any]:
    """
    Initialize world using the old function-based approach.
    This function maintains backward compatibility.
    
    Returns:
        Dictionary representation of world (for compatibility)
    """
    world = World()
    return world.to_dict()


def get_current_location(world_data: Dict[str, Any]) -> str:
    """
    Get current location from dictionary data.
    This function maintains backward compatibility.
    
    Args:
        world_data: Dictionary containing world data
        
    Returns:
        Current location name
    """
    if isinstance(world_data, dict):
        return world_data.get("current_location", "Village")
    else:
        raise ValueError("world_data must be a dictionary")


def get_location_description(world_data: Dict[str, Any], location: str) -> str:
    """
    Get location description from dictionary data.
    This function maintains backward compatibility.
    
    Args:
        world_data: Dictionary containing world data
        location: Location name
        
    Returns:
        Location description
    """
    if isinstance(world_data, dict) and "locations" in world_data:
        locations = world_data["locations"]
        if location in locations:
            return locations[location].get("description", "Unknown location.")
    return "Unknown location."


def get_available_locations(world_data: Dict[str, Any]) -> List[str]:
    """
    Get available locations from dictionary data.
    This function maintains backward compatibility.
    
    Args:
        world_data: Dictionary containing world data
        
    Returns:
        List of available location names
    """
    if isinstance(world_data, dict) and "locations" in world_data:
        current_location = get_current_location(world_data)
        locations = world_data["locations"]
        if current_location in locations:
            return locations[current_location].get("connections", [])
    return []


def change_location(world_data: Dict[str, Any], new_location: str) -> bool:
    """
    Change location in dictionary data.
    This function maintains backward compatibility.
    
    Args:
        world_data: Dictionary containing world data
        new_location: New location name
        
    Returns:
        True if location change was successful
    """
    if isinstance(world_data, dict):
        available = get_available_locations(world_data)
        if new_location in available:
            world_data["current_location"] = new_location
            return True
    return False


def get_all_locations(world_data: Dict[str, Any]) -> List[str]:
    """
    Get all locations from dictionary data.
    This function maintains backward compatibility.
    
    Args:
        world_data: Dictionary containing world data
        
    Returns:
        List of all location names
    """
    if isinstance(world_data, dict) and "locations" in world_data:
        return list(world_data["locations"].keys())
    return []


def is_location_accessible(world_data: Dict[str, Any], location: str) -> bool:
    """
    Check if location is accessible from dictionary data.
    This function maintains backward compatibility.
    
    Args:
        world_data: Dictionary containing world data
        location: Location to check
        
    Returns:
        True if location is accessible
    """
    return location in get_available_locations(world_data)

