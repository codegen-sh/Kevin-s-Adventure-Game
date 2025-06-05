"""
Custom exceptions for the game.
Provides specific error types for better error handling and debugging.
"""


class GameError(Exception):
    """Base exception for all game-related errors."""
    pass


class InvalidActionError(GameError):
    """Raised when an invalid action is attempted."""
    pass


class ItemNotFoundError(GameError):
    """Raised when trying to use or access an item that doesn't exist."""
    pass


class LocationNotFoundError(GameError):
    """Raised when trying to access a location that doesn't exist."""
    pass


class LocationNotAccessibleError(GameError):
    """Raised when trying to move to an inaccessible location."""
    pass


class InsufficientHealthError(GameError):
    """Raised when player health is too low for an action."""
    pass


class InsufficientGoldError(GameError):
    """Raised when player doesn't have enough gold for a transaction."""
    pass


class InventoryFullError(GameError):
    """Raised when trying to add items to a full inventory."""
    pass


class SaveGameError(GameError):
    """Raised when there's an error saving the game."""
    pass


class LoadGameError(GameError):
    """Raised when there's an error loading the game."""
    pass


class InvalidInputError(GameError):
    """Raised when user provides invalid input."""
    pass

