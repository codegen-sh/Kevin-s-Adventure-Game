"""
Main Game class - handles the core game loop and coordination.
"""
from typing import Optional
from game.game_state import GameState
from game.actions import perform_action
from game.world import get_current_location
from utils.text_formatting import print_help, print_welcome_message


class Game:
    """
    Main game class that handles the game loop and user interaction.
    """
    
    def __init__(self):
        """Initialize the game."""
        self.game_state = GameState()
        self.running = False
    
    def start(self) -> None:
        """Start the game and handle initial setup."""
        print_welcome_message()
        
        # Handle game loading or creation
        if not self._handle_game_initialization():
            return
        
        # Start main game loop
        self._run_game_loop()
    
    def _handle_game_initialization(self) -> bool:
        """
        Handle game initialization (new game or load saved game).
        
        Returns:
            True if initialization was successful, False otherwise
        """
        try:
            load_option = input("Do you want to load a saved game? (y/n): ").lower().strip()
            
            if load_option == 'y':
                if self.game_state.load_saved_game():
                    return True
                else:
                    print("Starting a new game instead.")
                    self.game_state.initialize_new_game("Kevin")
                    return True
            else:
                self.game_state.initialize_new_game("Kevin")
                return True
                
        except (KeyboardInterrupt, EOFError):
            print("\nGame cancelled by user.")
            return False
        except Exception as e:
            print(f"Error during initialization: {e}")
            return False
    
    def _run_game_loop(self) -> None:
        """Run the main game loop."""
        self.running = True
        
        try:
            while self.running and self.game_state.game_running:
                # Check if game is over
                if self.game_state.is_game_over():
                    print("Game Over!")
                    break
                
                # Validate game state
                if not self.game_state.validate_state():
                    print("Game state is invalid. Attempting to fix...")
                    if not self._attempt_state_recovery():
                        print("Could not recover game state. Ending game.")
                        break
                
                # Display current status
                self._display_current_status()
                
                # Get and process user input
                if not self._process_user_input():
                    break
                
                # Increment turn counter
                self.game_state.increment_turn()
                
        except KeyboardInterrupt:
            print("\n\nGame interrupted by user.")
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            print("Game will be saved and terminated.")
        finally:
            self._cleanup_and_exit()
    
    def _display_current_status(self) -> None:
        """Display the current game status to the player."""
        try:
            current_location = get_current_location(self.game_state.world)
            print(f"\nYou are in the {current_location}.")
            print(self.game_state.get_player_status())
        except Exception as e:
            print(f"Error displaying status: {e}")
    
    def _process_user_input(self) -> bool:
        """
        Process user input and execute actions.
        
        Returns:
            True to continue game loop, False to exit
        """
        try:
            action = input("What would you like to do? ").strip()
            
            if not action:
                print("Please enter a command. Type 'help' for available commands.")
                return True
            
            action = action.lower()
            
            # Handle special commands
            if action == "quit":
                return self._handle_quit_command()
            elif action == "help":
                print_help()
                return True
            elif action == "save":
                self.game_state.save_current_game()
                return True
            elif action == "stats":
                self._display_game_stats()
                return True
            else:
                # Process regular game actions
                perform_action(self.game_state.player, self.game_state.world, action)
                return True
                
        except (KeyboardInterrupt, EOFError):
            print("\nExiting game...")
            return False
        except Exception as e:
            print(f"Error processing input: {e}")
            return True
    
    def _handle_quit_command(self) -> bool:
        """
        Handle the quit command.
        
        Returns:
            False to exit game loop
        """
        try:
            save_choice = input("Do you want to save before quitting? (y/n): ").lower().strip()
            if save_choice == 'y':
                self.game_state.save_current_game()
            
            print("Thanks for playing!")
            return False
            
        except (KeyboardInterrupt, EOFError):
            print("\nQuitting without saving...")
            return False
    
    def _display_game_stats(self) -> None:
        """Display current game statistics."""
        stats = self.game_state.get_game_stats()
        if stats:
            print("\n=== Game Statistics ===")
            print(f"Player: {stats['player_name']}")
            print(f"Location: {stats['current_location']}")
            print(f"Health: {stats['health']}")
            print(f"Gold: {stats['gold']}")
            print(f"Items: {stats['inventory_count']}")
            print(f"Turns: {stats['turn_count']}")
            print(f"Events: {stats['events_count']}")
        else:
            print("No game statistics available.")
    
    def _attempt_state_recovery(self) -> bool:
        """
        Attempt to recover from an invalid game state.
        
        Returns:
            True if recovery was successful, False otherwise
        """
        try:
            # Try to re-validate after potential auto-fixes
            return self.game_state.validate_state()
        except Exception as e:
            print(f"State recovery failed: {e}")
            return False
    
    def _cleanup_and_exit(self) -> None:
        """Perform cleanup operations before exiting."""
        try:
            if self.game_state.player and self.game_state.world:
                # Auto-save on exit
                self.game_state.save_current_game()
            
            self.running = False
            print("Game session ended.")
            
        except Exception as e:
            print(f"Error during cleanup: {e}")
    
    def stop(self) -> None:
        """Stop the game loop."""
        self.running = False
        self.game_state.end_game()


def create_game() -> Game:
    """
    Create and return a new Game instance.
    
    Returns:
        New Game instance
    """
    return Game()
