import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Tuple, Optional, List, Dict, Any

from exceptions import SaveError, LoadError, ValidationError
from utils.logging_config import get_logger, log_error_with_context
from utils.validation import validate_player_state, validate_world_state, validate_save_filename

SAVE_DIRECTORY = "saves"
BACKUP_DIRECTORY = "saves/backups"
MAX_BACKUP_FILES = 10

# Initialize logger
logger = get_logger('save_load')

def ensure_save_directory():
    """Ensure that the save directory exists. Use save_game() to actually save the game."""
    try:
        Path(SAVE_DIRECTORY).mkdir(exist_ok=True)
        Path(BACKUP_DIRECTORY).mkdir(exist_ok=True)
        logger.debug(f"Save directories ensured: {SAVE_DIRECTORY}, {BACKUP_DIRECTORY}")
    except OSError as e:
        logger.error(f"Failed to create save directories: {e}")
        raise SaveError(
            f"Cannot create save directory: {e}",
            context={'save_directory': SAVE_DIRECTORY, 'backup_directory': BACKUP_DIRECTORY}
        )

def generate_save_filename(player_name):
    """Generate a unique filename for the save file. Use save_game() to actually save the game."""
    try:
        # Validate player name for filename safety
        safe_name = validate_save_filename(f"{player_name}.json")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{Path(safe_name).stem}_{timestamp}.json"
        logger.debug(f"Generated save filename: {filename}")
        return filename
    except Exception as e:
        logger.error(f"Failed to generate save filename for player '{player_name}': {e}")
        raise SaveError(
            f"Cannot generate save filename: {e}",
            context={'player_name': player_name}
        )

def create_backup(filepath: Path) -> bool:
    """
    Create a backup of an existing save file.
    
    Args:
        filepath (Path): Path to the file to backup
    
    Returns:
        bool: True if backup was created successfully
    """
    try:
        if not filepath.exists():
            return True  # No file to backup
        
        backup_filename = f"{filepath.stem}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        backup_path = Path(BACKUP_DIRECTORY) / backup_filename
        
        shutil.copy2(filepath, backup_path)
        logger.info(f"Created backup: {backup_path}")
        
        # Clean up old backups
        cleanup_old_backups()
        return True
        
    except Exception as e:
        logger.warning(f"Failed to create backup for {filepath}: {e}")
        return False

def cleanup_old_backups():
    """Remove old backup files, keeping only the most recent ones."""
    try:
        backup_dir = Path(BACKUP_DIRECTORY)
        if not backup_dir.exists():
            return
        
        backup_files = list(backup_dir.glob("*_backup_*.json"))
        backup_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
        
        # Remove excess backup files
        for old_backup in backup_files[MAX_BACKUP_FILES:]:
            old_backup.unlink()
            logger.debug(f"Removed old backup: {old_backup}")
            
    except Exception as e:
        logger.warning(f"Failed to cleanup old backups: {e}")

def validate_save_data(player: Dict[str, Any], world: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Validate save data before saving.
    
    Args:
        player (dict): Player state
        world (dict): World state
    
    Returns:
        tuple: Validated player and world states
    
    Raises:
        ValidationError: If data is invalid
    """
    try:
        validated_player = validate_player_state(player)
        validated_world = validate_world_state(world)
        logger.debug("Save data validation successful")
        return validated_player, validated_world
    except Exception as e:
        logger.error(f"Save data validation failed: {e}")
        raise ValidationError(f"Invalid save data: {e}")

def save_game(player, world):
    """Save the current game state to a file."""
    try:
        logger.info(f"Starting save operation for player: {player.get('name', 'unknown')}")
        
        # Ensure save directory exists
        ensure_save_directory()
        
        # Validate save data
        validated_player, validated_world = validate_save_data(player, world)
        
        # Create save data structure
        save_data = {
            "version": "1.0",
            "timestamp": datetime.now().isoformat(),
            "player": validated_player,
            "world": validated_world,
            "metadata": {
                "game_version": "1.0",
                "save_format_version": "1.0"
            }
        }
        
        # Generate filename
        filename = generate_save_filename(validated_player["name"])
        filepath = Path(SAVE_DIRECTORY) / filename
        
        # Create backup if file exists
        create_backup(filepath)
        
        # Write save file with atomic operation
        temp_filepath = filepath.with_suffix('.tmp')
        try:
            with open(temp_filepath, 'w', encoding='utf-8') as save_file:
                json.dump(save_data, save_file, indent=2, ensure_ascii=False)
            
            # Atomic move
            temp_filepath.replace(filepath)
            
            logger.info(f"Game saved successfully: {filename}")
            print(f"Game saved successfully as {filename}")
            
        except Exception as e:
            # Clean up temp file if it exists
            if temp_filepath.exists():
                temp_filepath.unlink()
            raise e
            
    except (SaveError, ValidationError):
        raise
    except OSError as e:
        error_msg = f"File system error during save: {e}"
        logger.error(error_msg)
        log_error_with_context(e, player=player, world=world, action="save_game")
        raise SaveError(error_msg, context={'error_type': 'filesystem', 'original_error': str(e)})
    except Exception as e:
        error_msg = f"Unexpected error during save: {e}"
        logger.error(error_msg)
        log_error_with_context(e, player=player, world=world, action="save_game")
        raise SaveError(error_msg, context={'error_type': 'unexpected', 'original_error': str(e)})

def verify_save_file(filepath: Path) -> bool:
    """
    Verify that a save file is valid and not corrupted.
    
    Args:
        filepath (Path): Path to the save file
    
    Returns:
        bool: True if file is valid
    """
    try:
        if not filepath.exists():
            return False
        
        if filepath.stat().st_size == 0:
            logger.warning(f"Save file is empty: {filepath}")
            return False
        
        with open(filepath, 'r', encoding='utf-8') as save_file:
            save_data = json.load(save_file)
        
        # Check required fields
        required_fields = ['player', 'world']
        for field in required_fields:
            if field not in save_data:
                logger.warning(f"Save file missing required field '{field}': {filepath}")
                return False
        
        # Basic validation of player and world data
        validate_player_state(save_data['player'])
        validate_world_state(save_data['world'])
        
        logger.debug(f"Save file verification successful: {filepath}")
        return True
        
    except json.JSONDecodeError as e:
        logger.warning(f"Save file has invalid JSON: {filepath} - {e}")
        return False
    except Exception as e:
        logger.warning(f"Save file verification failed: {filepath} - {e}")
        return False

def load_game(filename):
    """Load a game state from a file."""
    try:
        logger.info(f"Starting load operation for file: {filename}")
        
        # Validate filename
        safe_filename = validate_save_filename(filename)
        filepath = Path(SAVE_DIRECTORY) / safe_filename
        
        # Check if file exists
        if not filepath.exists():
            error_msg = f"Save file not found: {filename}"
            logger.error(error_msg)
            raise LoadError(error_msg, filename=filename)
        
        # Verify file integrity
        if not verify_save_file(filepath):
            error_msg = f"Save file is corrupted or invalid: {filename}"
            logger.error(error_msg)
            
            # Try to find a backup
            backup_file = find_backup_file(filename)
            if backup_file:
                logger.info(f"Attempting to load from backup: {backup_file}")
                return load_game(backup_file.name)
            
            raise LoadError(error_msg, filename=filename)
        
        # Load the save file
        with open(filepath, 'r', encoding='utf-8') as save_file:
            save_data = json.load(save_file)
        
        # Extract player and world data
        player = save_data["player"]
        world = save_data["world"]
        
        # Validate loaded data
        validated_player = validate_player_state(player)
        validated_world = validate_world_state(world)
        
        logger.info(f"Game loaded successfully from {filename}")
        print(f"Game loaded successfully from {filename}")
        
        # Log metadata if available
        if "metadata" in save_data:
            metadata = save_data["metadata"]
            logger.debug(f"Loaded save metadata: {metadata}")
        
        return validated_player, validated_world
        
    except (LoadError, ValidationError):
        raise
    except json.JSONDecodeError as e:
        error_msg = f"Save file is corrupted (invalid JSON): {e}"
        logger.error(error_msg)
        log_error_with_context(e, action="load_game", filename=filename)
        raise LoadError(error_msg, filename=filename)
    except OSError as e:
        error_msg = f"File system error during load: {e}"
        logger.error(error_msg)
        log_error_with_context(e, action="load_game", filename=filename)
        raise LoadError(error_msg, filename=filename)
    except Exception as e:
        error_msg = f"Unexpected error during load: {e}"
        logger.error(error_msg)
        log_error_with_context(e, action="load_game", filename=filename)
        raise LoadError(error_msg, filename=filename)

def find_backup_file(original_filename: str) -> Optional[Path]:
    """
    Find a backup file for the given original filename.
    
    Args:
        original_filename (str): Original save filename
    
    Returns:
        Optional[Path]: Path to backup file if found
    """
    try:
        backup_dir = Path(BACKUP_DIRECTORY)
        if not backup_dir.exists():
            return None
        
        # Look for backup files matching the original filename
        base_name = Path(original_filename).stem.split('_')[0]  # Remove timestamp
        backup_pattern = f"{base_name}_*_backup_*.json"
        backup_files = list(backup_dir.glob(backup_pattern))
        
        if backup_files:
            # Return the most recent backup
            backup_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
            logger.info(f"Found backup file: {backup_files[0]}")
            return backup_files[0]
        
        return None
        
    except Exception as e:
        logger.warning(f"Failed to find backup file for {original_filename}: {e}")
        return None

def list_save_files():
    """List all available save files. Use load_most_recent_save() to load the most recent save."""
    try:
        ensure_save_directory()
        save_dir = Path(SAVE_DIRECTORY)
        save_files = [f.name for f in save_dir.glob('*.json') if verify_save_file(f)]
        
        # Sort by modification time (newest first)
        save_files.sort(key=lambda f: Path(SAVE_DIRECTORY, f).stat().st_mtime, reverse=True)
        
        logger.debug(f"Found {len(save_files)} valid save files")
        return save_files
        
    except Exception as e:
        logger.error(f"Failed to list save files: {e}")
        return []

def delete_save_file(filename):
    """Delete a save file. Use list_save_files() to list all available save files."""
    try:
        # Validate filename
        safe_filename = validate_save_filename(filename)
        filepath = Path(SAVE_DIRECTORY) / safe_filename
        
        if not filepath.exists():
            error_msg = f"Save file not found: {filename}"
            logger.warning(error_msg)
            print(error_msg)
            return False
        
        # Create backup before deletion
        create_backup(filepath)
        
        # Delete the file
        filepath.unlink()
        logger.info(f"Save file deleted: {filename}")
        print(f"Save file {filename} deleted successfully.")
        return True
        
    except Exception as e:
        error_msg = f"Error deleting save file {filename}: {e}"
        logger.error(error_msg)
        log_error_with_context(e, action="delete_save_file", filename=filename)
        print(error_msg)
        return False

def load_most_recent_save():
    """Load the most recent save file. Use list_save_files() to list all available save files."""
    try:
        save_files = list_save_files()
        if not save_files:
            logger.info("No save files found")
            print("No save files found.")
            return None, None

        most_recent = save_files[0]  # Already sorted by modification time
        logger.info(f"Loading most recent save: {most_recent}")
        return load_game(most_recent)
        
    except Exception as e:
        error_msg = f"Failed to load most recent save: {e}"
        logger.error(error_msg)
        log_error_with_context(e, action="load_most_recent_save")
        print(error_msg)
        return None, None

def get_save_file_info(filename: str) -> Optional[Dict[str, Any]]:
    """
    Get information about a save file.
    
    Args:
        filename (str): Save file name
    
    Returns:
        Optional[Dict]: Save file information or None if file doesn't exist
    """
    try:
        safe_filename = validate_save_filename(filename)
        filepath = Path(SAVE_DIRECTORY) / safe_filename
        
        if not filepath.exists():
            return None
        
        stat = filepath.stat()
        info = {
            'filename': filename,
            'size': stat.st_size,
            'created': datetime.fromtimestamp(stat.st_ctime),
            'modified': datetime.fromtimestamp(stat.st_mtime),
            'is_valid': verify_save_file(filepath)
        }
        
        # Try to get additional info from the save file
        if info['is_valid']:
            try:
                with open(filepath, 'r', encoding='utf-8') as save_file:
                    save_data = json.load(save_file)
                
                info.update({
                    'player_name': save_data.get('player', {}).get('name', 'Unknown'),
                    'player_level': save_data.get('player', {}).get('health', 'Unknown'),
                    'location': save_data.get('player', {}).get('location', 'Unknown'),
                    'save_version': save_data.get('version', 'Unknown'),
                    'timestamp': save_data.get('timestamp')
                })
                
            except Exception:
                pass  # Additional info is optional
        
        return info
        
    except Exception as e:
        logger.warning(f"Failed to get save file info for {filename}: {e}")
        return None

def export_save_file(filename: str, export_path: str) -> bool:
    """
    Export a save file to a different location.
    
    Args:
        filename (str): Save file to export
        export_path (str): Destination path
    
    Returns:
        bool: True if export was successful
    """
    try:
        safe_filename = validate_save_filename(filename)
        source_path = Path(SAVE_DIRECTORY) / safe_filename
        destination_path = Path(export_path)
        
        if not source_path.exists():
            logger.error(f"Source save file not found: {filename}")
            return False
        
        if not verify_save_file(source_path):
            logger.error(f"Source save file is invalid: {filename}")
            return False
        
        # Ensure destination directory exists
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy the file
        shutil.copy2(source_path, destination_path)
        
        logger.info(f"Save file exported: {filename} -> {export_path}")
        print(f"Save file exported successfully to {export_path}")
        return True
        
    except Exception as e:
        error_msg = f"Failed to export save file {filename}: {e}"
        logger.error(error_msg)
        print(error_msg)
        return False

def import_save_file(import_path: str) -> bool:
    """
    Import a save file from an external location.
    
    Args:
        import_path (str): Path to the save file to import
    
    Returns:
        bool: True if import was successful
    """
    try:
        source_path = Path(import_path)
        
        if not source_path.exists():
            logger.error(f"Import file not found: {import_path}")
            print(f"Import file not found: {import_path}")
            return False
        
        # Verify the file before importing
        if not verify_save_file(source_path):
            logger.error(f"Import file is invalid: {import_path}")
            print(f"Import file is invalid or corrupted: {import_path}")
            return False
        
        # Generate a safe filename for the imported file
        original_name = source_path.stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"{original_name}_imported_{timestamp}.json"
        
        destination_path = Path(SAVE_DIRECTORY) / new_filename
        
        # Ensure save directory exists
        ensure_save_directory()
        
        # Copy the file
        shutil.copy2(source_path, destination_path)
        
        logger.info(f"Save file imported: {import_path} -> {new_filename}")
        print(f"Save file imported successfully as {new_filename}")
        return True
        
    except Exception as e:
        error_msg = f"Failed to import save file {import_path}: {e}"
        logger.error(error_msg)
        print(error_msg)
        return False

def repair_save_file(filename: str) -> bool:
    """
    Attempt to repair a corrupted save file.
    
    Args:
        filename (str): Save file to repair
    
    Returns:
        bool: True if repair was successful
    """
    try:
        safe_filename = validate_save_filename(filename)
        filepath = Path(SAVE_DIRECTORY) / safe_filename
        
        if not filepath.exists():
            logger.error(f"Save file not found for repair: {filename}")
            return False
        
        # Try to find a backup
        backup_file = find_backup_file(filename)
        if backup_file and verify_save_file(backup_file):
            # Restore from backup
            shutil.copy2(backup_file, filepath)
            logger.info(f"Save file repaired from backup: {filename}")
            print(f"Save file {filename} repaired from backup.")
            return True
        
        # Try to repair JSON if possible
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic JSON repair attempts
            if not content.strip().endswith('}'):
                content += '}'
            
            # Try to parse the repaired content
            repaired_data = json.loads(content)
            
            # Validate the repaired data
            if 'player' in repaired_data and 'world' in repaired_data:
                validate_player_state(repaired_data['player'])
                validate_world_state(repaired_data['world'])
                
                # Save the repaired file
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(repaired_data, f, indent=2, ensure_ascii=False)
                
                logger.info(f"Save file repaired: {filename}")
                print(f"Save file {filename} repaired successfully.")
                return True
            
        except Exception:
            pass  # Repair attempt failed
        
        logger.error(f"Could not repair save file: {filename}")
        print(f"Could not repair save file: {filename}")
        return False
        
    except Exception as e:
        error_msg = f"Error during save file repair: {e}"
        logger.error(error_msg)
        print(error_msg)
        return False
