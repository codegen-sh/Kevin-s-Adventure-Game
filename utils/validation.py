"""
Input validation and sanitization utilities for Kevin's Adventure Game.
Provides comprehensive validation for all user inputs and game data.
"""

import re
import os
from pathlib import Path
from typing import Any, List, Dict, Optional, Union
from exceptions import ValidationError, GameError


# Validation constants
MAX_PLAYER_NAME_LENGTH = 50
MIN_PLAYER_NAME_LENGTH = 1
MAX_SAVE_FILENAME_LENGTH = 100
VALID_LOCATION_NAMES = {"Village", "Forest", "Cave", "Mountain"}
VALID_ITEM_NAMES = {
    "map", "bread", "stick", "berries", "torch", "gemstone", "rope", "pickaxe",
    "sword", "shield", "potion", "key", "coin", "crystal", "herb", "food",
    "water", "lantern", "compass", "book", "scroll", "ring", "necklace",
    "gold coin", "silver ring", "ancient artifact", "precious gem",
    "crystal shard", "ancient coin", "carved stone", "shiny pebble",
    "rare crystal", "ancient map fragment", "hermit's blessing", "cave mushroom"
}
VALID_ACTIONS = {
    "go", "move", "take", "pick up", "drop", "use", "look", "examine", "observe",
    "inventory", "inv", "items", "status", "stats", "interact", "explore",
    "search", "wait", "rest", "help", "quit", "save", "load"
}

# Regex patterns for validation
ALPHANUMERIC_PATTERN = re.compile(r'^[a-zA-Z0-9_\-\s]+$')
FILENAME_PATTERN = re.compile(r'^[a-zA-Z0-9_\-\.]+$')
SAFE_STRING_PATTERN = re.compile(r'^[a-zA-Z0-9_\-\s\.\,\!\?]+$')


def sanitize_string(input_string: str, max_length: int = 100, allow_special_chars: bool = False) -> str:
    """
    Sanitize a string input by removing potentially harmful characters.
    
    Args:
        input_string (str): The string to sanitize
        max_length (int): Maximum allowed length
        allow_special_chars (bool): Whether to allow special characters
    
    Returns:
        str: Sanitized string
    
    Raises:
        ValidationError: If input is invalid
    """
    if not isinstance(input_string, str):
        raise ValidationError(
            "Input must be a string",
            input_value=input_string,
            expected_type="string"
        )
    
    # Remove leading/trailing whitespace
    sanitized = input_string.strip()
    
    # Check length
    if len(sanitized) > max_length:
        raise ValidationError(
            f"Input too long (max {max_length} characters)",
            input_value=sanitized,
            context={'max_length': max_length, 'actual_length': len(sanitized)}
        )
    
    if len(sanitized) == 0:
        raise ValidationError(
            "Input cannot be empty",
            input_value=input_string
        )
    
    # Check for valid characters
    if allow_special_chars:
        pattern = SAFE_STRING_PATTERN
    else:
        pattern = ALPHANUMERIC_PATTERN
    
    if not pattern.match(sanitized):
        raise ValidationError(
            "Input contains invalid characters",
            input_value=sanitized,
            context={'allowed_pattern': pattern.pattern}
        )
    
    return sanitized


def validate_player_name(name: str) -> str:
    """
    Validate and sanitize a player name.
    
    Args:
        name (str): Player name to validate
    
    Returns:
        str: Validated player name
    
    Raises:
        ValidationError: If name is invalid
    """
    try:
        sanitized_name = sanitize_string(
            name,
            max_length=MAX_PLAYER_NAME_LENGTH,
            allow_special_chars=False
        )
        
        if len(sanitized_name) < MIN_PLAYER_NAME_LENGTH:
            raise ValidationError(
                f"Player name too short (min {MIN_PLAYER_NAME_LENGTH} characters)",
                input_value=name,
                context={'min_length': MIN_PLAYER_NAME_LENGTH}
            )
        
        # Check for reserved names
        reserved_names = {"admin", "system", "null", "undefined", "test"}
        if sanitized_name.lower() in reserved_names:
            raise ValidationError(
                "Player name is reserved",
                input_value=sanitized_name,
                context={'reserved_names': list(reserved_names)}
            )
        
        return sanitized_name
        
    except ValidationError:
        raise
    except Exception as e:
        raise ValidationError(f"Failed to validate player name: {e}", input_value=name)


def validate_location_name(location: str) -> str:
    """
    Validate a location name.
    
    Args:
        location (str): Location name to validate
    
    Returns:
        str: Validated location name
    
    Raises:
        ValidationError: If location is invalid
    """
    if not isinstance(location, str):
        raise ValidationError(
            "Location must be a string",
            input_value=location,
            expected_type="string"
        )
    
    # Normalize location name (title case)
    normalized_location = location.strip().title()
    
    if normalized_location not in VALID_LOCATION_NAMES:
        raise ValidationError(
            f"Invalid location: {location}",
            input_value=location,
            context={'valid_locations': list(VALID_LOCATION_NAMES)}
        )
    
    return normalized_location


def validate_item_name(item: str) -> str:
    """
    Validate an item name.
    
    Args:
        item (str): Item name to validate
    
    Returns:
        str: Validated item name
    
    Raises:
        ValidationError: If item is invalid
    """
    if not isinstance(item, str):
        raise ValidationError(
            "Item name must be a string",
            input_value=item,
            expected_type="string"
        )
    
    # Normalize item name (lowercase)
    normalized_item = item.strip().lower()
    
    if normalized_item not in VALID_ITEM_NAMES:
        # Check for partial matches (fuzzy matching)
        close_matches = [name for name in VALID_ITEM_NAMES if normalized_item in name or name in normalized_item]
        
        context = {'valid_items': list(VALID_ITEM_NAMES)}
        if close_matches:
            context['suggestions'] = close_matches
        
        raise ValidationError(
            f"Invalid item: {item}",
            input_value=item,
            context=context
        )
    
    return normalized_item


def validate_action(action: str) -> str:
    """
    Validate a player action.
    
    Args:
        action (str): Action to validate
    
    Returns:
        str: Validated action
    
    Raises:
        ValidationError: If action is invalid
    """
    if not isinstance(action, str):
        raise ValidationError(
            "Action must be a string",
            input_value=action,
            expected_type="string"
        )
    
    # Sanitize and normalize action
    sanitized_action = sanitize_string(action, max_length=100, allow_special_chars=True).lower()
    
    # Extract the base action (first word or phrase)
    action_parts = sanitized_action.split()
    if not action_parts:
        raise ValidationError(
            "Action cannot be empty",
            input_value=action
        )
    
    base_action = action_parts[0]
    
    # Check for compound actions (e.g., "pick up")
    if len(action_parts) > 1 and f"{action_parts[0]} {action_parts[1]}" in VALID_ACTIONS:
        base_action = f"{action_parts[0]} {action_parts[1]}"
    
    # Validate against known actions (allow unknown actions for flexibility)
    return sanitized_action


def validate_save_filename(filename: str) -> str:
    """
    Validate a save file name.
    
    Args:
        filename (str): Filename to validate
    
    Returns:
        str: Validated filename
    
    Raises:
        ValidationError: If filename is invalid
    """
    if not isinstance(filename, str):
        raise ValidationError(
            "Filename must be a string",
            input_value=filename,
            expected_type="string"
        )
    
    # Remove path components for security
    filename = os.path.basename(filename.strip())
    
    if len(filename) > MAX_SAVE_FILENAME_LENGTH:
        raise ValidationError(
            f"Filename too long (max {MAX_SAVE_FILENAME_LENGTH} characters)",
            input_value=filename,
            context={'max_length': MAX_SAVE_FILENAME_LENGTH}
        )
    
    if not filename:
        raise ValidationError(
            "Filename cannot be empty",
            input_value=filename
        )
    
    # Check for valid filename characters
    if not FILENAME_PATTERN.match(filename):
        raise ValidationError(
            "Filename contains invalid characters",
            input_value=filename,
            context={'allowed_pattern': FILENAME_PATTERN.pattern}
        )
    
    # Check for reserved filenames
    reserved_names = {"con", "prn", "aux", "nul", "com1", "com2", "lpt1", "lpt2"}
    name_without_ext = Path(filename).stem.lower()
    if name_without_ext in reserved_names:
        raise ValidationError(
            "Filename is reserved",
            input_value=filename,
            context={'reserved_names': list(reserved_names)}
        )
    
    return filename


def validate_numeric_input(value: Any, min_value: Optional[float] = None, max_value: Optional[float] = None, 
                          integer_only: bool = False) -> Union[int, float]:
    """
    Validate numeric input.
    
    Args:
        value: Value to validate
        min_value (float): Minimum allowed value
        max_value (float): Maximum allowed value
        integer_only (bool): Whether to allow only integers
    
    Returns:
        Union[int, float]: Validated numeric value
    
    Raises:
        ValidationError: If value is invalid
    """
    try:
        if isinstance(value, str):
            value = value.strip()
            if integer_only:
                numeric_value = int(value)
            else:
                numeric_value = float(value)
        elif isinstance(value, (int, float)):
            numeric_value = value
        else:
            raise ValidationError(
                "Value must be numeric",
                input_value=value,
                expected_type="number"
            )
        
        if min_value is not None and numeric_value < min_value:
            raise ValidationError(
                f"Value too small (min {min_value})",
                input_value=value,
                context={'min_value': min_value, 'actual_value': numeric_value}
            )
        
        if max_value is not None and numeric_value > max_value:
            raise ValidationError(
                f"Value too large (max {max_value})",
                input_value=value,
                context={'max_value': max_value, 'actual_value': numeric_value}
            )
        
        return numeric_value
        
    except ValueError as e:
        raise ValidationError(
            f"Invalid numeric value: {e}",
            input_value=value,
            expected_type="number"
        )


def validate_player_state(player: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate player state dictionary.
    
    Args:
        player (dict): Player state to validate
    
    Returns:
        dict: Validated player state
    
    Raises:
        ValidationError: If player state is invalid
    """
    if not isinstance(player, dict):
        raise ValidationError(
            "Player state must be a dictionary",
            input_value=type(player).__name__,
            expected_type="dict"
        )
    
    required_fields = {'name', 'health', 'inventory', 'location', 'gold'}
    missing_fields = required_fields - set(player.keys())
    
    if missing_fields:
        raise ValidationError(
            f"Missing required player fields: {missing_fields}",
            context={'missing_fields': list(missing_fields), 'required_fields': list(required_fields)}
        )
    
    validated_player = {}
    
    # Validate name
    validated_player['name'] = validate_player_name(player['name'])
    
    # Validate health
    validated_player['health'] = validate_numeric_input(
        player['health'], min_value=0, max_value=100, integer_only=True
    )
    
    # Validate gold
    validated_player['gold'] = validate_numeric_input(
        player['gold'], min_value=0, integer_only=True
    )
    
    # Validate location
    validated_player['location'] = validate_location_name(player['location'])
    
    # Validate inventory
    if not isinstance(player['inventory'], list):
        raise ValidationError(
            "Inventory must be a list",
            input_value=type(player['inventory']).__name__,
            expected_type="list"
        )
    
    validated_inventory = []
    for item in player['inventory']:
        try:
            validated_item = validate_item_name(item)
            validated_inventory.append(validated_item)
        except ValidationError:
            # Skip invalid items but log the issue
            continue
    
    validated_player['inventory'] = validated_inventory
    
    return validated_player


def validate_world_state(world: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate world state dictionary.
    
    Args:
        world (dict): World state to validate
    
    Returns:
        dict: Validated world state
    
    Raises:
        ValidationError: If world state is invalid
    """
    if not isinstance(world, dict):
        raise ValidationError(
            "World state must be a dictionary",
            input_value=type(world).__name__,
            expected_type="dict"
        )
    
    required_fields = {'current_location', 'locations'}
    missing_fields = required_fields - set(world.keys())
    
    if missing_fields:
        raise ValidationError(
            f"Missing required world fields: {missing_fields}",
            context={'missing_fields': list(missing_fields), 'required_fields': list(required_fields)}
        )
    
    validated_world = {}
    
    # Validate current location
    validated_world['current_location'] = validate_location_name(world['current_location'])
    
    # Validate locations dictionary
    if not isinstance(world['locations'], dict):
        raise ValidationError(
            "Locations must be a dictionary",
            input_value=type(world['locations']).__name__,
            expected_type="dict"
        )
    
    validated_locations = {}
    for location_name, location_data in world['locations'].items():
        try:
            validated_location_name = validate_location_name(location_name)
            
            if not isinstance(location_data, dict):
                continue
            
            validated_location_data = {
                'description': location_data.get('description', ''),
                'connections': location_data.get('connections', []),
                'items': location_data.get('items', [])
            }
            
            # Validate connections
            validated_connections = []
            for connection in validated_location_data['connections']:
                try:
                    validated_connection = validate_location_name(connection)
                    validated_connections.append(validated_connection)
                except ValidationError:
                    continue
            validated_location_data['connections'] = validated_connections
            
            # Validate items
            validated_items = []
            for item in validated_location_data['items']:
                try:
                    validated_item = validate_item_name(item)
                    validated_items.append(validated_item)
                except ValidationError:
                    continue
            validated_location_data['items'] = validated_items
            
            validated_locations[validated_location_name] = validated_location_data
            
        except ValidationError:
            continue
    
    validated_world['locations'] = validated_locations
    
    return validated_world


def validate_choice_input(choice: str, valid_choices: List[str]) -> str:
    """
    Validate a choice input against a list of valid choices.
    
    Args:
        choice (str): User's choice
        valid_choices (list): List of valid choices
    
    Returns:
        str: Validated choice
    
    Raises:
        ValidationError: If choice is invalid
    """
    if not isinstance(choice, str):
        raise ValidationError(
            "Choice must be a string",
            input_value=choice,
            expected_type="string"
        )
    
    choice = choice.strip().lower()
    
    # Check for exact match
    for valid_choice in valid_choices:
        if choice == valid_choice.lower():
            return valid_choice
    
    # Check for numeric choice (1-based indexing)
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(valid_choices):
            return valid_choices[choice_index]
    except ValueError:
        pass
    
    raise ValidationError(
        f"Invalid choice: {choice}",
        input_value=choice,
        context={'valid_choices': valid_choices}
    )


# Decorator for input validation
def validate_input(validation_func):
    """
    Decorator to add input validation to functions.
    
    Args:
        validation_func: Function to validate inputs
    
    Returns:
        Decorated function
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # Apply validation
                validated_args, validated_kwargs = validation_func(*args, **kwargs)
                return func(*validated_args, **validated_kwargs)
            except ValidationError:
                raise
            except Exception as e:
                raise ValidationError(f"Validation failed: {e}")
        return wrapper
    return decorator

