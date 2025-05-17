"""
Main module for Kevin's Adventure Game.
Contains the entry point for the game.
"""
from src.game.game import Game
from src.utils.text_formatting import print_welcome_message


def main():
    """Main entry point for the game."""
    print_welcome_message()
    
    # Create and initialize the game
    game = Game()
    game.initialize()
    
    # Add load game option
    load_option = input("Do you want to load a saved game? (y/n): ").lower()
    if load_option == 'y':
        save_files = game.save_manager.list_save_files()
        if save_files:
            print("Available save files:")
            for i, file in enumerate(save_files, 1):
                print(f"{i}. {file}")
            try:
                choice = int(input("Enter the number of the save file to load: "))
                if 1 <= choice <= len(save_files):
                    if not game.load_game(save_files[choice - 1]):
                        print("Failed to load game. Starting a new game.")
                        game.start_new_game("Kevin")
                else:
                    print("Invalid choice. Starting a new game.")
                    game.start_new_game("Kevin")
            except ValueError:
                print("Invalid input. Starting a new game.")
                game.start_new_game("Kevin")
        else:
            print("No save files found. Starting a new game.")
            game.start_new_game("Kevin")
    else:
        game.start_new_game("Kevin")

    # Main game loop
    while game.running:
        current_location = game.world.get_current_location()
        print(f"\nYou are in the {current_location.name}.")
        print(game.player.get_status())

        command = input("What would you like to do? ")
        game.process_command(command)


if __name__ == "__main__":
    main()

