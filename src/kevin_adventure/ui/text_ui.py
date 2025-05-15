"""
Text-based user interface for the Kevin's Adventure Game.
"""
import textwrap
from typing import Optional


class TextUI:
    """Handles text-based user interface for the game."""

    def __init__(self, width: int = 80):
        """
        Initialize the text UI.
        
        Args:
            width: The maximum width for text wrapping
        """
        self.width = width

    def display_message(self, message: str) -> None:
        """Display a message to the user."""
        print(self.wrap_text(message))

    def display_error(self, message: str) -> None:
        """Display an error message to the user."""
        print(f"ERROR: {self.wrap_text(message)}")

    def get_input(self, prompt: str) -> str:
        """
        Get input from the user.
        
        Args:
            prompt: The prompt to display to the user
            
        Returns:
            The user's input
        """
        return input(prompt)

    def display_welcome(self) -> None:
        """Display a welcome message."""
        welcome_text = """
Welcome to Kevin's Adventure Game!

Explore a world of mystery and danger as you navigate through
forests, caves, villages, and mountains. Collect items, interact
with characters, and uncover the secrets of this magical realm.

Type 'help' at any time to see available commands.

Your journey begins now. Good luck, adventurer!
        """
        print(welcome_text.strip())

    def display_help(self) -> None:
        """Display help information."""
        help_text = """
Available commands:
- move [location]: Move to a new location
- go [location]: Same as 'move'
- look: Examine your surroundings
- inventory: Check your inventory
- pickup [item]: Pick up an item
- take [item]: Same as 'pickup'
- drop [item]: Drop an item from your inventory
- use [item]: Use an item
- examine [item]: Get a description of an item
- status: Check your current status
- interact: Interact with your current location
- help: Show this help message
- quit: Save and exit the game
        """
        print(help_text.strip())

    def display_game_over(self) -> None:
        """Display a game over message."""
        game_over_text = """
Game Over

Your adventure has come to an end. Thank you for playing!
        """
        self.display_separator("=")
        print(game_over_text)
        self.display_separator("=")

    def display_separator(self, char: str = "-", length: Optional[int] = None) -> None:
        """
        Display a separator line.
        
        Args:
            char: The character to use for the separator
            length: The length of the separator (defaults to self.width)
        """
        length = length or self.width
        print(char * length)

    def wrap_text(self, text: str) -> str:
        """
        Wrap text to the specified width.
        
        Args:
            text: The text to wrap
            
        Returns:
            The wrapped text
        """
        return textwrap.fill(text, width=self.width)

