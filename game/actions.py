"""
Actions module for Kevin's Adventure Game.
Handles action processing and provides backward compatibility.
"""
from typing import Dict, Any
from game.game_engine import GameEngine
from game.player_class import Player
from game.world_class import World


def perform_action(player_data: Dict[str, Any], world_data: Dict[str, Any], action: str) -> None:
    """
    Perform an action using the old function-based interface.
    This function maintains backward compatibility with the existing main.py.
    
    Args:
        player_data: Dictionary containing player data
        world_data: Dictionary containing world data
        action: The action string to perform
    """
    try:
        # Convert dictionary data to class instances
        player = Player.from_dict(player_data)
        world = World.from_dict(world_data)
        
        # Create a temporary game engine to process the action
        engine = GameEngine(player, world)
        
        # Process the command
        engine._process_command(action)
        
        # Update the original dictionaries with any changes
        new_player_data = engine.player.to_dict()
        new_world_data = engine.world.to_dict()
        
        # Update the original dictionaries in place
        player_data.clear()
        player_data.update(new_player_data)
        
        world_data.clear()
        world_data.update(new_world_data)
        
    except Exception as e:
        print(f"Action failed: {e}")
        print("Type 'help' for available commands.")

