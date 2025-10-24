"""
Custom exception hierarchy for Kevin's Adventure Game.
Provides specific exception types for different error scenarios with context and recovery suggestions.
"""


class GameError(Exception):
    """
    Base exception class for all game-related errors.
    
    Attributes:
        message (str): Error message
        context (dict): Additional context information
        recovery_suggestion (str): Suggested recovery action
    """
    
    def __init__(self, message, context=None, recovery_suggestion=None):
        self.message = message
        self.context = context or {}
        self.recovery_suggestion = recovery_suggestion
        super().__init__(self.message)
    
    def __str__(self):
        error_str = f"GameError: {self.message}"
        if self.context:
            error_str += f" | Context: {self.context}"
        if self.recovery_suggestion:
            error_str += f" | Suggestion: {self.recovery_suggestion}"
        return error_str


class SaveError(GameError):
    """Exception raised when save operations fail."""
    
    def __init__(self, message, filename=None, context=None):
        self.filename = filename
        context = context or {}
        if filename:
            context['filename'] = filename
        
        recovery_suggestion = "Try saving to a different location or check disk space and permissions."
        super().__init__(message, context, recovery_suggestion)


class LoadError(GameError):
    """Exception raised when load operations fail."""
    
    def __init__(self, message, filename=None, context=None):
        self.filename = filename
        context = context or {}
        if filename:
            context['filename'] = filename
        
        recovery_suggestion = "Check if the file exists and is not corrupted. Try loading a different save file."
        super().__init__(message, context, recovery_suggestion)


class LocationError(GameError):
    """Exception raised for location-related errors."""
    
    def __init__(self, message, location=None, current_location=None, context=None):
        self.location = location
        self.current_location = current_location
        context = context or {}
        if location:
            context['target_location'] = location
        if current_location:
            context['current_location'] = current_location
        
        recovery_suggestion = "Check available locations and ensure the target location is accessible."
        super().__init__(message, context, recovery_suggestion)


class ValidationError(GameError):
    """Exception raised for input validation failures."""
    
    def __init__(self, message, input_value=None, expected_type=None, context=None):
        self.input_value = input_value
        self.expected_type = expected_type
        context = context or {}
        if input_value is not None:
            context['input_value'] = input_value
        if expected_type:
            context['expected_type'] = expected_type
        
        recovery_suggestion = "Please provide valid input according to the expected format."
        super().__init__(message, context, recovery_suggestion)


class PlayerError(GameError):
    """Exception raised for player-related errors."""
    
    def __init__(self, message, player_name=None, player_state=None, context=None):
        self.player_name = player_name
        self.player_state = player_state
        context = context or {}
        if player_name:
            context['player_name'] = player_name
        if player_state:
            context['player_health'] = player_state.get('health', 'unknown')
            context['player_location'] = player_state.get('location', 'unknown')
        
        recovery_suggestion = "Check player state and ensure all required attributes are present."
        super().__init__(message, context, recovery_suggestion)


class ItemError(GameError):
    """Exception raised for item-related errors."""
    
    def __init__(self, message, item_name=None, location=None, context=None):
        self.item_name = item_name
        self.location = location
        context = context or {}
        if item_name:
            context['item_name'] = item_name
        if location:
            context['location'] = location
        
        recovery_suggestion = "Check if the item exists and is available in the specified location."
        super().__init__(message, context, recovery_suggestion)


class WeatherError(GameError):
    """Exception raised for weather system errors."""
    
    def __init__(self, message, weather_type=None, location=None, context=None):
        self.weather_type = weather_type
        self.location = location
        context = context or {}
        if weather_type:
            context['weather_type'] = weather_type
        if location:
            context['location'] = location
        
        recovery_suggestion = "Reset weather system or use default weather conditions."
        super().__init__(message, context, recovery_suggestion)


class WorldStateError(GameError):
    """Exception raised for world state inconsistencies."""
    
    def __init__(self, message, world_state=None, context=None):
        self.world_state = world_state
        context = context or {}
        if world_state:
            context['current_location'] = world_state.get('current_location', 'unknown')
            context['locations_count'] = len(world_state.get('locations', {}))
        
        recovery_suggestion = "Reinitialize world state or load from a backup."
        super().__init__(message, context, recovery_suggestion)


class ConfigurationError(GameError):
    """Exception raised for configuration-related errors."""
    
    def __init__(self, message, config_key=None, config_value=None, context=None):
        self.config_key = config_key
        self.config_value = config_value
        context = context or {}
        if config_key:
            context['config_key'] = config_key
        if config_value is not None:
            context['config_value'] = config_value
        
        recovery_suggestion = "Check configuration settings and use default values if necessary."
        super().__init__(message, context, recovery_suggestion)


class NetworkError(GameError):
    """Exception raised for network-related errors (future use)."""
    
    def __init__(self, message, endpoint=None, status_code=None, context=None):
        self.endpoint = endpoint
        self.status_code = status_code
        context = context or {}
        if endpoint:
            context['endpoint'] = endpoint
        if status_code:
            context['status_code'] = status_code
        
        recovery_suggestion = "Check network connection and try again later."
        super().__init__(message, context, recovery_suggestion)


class PermissionError(GameError):
    """Exception raised for permission-related errors."""
    
    def __init__(self, message, operation=None, resource=None, context=None):
        self.operation = operation
        self.resource = resource
        context = context or {}
        if operation:
            context['operation'] = operation
        if resource:
            context['resource'] = resource
        
        recovery_suggestion = "Check file permissions or run with appropriate privileges."
        super().__init__(message, context, recovery_suggestion)


# Utility functions for exception handling

def handle_exception(exception, logger=None):
    """
    Centralized exception handler that logs errors and provides user-friendly messages.
    
    Args:
        exception (Exception): The exception to handle
        logger: Logger instance for recording the error
    
    Returns:
        str: User-friendly error message
    """
    if logger:
        logger.error(f"Exception occurred: {exception}", exc_info=True)
    
    if isinstance(exception, GameError):
        user_message = f"Game Error: {exception.message}"
        if exception.recovery_suggestion:
            user_message += f"\nSuggestion: {exception.recovery_suggestion}"
        return user_message
    else:
        return f"An unexpected error occurred: {str(exception)}"


def create_error_context(player=None, world=None, action=None, **kwargs):
    """
    Create a standardized error context dictionary.
    
    Args:
        player (dict): Player state
        world (dict): World state
        action (str): Current action being performed
        **kwargs: Additional context information
    
    Returns:
        dict: Error context dictionary
    """
    context = {}
    
    if player:
        context.update({
            'player_name': player.get('name'),
            'player_health': player.get('health'),
            'player_location': player.get('location'),
            'inventory_count': len(player.get('inventory', []))
        })
    
    if world:
        context.update({
            'current_location': world.get('current_location'),
            'world_locations': list(world.get('locations', {}).keys())
        })
    
    if action:
        context['action'] = action
    
    context.update(kwargs)
    return context


def is_recoverable_error(exception):
    """
    Determine if an error is recoverable.
    
    Args:
        exception (Exception): The exception to check
    
    Returns:
        bool: True if the error is recoverable
    """
    recoverable_types = (
        ValidationError,
        ItemError,
        LocationError,
        WeatherError
    )
    
    return isinstance(exception, recoverable_types)


def get_error_severity(exception):
    """
    Get the severity level of an error.
    
    Args:
        exception (Exception): The exception to evaluate
    
    Returns:
        str: Severity level ('low', 'medium', 'high', 'critical')
    """
    if isinstance(exception, (ValidationError, ItemError)):
        return 'low'
    elif isinstance(exception, (LocationError, WeatherError, PlayerError)):
        return 'medium'
    elif isinstance(exception, (SaveError, LoadError, WorldStateError)):
        return 'high'
    elif isinstance(exception, (ConfigurationError, PermissionError)):
        return 'critical'
    else:
        return 'medium'  # Default for unknown exceptions

