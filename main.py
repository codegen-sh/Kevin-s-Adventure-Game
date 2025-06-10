"""
Main module for the game.
"""
import argparse

from game.game import Game


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Kevin's Adventure Game")
    parser.add_argument("--name", type=str, help="Player name (default: Kevin)")
    return parser.parse_args()


def main():
    """Main function."""
    args = parse_arguments()
    player_name = args.name
    
    game = Game(player_name)
    game.start()


if __name__ == "__main__":
    main()

