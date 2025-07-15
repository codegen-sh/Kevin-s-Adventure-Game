"""
Custom exceptions for Kevin's Adventure Game
"""


class GameError(Exception):
    """Base exception for all game-related errors"""
    pass


class PlayerError(GameError):
    """Exception raised for player-related errors"""
    pass


class LocationError(GameError):
    """Exception raised for location-related errors"""
    pass


class InventoryError(PlayerError):
    """Exception raised for inventory-related errors"""
    pass


class ItemNotFoundError(InventoryError):
    """Exception raised when an item is not found in inventory"""
    def __init__(self, item_name):
        self.item_name = item_name
        super().__init__(f"Item '{item_name}' not found in inventory")


class InsufficientGoldError(PlayerError):
    """Exception raised when player doesn't have enough gold"""
    def __init__(self, required, available):
        self.required = required
        self.available = available
        super().__init__(f"Insufficient gold: need {required}, have {available}")


class LocationNotFoundError(LocationError):
    """Exception raised when a location is not found"""
    def __init__(self, location_name):
        self.location_name = location_name
        super().__init__(f"Location '{location_name}' not found")


class LocationNotAccessibleError(LocationError):
    """Exception raised when trying to access an inaccessible location"""
    def __init__(self, location_name, current_location):
        self.location_name = location_name
        self.current_location = current_location
        super().__init__(f"Cannot access '{location_name}' from '{current_location}'")


class SaveLoadError(GameError):
    """Exception raised for save/load operations"""
    pass


class InvalidSaveFileError(SaveLoadError):
    """Exception raised when save file is invalid or corrupted"""
    def __init__(self, filename, reason=None):
        self.filename = filename
        self.reason = reason
        message = f"Invalid save file: {filename}"
        if reason:
            message += f" - {reason}"
        super().__init__(message)


class PlayerDeadError(PlayerError):
    """Exception raised when trying to perform actions with a dead player"""
    def __init__(self):
        super().__init__("Cannot perform action: player is dead")


class InvalidActionError(GameError):
    """Exception raised for invalid game actions"""
    def __init__(self, action):
        self.action = action
        super().__init__(f"Invalid action: '{action}'")
