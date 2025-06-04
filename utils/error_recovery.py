"""
Error recovery mechanisms and graceful degradation for Kevin's Adventure Game.
Provides automatic error recovery and fallback mechanisms for common failures.
"""

import json
import shutil
from pathlib import Path
from typing import Dict, Any, Optional, Tuple, List, Callable
from datetime import datetime

from exceptions import (
    GameError, SaveError, LoadError, LocationError, PlayerError, 
    ItemError, WorldStateError, ValidationError
)
from utils.logging_config import get_logger, log_error_with_context, log_game_event
from utils.validation import validate_player_state, validate_world_state

# Initialize logger
logger = get_logger('error_recovery')

# Recovery configuration
MAX_RECOVERY_ATTEMPTS = 3
FALLBACK_SAVE_DIRECTORY = "saves/emergency"
DEFAULT_PLAYER_STATE = {
    "name": "Player",
    "health": 100,
    "inventory": [],
    "location": "Village",
    "gold": 100
}

DEFAULT_WORLD_STATE = {
    "current_location": "Village",
    "locations": {
        "Village": {
            "description": "A small, peaceful village with thatched-roof houses and friendly inhabitants.",
            "connections": ["Forest", "Mountain"],
            "items": ["map", "bread"]
        },
        "Forest": {
            "description": "A dense, mysterious forest with towering trees and the sound of rustling leaves.",
            "connections": ["Village", "Cave"],
            "items": ["stick", "berries"]
        },
        "Cave": {
            "description": "A dark, damp cave with echoing sounds and glittering minerals on the walls.",
            "connections": ["Forest"],
            "items": ["torch", "gemstone"]
        },
        "Mountain": {
            "description": "A tall, snow-capped mountain with treacherous paths and breathtaking views.",
            "connections": ["Village"],
            "items": ["rope", "pickaxe"]
        }
    }
}


class RecoveryManager:
    """Manages error recovery and fallback mechanisms."""
    
    def __init__(self):
        self.recovery_attempts = {}
        self.fallback_states = {}
        self.recovery_strategies = {}
        self._setup_recovery_strategies()
    
    def _setup_recovery_strategies(self):
        """Setup recovery strategies for different error types."""
        self.recovery_strategies = {
            SaveError: self._recover_save_error,
            LoadError: self._recover_load_error,
            LocationError: self._recover_location_error,
            PlayerError: self._recover_player_error,
            ItemError: self._recover_item_error,
            WorldStateError: self._recover_world_state_error,
            ValidationError: self._recover_validation_error
        }
    
    def attempt_recovery(self, error: Exception, context: Dict[str, Any] = None) -> Tuple[bool, Any]:
        """
        Attempt to recover from an error.
        
        Args:
            error (Exception): The error to recover from
            context (dict): Additional context for recovery
        
        Returns:
            tuple: (success, recovered_data)
        """
        error_type = type(error)
        error_key = f"{error_type.__name__}_{id(error)}"
        
        # Check recovery attempt count
        if error_key not in self.recovery_attempts:
            self.recovery_attempts[error_key] = 0
        
        if self.recovery_attempts[error_key] >= MAX_RECOVERY_ATTEMPTS:
            logger.error(f"Max recovery attempts reached for {error_type.__name__}")
            return False, None
        
        self.recovery_attempts[error_key] += 1
        
        # Find appropriate recovery strategy
        recovery_func = None
        for error_class, func in self.recovery_strategies.items():
            if isinstance(error, error_class):
                recovery_func = func
                break
        
        if not recovery_func:
            logger.warning(f"No recovery strategy found for {error_type.__name__}")
            return False, None
        
        try:
            logger.info(f"Attempting recovery for {error_type.__name__} (attempt {self.recovery_attempts[error_key]})")
            success, data = recovery_func(error, context or {})
            
            if success:
                logger.info(f"Recovery successful for {error_type.__name__}")
                log_game_event("error_recovery", f"Successfully recovered from {error_type.__name__}")
            else:
                logger.warning(f"Recovery failed for {error_type.__name__}")
            
            return success, data
            
        except Exception as recovery_error:
            logger.error(f"Recovery attempt failed with new error: {recovery_error}")
            log_error_with_context(recovery_error, action="error_recovery")
            return False, None
    
    def _recover_save_error(self, error: SaveError, context: Dict[str, Any]) -> Tuple[bool, Any]:
        """Recover from save errors."""
        logger.info("Attempting save error recovery")
        
        # Try alternative save location
        try:
            Path(FALLBACK_SAVE_DIRECTORY).mkdir(parents=True, exist_ok=True)
            
            player = context.get('player')
            world = context.get('world')
            
            if player and world:
                # Create emergency save
                emergency_filename = f"emergency_save_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                emergency_path = Path(FALLBACK_SAVE_DIRECTORY) / emergency_filename
                
                save_data = {
                    "version": "1.0",
                    "timestamp": datetime.now().isoformat(),
                    "player": player,
                    "world": world,
                    "metadata": {
                        "recovery_save": True,
                        "original_error": str(error)
                    }
                }
                
                with open(emergency_path, 'w', encoding='utf-8') as f:
                    json.dump(save_data, f, indent=2, ensure_ascii=False)
                
                logger.info(f"Emergency save created: {emergency_filename}")
                print(f"⚠️  Game saved to emergency location: {emergency_filename}")
                return True, emergency_filename
            
        except Exception as e:
            logger.error(f"Emergency save failed: {e}")
        
        return False, None
    
    def _recover_load_error(self, error: LoadError, context: Dict[str, Any]) -> Tuple[bool, Any]:
        """Recover from load errors."""
        logger.info("Attempting load error recovery")
        
        filename = getattr(error, 'filename', None)
        if not filename:
            return False, None
        
        # Try to find backup files
        try:
            save_dir = Path("saves")
            backup_dir = Path("saves/backups")
            
            # Look for backup files
            if backup_dir.exists():
                base_name = Path(filename).stem.split('_')[0]
                backup_files = list(backup_dir.glob(f"{base_name}_*_backup_*.json"))
                
                if backup_files:
                    # Try the most recent backup
                    backup_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
                    latest_backup = backup_files[0]
                    
                    logger.info(f"Attempting to load from backup: {latest_backup}")
                    
                    with open(latest_backup, 'r', encoding='utf-8') as f:
                        save_data = json.load(f)
                    
                    # Validate the backup data
                    player = validate_player_state(save_data['player'])
                    world = validate_world_state(save_data['world'])
                    
                    logger.info(f"Successfully loaded from backup: {latest_backup}")
                    print(f"⚠️  Loaded from backup file: {latest_backup.name}")
                    return True, (player, world)
            
            # Try to repair the original file
            original_path = save_dir / filename
            if original_path.exists():
                repaired_data = self._attempt_file_repair(original_path)
                if repaired_data:
                    player = validate_player_state(repaired_data['player'])
                    world = validate_world_state(repaired_data['world'])
                    
                    logger.info(f"Successfully repaired and loaded: {filename}")
                    print(f"⚠️  Repaired and loaded corrupted save file")
                    return True, (player, world)
        
        except Exception as e:
            logger.error(f"Load recovery failed: {e}")
        
        # Last resort: create new game with default state
        logger.info("Creating new game with default state")
        print("⚠️  Creating new game with default settings")
        return True, (DEFAULT_PLAYER_STATE.copy(), DEFAULT_WORLD_STATE.copy())
    
    def _recover_location_error(self, error: LocationError, context: Dict[str, Any]) -> Tuple[bool, Any]:
        """Recover from location errors."""
        logger.info("Attempting location error recovery")
        
        player = context.get('player')
        world = context.get('world')
        
        if not player or not world:
            return False, None
        
        # Reset player to a safe location
        safe_location = "Village"
        if safe_location in world.get('locations', {}):
            player['location'] = safe_location
            world['current_location'] = safe_location
            
            logger.info(f"Reset player to safe location: {safe_location}")
            print(f"⚠️  Moved to safe location: {safe_location}")
            return True, (player, world)
        
        # If Village doesn't exist, use the first available location
        locations = world.get('locations', {})
        if locations:
            first_location = list(locations.keys())[0]
            player['location'] = first_location
            world['current_location'] = first_location
            
            logger.info(f"Reset player to first available location: {first_location}")
            print(f"⚠️  Moved to available location: {first_location}")
            return True, (player, world)
        
        return False, None
    
    def _recover_player_error(self, error: PlayerError, context: Dict[str, Any]) -> Tuple[bool, Any]:
        """Recover from player errors."""
        logger.info("Attempting player error recovery")
        
        player = context.get('player')
        if not player:
            # Create new player with default state
            logger.info("Creating new player with default state")
            print("⚠️  Creating new player with default settings")
            return True, DEFAULT_PLAYER_STATE.copy()
        
        # Try to fix player state
        try:
            # Ensure required fields exist
            if 'name' not in player:
                player['name'] = 'Player'
            if 'health' not in player or not isinstance(player['health'], int):
                player['health'] = 100
            if 'inventory' not in player or not isinstance(player['inventory'], list):
                player['inventory'] = []
            if 'location' not in player:
                player['location'] = 'Village'
            if 'gold' not in player or not isinstance(player['gold'], int):
                player['gold'] = 100
            
            # Validate ranges
            player['health'] = max(0, min(100, player['health']))
            player['gold'] = max(0, player['gold'])
            
            # Clean inventory
            player['inventory'] = [item for item in player['inventory'] if isinstance(item, str)]
            
            logger.info("Player state repaired")
            print("⚠️  Player state has been repaired")
            return True, player
            
        except Exception as e:
            logger.error(f"Player recovery failed: {e}")
            return False, None
    
    def _recover_item_error(self, error: ItemError, context: Dict[str, Any]) -> Tuple[bool, Any]:
        """Recover from item errors."""
        logger.info("Attempting item error recovery")
        
        # For item errors, we typically just skip the problematic item
        item_name = getattr(error, 'item_name', 'unknown')
        logger.info(f"Skipping problematic item: {item_name}")
        print(f"⚠️  Skipping invalid item: {item_name}")
        
        return True, None
    
    def _recover_world_state_error(self, error: WorldStateError, context: Dict[str, Any]) -> Tuple[bool, Any]:
        """Recover from world state errors."""
        logger.info("Attempting world state error recovery")
        
        world = context.get('world')
        if not world:
            # Create new world with default state
            logger.info("Creating new world with default state")
            print("⚠️  Creating new world with default settings")
            return True, DEFAULT_WORLD_STATE.copy()
        
        # Try to fix world state
        try:
            # Ensure required fields exist
            if 'current_location' not in world:
                world['current_location'] = 'Village'
            if 'locations' not in world or not isinstance(world['locations'], dict):
                world['locations'] = DEFAULT_WORLD_STATE['locations'].copy()
            
            # Ensure current location exists in locations
            if world['current_location'] not in world['locations']:
                if 'Village' in world['locations']:
                    world['current_location'] = 'Village'
                elif world['locations']:
                    world['current_location'] = list(world['locations'].keys())[0]
                else:
                    world = DEFAULT_WORLD_STATE.copy()
            
            logger.info("World state repaired")
            print("⚠️  World state has been repaired")
            return True, world
            
        except Exception as e:
            logger.error(f"World state recovery failed: {e}")
            return False, None
    
    def _recover_validation_error(self, error: ValidationError, context: Dict[str, Any]) -> Tuple[bool, Any]:
        """Recover from validation errors."""
        logger.info("Attempting validation error recovery")
        
        # For validation errors, we typically use default values
        input_value = getattr(error, 'input_value', None)
        expected_type = getattr(error, 'expected_type', None)
        
        if expected_type == 'string' and input_value is not None:
            # Try to convert to string
            try:
                recovered_value = str(input_value)
                logger.info(f"Converted invalid input to string: {recovered_value}")
                return True, recovered_value
            except Exception:
                pass
        
        elif expected_type == 'number' and input_value is not None:
            # Try to convert to number
            try:
                if isinstance(input_value, str):
                    recovered_value = int(input_value) if input_value.isdigit() else float(input_value)
                else:
                    recovered_value = float(input_value)
                logger.info(f"Converted invalid input to number: {recovered_value}")
                return True, recovered_value
            except Exception:
                pass
        
        logger.info("Using default value for validation error")
        return True, None
    
    def _attempt_file_repair(self, filepath: Path) -> Optional[Dict[str, Any]]:
        """
        Attempt to repair a corrupted JSON file.
        
        Args:
            filepath (Path): Path to the file to repair
        
        Returns:
            Optional[Dict]: Repaired data or None if repair failed
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Try basic JSON repairs
            content = content.strip()
            
            # Fix common JSON issues
            if not content.endswith('}') and content.count('{') > content.count('}'):
                content += '}'
            
            if not content.endswith(']') and content.count('[') > content.count(']'):
                content += ']'
            
            # Remove trailing commas
            content = content.replace(',}', '}').replace(',]', ']')
            
            # Try to parse the repaired content
            repaired_data = json.loads(content)
            
            # Basic validation
            if 'player' in repaired_data and 'world' in repaired_data:
                logger.info(f"Successfully repaired file: {filepath}")
                return repaired_data
            
        except Exception as e:
            logger.warning(f"File repair failed for {filepath}: {e}")
        
        return None
    
    def create_checkpoint(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        """
        Create a checkpoint save for recovery purposes.
        
        Args:
            player (dict): Player state
            world (dict): World state
        
        Returns:
            bool: True if checkpoint was created successfully
        """
        try:
            checkpoint_dir = Path("saves/checkpoints")
            checkpoint_dir.mkdir(parents=True, exist_ok=True)
            
            checkpoint_filename = f"checkpoint_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            checkpoint_path = checkpoint_dir / checkpoint_filename
            
            checkpoint_data = {
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "player": player,
                "world": world,
                "metadata": {
                    "checkpoint": True
                }
            }
            
            with open(checkpoint_path, 'w', encoding='utf-8') as f:
                json.dump(checkpoint_data, f, indent=2, ensure_ascii=False)
            
            # Keep only the last 5 checkpoints
            checkpoint_files = list(checkpoint_dir.glob("checkpoint_*.json"))
            checkpoint_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
            
            for old_checkpoint in checkpoint_files[5:]:
                old_checkpoint.unlink()
            
            logger.debug(f"Checkpoint created: {checkpoint_filename}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to create checkpoint: {e}")
            return False
    
    def get_recovery_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about recovery attempts.
        
        Returns:
            dict: Recovery statistics
        """
        stats = {
            'total_recovery_attempts': sum(self.recovery_attempts.values()),
            'recovery_attempts_by_error': self.recovery_attempts.copy(),
            'available_strategies': list(self.recovery_strategies.keys()),
            'max_attempts_per_error': MAX_RECOVERY_ATTEMPTS
        }
        
        return stats


# Global recovery manager instance
recovery_manager = RecoveryManager()


def attempt_recovery(error: Exception, context: Dict[str, Any] = None) -> Tuple[bool, Any]:
    """
    Convenience function to attempt error recovery.
    
    Args:
        error (Exception): Error to recover from
        context (dict): Additional context
    
    Returns:
        tuple: (success, recovered_data)
    """
    return recovery_manager.attempt_recovery(error, context)


def create_checkpoint(player: Dict[str, Any], world: Dict[str, Any]) -> bool:
    """
    Convenience function to create a checkpoint.
    
    Args:
        player (dict): Player state
        world (dict): World state
    
    Returns:
        bool: True if successful
    """
    return recovery_manager.create_checkpoint(player, world)


def get_recovery_stats() -> Dict[str, Any]:
    """
    Get recovery statistics.
    
    Returns:
        dict: Recovery statistics
    """
    return recovery_manager.get_recovery_statistics()


def handle_error_with_recovery(error: Exception, player: Dict[str, Any] = None, 
                              world: Dict[str, Any] = None, action: str = None) -> Tuple[bool, Any]:
    """
    Handle an error with automatic recovery attempt.
    
    Args:
        error (Exception): Error to handle
        player (dict): Player state
        world (dict): World state
        action (str): Action being performed
    
    Returns:
        tuple: (recovery_successful, recovered_data)
    """
    context = {}
    if player:
        context['player'] = player
    if world:
        context['world'] = world
    if action:
        context['action'] = action
    
    # Log the error
    log_error_with_context(error, player=player, world=world, action=action)
    
    # Attempt recovery
    success, data = attempt_recovery(error, context)
    
    if success:
        log_game_event("error_recovery", f"Recovered from {type(error).__name__}", 
                      player=player, world=world)
    else:
        log_game_event("error_recovery_failed", f"Failed to recover from {type(error).__name__}", 
                      player=player, world=world)
    
    return success, data

