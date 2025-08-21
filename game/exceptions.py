"""
Exceptions module for Kevin's Adventure Game.
This module defines custom exceptions used in the game.
"""


class GameError(Exception):
    """Base class for all game exceptions."""
    pass


class InvalidCommandError(GameError):
    """Raised when an invalid command is entered."""
    pass


class InvalidLocationError(GameError):
    """Raised when an invalid location is specified."""
    pass


class InvalidItemError(GameError):
    """Raised when an invalid item is specified."""
    pass


class InventoryError(GameError):
    """Raised when there's an issue with the player's inventory."""
    pass


class SaveLoadError(GameError):
    """Raised when there's an issue with saving or loading the game."""
    pass


class GameStateError(GameError):
    """Raised when there's an issue with the game state."""
    pass

