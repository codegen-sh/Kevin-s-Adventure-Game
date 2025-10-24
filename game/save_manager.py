"""
Advanced save manager for Kevin's Adventure Game.
Provides multiple save slots, auto-save, metadata management, and robust error handling.
"""

import os
import json
import logging
import threading
import time
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Tuple, Callable
from pathlib import Path

from utils.serialization import SaveDataSerializer, SaveDataValidator, SaveMigrator, get_save_metadata, SerializationError
from utils.backup_manager import BackupManager

logger = logging.getLogger(__name__)


class SaveSlot:
    """Represents a single save slot with metadata."""
    
    def __init__(self, slot_id: int, filename: str, metadata: Dict[str, Any]):
        self.slot_id = slot_id
        self.filename = filename
        self.metadata = metadata
        self.last_accessed = datetime.now()
    
    def __str__(self):
        return f"Slot {self.slot_id}: {self.metadata.get('player_name', 'Unknown')} - {self.metadata.get('location', 'Unknown')}"


class AutoSaveManager:
    """Manages automatic saving functionality."""
    
    def __init__(self, save_callback: Callable, interval_minutes: int = 5):
        self.save_callback = save_callback
        self.interval_seconds = interval_minutes * 60
        self.enabled = False
        self.thread = None
        self.stop_event = threading.Event()
        self.last_save_time = None
    
    def start(self):
        """Start auto-save functionality."""
        if self.enabled:
            return
        
        self.enabled = True
        self.stop_event.clear()
        self.thread = threading.Thread(target=self._auto_save_loop, daemon=True)
        self.thread.start()
        logger.info(f"Auto-save started with {self.interval_seconds}s interval")
    
    def stop(self):
        """Stop auto-save functionality."""
        if not self.enabled:
            return
        
        self.enabled = False
        self.stop_event.set()
        if self.thread:
            self.thread.join(timeout=5)
        logger.info("Auto-save stopped")
    
    def _auto_save_loop(self):
        """Main auto-save loop."""
        while self.enabled and not self.stop_event.wait(self.interval_seconds):
            try:
                self.save_callback()
                self.last_save_time = datetime.now()
                logger.debug("Auto-save completed")
            except Exception as e:
                logger.error(f"Auto-save failed: {e}")
    
    def set_interval(self, minutes: int):
        """Set auto-save interval in minutes."""
        self.interval_seconds = minutes * 60
        logger.info(f"Auto-save interval set to {minutes} minutes")


class SaveManager:
    """Advanced save manager with multiple slots, auto-save, and backup functionality."""
    
    def __init__(self, save_directory: str = "saves", max_slots: int = 10):
        self.save_directory = Path(save_directory)
        self.max_slots = max_slots
        self.slots: Dict[int, SaveSlot] = {}
        self.current_slot = None
        
        # Initialize components
        self.serializer = SaveDataSerializer()
        self.backup_manager = BackupManager(str(self.save_directory))
        self.auto_save_manager = AutoSaveManager(self._auto_save_current_slot)
        
        # Ensure directory exists
        self._ensure_save_directory()
        
        # Load existing save slots
        self._load_save_slots()
        
        # Configure logging
        self._setup_logging()
    
    def _setup_logging(self):
        """Setup logging for save operations."""
        log_file = self.save_directory / "save_operations.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    def _ensure_save_directory(self):
        """Ensure save directory exists."""
        try:
            self.save_directory.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            logger.error(f"Failed to create save directory: {e}")
            raise
    
    def _load_save_slots(self):
        """Load existing save slots from directory."""
        try:
            self.slots.clear()
            
            # Look for save files in the directory
            for save_file in self.save_directory.glob("slot_*.sav"):
                try:
                    slot_id = int(save_file.stem.split('_')[1])
                    
                    # Load and validate save data
                    with open(save_file, 'rb') as f:
                        data = f.read()
                    
                    player, world, metadata = self.serializer.deserialize(data)
                    save_metadata = get_save_metadata({
                        "player": player,
                        "world": world,
                        "metadata": metadata
                    })
                    
                    self.slots[slot_id] = SaveSlot(slot_id, save_file.name, save_metadata)
                    logger.info(f"Loaded save slot {slot_id}")
                    
                except Exception as e:
                    logger.error(f"Failed to load save slot from {save_file}: {e}")
                    continue
            
            logger.info(f"Loaded {len(self.slots)} save slots")
            
        except Exception as e:
            logger.error(f"Failed to load save slots: {e}")
    
    def create_save_slot(self, slot_id: int, player: Dict[str, Any], world: Dict[str, Any], 
                        metadata: Optional[Dict[str, Any]] = None) -> bool:
        """
        Create a new save slot.
        
        Args:
            slot_id: Slot number (1-max_slots)
            player: Player data
            world: World data
            metadata: Optional metadata
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not (1 <= slot_id <= self.max_slots):
                logger.error(f"Invalid slot ID: {slot_id}. Must be between 1 and {self.max_slots}")
                return False
            
            # Create backup if slot already exists
            if slot_id in self.slots:
                existing_filename = self.slots[slot_id].filename
                self.backup_manager.create_backup(existing_filename, "slot_overwrite")
            
            # Prepare metadata
            save_metadata = metadata or {}
            save_metadata.update({
                "slot_id": slot_id,
                "created_time": datetime.now().isoformat(),
                "game_version": "1.0.0"
            })
            
            # Serialize data
            serialized_data = self.serializer.serialize(player, world, True, save_metadata)
            
            # Save to file
            filename = f"slot_{slot_id:02d}.sav"
            filepath = self.save_directory / filename
            
            with open(filepath, 'wb') as f:
                f.write(serialized_data)
            
            # Update slot registry
            display_metadata = get_save_metadata({
                "player": player,
                "world": world,
                "metadata": save_metadata
            })
            self.slots[slot_id] = SaveSlot(slot_id, filename, display_metadata)
            
            logger.info(f"Created save slot {slot_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to create save slot {slot_id}: {e}")
            return False
    
    def load_save_slot(self, slot_id: int) -> Optional[Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]]:
        """
        Load data from a save slot.
        
        Args:
            slot_id: Slot number to load
            
        Returns:
            Tuple of (player, world, metadata) or None if failed
        """
        try:
            if slot_id not in self.slots:
                logger.error(f"Save slot {slot_id} does not exist")
                return None
            
            slot = self.slots[slot_id]
            filepath = self.save_directory / slot.filename
            
            if not filepath.exists():
                logger.error(f"Save file not found: {slot.filename}")
                return None
            
            # Load and deserialize data
            with open(filepath, 'rb') as f:
                data = f.read()
            
            player, world, metadata = self.serializer.deserialize(data)
            
            # Check if migration is needed
            save_data = {"player": player, "world": world, "metadata": metadata}
            if SaveMigrator.is_migration_needed(save_data):
                logger.info(f"Migrating save slot {slot_id}")
                migrated_data = SaveMigrator.migrate_save_data(save_data)
                
                # Save migrated data back
                self.create_save_slot(slot_id, migrated_data["player"], 
                                    migrated_data["world"], migrated_data["metadata"])
                
                player = migrated_data["player"]
                world = migrated_data["world"]
                metadata = migrated_data["metadata"]
            
            # Update last accessed time
            slot.last_accessed = datetime.now()
            self.current_slot = slot_id
            
            logger.info(f"Loaded save slot {slot_id}")
            return player, world, metadata
            
        except SerializationError as e:
            logger.error(f"Serialization error loading slot {slot_id}: {e}")
            
            # Try to restore from backup
            if self._attempt_backup_restore(slot_id):
                return self.load_save_slot(slot_id)
            
            return None
        except Exception as e:
            logger.error(f"Failed to load save slot {slot_id}: {e}")
            return None
    
    def delete_save_slot(self, slot_id: int) -> bool:
        """
        Delete a save slot.
        
        Args:
            slot_id: Slot number to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if slot_id not in self.slots:
                logger.error(f"Save slot {slot_id} does not exist")
                return False
            
            slot = self.slots[slot_id]
            filepath = self.save_directory / slot.filename
            
            # Create backup before deletion
            self.backup_manager.create_backup(slot.filename, "pre_deletion")
            
            # Delete file
            if filepath.exists():
                filepath.unlink()
            
            # Remove from slots
            del self.slots[slot_id]
            
            # Clear current slot if it was deleted
            if self.current_slot == slot_id:
                self.current_slot = None
            
            logger.info(f"Deleted save slot {slot_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete save slot {slot_id}: {e}")
            return False
    
    def list_save_slots(self) -> List[Dict[str, Any]]:
        """
        List all available save slots with metadata.
        
        Returns:
            List of slot information dictionaries
        """
        try:
            slot_list = []
            
            for slot_id in range(1, self.max_slots + 1):
                if slot_id in self.slots:
                    slot = self.slots[slot_id]
                    slot_info = {
                        "slot_id": slot_id,
                        "filename": slot.filename,
                        "metadata": slot.metadata,
                        "last_accessed": slot.last_accessed.isoformat(),
                        "is_current": slot_id == self.current_slot,
                        "exists": True
                    }
                else:
                    slot_info = {
                        "slot_id": slot_id,
                        "filename": None,
                        "metadata": {},
                        "last_accessed": None,
                        "is_current": False,
                        "exists": False
                    }
                
                slot_list.append(slot_info)
            
            return slot_list
            
        except Exception as e:
            logger.error(f"Failed to list save slots: {e}")
            return []
    
    def quick_save(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        """
        Quick save to the current slot or create a new one.
        
        Args:
            player: Player data
            world: World data
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Use current slot or find first available slot
            slot_id = self.current_slot
            if slot_id is None:
                # Find first available slot
                for i in range(1, self.max_slots + 1):
                    if i not in self.slots:
                        slot_id = i
                        break
                else:
                    # All slots full, use slot 1
                    slot_id = 1
            
            metadata = {
                "save_type": "quick_save",
                "quick_save_time": datetime.now().isoformat()
            }
            
            return self.create_save_slot(slot_id, player, world, metadata)
            
        except Exception as e:
            logger.error(f"Quick save failed: {e}")
            return False
    
    def _auto_save_current_slot(self):
        """Auto-save callback for current slot."""
        if hasattr(self, '_current_game_state'):
            player, world = self._current_game_state
            
            # Use current slot or create auto-save slot
            slot_id = self.current_slot or self.max_slots  # Use last slot for auto-save
            
            metadata = {
                "save_type": "auto_save",
                "auto_save_time": datetime.now().isoformat()
            }
            
            self.create_save_slot(slot_id, player, world, metadata)
    
    def set_current_game_state(self, player: Dict[str, Any], world: Dict[str, Any]):
        """Set current game state for auto-save."""
        self._current_game_state = (player, world)
    
    def start_auto_save(self, interval_minutes: int = 5):
        """Start auto-save with specified interval."""
        self.auto_save_manager.set_interval(interval_minutes)
        self.auto_save_manager.start()
    
    def stop_auto_save(self):
        """Stop auto-save."""
        self.auto_save_manager.stop()
    
    def _attempt_backup_restore(self, slot_id: int) -> bool:
        """Attempt to restore a corrupted save from backup."""
        try:
            if slot_id not in self.slots:
                return False
            
            slot = self.slots[slot_id]
            backups = self.backup_manager.list_backups(slot.filename)
            
            if not backups:
                logger.error(f"No backups available for slot {slot_id}")
                return False
            
            # Try to restore from the most recent backup
            latest_backup = backups[0]
            logger.info(f"Attempting to restore slot {slot_id} from backup: {latest_backup['backup_filename']}")
            
            if self.backup_manager.restore_backup(latest_backup['backup_filename'], overwrite_existing=True):
                # Reload the slot
                self._load_save_slots()
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Failed to restore from backup for slot {slot_id}: {e}")
            return False
    
    def get_save_statistics(self) -> Dict[str, Any]:
        """Get statistics about save files."""
        try:
            total_size = 0
            oldest_save = None
            newest_save = None
            
            for slot in self.slots.values():
                filepath = self.save_directory / slot.filename
                if filepath.exists():
                    size = filepath.stat().st_size
                    total_size += size
                    
                    mtime = datetime.fromtimestamp(filepath.stat().st_mtime)
                    if oldest_save is None or mtime < oldest_save:
                        oldest_save = mtime
                    if newest_save is None or mtime > newest_save:
                        newest_save = mtime
            
            backup_stats = self.backup_manager.get_backup_statistics()
            
            return {
                "total_slots": len(self.slots),
                "max_slots": self.max_slots,
                "total_size_mb": round(total_size / (1024 * 1024), 2),
                "oldest_save": oldest_save.isoformat() if oldest_save else None,
                "newest_save": newest_save.isoformat() if newest_save else None,
                "auto_save_enabled": self.auto_save_manager.enabled,
                "auto_save_interval_minutes": self.auto_save_manager.interval_seconds // 60,
                "backup_stats": backup_stats,
                "save_directory": str(self.save_directory)
            }
            
        except Exception as e:
            logger.error(f"Failed to get save statistics: {e}")
            return {"error": str(e)}
    
    def cleanup_old_saves(self, keep_count: int = 5):
        """Clean up old save files, keeping only the most recent ones."""
        try:
            if len(self.slots) <= keep_count:
                return
            
            # Sort slots by last accessed time
            sorted_slots = sorted(self.slots.values(), key=lambda x: x.last_accessed, reverse=True)
            
            # Delete oldest slots beyond keep_count
            for slot in sorted_slots[keep_count:]:
                self.delete_save_slot(slot.slot_id)
            
            logger.info(f"Cleaned up old saves, kept {keep_count} most recent")
            
        except Exception as e:
            logger.error(f"Failed to cleanup old saves: {e}")
    
    def export_save_slot(self, slot_id: int, export_path: str) -> bool:
        """
        Export a save slot to a specified path.
        
        Args:
            slot_id: Slot to export
            export_path: Path to export to
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if slot_id not in self.slots:
                logger.error(f"Save slot {slot_id} does not exist")
                return False
            
            slot = self.slots[slot_id]
            source_path = self.save_directory / slot.filename
            
            if not source_path.exists():
                logger.error(f"Save file not found: {slot.filename}")
                return False
            
            # Copy file to export location
            import shutil
            shutil.copy2(source_path, export_path)
            
            logger.info(f"Exported save slot {slot_id} to {export_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to export save slot {slot_id}: {e}")
            return False
    
    def import_save_slot(self, slot_id: int, import_path: str) -> bool:
        """
        Import a save file to a specific slot.
        
        Args:
            slot_id: Target slot ID
            import_path: Path to import from
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not os.path.exists(import_path):
                logger.error(f"Import file not found: {import_path}")
                return False
            
            # Validate the import file
            with open(import_path, 'rb') as f:
                data = f.read()
            
            try:
                player, world, metadata = self.serializer.deserialize(data)
            except SerializationError as e:
                logger.error(f"Invalid save file format: {e}")
                return False
            
            # Create the save slot
            return self.create_save_slot(slot_id, player, world, metadata)
            
        except Exception as e:
            logger.error(f"Failed to import save slot {slot_id}: {e}")
            return False

