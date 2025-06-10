"""
Text formatting utilities for Kevin's Adventure Game.
"""
import textwrap
from typing import List


def wrap_text(text: str, width: int = 80) -> str:
    """
    Wrap text to a specified width.

    Args:
        text: The text to wrap
        width: The width to wrap to

    Returns:
        The wrapped text
    """
    return textwrap.fill(text, width=width)


def print_welcome_message() -> None:
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


def print_help() -> None:
    """
    Print a formatted help message with available commands.
    """
    help_text = """
Available commands:
- move [location]: Move to a new location
- look: Examine your surroundings
- inventory: Check your inventory
- pickup [item]: Pick up an item
- drop [item]: Drop an item from your inventory
- use [item]: Use an item
- examine [item]: Get a description of an item
- status: Check your current status
- interact: Interact with your current location
- help: Show this help message
- quit: Save and exit the game
    """
    print(help_text.strip())


def format_inventory(inventory: List[str]) -> str:
    """
    Format the player's inventory for display.

    Args:
        inventory: The player's inventory

    Returns:
        A formatted string representation of the inventory
    """
    if not inventory:
        return "empty"
    return ", ".join(inventory)


def print_separator(char: str = "-", length: int = 80) -> None:
    """
    Print a separator line.

    Args:
        char: The character to use for the separator
        length: The length of the separator
    """
    print(char * length)


def print_event(event_text: str) -> None:
    """
    Print a formatted event message.

    Args:
        event_text: The event text to print
    """
    print_separator()
    print(wrap_text(event_text))
    print_separator()


def print_game_over() -> None:
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

