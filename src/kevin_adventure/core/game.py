"""
Game module for Kevin's Adventure Game.
"""
from typing import Dict, List, Optional, Tuple

from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World
from kevin_adventure.utils.save_load import list_save_files, load_game, save_game
from kevin_adventure.utils.text_formatting import print_help, print_welcome_message


class Game:
    """
    Game class representing the game state and main loop.
    """

    def __init__(self):
        """
        Initialize a new game.
        """
        self.player: Optional[Player] = None
        self.world: Optional[World] = None

    def start(self) -> None:
        """
        Start the game.
        """
        print_welcome_message()

        # Add load game option
        load_option = input("Do you want to load a saved game? (y/n): ").lower()
        if load_option == 'y':
            save_files = list_save_files()
            if save_files:
                print("Available save files:")
                for i, file in enumerate(save_files, 1):
                    print(f"{i}. {file}")
                choice = int(input("Enter the number of the save file to load: "))
                self.player, self.world = load_game(save_files[choice - 1])
                if self.player is None or self.world is None:
                    print("Failed to load game. Starting a new game.")
                    self.player = Player("Kevin")
                    self.world = World()
                    self.world.initialize()
            else:
                print("No save files found. Starting a new game.")
                self.player = Player("Kevin")
                self.world = World()
                self.world.initialize()
        else:
            self.player = Player("Kevin")
            self.world = World()
            self.world.initialize()

        self.main_loop()

    def main_loop(self) -> None:
        """
        Main game loop.
        """
        while True:
            current_location = self.world.get_current_location()
            print(f"\nYou are in the {current_location}.")
            print(self.player.get_status())

            action = input("What would you like to do? ").lower()

            if action == "quit":
                save_game(self.player, self.world)
                print("Thanks for playing! Your progress has been saved.")
                break
            elif action == "help":
                print_help()
            else:
                self.perform_action(action)

    def perform_action(self, action: str) -> None:
        """
        Perform an action based on user input.

        Args:
            action: The action to perform
        """
        from kevin_adventure.core.actions import perform_action
        perform_action(self.player, self.world, action)

