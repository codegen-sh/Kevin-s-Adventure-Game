"""
Custom exceptions for Kevin's Adventure Game.
Defines game-specific exception classes for better error handling.
"""


class GameError(Exception):
    """Base exception class for all game-related errors."""
    pass


class PlayerError(GameError):
    """Exception raised for player-related errors."""
    pass


class WorldError(GameError):
    """Exception raised for world-related errors."""
    pass


class LocationError(WorldError):
    """Exception raised for location-related errors."""
    pass


class InventoryError(PlayerError):
    """Exception raised for inventory-related errors."""
    pass


class ActionError(GameError):
    """Exception raised for action-related errors."""
    pass


class SaveLoadError(GameError):
    """Exception raised for save/load operations."""
    pass


class InvalidLocationError(LocationError):
    """Exception raised when trying to access an invalid location."""
    
    def __init__(self, location_name: str):
        self.location_name = location_name
        super().__init__(f"Invalid location: {location_name}")


class LocationNotAccessibleError(LocationError):
    """Exception raised when trying to move to an inaccessible location."""
    
    def __init__(self, location_name: str, current_location: str):
        self.location_name = location_name
        self.current_location = current_location
        super().__init__(f"Cannot reach {location_name} from {current_location}")


class ItemNotFoundError(InventoryError):
    """Exception raised when trying to use an item that doesn't exist."""
    
    def __init__(self, item_name: str):
        self.item_name = item_name
        super().__init__(f"Item not found: {item_name}")


class InsufficientGoldError(PlayerError):
    """Exception raised when player doesn't have enough gold for a transaction."""
    
    def __init__(self, required: int, available: int):
        self.required = required
        self.available = available
        super().__init__(f"Insufficient gold: need {required}, have {available}")


class PlayerDeadError(PlayerError):
    """Exception raised when trying to perform actions with a dead player."""
    
    def __init__(self):
        super().__init__("Cannot perform action: player is dead")


class InvalidActionError(ActionError):
    """Exception raised for invalid or malformed actions."""
    
    def __init__(self, action: str):
        self.action = action
        super().__init__(f"Invalid action: {action}")


class GameNotInitializedError(GameError):
    """Exception raised when trying to use game engine before initialization."""
    
    def __init__(self):
        super().__init__("Game not initialized: call start_new_game() or load_game_from_file() first")

