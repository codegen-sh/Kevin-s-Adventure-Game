#!/usr/bin/env python3
"""
Main entry point for Kevin's Adventure Game.
"""
from kevin_adventure.core.game import Game


def main():
    """Run the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

