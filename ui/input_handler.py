"""
Module for handling user input in the game.
This separates the UI code from the game logic.
"""

from ui.display import print_error


def get_input(prompt):
    """
    Get input from the user with a prompt.
    
    Args:
        prompt (str): The prompt to display
    
    Returns:
        str: The user's input
    """
    return input(prompt).strip()


def get_command():
    """
    Get a command from the user.
    
    Returns:
        str: The user's command
    """
    return get_input("What would you like to do? ").lower()


def get_choice(options, prompt="Enter your choice: "):
    """
    Get a choice from the user from a list of options.
    
    Args:
        options (list): The list of options
        prompt (str, optional): The prompt to display. Defaults to "Enter your choice: ".
    
    Returns:
        str: The user's choice
    """
    while True:
        choice = get_input(prompt)
        if choice in options:
            return choice
        print_error(f"Invalid choice. Please choose from: {', '.join(options)}")


def get_numeric_choice(min_value, max_value, prompt="Enter your choice: "):
    """
    Get a numeric choice from the user within a range.
    
    Args:
        min_value (int): The minimum value
        max_value (int): The maximum value
        prompt (str, optional): The prompt to display. Defaults to "Enter your choice: ".
    
    Returns:
        int: The user's choice
    """
    while True:
        try:
            choice = int(get_input(prompt))
            if min_value <= choice <= max_value:
                return choice
            print_error(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print_error("Please enter a valid number.")


def get_yes_no(prompt="(y/n): "):
    """
    Get a yes/no response from the user.
    
    Args:
        prompt (str, optional): The prompt to display. Defaults to "(y/n): ".
    
    Returns:
        bool: True if the user answered yes, False otherwise
    """
    while True:
        choice = get_input(prompt).lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        print_error("Please answer 'y' or 'n'.")


def parse_command(command):
    """
    Parse a command string into a command and arguments.
    
    Args:
        command (str): The command string
    
    Returns:
        tuple: A tuple containing the command and arguments
    """
    parts = command.split(" ", 1)
    cmd = parts[0]
    args = parts[1] if len(parts) > 1 else ""
    return cmd, args


def validate_command(command, valid_commands):
    """
    Validate a command against a list of valid commands.
    
    Args:
        command (str): The command to validate
        valid_commands (list): The list of valid commands
    
    Returns:
        bool: True if the command is valid, False otherwise
    """
    return command in valid_commands

