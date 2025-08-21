"""
Exceptions module for Kevin's Adventure Game.
Contains custom exceptions for the game.
"""


class GameError(Exception):
    """Base class for all game-related exceptions."""
    pass


class InvalidCommandError(GameError):
    """Exception raised when an invalid command is entered."""
    def __init__(self, command, message="Invalid command"):
        self.command = command
        self.message = f"{message}: {command}"
        super().__init__(self.message)


class InvalidLocationError(GameError):
    """Exception raised when an invalid location is specified."""
    def __init__(self, location, message="Invalid location"):
        self.location = location
        self.message = f"{message}: {location}"
        super().__init__(self.message)


class InvalidItemError(GameError):
    """Exception raised when an invalid item is specified."""
    def __init__(self, item, message="Invalid item"):
        self.item = item
        self.message = f"{message}: {item}"
        super().__init__(self.message)


class InventoryError(GameError):
    """Exception raised when there's an issue with the player's inventory."""
    pass


class SaveLoadError(GameError):
    """Exception raised when there's an issue with saving or loading the game."""
    pass


class GameStateError(GameError):
    """Exception raised when there's an issue with the game state."""
    pass

