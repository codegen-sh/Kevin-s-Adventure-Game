"""
Input handling utilities with validation and error handling.
"""
from typing import List, Optional, Union, Callable, Any
import re


class InputValidator:
    """
    Utility class for validating and processing user input.
    """
    
    @staticmethod
    def get_valid_choice(prompt: str, valid_choices: List[str], case_sensitive: bool = False) -> str:
        """
        Get a valid choice from the user.
        
        Args:
            prompt: Prompt to display to user
            valid_choices: List of valid choices
            case_sensitive: Whether choices are case sensitive
            
        Returns:
            Valid choice from the user
        """
        while True:
            try:
                choice = input(prompt).strip()
                
                if not case_sensitive:
                    choice = choice.lower()
                    valid_choices = [c.lower() for c in valid_choices]
                
                if choice in valid_choices:
                    return choice
                else:
                    print(f"Invalid choice. Please choose from: {', '.join(valid_choices)}")
                    
            except (KeyboardInterrupt, EOFError):
                print("\nInput cancelled.")
                raise
            except Exception as e:
                print(f"Input error: {e}")
    
    @staticmethod
    def get_integer_input(prompt: str, min_value: Optional[int] = None, max_value: Optional[int] = None) -> int:
        """
        Get a valid integer from the user.
        
        Args:
            prompt: Prompt to display to user
            min_value: Minimum allowed value (optional)
            max_value: Maximum allowed value (optional)
            
        Returns:
            Valid integer from the user
        """
        while True:
            try:
                value = int(input(prompt).strip())
                
                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}")
                    continue
                
                if max_value is not None and value > max_value:
                    print(f"Value must be at most {max_value}")
                    continue
                
                return value
                
            except ValueError:
                print("Please enter a valid number.")
            except (KeyboardInterrupt, EOFError):
                print("\nInput cancelled.")
                raise
            except Exception as e:
                print(f"Input error: {e}")
    
    @staticmethod
    def get_yes_no_input(prompt: str, default: Optional[bool] = None) -> bool:
        """
        Get a yes/no response from the user.
        
        Args:
            prompt: Prompt to display to user
            default: Default value if user just presses enter
            
        Returns:
            True for yes, False for no
        """
        if default is not None:
            default_text = " (Y/n)" if default else " (y/N)"
            prompt += default_text
        
        while True:
            try:
                response = input(prompt + ": ").strip().lower()
                
                if not response and default is not None:
                    return default
                
                if response in ['y', 'yes', 'true', '1']:
                    return True
                elif response in ['n', 'no', 'false', '0']:
                    return False
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
                    
            except (KeyboardInterrupt, EOFError):
                print("\nInput cancelled.")
                raise
            except Exception as e:
                print(f"Input error: {e}")
    
    @staticmethod
    def get_string_input(prompt: str, min_length: int = 0, max_length: Optional[int] = None, 
                        pattern: Optional[str] = None, allow_empty: bool = True) -> str:
        """
        Get a validated string from the user.
        
        Args:
            prompt: Prompt to display to user
            min_length: Minimum string length
            max_length: Maximum string length (optional)
            pattern: Regex pattern to match (optional)
            allow_empty: Whether to allow empty strings
            
        Returns:
            Valid string from the user
        """
        while True:
            try:
                value = input(prompt).strip()
                
                if not allow_empty and not value:
                    print("Input cannot be empty.")
                    continue
                
                if len(value) < min_length:
                    print(f"Input must be at least {min_length} characters long.")
                    continue
                
                if max_length is not None and len(value) > max_length:
                    print(f"Input must be at most {max_length} characters long.")
                    continue
                
                if pattern is not None and not re.match(pattern, value):
                    print("Input format is invalid.")
                    continue
                
                return value
                
            except (KeyboardInterrupt, EOFError):
                print("\nInput cancelled.")
                raise
            except Exception as e:
                print(f"Input error: {e}")
    
    @staticmethod
    def get_menu_choice(options: List[str], prompt: str = "Enter your choice", 
                       allow_cancel: bool = True) -> Optional[int]:
        """
        Display a menu and get the user's choice.
        
        Args:
            options: List of menu options
            prompt: Prompt to display
            allow_cancel: Whether to allow cancelling (returns None)
            
        Returns:
            Index of chosen option (0-based), or None if cancelled
        """
        print("\nMenu:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        if allow_cancel:
            print("0. Cancel")
        
        while True:
            try:
                choice = InputValidator.get_integer_input(
                    f"{prompt} (1-{len(options)}" + (", 0 to cancel" if allow_cancel else "") + "): ",
                    min_value=0 if allow_cancel else 1,
                    max_value=len(options)
                )
                
                if choice == 0 and allow_cancel:
                    return None
                
                return choice - 1  # Convert to 0-based index
                
            except (KeyboardInterrupt, EOFError):
                if allow_cancel:
                    return None
                raise


class SafeInput:
    """
    Safe input handling with automatic error recovery.
    """
    
    @staticmethod
    def safe_input(prompt: str, default: str = "", timeout: Optional[float] = None) -> str:
        """
        Safely get input from user with error handling.
        
        Args:
            prompt: Prompt to display
            default: Default value if input fails
            timeout: Input timeout in seconds (optional)
            
        Returns:
            User input or default value
        """
        try:
            if timeout:
                # Note: timeout functionality would require additional implementation
                # For now, just use regular input
                pass
            
            result = input(prompt).strip()
            return result if result else default
            
        except (KeyboardInterrupt, EOFError):
            print(f"\nInput interrupted. Using default: '{default}'")
            return default
        except Exception as e:
            print(f"Input error: {e}. Using default: '{default}'")
            return default
    
    @staticmethod
    def safe_choice(prompt: str, choices: List[str], default: str = "") -> str:
        """
        Safely get a choice from user with error handling.
        
        Args:
            prompt: Prompt to display
            choices: List of valid choices
            default: Default choice if input fails
            
        Returns:
            Valid choice or default
        """
        try:
            return InputValidator.get_valid_choice(prompt, choices)
        except (KeyboardInterrupt, EOFError):
            print(f"\nChoice interrupted. Using default: '{default}'")
            return default
        except Exception as e:
            print(f"Choice error: {e}. Using default: '{default}'")
            return default


def handle_input_error(func: Callable) -> Callable:
    """
    Decorator to handle input errors gracefully.
    
    Args:
        func: Function to wrap
        
    Returns:
        Wrapped function with error handling
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled by user.")
            return None
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            return None
    
    return wrapper


# Convenience functions for common input patterns
def get_player_name(default: str = "Kevin") -> str:
    """Get player name with validation."""
    return InputValidator.get_string_input(
        f"Enter your character's name (default: {default}): ",
        min_length=1,
        max_length=20,
        pattern=r'^[a-zA-Z][a-zA-Z0-9_]*$'
    ) or default


def get_save_file_choice(save_files: List[str]) -> Optional[int]:
    """Get save file choice from user."""
    if not save_files:
        return None
    
    return InputValidator.get_menu_choice(
        save_files,
        "Choose a save file to load",
        allow_cancel=True
    )


def confirm_action(action: str) -> bool:
    """Get confirmation for an action."""
    return InputValidator.get_yes_no_input(f"Are you sure you want to {action}?")


def get_command_input() -> str:
    """Get game command input with basic validation."""
    return SafeInput.safe_input("What would you like to do? ", "help").lower()
