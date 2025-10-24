"""
Advanced serialization utilities for Kevin's Adventure Game.
Provides schema versioning, compression, and validation for save data.
"""

import json
import gzip
import hashlib
from datetime import datetime
from typing import Dict, Any, Optional, Tuple
import logging

# Current save format version
CURRENT_SAVE_VERSION = "1.0.0"

# Schema definitions for different versions
SAVE_SCHEMAS = {
    "1.0.0": {
        "required_fields": ["version", "timestamp", "checksum", "player", "world"],
        "player_fields": ["name", "health", "inventory", "location", "gold"],
        "world_fields": ["current_location", "locations"]
    }
}

logger = logging.getLogger(__name__)


class SerializationError(Exception):
    """Custom exception for serialization errors."""
    pass


class SaveDataValidator:
    """Validates save data against schema versions."""
    
    @staticmethod
    def validate_save_data(data: Dict[str, Any], version: str = CURRENT_SAVE_VERSION) -> bool:
        """
        Validate save data against the specified schema version.
        
        Args:
            data: The save data to validate
            version: The schema version to validate against
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            if version not in SAVE_SCHEMAS:
                logger.error(f"Unknown schema version: {version}")
                return False
                
            schema = SAVE_SCHEMAS[version]
            
            # Check required top-level fields
            for field in schema["required_fields"]:
                if field not in data:
                    logger.error(f"Missing required field: {field}")
                    return False
            
            # Validate player data
            if "player" in data:
                player = data["player"]
                for field in schema["player_fields"]:
                    if field not in player:
                        logger.error(f"Missing player field: {field}")
                        return False
            
            # Validate world data
            if "world" in data:
                world = data["world"]
                for field in schema["world_fields"]:
                    if field not in world:
                        logger.error(f"Missing world field: {field}")
                        return False
            
            return True
            
        except Exception as e:
            logger.error(f"Validation error: {e}")
            return False
    
    @staticmethod
    def calculate_checksum(data: Dict[str, Any]) -> str:
        """Calculate MD5 checksum of save data for integrity verification."""
        # Create a copy without the checksum field for calculation
        data_copy = data.copy()
        data_copy.pop('checksum', None)
        
        # Convert to JSON string with sorted keys for consistent hashing
        json_str = json.dumps(data_copy, sort_keys=True, separators=(',', ':'))
        return hashlib.md5(json_str.encode()).hexdigest()
    
    @staticmethod
    def verify_checksum(data: Dict[str, Any]) -> bool:
        """Verify the integrity of save data using checksum."""
        if 'checksum' not in data:
            logger.warning("No checksum found in save data")
            return False
            
        stored_checksum = data['checksum']
        calculated_checksum = SaveDataValidator.calculate_checksum(data)
        
        if stored_checksum != calculated_checksum:
            logger.error("Checksum mismatch - save data may be corrupted")
            return False
            
        return True


class SaveDataSerializer:
    """Handles serialization and deserialization of save data."""
    
    @staticmethod
    def serialize(player: Dict[str, Any], world: Dict[str, Any], 
                 compress: bool = True, metadata: Optional[Dict[str, Any]] = None) -> bytes:
        """
        Serialize game data to bytes with optional compression.
        
        Args:
            player: Player data dictionary
            world: World data dictionary
            compress: Whether to compress the data
            metadata: Optional metadata to include
            
        Returns:
            bytes: Serialized data
        """
        try:
            # Create save data structure
            save_data = {
                "version": CURRENT_SAVE_VERSION,
                "timestamp": datetime.now().isoformat(),
                "player": player,
                "world": world,
                "metadata": metadata or {}
            }
            
            # Calculate checksum
            save_data["checksum"] = SaveDataValidator.calculate_checksum(save_data)
            
            # Validate before serializing
            if not SaveDataValidator.validate_save_data(save_data):
                raise SerializationError("Save data validation failed")
            
            # Convert to JSON
            json_data = json.dumps(save_data, indent=2).encode('utf-8')
            
            # Compress if requested
            if compress:
                return gzip.compress(json_data)
            else:
                return json_data
                
        except Exception as e:
            logger.error(f"Serialization error: {e}")
            raise SerializationError(f"Failed to serialize save data: {e}")
    
    @staticmethod
    def deserialize(data: bytes, verify_integrity: bool = True) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
        """
        Deserialize game data from bytes.
        
        Args:
            data: Serialized data bytes
            verify_integrity: Whether to verify data integrity
            
        Returns:
            Tuple of (player, world, metadata)
        """
        try:
            # Try to decompress first (handles both compressed and uncompressed)
            try:
                json_data = gzip.decompress(data)
            except gzip.BadGzipFile:
                # Not compressed, use as-is
                json_data = data
            
            # Parse JSON
            save_data = json.loads(json_data.decode('utf-8'))
            
            # Verify integrity if requested
            if verify_integrity:
                if not SaveDataValidator.verify_checksum(save_data):
                    raise SerializationError("Save data integrity check failed")
            
            # Validate structure
            version = save_data.get("version", "1.0.0")
            if not SaveDataValidator.validate_save_data(save_data, version):
                raise SerializationError("Save data structure validation failed")
            
            return (
                save_data["player"],
                save_data["world"],
                save_data.get("metadata", {})
            )
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}")
            raise SerializationError(f"Failed to parse save data: {e}")
        except Exception as e:
            logger.error(f"Deserialization error: {e}")
            raise SerializationError(f"Failed to deserialize save data: {e}")


class SaveMigrator:
    """Handles migration of save data between versions."""
    
    @staticmethod
    def migrate_save_data(data: Dict[str, Any], target_version: str = CURRENT_SAVE_VERSION) -> Dict[str, Any]:
        """
        Migrate save data to the target version.
        
        Args:
            data: Save data to migrate
            target_version: Target schema version
            
        Returns:
            Dict: Migrated save data
        """
        current_version = data.get("version", "1.0.0")
        
        if current_version == target_version:
            return data
        
        logger.info(f"Migrating save data from {current_version} to {target_version}")
        
        # For now, we only have one version, but this structure allows for future migrations
        migrated_data = data.copy()
        migrated_data["version"] = target_version
        
        # Recalculate checksum after migration
        migrated_data["checksum"] = SaveDataValidator.calculate_checksum(migrated_data)
        
        return migrated_data
    
    @staticmethod
    def is_migration_needed(data: Dict[str, Any], target_version: str = CURRENT_SAVE_VERSION) -> bool:
        """Check if migration is needed for the save data."""
        current_version = data.get("version", "1.0.0")
        return current_version != target_version


def get_save_metadata(data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract metadata from save data for display purposes."""
    try:
        player = data.get("player", {})
        world = data.get("world", {})
        
        return {
            "version": data.get("version", "Unknown"),
            "timestamp": data.get("timestamp", "Unknown"),
            "player_name": player.get("name", "Unknown"),
            "player_level": player.get("health", 0),
            "location": player.get("location", "Unknown"),
            "gold": player.get("gold", 0),
            "inventory_count": len(player.get("inventory", [])),
            "world_location": world.get("current_location", "Unknown")
        }
    except Exception as e:
        logger.error(f"Error extracting metadata: {e}")
        return {"error": str(e)}

