"""
Input validation and error handling utilities for Kevin's Adventure Game.
"""

import re
from typing import List, Optional, Union


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def validate_player_name(name: str) -> str:
    """
    Validate and sanitize player name.
    
    Args:
        name (str): The player name to validate
        
    Returns:
        str: The validated and sanitized name
        
    Raises:
        ValidationError: If the name is invalid
    """
    if not name or not name.strip():
        raise ValidationError("Player name cannot be empty.")
    
    # Remove extra whitespace and limit length
    name = name.strip()[:20]
    
    # Check for valid characters (letters, numbers, spaces, basic punctuation)
    if not re.match(r"^[a-zA-Z0-9\s\-_'\.]+$", name):
        raise ValidationError("Player name contains invalid characters.")
    
    return name


def validate_action_input(action: str) -> str:
    """
    Validate and sanitize user action input.
    
    Args:
        action (str): The action string to validate
        
    Returns:
        str: The validated and sanitized action
        
    Raises:
        ValidationError: If the action is invalid
    """
    if not action or not action.strip():
        raise ValidationError("Action cannot be empty.")
    
    # Remove extra whitespace and convert to lowercase
    action = action.strip().lower()
    
    # Limit length to prevent abuse
    if len(action) > 100:
        raise ValidationError("Action is too long.")
    
    # Check for basic safety (no special characters that could be harmful)
    if re.search(r'[<>"\';\\]', action):
        raise ValidationError("Action contains invalid characters.")
    
    return action


def validate_item_name(item: str) -> str:
    """
    Validate and sanitize item name.
    
    Args:
        item (str): The item name to validate
        
    Returns:
        str: The validated and sanitized item name
        
    Raises:
        ValidationError: If the item name is invalid
    """
    if not item or not item.strip():
        raise ValidationError("Item name cannot be empty.")
    
    # Remove extra whitespace and convert to lowercase
    item = item.strip().lower()
    
    # Replace spaces with underscores for consistency
    item = item.replace(" ", "_")
    
    # Check for valid characters
    if not re.match(r"^[a-zA-Z0-9_]+$", item):
        raise ValidationError("Item name contains invalid characters.")
    
    return item


def validate_location_name(location: str) -> str:
    """
    Validate and sanitize location name.
    
    Args:
        location (str): The location name to validate
        
    Returns:
        str: The validated and sanitized location name
        
    Raises:
        ValidationError: If the location name is invalid
    """
    if not location or not location.strip():
        raise ValidationError("Location name cannot be empty.")
    
    # Remove extra whitespace and title case
    location = location.strip().title()
    
    # Check for valid characters
    if not re.match(r"^[a-zA-Z\s]+$", location):
        raise ValidationError("Location name contains invalid characters.")
    
    return location


def validate_save_filename(filename: str) -> str:
    """
    Validate and sanitize save file name.
    
    Args:
        filename (str): The filename to validate
        
    Returns:
        str: The validated and sanitized filename
        
    Raises:
        ValidationError: If the filename is invalid
    """
    if not filename or not filename.strip():
        raise ValidationError("Filename cannot be empty.")
    
    # Remove extra whitespace
    filename = filename.strip()
    
    # Check for valid filename characters
    if not re.match(r"^[a-zA-Z0-9_\-\.]+$", filename):
        raise ValidationError("Filename contains invalid characters.")
    
    # Ensure .json extension
    if not filename.endswith('.json'):
        filename += '.json'
    
    return filename


def validate_numeric_input(value: str, min_val: int = None, max_val: int = None) -> int:
    """
    Validate and convert numeric input.
    
    Args:
        value (str): The string value to validate
        min_val (int, optional): Minimum allowed value
        max_val (int, optional): Maximum allowed value
        
    Returns:
        int: The validated numeric value
        
    Raises:
        ValidationError: If the value is invalid
    """
    try:
        num = int(value.strip())
    except ValueError:
        raise ValidationError("Value must be a number.")
    
    if min_val is not None and num < min_val:
        raise ValidationError(f"Value must be at least {min_val}.")
    
    if max_val is not None and num > max_val:
        raise ValidationError(f"Value must be at most {max_val}.")
    
    return num


def validate_choice_input(choice: str, valid_choices: List[str]) -> str:
    """
    Validate user choice against a list of valid options.
    
    Args:
        choice (str): The user's choice
        valid_choices (List[str]): List of valid choices
        
    Returns:
        str: The validated choice
        
    Raises:
        ValidationError: If the choice is invalid
    """
    if not choice or not choice.strip():
        raise ValidationError("Choice cannot be empty.")
    
    choice = choice.strip().lower()
    valid_choices_lower = [c.lower() for c in valid_choices]
    
    if choice not in valid_choices_lower:
        raise ValidationError(f"Invalid choice. Valid options are: {', '.join(valid_choices)}")
    
    # Return the original case version
    return valid_choices[valid_choices_lower.index(choice)]


def safe_input(prompt: str, validator=None, max_attempts: int = 3) -> Optional[str]:
    """
    Safely get user input with validation and error handling.
    
    Args:
        prompt (str): The input prompt to display
        validator (callable, optional): Validation function to apply
        max_attempts (int): Maximum number of input attempts
        
    Returns:
        str or None: The validated input, or None if max attempts exceeded
    """
    for attempt in range(max_attempts):
        try:
            user_input = input(prompt).strip()
            
            if validator:
                return validator(user_input)
            else:
                return user_input
                
        except ValidationError as e:
            print(f"Error: {e}")
            if attempt < max_attempts - 1:
                print("Please try again.")
            else:
                print("Maximum attempts exceeded.")
                return None
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled.")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    return None


def handle_file_operation(operation, *args, **kwargs):
    """
    Safely handle file operations with proper error handling.
    
    Args:
        operation (callable): The file operation function to execute
        *args: Arguments to pass to the operation
        **kwargs: Keyword arguments to pass to the operation
        
    Returns:
        tuple: (success: bool, result: any, error: str or None)
    """
    try:
        result = operation(*args, **kwargs)
        return True, result, None
    except FileNotFoundError as e:
        return False, None, f"File not found: {e}"
    except PermissionError as e:
        return False, None, f"Permission denied: {e}"
    except IOError as e:
        return False, None, f"File operation failed: {e}"
    except Exception as e:
        return False, None, f"Unexpected error: {e}"


def sanitize_user_input(text: str) -> str:
    """
    Sanitize user input to prevent potential security issues.
    
    Args:
        text (str): The text to sanitize
        
    Returns:
        str: The sanitized text
    """
    if not text:
        return ""
    
    # Remove potentially dangerous characters
    text = re.sub(r'[<>"\';\\]', '', text)
    
    # Limit length
    text = text[:200]
    
    # Remove excessive whitespace
    text = ' '.join(text.split())
    
    return text

