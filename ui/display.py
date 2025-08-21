"""
Module for handling game display and output.
This separates the UI code from the game logic.
"""

import textwrap


def wrap_text(text, width=80):
    """
    Wrap text to a specified width.
    
    Args:
        text (str): The text to wrap
        width (int, optional): The width to wrap to. Defaults to 80.
    
    Returns:
        str: The wrapped text
    """
    return textwrap.fill(text, width=width)


def print_welcome_message():
    """
    Print a formatted welcome message for the game.
    """
    welcome_text = """
Welcome to Kevin's Adventure Game!

Explore a world of mystery and danger as you navigate through
forests, caves, villages, and mountains. Collect items, interact
with characters, and uncover the secrets of this magical realm.

Type 'help' at any time to see available commands.

Your journey begins now. Good luck, adventurer!
    """
    print(welcome_text.strip())


def print_help():
    """
    Print a formatted help message with available commands.
    """
    help_text = """
Available commands:
- move [location]: Move to a new location
- look: Examine your surroundings
- inventory: Check your inventory
- pickup [item] or take [item]: Pick up an item
- drop [item]: Drop an item from your inventory
- use [item]: Use an item
- examine [item]: Get a description of an item
- status: Check your current status
- interact: Interact with your current location
- help: Show this help message
- quit: Save and exit the game
    """
    print(help_text.strip())


def format_inventory(inventory):
    """
    Format the player's inventory for display.
    
    Args:
        inventory (list): The player's inventory
    
    Returns:
        str: A formatted string representation of the inventory
    """
    if not inventory:
        return "empty"
    return ", ".join(inventory)


def print_separator(char="-", length=80):
    """
    Print a separator line.
    
    Args:
        char (str, optional): The character to use for the separator. Defaults to "-".
        length (int, optional): The length of the separator. Defaults to 80.
    """
    print(char * length)


def print_event(event_text):
    """
    Print a formatted event message.
    
    Args:
        event_text (str): The event text to print
    """
    print_separator()
    print(wrap_text(event_text))
    print_separator()


def print_game_over():
    """
    Print a formatted game over message.
    """
    game_over_text = """
    Game Over

    Your adventure has come to an end. Thank you for playing!
    """
    print_separator("=")
    print(game_over_text)
    print_separator("=")


def print_location_description(description, items=None, exits=None):
    """
    Print a formatted location description.
    
    Args:
        description (str): The location description
        items (list, optional): Items at the location. Defaults to None.
        exits (list, optional): Available exits. Defaults to None.
    """
    print("\n" + wrap_text(description))
    
    if items:
        print("\nYou see:")
        for item in items:
            print(f"- {item}")
    
    if exits:
        print("\nAvailable exits:")
        for exit in exits:
            print(f"- {exit}")


def print_player_status(player):
    """
    Print the player's current status.
    
    Args:
        player: The player object or dictionary
    """
    if hasattr(player, 'get_status'):
        status = player.get_status()
    else:
        status = f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"
    
    print(status)


def print_item_description(item, description):
    """
    Print a formatted item description.
    
    Args:
        item (str): The item name
        description (str): The item description
    """
    print(f"\n{item.capitalize()}: {description}")


def print_error(message):
    """
    Print a formatted error message.
    
    Args:
        message (str): The error message
    """
    print(f"\nError: {message}")


def print_success(message):
    """
    Print a formatted success message.
    
    Args:
        message (str): The success message
    """
    print(f"\nSuccess: {message}")


def print_warning(message):
    """
    Print a formatted warning message.
    
    Args:
        message (str): The warning message
    """
    print(f"\nWarning: {message}")


def print_info(message):
    """
    Print a formatted info message.
    
    Args:
        message (str): The info message
    """
    print(f"\n{message}")

