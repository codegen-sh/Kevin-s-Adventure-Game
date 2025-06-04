import textwrap

from config import DISPLAY_SETTINGS, MESSAGES, HELP_TEXT


def wrap_text(text, width=None):
    """Wrap text to a specified width."""
    if width is None:
        width = DISPLAY_SETTINGS["text_width"]
    return textwrap.fill(text, width=width)


def print_welcome_message():
    """Print a formatted welcome message for the game."""
    print(MESSAGES["welcome"].strip())


def print_help():
    """Print a formatted help message with available commands."""
    print(HELP_TEXT.strip())

def format_inventory(inventory):
    """Format the player's inventory for display."""
    if not inventory:
        return "empty"
    return ", ".join(inventory)

def print_separator(char="-", length=80):
    """Print a separator line."""
    print(char * length)

def print_event(event_text):
    """Print a formatted event message."""
    print_separator()
    print(wrap_text(event_text))
    print_separator()

def print_game_over():
    """Print a formatted game over message."""
    game_over_text = """
    Game Over

    Your adventure has come to an end. Thank you for playing!
    """
    print_separator("=")
    print(game_over_text)
    print_separator("=")
