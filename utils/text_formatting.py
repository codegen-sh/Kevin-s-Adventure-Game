"""
Text formatting utilities - Legacy module for backward compatibility.
New code should use ui.display module instead.
"""
from typing import List
from ui.display import display


def print_welcome_message() -> None:
    """Print welcome message - delegates to display module."""
    display.print_welcome_message()


def print_help() -> None:
    """Print help information - delegates to display module."""
    display.print_help()


def print_colored(text: str, color: str = "white") -> None:
    """Print colored text - delegates to display module."""
    display.print_colored(text, color)


def print_event(text: str) -> None:
    """Print event message - delegates to display module."""
    display.print_event(text)


def format_inventory(inventory: List[str]) -> str:
    """Format inventory as string - delegates to display module."""
    return display.format_inventory(inventory)


def print_game_over() -> None:
    """Print game over message - delegates to display module."""
    display.print_game_over()
