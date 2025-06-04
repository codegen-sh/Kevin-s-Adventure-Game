"""
Desert location plugin - Example location plugin for Kevin's Adventure Game.
"""

from plugins.base import BaseLocation, PluginMetadata
from game.player import add_item_to_inventory, damage_player, heal_player
from utils.random_events import generate_random_event
from typing import Dict, Any, List


class Desert(BaseLocation):
    """A desert location plugin."""
    
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="Desert",
            version="1.0.0",
            description="A vast desert location with sandstorms and hidden oases",
            author="Plugin Developer"
        )
    
    def initialize(self) -> bool:
        """Initialize the desert location plugin."""
        return True
    
    def cleanup(self) -> None:
        """Clean up desert location resources."""
        pass
    
    def get_description(self) -> str:
        """Return the location description."""
        return "A vast, sun-scorched desert with rolling sand dunes and the occasional mirage."
    
    def get_connections(self) -> List[str]:
        """Return list of connected location names."""
        return ["Village", "Mountain"]
    
    def get_items(self) -> List[str]:
        """Return list of items available in this location."""
        return ["cactus_fruit", "sand_crystal", "desert_map"]
    
    def enter_location(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """Handle player entering the desert."""
        print("You step into the scorching desert. The sun beats down mercilessly.")
        print("Sand stretches endlessly in all directions, broken only by occasional dunes.")
        
        while True:
            print("\nWhat would you like to do in the desert?")
            print("1. Search for an oasis")
            print("2. Climb a sand dune")
            print("3. Seek shelter from the sun")
            print("4. Follow mysterious tracks")
            print("5. Leave the desert")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                self._search_for_oasis(world, player)
            elif choice == "2":
                self._climb_sand_dune(world, player)
            elif choice == "3":
                self._seek_shelter(world, player)
            elif choice == "4":
                self._follow_tracks(world, player)
            elif choice == "5":
                print("You decide to leave the harsh desert behind.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def _search_for_oasis(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """Search for an oasis in the desert."""
        print("You wander through the desert, searching for signs of water...")
        
        event = generate_random_event(events=[
            ("find_oasis", 25),
            ("find_mirage", 35),
            ("get_lost", 25),
            ("sandstorm", 15)
        ])
        
        if event == "find_oasis":
            print("Incredible! You discover a hidden oasis with crystal-clear water!")
            print("You drink deeply and rest in the shade of palm trees.")
            heal_player(player, 30)
            add_item_to_inventory(player, "oasis_water")
        elif event == "find_mirage":
            print("You see what appears to be an oasis, but as you approach, it vanishes.")
            print("It was just a mirage. The disappointment is crushing.")
            damage_player(player, 5)
        elif event == "get_lost":
            print("You become disoriented in the endless sand dunes.")
            print("It takes hours to find your bearings again.")
            damage_player(player, 10)
        elif event == "sandstorm":
            print("A sudden sandstorm engulfs you! You struggle to find shelter.")
            damage_player(player, 15)
            if "desert_cloak" in player["inventory"]:
                print("Your desert cloak protects you from the worst of the storm.")
                heal_player(player, 10)
    
    def _climb_sand_dune(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """Climb a large sand dune."""
        print("You begin the arduous climb up a massive sand dune...")
        
        if "rope" in player["inventory"]:
            print("Using your rope, you make steady progress up the dune.")
            print("From the top, you can see for miles in every direction!")
            
            event = generate_random_event(events=[
                ("spot_ruins", 40),
                ("see_caravan", 30),
                ("find_treasure", 20),
                ("nothing_special", 10)
            ])
            
            if event == "spot_ruins":
                print("You spot ancient ruins partially buried in the sand to the east.")
                print("They might be worth investigating.")
            elif event == "see_caravan":
                print("You see a distant caravan moving across the desert.")
                print("Perhaps you could catch up to them for supplies.")
                if generate_random_event(events=[("success", 50), ("failure", 50)]) == "success":
                    print("You manage to signal the caravan and they share some supplies!")
                    player["gold"] += 20
                    add_item_to_inventory(player, "dried_dates")
            elif event == "find_treasure":
                print("Something glints in the sand near the dune's peak!")
                add_item_to_inventory(player, "ancient_coin")
                player["gold"] += 15
            else:
                print("The view is breathtaking, but you don't see anything unusual.")
        else:
            print("The sand is too loose and steep. You slide back down repeatedly.")
            print("You need rope or climbing gear to make this ascent.")
            damage_player(player, 8)
    
    def _seek_shelter(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """Seek shelter from the desert sun."""
        print("You look for shelter from the relentless desert sun...")
        
        event = generate_random_event(events=[
            ("find_cave", 30),
            ("find_rocks", 40),
            ("no_shelter", 30)
        ])
        
        if event == "find_cave":
            print("You discover a small cave carved into a rocky outcrop.")
            print("Inside, you find ancient cave paintings and blessed coolness.")
            heal_player(player, 20)
            
            if generate_random_event(events=[("treasure", 30), ("nothing", 70)]) == "treasure":
                print("Hidden behind the paintings, you find a small cache!")
                add_item_to_inventory(player, "ancient_artifact")
        elif event == "find_rocks":
            print("You find some large rocks that provide partial shade.")
            print("It's not much, but it's better than nothing.")
            heal_player(player, 10)
        else:
            print("Despite your search, you can't find any shelter.")
            print("The sun continues to beat down mercilessly.")
            damage_player(player, 12)
    
    def _follow_tracks(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """Follow mysterious tracks in the sand."""
        print("You notice strange tracks in the sand and decide to follow them...")
        
        event = generate_random_event(events=[
            ("desert_nomad", 25),
            ("dangerous_creature", 20),
            ("abandoned_camp", 30),
            ("tracks_vanish", 25)
        ])
        
        if event == "desert_nomad":
            print("The tracks lead you to a friendly desert nomad!")
            print("They share wisdom about surviving in the desert.")
            heal_player(player, 15)
            
            if player.get("gold", 0) >= 25:
                choice = input("The nomad offers to sell you a desert cloak for 25 gold. Buy it? (y/n): ")
                if choice.lower() == 'y':
                    player["gold"] -= 25
                    add_item_to_inventory(player, "desert_cloak")
                    print("You purchase the desert cloak. It will protect you from sandstorms.")
        elif event == "dangerous_creature":
            print("The tracks belong to a dangerous desert predator!")
            print("It attacks you before you can retreat!")
            damage_player(player, 20)
            
            if "sword" in player["inventory"]:
                print("You fight back with your sword and drive it away!")
                print("Searching the area, you find some valuable items it was hoarding.")
                add_item_to_inventory(player, "predator_fang")
                player["gold"] += 10
        elif event == "abandoned_camp":
            print("The tracks lead to an abandoned desert camp.")
            print("Whoever was here left in a hurry, leaving supplies behind.")
            add_item_to_inventory(player, "water_skin")
            add_item_to_inventory(player, "dried_meat")
            print("You take what you can carry.")
        else:
            print("The tracks mysteriously vanish, as if swept away by the wind.")
            print("You're left wondering what made them.")

