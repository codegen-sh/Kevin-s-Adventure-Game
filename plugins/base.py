"""
Base classes for the plugin system.

This module defines the abstract base classes that all plugins must inherit from.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
import logging

logger = logging.getLogger(__name__)


class PluginMetadata:
    """Metadata for plugins including versioning and dependencies."""
    
    def __init__(self, name: str, version: str, description: str = "", 
                 author: str = "", dependencies: List[str] = None,
                 min_game_version: str = "1.0.0"):
        self.name = name
        self.version = version
        self.description = description
        self.author = author
        self.dependencies = dependencies or []
        self.min_game_version = min_game_version
    
    def __repr__(self):
        return f"PluginMetadata(name='{self.name}', version='{self.version}')"


class BasePlugin(ABC):
    """
    Abstract base class for all plugins.
    
    All plugins must inherit from this class and implement the required methods.
    """
    
    def __init__(self):
        self._metadata: Optional[PluginMetadata] = None
        self._enabled = True
        self._initialized = False
    
    @property
    @abstractmethod
    def metadata(self) -> PluginMetadata:
        """Return plugin metadata."""
        pass
    
    @abstractmethod
    def initialize(self) -> bool:
        """
        Initialize the plugin.
        
        Returns:
            bool: True if initialization was successful, False otherwise.
        """
        pass
    
    @abstractmethod
    def cleanup(self) -> None:
        """Clean up plugin resources."""
        pass
    
    def enable(self) -> None:
        """Enable the plugin."""
        self._enabled = True
        logger.info(f"Plugin {self.metadata.name} enabled")
    
    def disable(self) -> None:
        """Disable the plugin."""
        self._enabled = False
        logger.info(f"Plugin {self.metadata.name} disabled")
    
    @property
    def enabled(self) -> bool:
        """Check if plugin is enabled."""
        return self._enabled
    
    @property
    def initialized(self) -> bool:
        """Check if plugin is initialized."""
        return self._initialized
    
    def validate(self) -> List[str]:
        """
        Validate the plugin configuration.
        
        Returns:
            List[str]: List of validation errors, empty if valid.
        """
        errors = []
        
        if not self.metadata:
            errors.append("Plugin metadata is missing")
        elif not self.metadata.name:
            errors.append("Plugin name is required")
        elif not self.metadata.version:
            errors.append("Plugin version is required")
        
        return errors


class BaseLocation(BasePlugin):
    """
    Abstract base class for location plugins.
    
    Location plugins define new areas that players can visit and interact with.
    """
    
    @abstractmethod
    def get_description(self) -> str:
        """Return the location description."""
        pass
    
    @abstractmethod
    def get_connections(self) -> List[str]:
        """Return list of connected location names."""
        pass
    
    @abstractmethod
    def get_items(self) -> List[str]:
        """Return list of items available in this location."""
        pass
    
    @abstractmethod
    def enter_location(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """
        Handle player entering this location.
        
        Args:
            world: The game world state
            player: The player state
        """
        pass
    
    def get_location_data(self) -> Dict[str, Any]:
        """
        Get the location data structure for the world.
        
        Returns:
            Dict containing location information for world initialization.
        """
        return {
            "description": self.get_description(),
            "connections": self.get_connections(),
            "items": self.get_items()
        }
    
    def validate(self) -> List[str]:
        """Validate location plugin."""
        errors = super().validate()
        
        try:
            description = self.get_description()
            if not description or not isinstance(description, str):
                errors.append("Location must have a valid description")
        except Exception as e:
            errors.append(f"Error getting location description: {e}")
        
        try:
            connections = self.get_connections()
            if not isinstance(connections, list):
                errors.append("Location connections must be a list")
        except Exception as e:
            errors.append(f"Error getting location connections: {e}")
        
        try:
            items = self.get_items()
            if not isinstance(items, list):
                errors.append("Location items must be a list")
        except Exception as e:
            errors.append(f"Error getting location items: {e}")
        
        return errors


class BaseAction(BasePlugin):
    """
    Abstract base class for action plugins.
    
    Action plugins define new commands that players can execute.
    """
    
    @abstractmethod
    def get_triggers(self) -> List[str]:
        """
        Return list of command triggers for this action.
        
        Returns:
            List[str]: Command words that trigger this action.
        """
        pass
    
    @abstractmethod
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], 
                command: str, args: List[str]) -> bool:
        """
        Execute the action.
        
        Args:
            player: The player state
            world: The game world state
            command: The command that triggered this action
            args: Additional arguments from the command
            
        Returns:
            bool: True if action was handled, False otherwise.
        """
        pass
    
    @abstractmethod
    def get_help_text(self) -> str:
        """Return help text for this action."""
        pass
    
    def can_execute(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        """
        Check if this action can be executed in the current context.
        
        Args:
            player: The player state
            world: The game world state
            
        Returns:
            bool: True if action can be executed, False otherwise.
        """
        return True
    
    def validate(self) -> List[str]:
        """Validate action plugin."""
        errors = super().validate()
        
        try:
            triggers = self.get_triggers()
            if not isinstance(triggers, list) or not triggers:
                errors.append("Action must have at least one trigger")
            elif not all(isinstance(t, str) and t.strip() for t in triggers):
                errors.append("All action triggers must be non-empty strings")
        except Exception as e:
            errors.append(f"Error getting action triggers: {e}")
        
        try:
            help_text = self.get_help_text()
            if not help_text or not isinstance(help_text, str):
                errors.append("Action must have valid help text")
        except Exception as e:
            errors.append(f"Error getting action help text: {e}")
        
        return errors


class BaseGameMechanic(BasePlugin):
    """
    Abstract base class for game mechanic plugins.
    
    Game mechanic plugins add new systems and features to the game.
    """
    
    @abstractmethod
    def on_game_start(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called when a new game starts."""
        pass
    
    @abstractmethod
    def on_game_load(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called when a game is loaded."""
        pass
    
    @abstractmethod
    def on_game_save(self, player: Dict[str, Any], world: Dict[str, Any]) -> Dict[str, Any]:
        """
        Called when game is saved.
        
        Returns:
            Dict[str, Any]: Additional data to save with the game.
        """
        pass
    
    @abstractmethod
    def on_turn_start(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called at the start of each turn."""
        pass
    
    @abstractmethod
    def on_turn_end(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called at the end of each turn."""
        pass

