"""
State module for Kevin's Adventure Game.
This module manages the game state.
"""
from typing import Dict, List, Optional, Tuple, Union

from game.exceptions import GameStateError
from game.models import Player, World


class GameState:
    """
    GameState class for managing the game state.
    
    Attributes:
        player (Player): The player
        world (World): The game world
        flags (Dict[str, bool]): Game state flags
    """
    
    def __init__(self, player: Player, world: World):
        """
        Initialize a new GameState.
        
        Args:
            player (Player): The player
            world (World): The game world
        """
        self.player = player
        self.world = world
        self.flags: Dict[str, bool] = {}
    
    def set_flag(self, flag: str, value: bool = True) -> None:
        """
        Set a game state flag.
        
        Args:
            flag (str): The flag to set
            value (bool, optional): The value to set the flag to. Defaults to True.
        """
        self.flags[flag] = value
    
    def get_flag(self, flag: str) -> bool:
        """
        Get a game state flag.
        
        Args:
            flag (str): The flag to get
        
        Returns:
            bool: The value of the flag, or False if the flag is not set
        """
        return self.flags.get(flag, False)
    
    def update_world_state(self, event: str) -> None:
        """
        Update the world state based on an event.
        
        Args:
            event (str): The event that occurred
        """
        if event.startswith("weather_"):
            # Handle weather events
            weather = event.replace("weather_", "")
            self.world.weather = weather
            print(f"The weather has changed to {weather}.")
        elif event == "add_clearing":
            # Add a clearing to the forest
            self.set_flag("forest_clearing_discovered", True)
            print("You've discovered a clearing in the forest.")
        elif event == "add_river":
            # Add a river to the forest
            self.set_flag("forest_river_discovered", True)
            print("You've discovered a river in the forest.")
        elif event == "add_hidden_cave":
            # Add a hidden cave to the mountain
            self.set_flag("mountain_hidden_cave_discovered", True)
            print("You've discovered a hidden cave in the mountain.")
        elif event == "reveal_hidden_path":
            # Reveal a hidden path in the forest
            self.set_flag("forest_hidden_path_discovered", True)
            print("You've discovered a hidden path in the forest.")
        elif event == "cave_whispers_heard":
            # Player heard whispers in the cave
            self.set_flag("cave_whispers_heard", True)
            print("You've heard whispers in the cave.")
        elif event == "reveal_map":
            # Reveal the entire map
            self.set_flag("map_revealed", True)
            print("You can now see the entire map.")
        elif event == "improve_visibility":
            # Improve visibility in the current location
            self.set_flag("improved_visibility", True)
            print("Visibility has improved.")
        elif event == "approaching_storm":
            # An approaching storm
            self.set_flag("approaching_storm", True)
            print("A storm is approaching.")
        else:
            # Unknown event
            raise GameStateError(f"Unknown event: {event}")
    
    def to_dict(self) -> Dict:
        """
        Convert the game state to a dictionary for serialization.
        
        Returns:
            Dict: A dictionary representation of the game state
        """
        return {
            "player": self.player.to_dict(),
            "world": self.world.to_dict(),
            "flags": self.flags
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'GameState':
        """
        Create a game state from a dictionary.
        
        Args:
            data (Dict): A dictionary representation of a game state
        
        Returns:
            GameState: A new GameState instance
        """
        player = Player.from_dict(data["player"])
        world = World.from_dict(data["world"])
        game_state = cls(player, world)
        game_state.flags = data.get("flags", {})
        return game_state

