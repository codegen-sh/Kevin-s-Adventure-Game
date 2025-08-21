"""
Data models for Kevin's Adventure Game.
Provides object-oriented representations of game entities.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
import json


@dataclass
class Item:
    """Represents an item in the game."""
    id: str
    name: str
    description: str
    portable: bool = True
    value: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert item to dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'portable': self.portable,
            'value': self.value
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Item':
        """Create item from dictionary."""
        return cls(**data)


@dataclass
class Inventory:
    """Manages a collection of items."""
    items: List[Item] = field(default_factory=list)
    max_capacity: int = 20
    
    def add_item(self, item: Item) -> bool:
        """Add an item to the inventory."""
        if len(self.items) >= self.max_capacity:
            return False
        self.items.append(item)
        return True
    
    def remove_item(self, item_id: str) -> Optional[Item]:
        """Remove an item from the inventory by ID."""
        for i, item in enumerate(self.items):
            if item.id == item_id:
                return self.items.pop(i)
        return None
    
    def has_item(self, item_id: str) -> bool:
        """Check if inventory contains an item."""
        return any(item.id == item_id for item in self.items)
    
    def get_item(self, item_id: str) -> Optional[Item]:
        """Get an item by ID without removing it."""
        for item in self.items:
            if item.id == item_id:
                return item
        return None
    
    def is_empty(self) -> bool:
        """Check if inventory is empty."""
        return len(self.items) == 0
    
    def get_item_names(self) -> List[str]:
        """Get list of item names."""
        return [item.name for item in self.items]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert inventory to dictionary for serialization."""
        return {
            'items': [item.to_dict() for item in self.items],
            'max_capacity': self.max_capacity
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Inventory':
        """Create inventory from dictionary."""
        items = [Item.from_dict(item_data) for item_data in data.get('items', [])]
        return cls(items=items, max_capacity=data.get('max_capacity', 20))


@dataclass
class Location:
    """Represents a location in the game world."""
    id: str
    name: str
    description: str
    connections: List[str] = field(default_factory=list)
    items: List[Item] = field(default_factory=list)
    visited: bool = False
    
    def add_item(self, item: Item):
        """Add an item to this location."""
        self.items.append(item)
    
    def remove_item(self, item_id: str) -> Optional[Item]:
        """Remove an item from this location."""
        for i, item in enumerate(self.items):
            if item.id == item_id:
                return self.items.pop(i)
        return None
    
    def has_item(self, item_id: str) -> bool:
        """Check if location contains an item."""
        return any(item.id == item_id for item in self.items)
    
    def get_item(self, item_id: str) -> Optional[Item]:
        """Get an item by ID."""
        for item in self.items:
            if item.id == item_id:
                return item
        return None
    
    def get_item_names(self) -> List[str]:
        """Get list of item names at this location."""
        return [item.name for item in self.items]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert location to dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'connections': self.connections,
            'items': [item.to_dict() for item in self.items],
            'visited': self.visited
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Location':
        """Create location from dictionary."""
        items = [Item.from_dict(item_data) for item_data in data.get('items', [])]
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            connections=data.get('connections', []),
            items=items,
            visited=data.get('visited', False)
        )


@dataclass
class Player:
    """Represents the player character."""
    name: str
    health: int = 100
    max_health: int = 100
    gold: int = 100
    current_location_id: str = "village"
    inventory: Inventory = field(default_factory=Inventory)
    flags: Dict[str, Any] = field(default_factory=dict)
    
    def is_alive(self) -> bool:
        """Check if player is alive."""
        return self.health > 0
    
    def take_damage(self, amount: int):
        """Reduce player health."""
        self.health = max(0, self.health - amount)
    
    def heal(self, amount: int):
        """Restore player health."""
        self.health = min(self.max_health, self.health + amount)
    
    def add_gold(self, amount: int):
        """Add gold to player."""
        self.gold += amount
    
    def spend_gold(self, amount: int) -> bool:
        """Spend gold if player has enough."""
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
    
    def set_flag(self, flag: str, value: Any):
        """Set a player flag."""
        self.flags[flag] = value
    
    def get_flag(self, flag: str, default: Any = None) -> Any:
        """Get a player flag."""
        return self.flags.get(flag, default)
    
    def has_flag(self, flag: str) -> bool:
        """Check if player has a flag."""
        return flag in self.flags
    
    def get_status(self) -> str:
        """Get player status string."""
        inventory_text = "empty" if self.inventory.is_empty() else ", ".join(self.inventory.get_item_names())
        return f"Health: {self.health}/{self.max_health} | Inventory: {inventory_text} | Gold: {self.gold}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert player to dictionary for serialization."""
        return {
            'name': self.name,
            'health': self.health,
            'max_health': self.max_health,
            'gold': self.gold,
            'current_location_id': self.current_location_id,
            'inventory': self.inventory.to_dict(),
            'flags': self.flags
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Player':
        """Create player from dictionary."""
        inventory = Inventory.from_dict(data.get('inventory', {}))
        return cls(
            name=data['name'],
            health=data.get('health', 100),
            max_health=data.get('max_health', 100),
            gold=data.get('gold', 100),
            current_location_id=data.get('current_location_id', 'village'),
            inventory=inventory,
            flags=data.get('flags', {})
        )


@dataclass
class World:
    """Represents the game world."""
    locations: Dict[str, Location] = field(default_factory=dict)
    starting_location_id: str = "village"
    flags: Dict[str, Any] = field(default_factory=dict)
    
    def add_location(self, location: Location):
        """Add a location to the world."""
        self.locations[location.id] = location
    
    def get_location(self, location_id: str) -> Optional[Location]:
        """Get a location by ID."""
        return self.locations.get(location_id)
    
    def get_location_names(self) -> List[str]:
        """Get list of all location names."""
        return [loc.name for loc in self.locations.values()]
    
    def set_flag(self, flag: str, value: Any):
        """Set a world flag."""
        self.flags[flag] = value
    
    def get_flag(self, flag: str, default: Any = None) -> Any:
        """Get a world flag."""
        return self.flags.get(flag, default)
    
    def has_flag(self, flag: str) -> bool:
        """Check if world has a flag."""
        return flag in self.flags
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert world to dictionary for serialization."""
        return {
            'locations': {loc_id: loc.to_dict() for loc_id, loc in self.locations.items()},
            'starting_location_id': self.starting_location_id,
            'flags': self.flags
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'World':
        """Create world from dictionary."""
        locations = {}
        for loc_id, loc_data in data.get('locations', {}).items():
            locations[loc_id] = Location.from_dict(loc_data)
        
        return cls(
            locations=locations,
            starting_location_id=data.get('starting_location_id', 'village'),
            flags=data.get('flags', {})
        )


# Factory functions for backward compatibility
def create_default_items() -> Dict[str, Item]:
    """Create default game items."""
    return {
        'map': Item('map', 'Map', 'A detailed map of the surrounding area', True, 10),
        'bread': Item('bread', 'Bread', 'A loaf of fresh bread', True, 5),
        'stick': Item('stick', 'Stick', 'A sturdy wooden stick', True, 2),
        'berries': Item('berries', 'Berries', 'Sweet wild berries', True, 3),
        'torch': Item('torch', 'Torch', 'A burning torch that provides light', True, 8),
        'gemstone': Item('gemstone', 'Gemstone', 'A sparkling precious gemstone', True, 50),
        'rope': Item('rope', 'Rope', 'Strong climbing rope', True, 15),
        'pickaxe': Item('pickaxe', 'Pickaxe', 'A heavy mining pickaxe', True, 25),
    }


def create_default_world() -> World:
    """Create the default game world."""
    world = World()
    items = create_default_items()
    
    # Create locations
    village = Location(
        id='village',
        name='Village',
        description='A small, peaceful village with thatched-roof houses and friendly inhabitants.',
        connections=['forest', 'mountain'],
        items=[items['map'], items['bread']]
    )
    
    forest = Location(
        id='forest',
        name='Forest',
        description='A dense, mysterious forest with towering trees and the sound of rustling leaves.',
        connections=['village', 'cave'],
        items=[items['stick'], items['berries']]
    )
    
    cave = Location(
        id='cave',
        name='Cave',
        description='A dark, damp cave with echoing sounds and glittering minerals on the walls.',
        connections=['forest'],
        items=[items['torch'], items['gemstone']]
    )
    
    mountain = Location(
        id='mountain',
        name='Mountain',
        description='A tall, snow-capped mountain with treacherous paths and breathtaking views.',
        connections=['village'],
        items=[items['rope'], items['pickaxe']]
    )
    
    # Add locations to world
    world.add_location(village)
    world.add_location(forest)
    world.add_location(cave)
    world.add_location(mountain)
    
    return world

