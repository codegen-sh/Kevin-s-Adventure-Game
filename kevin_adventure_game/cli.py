"""
Command-line interface for Kevin's Adventure Game.
"""

import sys

from kevin_adventure_game.main import main


def cli_main():
    """Entry point for the CLI."""
    sys.exit(main())


if __name__ == "__main__":
    cli_main()
