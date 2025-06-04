"""
Village location class for Kevin's Adventure Game.
Demonstrates the new class-based location architecture.
"""
import random
from typing import List, Dict, Any, Optional
from game.base_location import BaseLocation, LocationData


class VillageLocation(BaseLocation):
    """
    Village location with shops, NPCs, and quests.
    
    This class demonstrates how to extend BaseLocation for specific locations
    with unique behaviors and interactions.
    """
    
    def __init__(self) -> None:
        """Initialize the Village location."""
        location_data = LocationData(
            name="Village",
            description="A small, peaceful village with thatched-roof houses and friendly inhabitants. The village square bustles with activity, and you can see a shop, an inn, and villagers going about their daily business.",
            connections=["Forest", "Mountain"],
            items=["map", "bread"],
            special_properties={
                "has_shop": True,
                "has_inn": True,
                "has_quest_giver": True,
                "shop_inventory": ["rope", "torch", "bread", "mysterious_potion"],
                "shop_prices": {"rope": 20, "torch": 15, "bread": 5, "mysterious_potion": 50},
                "inn_cost": 10,
                "quests_available": ["find_lost_cat", "deliver_message", "collect_herbs"]
            }
        )
        super().__init__(location_data)
    
    def enter(self, player: 'Player', world: 'World') -> None:
        """Handle player entering the village."""
        if not self.visited:
            print(f"\n=== Welcome to {self.name} ===")
            print(self.description)
            print("\nThe villagers notice your arrival and wave friendly greetings.")
            print("You see several places of interest:")
            print("- A general store with various supplies")
            print("- A cozy inn with smoke rising from its chimney")
            print("- Villagers who might have tasks or information")
            self.mark_visited()
        else:
            print(f"\nYou return to the familiar {self.name}.")
            print("The villagers recognize you and nod in greeting.")
        
        # Show available items
        if self.items:
            print(f"\nItems available here: {', '.join(self.items)}")
        
        # Random village events
        self._trigger_random_event(player, world)
    
    def get_available_actions(self, player: 'Player', world: 'World') -> List[str]:
        """Get available actions in the village."""
        actions = ["look", "inventory", "status", "shop", "inn", "talk", "quest"]
        
        # Add item-related actions
        if self.items:
            actions.extend(["take", "examine"])
        
        # Add movement actions
        if self.connections:
            actions.append("go")
        
        return actions
    
    def perform_action(self, action: str, player: 'Player', world: 'World') -> bool:
        """Perform action in the village."""
        action = action.lower().strip()
        
        # Handle basic actions first
        if action in ["look", "inventory", "status", "take", "examine", "go"]:
            # Use parent class implementation for basic actions
            return super().perform_action(action, player, world)
        
        # Village-specific actions
        elif action == "shop":
            return self._visit_shop(player, world)
        elif action == "inn":
            return self._visit_inn(player, world)
        elif action in ["talk", "villagers"]:
            return self._talk_to_villagers(player, world)
        elif action == "quest":
            return self._handle_quests(player, world)
        else:
            print(f"You can't {action} in the village.")
            print("Available actions: " + ", ".join(self.get_available_actions(player, world)))
            return False
    
    def _visit_shop(self, player: 'Player', world: 'World') -> bool:
        """Handle shop interactions."""
        print("\n=== Village General Store ===")
        print("The shopkeeper greets you warmly.")
        print("'Welcome! Take a look at what I have for sale.'")
        
        shop_inventory = self.get_special_property("shop_inventory", [])
        shop_prices = self.get_special_property("shop_prices", {})
        
        if not shop_inventory:
            print("The shop is currently out of stock.")
            return True
        
        print("\nAvailable items:")
        for item in shop_inventory:
            price = shop_prices.get(item, 10)
            print(f"- {item}: {price} gold")
        
        print(f"\nYour gold: {player.gold}")
        
        choice = input("What would you like to buy? (or 'leave' to exit): ").strip().lower()
        
        if choice == "leave":
            print("'Come back anytime!' says the shopkeeper.")
            return True
        
        if choice in shop_inventory:
            price = shop_prices.get(choice, 10)
            if player.spend_gold(price):
                player.add_item(choice)
                print(f"'Thank you for your purchase!' says the shopkeeper.")
                return True
            else:
                print("'You don't have enough gold for that,' says the shopkeeper sadly.")
                return False
        else:
            print("'I don't have that item,' says the shopkeeper.")
            return False
    
    def _visit_inn(self, player: 'Player', world: 'World') -> bool:
        """Handle inn interactions."""
        print("\n=== The Cozy Inn ===")
        print("The innkeeper looks up from cleaning a mug.")
        print("'Welcome, traveler! Would you like to rest here?'")
        
        inn_cost = self.get_special_property("inn_cost", 10)
        
        print(f"Rest at the inn: {inn_cost} gold")
        print("(Restores full health and advances time)")
        print(f"Your current health: {player.health}/{player.max_health}")
        print(f"Your gold: {player.gold}")
        
        if player.is_at_max_health:
            print("You're already at full health, but you could rest to pass time.")
        
        choice = input("Would you like to rest? (y/n): ").strip().lower()
        
        if choice == 'y':
            if player.spend_gold(inn_cost):
                player.heal(player.max_health - player.health)
                world.advance_time()
                print("You have a restful sleep at the inn.")
                print("You wake up feeling completely refreshed!")
                print(f"Time has advanced to: {world.get_time_of_day()}")
                return True
            else:
                print("'I'm sorry, but you don't have enough gold,' says the innkeeper.")
                return False
        else:
            print("'Feel free to come back when you need rest!' says the innkeeper.")
            return True
    
    def _talk_to_villagers(self, player: 'Player', world: 'World') -> bool:
        """Handle talking to villagers."""
        print("\n=== Talking to Villagers ===")
        
        villager_conversations = [
            "A farmer tells you: 'The weather has been strange lately. The crops are growing faster than usual.'",
            "An elderly woman says: 'I've heard strange sounds coming from the forest at night.'",
            "A child exclaims: 'I saw a shiny thing in the mountain caves! But mama won't let me go there.'",
            "A merchant mentions: 'Trade has been good, but some travelers speak of mysterious creatures.'",
            "A blacksmith notes: 'My tools have been working better since that strange meteor fell last month.'",
            "A baker shares: 'The bread has been rising perfectly lately. Something magical in the air!'"
        ]
        
        conversation = random.choice(villager_conversations)
        print(conversation)
        
        # Chance for useful information or items
        event_chance = random.randint(1, 100)
        if event_chance <= 20:  # 20% chance
            print("\nThe villager also mentions:")
            
            helpful_info = [
                "'If you're heading to the forest, take a stick. The birds there drop shiny things when startled.'",
                "'The mountain hermit sometimes gives blessings to kind travelers.'",
                "'I heard there are healing herbs growing on the mountain slopes.'",
                "'The cave near the forest has ancient paintings. Quite fascinating!'",
                "'A torch is essential for cave exploration. Very dangerous without light.'"
            ]
            
            print(random.choice(helpful_info))
        
        elif event_chance <= 5:  # 5% chance for item
            print("\nThe grateful villager gives you a small gift!")
            gifts = ["bread", "ancient_coin", "rope"]
            gift = random.choice(gifts)
            player.add_item(gift)
        
        return True
    
    def _handle_quests(self, player: 'Player', world: 'World') -> bool:
        """Handle quest interactions."""
        print("\n=== Village Quests ===")
        
        available_quests = self.get_special_property("quests_available", [])
        completed_quests = world.get_global_state("completed_quests", [])
        
        # Filter out completed quests
        active_quests = [q for q in available_quests if q not in completed_quests]
        
        if not active_quests:
            print("There are no quests available at the moment.")
            print("Check back later or complete current objectives.")
            return True
        
        print("Available quests:")
        for i, quest in enumerate(active_quests, 1):
            quest_desc = self._get_quest_description(quest)
            print(f"{i}. {quest_desc}")
        
        try:
            choice = int(input("Choose a quest (number) or 0 to cancel: "))
            if choice == 0:
                print("Maybe another time.")
                return True
            elif 1 <= choice <= len(active_quests):
                quest = active_quests[choice - 1]
                return self._start_quest(quest, player, world)
            else:
                print("Invalid quest number.")
                return False
        except ValueError:
            print("Please enter a valid number.")
            return False
    
    def _get_quest_description(self, quest: str) -> str:
        """Get description for a quest."""
        descriptions = {
            "find_lost_cat": "Find Mrs. Henderson's lost cat (Reward: 30 gold)",
            "deliver_message": "Deliver a message to the mountain hermit (Reward: Ancient blessing)",
            "collect_herbs": "Collect 3 mountain herbs for the village healer (Reward: Healing potion)"
        }
        return descriptions.get(quest, f"Unknown quest: {quest}")
    
    def _start_quest(self, quest: str, player: 'Player', world: 'World') -> bool:
        """Start a specific quest."""
        active_quests = world.get_global_state("active_quests", [])
        
        if quest in active_quests:
            print("You're already working on this quest!")
            return False
        
        active_quests.append(quest)
        world.set_global_state("active_quests", active_quests)
        
        quest_messages = {
            "find_lost_cat": "Mrs. Henderson tearfully asks you to find her cat Whiskers. Last seen near the forest.",
            "deliver_message": "The village elder gives you a sealed letter to deliver to the mountain hermit.",
            "collect_herbs": "The village healer needs mountain herbs for medicine. Bring back 3 herbs."
        }
        
        message = quest_messages.get(quest, f"You've accepted the quest: {quest}")
        print(f"\nQuest accepted: {self._get_quest_description(quest)}")
        print(message)
        
        return True
    
    def _trigger_random_event(self, player: 'Player', world: 'World') -> None:
        """Trigger random village events."""
        event_chance = random.randint(1, 100)
        
        if event_chance <= 10:  # 10% chance
            events = [
                "A traveling merchant passes through, offering exotic wares.",
                "Children are playing in the square, their laughter filling the air.",
                "A town crier announces news from distant lands.",
                "Smoke rises from the blacksmith's forge as he works on new tools.",
                "A group of travelers shares stories of their adventures.",
                "The village bell rings, calling people to a community gathering."
            ]
            
            print(f"\n[Village Event] {random.choice(events)}")
    
    def get_random_event(self, player: 'Player', world: 'World') -> Optional[str]:
        """Get a random event specific to the village."""
        events = [
            "You notice a bulletin board with job postings and news.",
            "A friendly dog approaches and seems to want to play.",
            "You overhear villagers discussing recent strange occurrences.",
            "The smell of fresh bread wafts from the bakery.",
            "A merchant's cart arrives, bringing goods from other towns.",
            "Children run past, chasing a colorful butterfly."
        ]
        
        if random.randint(1, 100) <= 30:  # 30% chance
            return random.choice(events)
        return None
    
    def on_item_used(self, item: str, player: 'Player', world: 'World') -> bool:
        """Handle item usage in the village."""
        if item == "map":
            print("You consult your map in the village square.")
            print("Villagers gather around, pointing out local landmarks and sharing directions.")
            return True
        elif item == "bread":
            print("You share your bread with some hungry village children.")
            print("They thank you warmly, and their parents express gratitude.")
            # Small reputation boost could be tracked here
            return True
        elif item == "gold_coin":
            print("You flip the gold coin in the village square.")
            print("A merchant notices and offers to trade some goods.")
            return True
        
        return False  # Item has no special effect in village

