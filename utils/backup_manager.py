"""
Backup and restore manager for Kevin's Adventure Game save files.
Provides automatic backup creation, restoration, and cleanup functionality.
"""

import os
import shutil
import json
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from pathlib import Path

logger = logging.getLogger(__name__)


class BackupManager:
    """Manages backup and restore operations for save files."""
    
    def __init__(self, save_directory: str = "saves", backup_directory: str = "saves/backups"):
        self.save_directory = Path(save_directory)
        self.backup_directory = Path(backup_directory)
        self.max_backups_per_save = 5  # Maximum number of backups to keep per save file
        self.max_backup_age_days = 30  # Maximum age of backups in days
        
        # Ensure directories exist
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Ensure backup directories exist."""
        try:
            self.backup_directory.mkdir(parents=True, exist_ok=True)
            logger.info(f"Backup directory ensured: {self.backup_directory}")
        except Exception as e:
            logger.error(f"Failed to create backup directory: {e}")
            raise
    
    def create_backup(self, save_filename: str, backup_reason: str = "manual") -> Optional[str]:
        """
        Create a backup of a save file.
        
        Args:
            save_filename: Name of the save file to backup
            backup_reason: Reason for creating the backup
            
        Returns:
            str: Backup filename if successful, None otherwise
        """
        try:
            save_path = self.save_directory / save_filename
            
            if not save_path.exists():
                logger.error(f"Save file not found: {save_filename}")
                return None
            
            # Generate backup filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = save_filename.replace('.json', '')
            backup_filename = f"{base_name}_backup_{timestamp}.json"
            backup_path = self.backup_directory / backup_filename
            
            # Copy the save file to backup location
            shutil.copy2(save_path, backup_path)
            
            # Create backup metadata
            metadata = {
                "original_file": save_filename,
                "backup_time": datetime.now().isoformat(),
                "backup_reason": backup_reason,
                "original_size": save_path.stat().st_size,
                "backup_size": backup_path.stat().st_size
            }
            
            # Save metadata alongside backup
            metadata_path = backup_path.with_suffix('.meta.json')
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            logger.info(f"Backup created: {backup_filename}")
            
            # Clean up old backups for this save file
            self._cleanup_old_backups(base_name)
            
            return backup_filename
            
        except Exception as e:
            logger.error(f"Failed to create backup for {save_filename}: {e}")
            return None
    
    def restore_backup(self, backup_filename: str, overwrite_existing: bool = False) -> bool:
        """
        Restore a save file from backup.
        
        Args:
            backup_filename: Name of the backup file to restore
            overwrite_existing: Whether to overwrite existing save file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            backup_path = self.backup_directory / backup_filename
            
            if not backup_path.exists():
                logger.error(f"Backup file not found: {backup_filename}")
                return False
            
            # Load backup metadata to get original filename
            metadata_path = backup_path.with_suffix('.meta.json')
            if metadata_path.exists():
                with open(metadata_path, 'r') as f:
                    metadata = json.load(f)
                original_filename = metadata.get("original_file")
            else:
                # Fallback: derive original filename from backup filename
                original_filename = backup_filename.replace('_backup_', '_').split('_')[0] + '.json'
            
            restore_path = self.save_directory / original_filename
            
            # Check if original file exists and handle overwrite
            if restore_path.exists() and not overwrite_existing:
                logger.warning(f"Save file already exists: {original_filename}")
                return False
            
            # Create backup of existing file before overwriting
            if restore_path.exists():
                self.create_backup(original_filename, "pre_restore")
            
            # Copy backup to save location
            shutil.copy2(backup_path, restore_path)
            
            logger.info(f"Backup restored: {backup_filename} -> {original_filename}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to restore backup {backup_filename}: {e}")
            return False
    
    def list_backups(self, save_filename: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List available backups.
        
        Args:
            save_filename: If provided, only list backups for this save file
            
        Returns:
            List of backup information dictionaries
        """
        try:
            backups = []
            
            for backup_file in self.backup_directory.glob("*_backup_*.json"):
                metadata_file = backup_file.with_suffix('.meta.json')
                
                # Load metadata if available
                metadata = {}
                if metadata_file.exists():
                    try:
                        with open(metadata_file, 'r') as f:
                            metadata = json.load(f)
                    except Exception as e:
                        logger.warning(f"Failed to load metadata for {backup_file.name}: {e}")
                
                # Extract information
                backup_info = {
                    "backup_filename": backup_file.name,
                    "original_file": metadata.get("original_file", "Unknown"),
                    "backup_time": metadata.get("backup_time", "Unknown"),
                    "backup_reason": metadata.get("backup_reason", "Unknown"),
                    "size": backup_file.stat().st_size,
                    "age_days": (datetime.now() - datetime.fromtimestamp(backup_file.stat().st_mtime)).days
                }
                
                # Filter by save filename if specified
                if save_filename is None or backup_info["original_file"] == save_filename:
                    backups.append(backup_info)
            
            # Sort by backup time (newest first)
            backups.sort(key=lambda x: x["backup_time"], reverse=True)
            return backups
            
        except Exception as e:
            logger.error(f"Failed to list backups: {e}")
            return []
    
    def delete_backup(self, backup_filename: str) -> bool:
        """
        Delete a backup file and its metadata.
        
        Args:
            backup_filename: Name of the backup file to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            backup_path = self.backup_directory / backup_filename
            metadata_path = backup_path.with_suffix('.meta.json')
            
            # Delete backup file
            if backup_path.exists():
                backup_path.unlink()
                logger.info(f"Deleted backup file: {backup_filename}")
            
            # Delete metadata file
            if metadata_path.exists():
                metadata_path.unlink()
                logger.info(f"Deleted backup metadata: {metadata_path.name}")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete backup {backup_filename}: {e}")
            return False
    
    def _cleanup_old_backups(self, save_base_name: str):
        """Clean up old backups for a specific save file."""
        try:
            # Get all backups for this save file
            pattern = f"{save_base_name}_backup_*.json"
            backups = list(self.backup_directory.glob(pattern))
            
            # Sort by modification time (newest first)
            backups.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            
            # Remove excess backups (keep only max_backups_per_save)
            for backup in backups[self.max_backups_per_save:]:
                self.delete_backup(backup.name)
                logger.info(f"Cleaned up old backup: {backup.name}")
            
        except Exception as e:
            logger.error(f"Failed to cleanup old backups for {save_base_name}: {e}")
    
    def cleanup_expired_backups(self):
        """Clean up backups older than max_backup_age_days."""
        try:
            cutoff_date = datetime.now() - timedelta(days=self.max_backup_age_days)
            
            for backup_file in self.backup_directory.glob("*_backup_*.json"):
                backup_time = datetime.fromtimestamp(backup_file.stat().st_mtime)
                
                if backup_time < cutoff_date:
                    self.delete_backup(backup_file.name)
                    logger.info(f"Cleaned up expired backup: {backup_file.name}")
            
        except Exception as e:
            logger.error(f"Failed to cleanup expired backups: {e}")
    
    def get_backup_statistics(self) -> Dict[str, Any]:
        """Get statistics about backups."""
        try:
            backups = self.list_backups()
            
            if not backups:
                return {
                    "total_backups": 0,
                    "total_size_mb": 0,
                    "oldest_backup": None,
                    "newest_backup": None
                }
            
            total_size = sum(backup["size"] for backup in backups)
            backup_times = [backup["backup_time"] for backup in backups if backup["backup_time"] != "Unknown"]
            
            return {
                "total_backups": len(backups),
                "total_size_mb": round(total_size / (1024 * 1024), 2),
                "oldest_backup": min(backup_times) if backup_times else None,
                "newest_backup": max(backup_times) if backup_times else None,
                "backup_directory": str(self.backup_directory)
            }
            
        except Exception as e:
            logger.error(f"Failed to get backup statistics: {e}")
            return {"error": str(e)}
    
    def verify_backup_integrity(self, backup_filename: str) -> bool:
        """
        Verify the integrity of a backup file.
        
        Args:
            backup_filename: Name of the backup file to verify
            
        Returns:
            bool: True if backup is valid, False otherwise
        """
        try:
            backup_path = self.backup_directory / backup_filename
            
            if not backup_path.exists():
                logger.error(f"Backup file not found: {backup_filename}")
                return False
            
            # Try to load and parse the backup file
            with open(backup_path, 'r') as f:
                data = json.load(f)
            
            # Basic validation - check if it has required save data structure
            required_fields = ["player", "world"]
            for field in required_fields:
                if field not in data:
                    logger.error(f"Backup missing required field: {field}")
                    return False
            
            logger.info(f"Backup integrity verified: {backup_filename}")
            return True
            
        except json.JSONDecodeError as e:
            logger.error(f"Backup file corrupted (JSON error): {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to verify backup integrity: {e}")
            return False

