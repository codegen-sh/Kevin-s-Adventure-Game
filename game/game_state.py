"""
Game State Manager - centralized game state management system.
"""
from typing import Dict, Any, Optional
from game.player import Player, create_player
from game.world import initialize_world
from utils.save_load import save_game, load_game, list_save_files


class GameState:
    """
    Centralized game state manager that coordinates between different systems.
    """
    
    def __init__(self):
        """Initialize the game state manager."""
        self.player: Optional[Player] = None
        self.world: Optional[Dict[str, Any]] = None
        self.game_running = False
        self.turn_count = 0
        self.game_events = []
    
    def initialize_new_game(self, player_name: str = "Kevin") -> None:
        """
        Initialize a new game with default settings.
        
        Args:
            player_name: Name for the player character
        """
        self.player = create_player(player_name)
        self.world = initialize_world()
        self.game_running = True
        self.turn_count = 0
        self.game_events = []
        print(f"New game started! Welcome, {player_name}!")
    
    def load_saved_game(self) -> bool:
        """
        Load a saved game from available save files.
        
        Returns:
            True if game was loaded successfully, False otherwise
        """
        save_files = list_save_files()
        if not save_files:
            print("No save files found.")
            return False
        
        print("Available save files:")
        for i, file in enumerate(save_files, 1):
            print(f"{i}. {file}")
        
        try:
            choice = int(input("Enter the number of the save file to load: "))
            if 1 <= choice <= len(save_files):
                player_data, world_data = load_game(save_files[choice - 1])
                
                if player_data is None or world_data is None:
                    print("Failed to load game.")
                    return False
                
                # Convert loaded data to proper objects
                if isinstance(player_data, dict):
                    self.player = Player.from_dict(player_data)
                else:
                    self.player = player_data
                
                self.world = world_data
                self.game_running = True
                print(f"Game loaded successfully! Welcome back, {self.player.name}!")
                return True
            else:
                print("Invalid choice.")
                return False
                
        except (ValueError, IndexError):
            print("Invalid input.")
            return False
    
    def save_current_game(self) -> bool:
        """
        Save the current game state.
        
        Returns:
            True if game was saved successfully, False otherwise
        """
        if not self.player or not self.world:
            print("No game to save.")
            return False
        
        try:
            # Convert player to dict for saving if needed
            player_data = self.player.to_dict() if isinstance(self.player, Player) else self.player
            save_game(player_data, self.world)
            print("Game saved successfully!")
            return True
        except Exception as e:
            print(f"Failed to save game: {e}")
            return False
    
    def get_current_location(self) -> str:
        """Get the player's current location."""
        if not self.player:
            return "Unknown"
        return self.player.location
    
    def get_player_status(self) -> str:
        """Get formatted player status."""
        if not self.player:
            return "No player"
        return self.player.get_status()
    
    def is_game_over(self) -> bool:
        """Check if the game is over."""
        if not self.player:
            return True
        return not self.player.is_alive()
    
    def end_game(self) -> None:
        """End the current game."""
        self.game_running = False
        if self.player and self.world:
            self.save_current_game()
        print("Thanks for playing! Your progress has been saved.")
    
    def increment_turn(self) -> None:
        """Increment the turn counter."""
        self.turn_count += 1
    
    def add_game_event(self, event: str) -> None:
        """
        Add an event to the game history.
        
        Args:
            event: Description of the event
        """
        self.game_events.append({
            "turn": self.turn_count,
            "event": event,
            "location": self.get_current_location()
        })
    
    def get_game_stats(self) -> Dict[str, Any]:
        """
        Get current game statistics.
        
        Returns:
            Dictionary containing game statistics
        """
        if not self.player:
            return {}
        
        return {
            "player_name": self.player.name,
            "current_location": self.player.location,
            "health": self.player.health,
            "gold": self.player.gold,
            "inventory_count": len(self.player.inventory),
            "turn_count": self.turn_count,
            "events_count": len(self.game_events)
        }
    
    def validate_state(self) -> bool:
        """
        Validate that the game state is consistent.
        
        Returns:
            True if state is valid, False otherwise
        """
        if not self.player or not self.world:
            return False
        
        # Check if player's location exists in world
        if self.player.location not in self.world.get("locations", {}):
            print(f"Warning: Player location '{self.player.location}' not found in world!")
            return False
        
        # Check if world's current location matches player location
        if self.world.get("current_location") != self.player.location:
            print("Warning: World and player locations are out of sync!")
            # Auto-fix by syncing world to player location
            self.world["current_location"] = self.player.location
        
        return True
    
    def reset_game(self) -> None:
        """Reset the game state to initial values."""
        self.player = None
        self.world = None
        self.game_running = False
        self.turn_count = 0
        self.game_events = []
        print("Game state reset.")


# Global game state instance
game_state = GameState()
