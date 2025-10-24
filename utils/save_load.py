"""
Enhanced save/load utilities for Kevin's Adventure Game.
Provides backward compatibility while integrating with the new advanced save system.
"""

import json
import os
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple

from game.save_manager import SaveManager
from utils.serialization import SaveDataSerializer, SerializationError

# Legacy support
SAVE_DIRECTORY = "saves"

# Initialize advanced save manager
save_manager = SaveManager(SAVE_DIRECTORY)
logger = logging.getLogger(__name__)

def ensure_save_directory():
    """Ensure that the save directory exists. Use save_game() to actually save the game."""
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)

def generate_save_filename(player_name):
    """Generate a unique filename for the save file. Use save_game() to actually save the game."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{player_name}_{timestamp}.json"

def save_game(player, world, use_advanced_system=True):
    """
    Save the current game state to a file.
    
    Args:
        player: Player data dictionary
        world: World data dictionary
        use_advanced_system: Whether to use the new advanced save system
    """
    try:
        if use_advanced_system:
            # Use the new save manager for quick save
            save_manager.set_current_game_state(player, world)
            success = save_manager.quick_save(player, world)
            if success:
                print("Game saved successfully using advanced save system")
                return True
            else:
                print("Advanced save failed, falling back to legacy system")
                # Fall through to legacy system
        
        # Legacy save system (fallback)
        ensure_save_directory()

        save_data = {
            "player": player,
            "world": world,
            "version": "1.0.0",
            "timestamp": datetime.now().isoformat()
        }

        filename = generate_save_filename(player["name"])
        filepath = os.path.join(SAVE_DIRECTORY, filename)

        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        print(f"Game saved successfully as {filename}")
        return True
        
    except Exception as e:
        logger.error(f"Error saving game: {e}")
        print(f"Error saving game: {e}")
        return False

def load_game(filename):
    """
    Load a game state from a file.
    
    Args:
        filename: Name of the save file to load
        
    Returns:
        Tuple of (player, world) or (None, None) if failed
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    try:
        # Try to determine if this is a new format save file
        if filename.endswith('.sav'):
            # New format - use save manager
            try:
                slot_id = int(filename.split('_')[1].split('.')[0])
                result = save_manager.load_save_slot(slot_id)
                if result:
                    player, world, metadata = result
                    print(f"Game loaded successfully from slot {slot_id}")
                    return player, world
                else:
                    print(f"Failed to load from slot {slot_id}")
                    return None, None
            except (ValueError, IndexError):
                print(f"Invalid save file format: {filename}")
                return None, None
        
        # Legacy format - load directly
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        
        print(f"Game loaded successfully from {filename}")
        
        # Handle both old and new save data formats
        if "player" in save_data and "world" in save_data:
            return save_data["player"], save_data["world"]
        else:
            # Very old format - assume the entire data is the save
            return save_data.get("player"), save_data.get("world")
            
    except IOError as e:
        logger.error(f"Error loading game: {e}")
        print(f"Error loading game: {e}")
        return None, None
    except json.JSONDecodeError:
        logger.error(f"The save file {filename} is corrupted")
        print(f"Error: The save file {filename} is corrupted.")
        return None, None
    except Exception as e:
        logger.error(f"Unexpected error loading game: {e}")
        print(f"Unexpected error loading game: {e}")
        return None, None

def list_save_files():
    """List all available save files. Use load_most_recent_save() to load the most recent save."""
    ensure_save_directory()
    
    # Get both legacy and new format save files
    legacy_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]
    new_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.sav')]
    
    return legacy_files + new_files

def delete_save_file(filename):
    """Delete a save file. Use list_save_files() to list all available save files."""
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    try:
        # If it's a new format file, use save manager
        if filename.endswith('.sav'):
            try:
                slot_id = int(filename.split('_')[1].split('.')[0])
                success = save_manager.delete_save_slot(slot_id)
                if success:
                    print(f"Save slot {slot_id} deleted successfully.")
                else:
                    print(f"Failed to delete save slot {slot_id}.")
                return success
            except (ValueError, IndexError):
                pass  # Fall through to legacy deletion
        
        # Legacy deletion
        os.remove(filepath)
        print(f"Save file {filename} deleted successfully.")
        return True
        
    except OSError as e:
        logger.error(f"Error deleting save file: {e}")
        print(f"Error deleting save file: {e}")
        return False

def load_most_recent_save():
    """Load the most recent save file. Use list_save_files() to list all available save files."""
    save_files = list_save_files()
    if not save_files:
        print("No save files found.")
        return None, None

    most_recent = max(save_files, key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)))
    return load_game(most_recent)

# New advanced functions

def list_save_slots():
    """List all save slots with detailed metadata."""
    try:
        slots = save_manager.list_save_slots()
        return slots
    except Exception as e:
        logger.error(f"Error listing save slots: {e}")
        return []

def save_to_slot(slot_id: int, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
    """
    Save game to a specific slot.
    
    Args:
        slot_id: Slot number (1-10)
        player: Player data
        world: World data
        
    Returns:
        bool: True if successful
    """
    try:
        save_manager.set_current_game_state(player, world)
        success = save_manager.create_save_slot(slot_id, player, world)
        if success:
            print(f"Game saved to slot {slot_id}")
        else:
            print(f"Failed to save to slot {slot_id}")
        return success
    except Exception as e:
        logger.error(f"Error saving to slot {slot_id}: {e}")
        print(f"Error saving to slot {slot_id}: {e}")
        return False

def load_from_slot(slot_id: int) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """
    Load game from a specific slot.
    
    Args:
        slot_id: Slot number to load
        
    Returns:
        Tuple of (player, world) or (None, None) if failed
    """
    try:
        result = save_manager.load_save_slot(slot_id)
        if result:
            player, world, metadata = result
            print(f"Game loaded from slot {slot_id}")
            return player, world
        else:
            print(f"Failed to load from slot {slot_id}")
            return None, None
    except Exception as e:
        logger.error(f"Error loading from slot {slot_id}: {e}")
        print(f"Error loading from slot {slot_id}: {e}")
        return None, None

def start_auto_save(player: Dict[str, Any], world: Dict[str, Any], interval_minutes: int = 5):
    """
    Start auto-save functionality.
    
    Args:
        player: Current player data
        world: Current world data
        interval_minutes: Auto-save interval in minutes
    """
    try:
        save_manager.set_current_game_state(player, world)
        save_manager.start_auto_save(interval_minutes)
        print(f"Auto-save started with {interval_minutes} minute interval")
    except Exception as e:
        logger.error(f"Error starting auto-save: {e}")
        print(f"Error starting auto-save: {e}")

def stop_auto_save():
    """Stop auto-save functionality."""
    try:
        save_manager.stop_auto_save()
        print("Auto-save stopped")
    except Exception as e:
        logger.error(f"Error stopping auto-save: {e}")
        print(f"Error stopping auto-save: {e}")

def get_save_statistics():
    """Get statistics about save files."""
    try:
        return save_manager.get_save_statistics()
    except Exception as e:
        logger.error(f"Error getting save statistics: {e}")
        return {"error": str(e)}

def backup_save_slot(slot_id: int) -> bool:
    """
    Create a backup of a save slot.
    
    Args:
        slot_id: Slot to backup
        
    Returns:
        bool: True if successful
    """
    try:
        slots = save_manager.list_save_slots()
        slot_info = next((s for s in slots if s["slot_id"] == slot_id and s["exists"]), None)
        
        if not slot_info:
            print(f"Save slot {slot_id} does not exist")
            return False
        
        backup_filename = save_manager.backup_manager.create_backup(slot_info["filename"], "manual")
        if backup_filename:
            print(f"Backup created: {backup_filename}")
            return True
        else:
            print(f"Failed to create backup for slot {slot_id}")
            return False
            
    except Exception as e:
        logger.error(f"Error backing up slot {slot_id}: {e}")
        print(f"Error backing up slot {slot_id}: {e}")
        return False

def restore_save_slot(slot_id: int, backup_filename: str) -> bool:
    """
    Restore a save slot from backup.
    
    Args:
        slot_id: Slot to restore to
        backup_filename: Backup file to restore from
        
    Returns:
        bool: True if successful
    """
    try:
        success = save_manager.backup_manager.restore_backup(backup_filename, overwrite_existing=True)
        if success:
            # Reload save slots to reflect the restored data
            save_manager._load_save_slots()
            print(f"Save slot {slot_id} restored from backup")
            return True
        else:
            print(f"Failed to restore slot {slot_id} from backup")
            return False
            
    except Exception as e:
        logger.error(f"Error restoring slot {slot_id}: {e}")
        print(f"Error restoring slot {slot_id}: {e}")
        return False

# Initialize logging
logging.basicConfig(level=logging.INFO)
