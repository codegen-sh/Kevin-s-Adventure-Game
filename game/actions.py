"""
Actions module for Kevin's Adventure Game.
This module handles all player actions and their effects on the game state.
"""
from game.commands import execute_command


def perform_action(player, world, action):
    """
    Process a player action and update the game state accordingly.
    
    Args:
        player: The player object
        world: The world object
        action (str): The action to perform
    
    Returns:
        bool: True if the action was executed successfully, False otherwise
    """
    return execute_command(player, world, action)

