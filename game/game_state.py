"""
Game state module for Kevin's Adventure Game.
Contains functions for managing the overall game state.
"""
from game.player import Player
from game.state import GameState
from game.world import World


def create_game_state(player_name="Kevin"):
    """
    Create a new game state with a player and world.
    
    Args:
        player_name (str, optional): The player's name. Defaults to "Kevin".
        
    Returns:
        GameState: A new GameState instance
    """
    from game.player import create_player
    from game.world import initialize_world
    
    player_dict = create_player(player_name)
    world_dict = initialize_world()
    
    player = Player.from_dict(player_dict)
    world = World.from_dict(world_dict)
    
    return GameState(player, world)


def save_game_state(game_state, filename=None):
    """
    Save the game state to a file.
    
    Args:
        game_state (GameState): The game state to save
        filename (str, optional): The filename to save to. Defaults to None.
        
    Returns:
        str: The filename the game was saved to
    """
    from utils.save_load import save_game
    
    player_dict = game_state.player.to_dict()
    world_dict = game_state.world.to_dict()
    
    return save_game(player_dict, world_dict, filename)


def load_game_state(filename):
    """
    Load a game state from a file.
    
    Args:
        filename (str): The filename to load from
        
    Returns:
        GameState: The loaded GameState instance, or None if loading failed
    """
    from utils.save_load import load_game
    
    player_dict, world_dict = load_game(filename)
    
    if player_dict is None or world_dict is None:
        return None
    
    player = Player.from_dict(player_dict)
    world = World.from_dict(world_dict)
    
    return GameState(player, world)

