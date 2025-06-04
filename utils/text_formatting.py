"""
Text formatting and display utilities for Kevin's Adventure Game.

This module provides functions for formatting game text, displaying messages,
and creating consistent user interface elements throughout the game.
"""

import textwrap


def print_welcome_message():
    """
    Display the welcome message when the game starts.
    
    Side Effects:
        - Prints a formatted welcome message to the console
        
    Example:
        >>> print_welcome_message()
        ========================================
        Welcome to Kevin's Adventure Game!
        ========================================
        ...
    """
    print("=" * 40)
    print("Welcome to Kevin's Adventure Game!")
    print("=" * 40)
    print("Embark on an epic adventure through mystical lands,")
    print("discover treasures, meet mythical creatures, and")
    print("uncover the secrets of this magical world!")
    print()
    print("Type 'help' at any time to see available commands.")
    print("=" * 40)

def print_help():
    """
    Display the help message with available commands.
    
    Side Effects:
        - Prints a formatted help message to the console
        
    Example:
        >>> print_help()
        ========================================
        Available Commands:
        ========================================
        ...
    """
    print("=" * 40)
    print("Available Commands:")
    print("=" * 40)
    print("Movement:")
    print("  go, move, travel - Show available locations")
    print("  [location name] - Move to a specific location")
    print()
    print("Items:")
    print("  use [item] - Use an item from your inventory")
    print("  take [item] - Pick up an item")
    print("  examine [item] - Look at an item closely")
    print("  inventory, inv - Show your inventory")
    print()
    print("Information:")
    print("  status, stats - Show your current status")
    print("  locations - Show where you can go")
    print("  explore, look around - Explore current location")
    print()
    print("Game:")
    print("  help - Show this help message")
    print("  quit - Save and exit the game")
    print("=" * 40)

def print_game_over():
    """
    Display the game over message when the player is defeated.
    
    Side Effects:
        - Prints a formatted game over message to the console
        
    Example:
        >>> print_game_over()
        ========================================
        GAME OVER
        ========================================
        ...
    """
    print("=" * 40)
    print("GAME OVER")
    print("=" * 40)
    print("Your adventure has come to an end.")
    print("Don't give up! You can start a new game")
    print("or load a previous save to continue your quest.")
    print("=" * 40)

def format_inventory(inventory):
    """
    Format the player's inventory for display.
    
    Args:
        inventory (list): List of item names in the player's inventory
        
    Returns:
        str: Formatted string representation of the inventory
        
    Example:
        >>> items = ["sword", "potion", "map"]
        >>> formatted = format_inventory(items)
        >>> print(formatted)
        sword, potion, map
        
        >>> empty = format_inventory([])
        >>> print(empty)
        empty
    """
    if not inventory:
        return "empty"
    return ", ".join(inventory)

def print_event(event_text, event_type="info"):
    """
    Print a formatted event message with appropriate styling.
    
    Args:
        event_text (str): The text of the event to display
        event_type (str): The type of event ("info", "warning", "success", "danger")
                         Defaults to "info"
    
    Side Effects:
        - Prints a formatted event message to the console
        
    Example:
        >>> print_event("You found a treasure!", "success")
        ✅ You found a treasure!
        
        >>> print_event("A monster appears!", "danger")
        ⚠️ A monster appears!
    """
    icons = {
        "info": "ℹ️",
        "warning": "⚠️",
        "success": "✅",
        "danger": "💀",
        "mystery": "🔮"
    }
    
    icon = icons.get(event_type, "ℹ️")
    print(f"{icon} {event_text}")

def wrap_text(text, width=70):
    """
    Wrap text to a specified width for better readability.
    
    Args:
        text (str): The text to wrap
        width (int): Maximum line width (default: 70)
        
    Returns:
        str: Text wrapped to the specified width
        
    Example:
        >>> long_text = "This is a very long line of text that should be wrapped."
        >>> wrapped = wrap_text(long_text, 20)
        >>> print(wrapped)
        This is a very long
        line of text that
        should be wrapped.
    """
    return textwrap.fill(text, width=width)

def print_location_header(location_name):
    """
    Print a formatted header for a location.
    
    Args:
        location_name (str): The name of the location
        
    Side Effects:
        - Prints a formatted location header to the console
        
    Example:
        >>> print_location_header("Mystical Forest")
        ╔══════════════════════════════════════╗
        ║            MYSTICAL FOREST           ║
        ╚══════════════════════════════════════╝
    """
    name_upper = location_name.upper()
    width = max(40, len(name_upper) + 4)
    
    print("╔" + "═" * (width - 2) + "╗")
    print(f"║{name_upper:^{width - 2}}║")
    print("╚" + "═" * (width - 2) + "╝")

def format_item_list(items, title="Items"):
    """
    Format a list of items for display.
    
    Args:
        items (list): List of item names
        title (str): Title for the item list (default: "Items")
        
    Returns:
        str: Formatted string representation of the item list
        
    Example:
        >>> items = ["sword", "shield", "potion"]
        >>> formatted = format_item_list(items, "Inventory")
        >>> print(formatted)
        Inventory:
        • sword
        • shield
        • potion
    """
    if not items:
        return f"{title}: None"
    
    formatted = f"{title}:\n"
    for item in items:
        formatted += f"• {item}\n"
    
    return formatted.rstrip()

def print_separator(char="=", length=40):
    """
    Print a separator line for visual organization.
    
    Args:
        char (str): Character to use for the separator (default: "=")
        length (int): Length of the separator line (default: 40)
        
    Side Effects:
        - Prints a separator line to the console
        
    Example:
        >>> print_separator()
        ========================================
        
        >>> print_separator("-", 20)
        --------------------
    """
    print(char * length)
