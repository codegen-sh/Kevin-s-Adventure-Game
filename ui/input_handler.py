"""
Input handler module for processing and validating user input.
Provides a clean interface for handling different types of user input.
"""
from typing import Optional, List, Tuple, Union
import re

from game.exceptions import InvalidInputError


class InputHandler:
    """Handles and validates user input."""
    
    @staticmethod
    def get_command() -> str:
        """Get a command from the user."""
        try:
            command = input("What would you like to do? ").strip()
            if not command:
                raise InvalidInputError("Please enter a command.")
            return command.lower()
        except EOFError:
            return "quit"
        except KeyboardInterrupt:
            return "quit"
    
    @staticmethod
    def get_yes_no(prompt: str, default: Optional[bool] = None) -> bool:
        """
        Get a yes/no response from the user.
        
        Args:
            prompt: The question to ask
            default: Default value if user just presses enter
            
        Returns:
            bool: True for yes, False for no
        """
        if default is True:
            prompt += " (Y/n): "
        elif default is False:
            prompt += " (y/N): "
        else:
            prompt += " (y/n): "
        
        while True:
            try:
                response = input(prompt).strip().lower()
                
                if not response and default is not None:
                    return default
                
                if response in ['y', 'yes', 'true', '1']:
                    return True
                elif response in ['n', 'no', 'false', '0']:
                    return False
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
                    
            except (EOFError, KeyboardInterrupt):
                return False
    
    @staticmethod
    def get_choice(prompt: str, choices: List[str], allow_numbers: bool = True) -> str:
        """
        Get a choice from a list of options.
        
        Args:
            prompt: The question to ask
            choices: List of valid choices
            allow_numbers: Whether to allow numeric selection
            
        Returns:
            str: The selected choice
        """
        if allow_numbers:
            print(f"\n{prompt}")
            for i, choice in enumerate(choices, 1):
                print(f"{i}. {choice}")
            print()
        
        while True:
            try:
                if allow_numbers:
                    response = input("Enter your choice (number or name): ").strip()
                else:
                    response = input(f"{prompt}: ").strip()
                
                if not response:
                    print("Please enter a choice.")
                    continue
                
                # Check if it's a number
                if allow_numbers and response.isdigit():
                    choice_num = int(response)
                    if 1 <= choice_num <= len(choices):
                        return choices[choice_num - 1]
                    else:
                        print(f"Please enter a number between 1 and {len(choices)}.")
                        continue
                
                # Check if it's a valid choice name
                response_lower = response.lower()
                for choice in choices:
                    if choice.lower() == response_lower:
                        return choice
                
                print(f"Invalid choice. Please select from: {', '.join(choices)}")
                
            except (EOFError, KeyboardInterrupt):
                raise InvalidInputError("Input cancelled by user")
    
    @staticmethod
    def get_number(prompt: str, min_val: Optional[int] = None, max_val: Optional[int] = None) -> int:
        """
        Get a number from the user with optional range validation.
        
        Args:
            prompt: The question to ask
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            
        Returns:
            int: The entered number
        """
        while True:
            try:
                response = input(f"{prompt}: ").strip()
                
                if not response:
                    print("Please enter a number.")
                    continue
                
                number = int(response)
                
                if min_val is not None and number < min_val:
                    print(f"Number must be at least {min_val}.")
                    continue
                
                if max_val is not None and number > max_val:
                    print(f"Number must be at most {max_val}.")
                    continue
                
                return number
                
            except ValueError:
                print("Please enter a valid number.")
            except (EOFError, KeyboardInterrupt):
                raise InvalidInputError("Input cancelled by user")
    
    @staticmethod
    def get_string(prompt: str, min_length: int = 1, max_length: Optional[int] = None) -> str:
        """
        Get a string from the user with length validation.
        
        Args:
            prompt: The question to ask
            min_length: Minimum string length
            max_length: Maximum string length
            
        Returns:
            str: The entered string
        """
        while True:
            try:
                response = input(f"{prompt}: ").strip()
                
                if len(response) < min_length:
                    print(f"Input must be at least {min_length} characters long.")
                    continue
                
                if max_length is not None and len(response) > max_length:
                    print(f"Input must be at most {max_length} characters long.")
                    continue
                
                return response
                
            except (EOFError, KeyboardInterrupt):
                raise InvalidInputError("Input cancelled by user")
    
    @staticmethod
    def parse_command(command: str) -> Tuple[str, List[str]]:
        """
        Parse a command into action and arguments.
        
        Args:
            command: The full command string
            
        Returns:
            Tuple of (action, arguments)
        """
        parts = command.strip().split()
        if not parts:
            return "", []
        
        action = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        return action, args
    
    @staticmethod
    def normalize_item_name(item_name: str) -> str:
        """
        Normalize an item name for consistent handling.
        
        Args:
            item_name: The raw item name
            
        Returns:
            str: Normalized item name
        """
        # Convert to lowercase and replace spaces with underscores
        normalized = item_name.lower().strip()
        normalized = re.sub(r'\s+', '_', normalized)
        normalized = re.sub(r'[^\w_]', '', normalized)  # Remove special characters
        return normalized
    
    @staticmethod
    def normalize_location_name(location_name: str) -> str:
        """
        Normalize a location name for consistent handling.
        
        Args:
            location_name: The raw location name
            
        Returns:
            str: Normalized location name
        """
        # Convert to title case for locations
        return location_name.strip().title()
    
    @staticmethod
    def validate_save_filename(filename: str) -> bool:
        """
        Validate a save file name.
        
        Args:
            filename: The proposed filename
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Check for valid characters and reasonable length
        if not filename or len(filename) > 50:
            return False
        
        # Allow alphanumeric, spaces, hyphens, and underscores
        pattern = r'^[a-zA-Z0-9\s\-_]+$'
        return bool(re.match(pattern, filename))


# Global input handler instance
input_handler = InputHandler()

