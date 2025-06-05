"""
Item handler system using Strategy pattern.
Each item type has its own handler class for better maintainability and extensibility.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import random

from game.constants import Items, Locations, ItemEffects
from game.player import (
    add_item_to_inventory, 
    remove_item_from_inventory, 
    heal_player, 
    damage_player,
    move_player
)
from game.world import get_available_locations, get_all_locations, change_location
from utils.random_events import generate_random_event


class ItemHandler(ABC):
    """Abstract base class for item handlers."""
    
    @abstractmethod
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        """
        Use the item and apply its effects.
        
        Args:
            player: Player state dictionary
            world: World state dictionary
            
        Returns:
            bool: True if item was used successfully, False otherwise
        """
        pass
    
    @abstractmethod
    def get_item_name(self) -> str:
        """Get the item name this handler manages."""
        pass
    
    def remove_from_inventory(self, player: Dict[str, Any]) -> bool:
        """Helper method to remove item from inventory after use."""
        return remove_item_from_inventory(player, self.get_item_name())


class MapHandler(ItemHandler):
    """Handler for map item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You consult the map. It shows the following locations you can go to:")
        available_locations = get_available_locations(world)
        for location in available_locations:
            print(f"- {location}")
        return True
    
    def get_item_name(self) -> str:
        return Items.MAP


class BreadHandler(ItemHandler):
    """Handler for bread item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You eat the bread. It's delicious and restores some health.")
        heal_player(player, 20)
        self.remove_from_inventory(player)
        return True
    
    def get_item_name(self) -> str:
        return Items.BREAD


class StickHandler(ItemHandler):
    """Handler for stick item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You wave the stick around. It makes a satisfying swoosh sound.")
        if world["current_location"] == Locations.FOREST:
            print("A nearby bird is startled and drops a shiny object!")
            add_item_to_inventory(player, Items.GOLD_COIN)
        return True
    
    def get_item_name(self) -> str:
        return Items.STICK


class BerriesHandler(ItemHandler):
    """Handler for berries item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You eat the berries. They're sweet and juicy.")
        if generate_random_event(events=[(ItemEffects.HEAL, 70), ("poison", 30)]) == ItemEffects.HEAL:
            print("You feel refreshed and gain some health.")
            heal_player(player, 10)
        else:
            print("Uh oh, those weren't safe to eat. You lose some health.")
            damage_player(player, 5)
        self.remove_from_inventory(player)
        return True
    
    def get_item_name(self) -> str:
        return Items.BERRIES


class TorchHandler(ItemHandler):
    """Handler for torch item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        current_location = world["current_location"]
        if current_location == Locations.CAVE:
            print("You light the torch, illuminating the dark cave around you.")
            world["locations"][Locations.CAVE]["description"] += " The cave is now well-lit by your torch."
        else:
            print("You light the torch. It provides warmth and light.")
        return True
    
    def get_item_name(self) -> str:
        return Items.TORCH


class GemstoneHandler(ItemHandler):
    """Handler for gemstone item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You examine the gemstone closely. It glimmers with an otherworldly light.")
        if world["current_location"] == Locations.VILLAGE:
            print("A merchant notices your gemstone and offers to buy it for 50 gold!")
            choice = input("Do you want to sell the gemstone? (y/n): ").lower()
            if choice == 'y':
                player["gold"] = player.get("gold", 0) + 50
                self.remove_from_inventory(player)
                print("You sold the gemstone for 50 gold.")
            else:
                print("You decide to keep the gemstone.")
        return True
    
    def get_item_name(self) -> str:
        return Items.GEMSTONE


class RopeHandler(ItemHandler):
    """Handler for rope item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        if world["current_location"] == Locations.MOUNTAIN:
            print("You use the rope to safely navigate a treacherous part of the mountain.")
            heal_player(player, 5)
            print("Your climbing technique improves, and you feel more confident.")
        else:
            print("You coil and uncoil the rope. It might be useful in the right situation.")
        return True
    
    def get_item_name(self) -> str:
        return Items.ROPE


class PickaxeHandler(ItemHandler):
    """Handler for pickaxe item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You swing the pickaxe, but there's nothing here to mine.")
        return True
    
    def get_item_name(self) -> str:
        return Items.PICKAXE


class MushroomsHandler(ItemHandler):
    """Handler for mushrooms item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You decide to eat the mushrooms.")
        if generate_random_event(events=[(ItemEffects.HEAL, 50), ("poison", 50)]) == ItemEffects.HEAL:
            print("The mushrooms were edible and restore some health.")
            heal_player(player, 20)
        else:
            print("The mushrooms were poisonous! You feel sick.")
            damage_player(player, 10)
        self.remove_from_inventory(player)
        return True
    
    def get_item_name(self) -> str:
        return Items.MUSHROOMS


class MountainHerbsHandler(ItemHandler):
    """Handler for mountain herbs item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You brew a tea with the mountain herbs and drink it.")
        heal_player(player, 30)
        print("You feel invigorated and ready for more adventures!")
        self.remove_from_inventory(player)
        return True
    
    def get_item_name(self) -> str:
        return Items.MOUNTAIN_HERBS


class AncientCoinHandler(ItemHandler):
    """Handler for ancient coin item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You flip the ancient coin. As it spins in the air, you feel a strange energy...")
        if generate_random_event(events=[(ItemEffects.TELEPORT, 50), (ItemEffects.REVEAL_SECRET, 50)]) == ItemEffects.TELEPORT:
            new_location = random.choice(get_all_locations(world))
            change_location(world, new_location)
            move_player(player, new_location)
            print(f"The coin vanishes and you find yourself teleported to {new_location}!")
        else:
            print("The coin glows and reveals a secret about your current location!")
            # Could add location-specific secrets here
        self.remove_from_inventory(player)
        return True
    
    def get_item_name(self) -> str:
        return Items.ANCIENT_COIN


class HermitsBlessingHandler(ItemHandler):
    """Handler for hermit's blessing item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You invoke the hermit's blessing. A warm, comforting light envelops you.")
        heal_player(player, 50)
        print("You feel completely refreshed and your mind is clear.")
        self.remove_from_inventory(player)
        return True
    
    def get_item_name(self) -> str:
        return Items.HERMITS_BLESSING


class SwordHandler(ItemHandler):
    """Handler for sword item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You swing the sword, practicing your combat moves.")
        if world["current_location"] == Locations.FOREST:
            print("Your sword slices through some thick vines, revealing a hidden path!")
            # Could update world state here
        return True
    
    def get_item_name(self) -> str:
        return Items.SWORD


class GoldCoinHandler(ItemHandler):
    """Handler for gold coin item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You flip the gold coin. It catches the light, shimmering brilliantly.")
        if world["current_location"] == Locations.VILLAGE:
            print("A street vendor notices your coin and offers you a mysterious potion in exchange.")
            choice = input("Do you want to trade the gold coin for the potion? (y/n): ").lower()
            if choice == 'y':
                self.remove_from_inventory(player)
                add_item_to_inventory(player, Items.MYSTERIOUS_POTION)
                print("You traded the gold coin for a mysterious potion.")
            else:
                print("You decide to keep the gold coin.")
        return True
    
    def get_item_name(self) -> str:
        return Items.GOLD_COIN


class SilverNecklaceHandler(ItemHandler):
    """Handler for silver necklace item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You hold up the silver necklace, admiring its craftsmanship.")
        if world["current_location"] == Locations.MOUNTAIN:
            print("The necklace begins to glow, revealing hidden runes on nearby rocks!")
            print("You discover a secret path leading to a hidden cave.")
            # Could update world state here
        else:
            print("The necklace sparkles beautifully, but nothing else happens.")
        return True
    
    def get_item_name(self) -> str:
        return Items.SILVER_NECKLACE


class AncientArtifactHandler(ItemHandler):
    """Handler for ancient artifact item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You examine the ancient artifact closely, turning it over in your hands.")
        event = generate_random_event(events=[(ItemEffects.WISDOM, 40), (ItemEffects.CURSE, 30), (None, 30)])
        
        if event == ItemEffects.WISDOM:
            print("Suddenly, knowledge of the ancient world floods your mind!")
            print("You gain insight into the history of this land.")
            # Could update player knowledge here
        elif event == ItemEffects.CURSE:
            print("A dark energy emanates from the artifact, making you feel weak.")
            damage_player(player, 10)
            print("You quickly put the artifact away, feeling drained.")
        else:
            print("Despite its age, the artifact remains inert and mysterious.")
        return True
    
    def get_item_name(self) -> str:
        return Items.ANCIENT_ARTIFACT


class MysteriousPotionHandler(ItemHandler):
    """Handler for mysterious potion item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You drink the mysterious potion. It tastes strange...")
        # Random effect
        effects = [
            (ItemEffects.HEAL, 40),
            (ItemEffects.DAMAGE, 30),
            ("magic_boost", 20),
            ("nothing", 10)
        ]
        effect = generate_random_event(events=effects)
        
        if effect == ItemEffects.HEAL:
            heal_amount = random.randint(20, 40)
            heal_player(player, heal_amount)
            print(f"You feel much better! Restored {heal_amount} health.")
        elif effect == ItemEffects.DAMAGE:
            damage_amount = random.randint(5, 15)
            damage_player(player, damage_amount)
            print(f"The potion was poisonous! You lose {damage_amount} health.")
        elif effect == "magic_boost":
            print("You feel a surge of magical energy! Your next action will be more effective.")
            # Could add temporary buff here
        else:
            print("Nothing happens. The potion seems to have no effect.")
        
        self.remove_from_inventory(player)
        return True
    
    def get_item_name(self) -> str:
        return Items.MYSTERIOUS_POTION


class MagicRingHandler(ItemHandler):
    """Handler for magic ring item."""
    
    def use(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        print("You put on the magic ring. It glows with a soft, mystical light.")
        print("You feel a protective aura surrounding you.")
        # Could add temporary protection or other magical effects
        return True
    
    def get_item_name(self) -> str:
        return Items.MAGIC_RING


class ItemHandlerRegistry:
    """Registry for managing item handlers."""
    
    def __init__(self):
        self._handlers: Dict[str, ItemHandler] = {}
        self._register_default_handlers()
    
    def _register_default_handlers(self):
        """Register all default item handlers."""
        handlers = [
            MapHandler(),
            BreadHandler(),
            StickHandler(),
            BerriesHandler(),
            TorchHandler(),
            GemstoneHandler(),
            RopeHandler(),
            PickaxeHandler(),
            MushroomsHandler(),
            MountainHerbsHandler(),
            AncientCoinHandler(),
            HermitsBlessingHandler(),
            SwordHandler(),
            GoldCoinHandler(),
            SilverNecklaceHandler(),
            AncientArtifactHandler(),
            MysteriousPotionHandler(),
            MagicRingHandler()
        ]
        
        for handler in handlers:
            self.register_handler(handler)
    
    def register_handler(self, handler: ItemHandler):
        """Register a new item handler."""
        self._handlers[handler.get_item_name()] = handler
    
    def get_handler(self, item_name: str) -> Optional[ItemHandler]:
        """Get the handler for a specific item."""
        return self._handlers.get(item_name)
    
    def use_item(self, player: Dict[str, Any], world: Dict[str, Any], item_name: str) -> bool:
        """Use an item through its handler."""
        handler = self.get_handler(item_name)
        if handler:
            return handler.use(player, world)
        else:
            print(f"You're not sure how to use the {item_name}.")
            return False


# Global registry instance
item_registry = ItemHandlerRegistry()

