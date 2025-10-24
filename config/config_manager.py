"""
Configuration Manager for Kevin's Adventure Game.

Handles loading, validation, and caching of configuration files.
Supports environment-specific configurations and graceful fallbacks.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union
import logging

logger = logging.getLogger(__name__)


class ConfigurationError(Exception):
    """Raised when there's an error with configuration loading or validation."""
    pass


class ConfigManager:
    """
    Centralized configuration manager for the game.
    
    Handles loading and caching of configuration files with support for
    environment-specific overrides and validation.
    """
    
    def __init__(self, config_dir: Optional[str] = None, environment: Optional[str] = None):
        """
        Initialize the configuration manager.
        
        Args:
            config_dir: Path to the configuration directory. Defaults to 'config' in project root.
            environment: Environment name for loading environment-specific configs.
        """
        self.config_dir = Path(config_dir or self._get_default_config_dir())
        self.environment = environment or os.getenv('GAME_ENVIRONMENT', 'production')
        self._cache: Dict[str, Any] = {}
        self._loaded_files: set = set()
        
        # Validate config directory exists
        if not self.config_dir.exists():
            raise ConfigurationError(f"Configuration directory not found: {self.config_dir}")
    
    def _get_default_config_dir(self) -> str:
        """Get the default configuration directory path."""
        # Get the project root (parent of the directory containing this file)
        current_file = Path(__file__)
        project_root = current_file.parent.parent
        return str(project_root / "config")
    
    def load_config(self, config_path: str, use_cache: bool = True) -> Dict[str, Any]:
        """
        Load a configuration file.
        
        Args:
            config_path: Path to the config file relative to config_dir
            use_cache: Whether to use cached version if available
            
        Returns:
            Dictionary containing the configuration data
            
        Raises:
            ConfigurationError: If the file cannot be loaded or parsed
        """
        if use_cache and config_path in self._cache:
            return self._cache[config_path]
        
        file_path = self.config_dir / config_path
        
        if not file_path.exists():
            raise ConfigurationError(f"Configuration file not found: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
            
            # Apply environment-specific overrides if they exist
            config_data = self._apply_environment_overrides(config_data, config_path)
            
            # Cache the loaded configuration
            self._cache[config_path] = config_data
            self._loaded_files.add(config_path)
            
            logger.info(f"Loaded configuration: {config_path}")
            return config_data
            
        except json.JSONDecodeError as e:
            raise ConfigurationError(f"Invalid JSON in {file_path}: {e}")
        except Exception as e:
            raise ConfigurationError(f"Error loading {file_path}: {e}")
    
    def _apply_environment_overrides(self, config_data: Dict[str, Any], config_path: str) -> Dict[str, Any]:
        """
        Apply environment-specific configuration overrides.
        
        Args:
            config_data: Base configuration data
            config_path: Path to the configuration file
            
        Returns:
            Configuration data with environment overrides applied
        """
        env_file = self.config_dir / "environments" / f"{self.environment}.json"
        
        if not env_file.exists():
            return config_data
        
        try:
            with open(env_file, 'r', encoding='utf-8') as f:
                env_overrides = json.load(f)
            
            # Look for overrides specific to this config file
            config_name = Path(config_path).stem
            if config_name in env_overrides:
                config_data = self._deep_merge(config_data, env_overrides[config_name])
                logger.info(f"Applied {self.environment} environment overrides to {config_path}")
            
        except Exception as e:
            logger.warning(f"Could not load environment overrides: {e}")
        
        return config_data
    
    def _deep_merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deep merge two dictionaries, with override values taking precedence.
        
        Args:
            base: Base dictionary
            override: Override dictionary
            
        Returns:
            Merged dictionary
        """
        result = base.copy()
        
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        
        return result
    
    def get_game_settings(self) -> Dict[str, Any]:
        """Get game settings configuration."""
        return self.load_config("game_settings/base.json")
    
    def get_items_config(self) -> Dict[str, Any]:
        """Get items configuration."""
        return self.load_config("items/items.json")
    
    def get_shop_config(self, shop_name: str = "village_shop") -> Dict[str, Any]:
        """Get shop configuration."""
        shop_config = self.load_config("items/shop_inventory.json")
        if shop_name in shop_config:
            return shop_config[shop_name]
        raise ConfigurationError(f"Shop configuration not found: {shop_name}")
    
    def get_world_config(self) -> Dict[str, Any]:
        """Get world and locations configuration."""
        return self.load_config("locations/world.json")
    
    def get_location_config(self, location_name: str) -> Dict[str, Any]:
        """
        Get location-specific configuration.
        
        Args:
            location_name: Name of the location (e.g., 'forest', 'village')
            
        Returns:
            Location configuration dictionary
        """
        location_file = f"locations/{location_name.lower()}.json"
        return self.load_config(location_file)
    
    def get_events_config(self) -> Dict[str, Any]:
        """Get random events configuration."""
        return self.load_config("events/random_events.json")
    
    def get_item_data(self, item_name: str) -> Dict[str, Any]:
        """
        Get data for a specific item.
        
        Args:
            item_name: Name of the item
            
        Returns:
            Item data dictionary
            
        Raises:
            ConfigurationError: If item is not found
        """
        items_config = self.get_items_config()
        if item_name in items_config["items"]:
            return items_config["items"][item_name]
        raise ConfigurationError(f"Item not found in configuration: {item_name}")
    
    def get_location_data(self, location_name: str) -> Dict[str, Any]:
        """
        Get data for a specific location from world config.
        
        Args:
            location_name: Name of the location
            
        Returns:
            Location data dictionary
            
        Raises:
            ConfigurationError: If location is not found
        """
        world_config = self.get_world_config()
        locations = world_config["world"]["locations"]
        if location_name in locations:
            return locations[location_name]
        raise ConfigurationError(f"Location not found in configuration: {location_name}")
    
    def reload_config(self, config_path: Optional[str] = None) -> None:
        """
        Reload configuration files, clearing cache.
        
        Args:
            config_path: Specific config file to reload, or None to reload all
        """
        if config_path:
            if config_path in self._cache:
                del self._cache[config_path]
                self._loaded_files.discard(config_path)
        else:
            self._cache.clear()
            self._loaded_files.clear()
        
        logger.info(f"Reloaded configuration: {config_path or 'all'}")
    
    def validate_configuration(self) -> bool:
        """
        Validate all loaded configurations.
        
        Returns:
            True if all configurations are valid
            
        Raises:
            ConfigurationError: If validation fails
        """
        try:
            # Load and validate core configurations
            self.get_game_settings()
            self.get_items_config()
            self.get_world_config()
            self.get_events_config()
            
            # Validate that all locations referenced in world config have detail files
            world_config = self.get_world_config()
            for location_name in world_config["world"]["locations"]:
                try:
                    self.get_location_config(location_name)
                except ConfigurationError:
                    logger.warning(f"No detailed configuration found for location: {location_name}")
            
            logger.info("Configuration validation successful")
            return True
            
        except Exception as e:
            raise ConfigurationError(f"Configuration validation failed: {e}")
    
    def get_config_info(self) -> Dict[str, Any]:
        """
        Get information about the current configuration state.
        
        Returns:
            Dictionary with configuration manager state information
        """
        return {
            "config_dir": str(self.config_dir),
            "environment": self.environment,
            "loaded_files": list(self._loaded_files),
            "cache_size": len(self._cache)
        }

