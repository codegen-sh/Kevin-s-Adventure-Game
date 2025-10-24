import random

from game.player import (
    add_item_to_inventory,
    damage_player,
    heal_player,
    move_player,
    remove_item_from_inventory,
)
from game.world import change_location, get_all_locations, get_available_locations
from utils.random_events import generate_random_event
from config import config


def get_item_description(item):
    """Get item description from configuration."""
    try:
        item_data = config.get_item_data(item)
        return item_data["description"]
    except:
        return "A mysterious item."

def use_item(player, item, world):
    if item not in player["inventory"]:
        print(f"You don't have {item} in your inventory.")
        return False

    if item == "map":
        print("You consult the map. It shows the following locations you can go to:")
        available_locations = get_available_locations(world)
        for location in available_locations:
            print(f"- {location}")
        return True
    elif item == "bread":
        print("You eat the bread. It's delicious and restores some health.")
        heal_player(player, 20)
        remove_item_from_inventory(player, item)
        return True
    elif item == "stick":
        print("You wave the stick around. It makes a satisfying swoosh sound.")
        if world["current_location"] == "Forest":
            print("A nearby bird is startled and drops a shiny object!")
            add_item_to_inventory(player, "gold_coin")
        return True
    elif item == "berries":
        print("You eat the berries. They're sweet and juicy.")
        if generate_random_event(events=[("heal", 70), ("poison", 30)]) == "heal":
            print("You feel refreshed and gain some health.")
            heal_player(player, 10)
        else:
            print("Uh oh, those weren't safe to eat. You lose some health.")
            damage_player(player, 5)
        remove_item_from_inventory(player, item)
        return True
    elif item == "torch":
        current_location = world["current_location"]
        if current_location == "Cave":
            print("You light the torch, illuminating the dark cave around you.")
            world["locations"]["Cave"]["description"] += " The cave is now well-lit by your torch."
            return True
        else:
            print("You light the torch. It provides warmth and light.")
            return True
    elif item == "gemstone":
        print("You examine the gemstone closely. It glimmers with an otherworldly light.")
        if world["current_location"] == "Village":
            print("A merchant notices your gemstone and offers to buy it for 50 gold!")
            choice = input("Do you want to sell the gemstone? (y/n): ").lower()
            if choice == 'y':
                player["gold"] += 50
                remove_item_from_inventory(player, item)
                print("You sold the gemstone for 50 gold.")
            else:
                print("You decide to keep the gemstone.")
        return True
    elif item == "rope":
        if world["current_location"] == "Mountain":
            print("You use the rope to safely navigate a treacherous part of the mountain.")
            heal_player(player, 5)
            print("Your climbing technique improves, and you feel more confident.")
        else:
            print("You coil and uncoil the rope. It might be useful in the right situation.")
        return True
    elif item == "pickaxe":
        print("You swing the pickaxe, but there's nothing here to mine.")
        return True
    elif item == "mushrooms":
        print("You decide to eat the mushrooms.")
        if generate_random_event(events=[("heal", 50), ("poison", 50)]) == "heal":
            print("The mushrooms were edible and restore some health.")
            heal_player(player, 20)
        else:
            print("The mushrooms were poisonous! You feel sick.")
            damage_player(player, 10)
        remove_item_from_inventory(player, item)
        return True
    elif item == "mountain_herbs":
        print("You brew a tea with the mountain herbs and drink it.")
        heal_player(player, 30)
        print("You feel invigorated and ready for more adventures!")
        remove_item_from_inventory(player, item)
        return True
    elif item == "ancient_coin":
        print("You flip the ancient coin. As it spins in the air, you feel a strange energy...")
        if generate_random_event(events=[("teleport", 50), ("reveal_secret", 50)]) == "teleport":
            new_location = random.choice(get_all_locations(world))
            change_location(world, new_location)
            move_player(player, new_location)
            print(f"The coin vanishes and you find yourself teleported to {new_location}!")
        else:
            print("The coin glows and reveals a secret about your current location!")
            # You might want to add some location-specific secrets here
        remove_item_from_inventory(player, item)
        return True
    elif item == "hermit's_blessing":
        print("You invoke the hermit's blessing. A warm, comforting light envelops you.")
        heal_player(player, 50)
        print("You feel completely refreshed and your mind is clear.")
        remove_item_from_inventory(player, item)
        return True
    elif item == "sword":
        print("You swing the sword, practicing your combat moves.")
        if world["current_location"] == "Forest":
            print("Your sword slices through some thick vines, revealing a hidden path!")
            # update_world_state(world, "reveal_hidden_path")
        return True
    elif item == "gold_coin":
        print("You flip the gold coin. It catches the light, shimmering brilliantly.")
        if world["current_location"] == "Village":
            print("A street vendor notices your coin and offers you a mysterious potion in exchange.")
            choice = input("Do you want to trade the gold coin for the potion? (y/n): ").lower()
            if choice == 'y':
                remove_item_from_inventory(player, item)
                add_item_to_inventory(player, "mysterious_potion")
                print("You traded the gold coin for a mysterious potion.")
            else:
                print("You decide to keep the gold coin.")
        return True
    elif item == "silver_necklace":
        print("You hold up the silver necklace, admiring its craftsmanship.")
        if world["current_location"] == "Mountain":
            print("The necklace begins to glow, revealing hidden runes on nearby rocks!")
            print("You discover a secret path leading to a hidden cave.")
            # update_player_knowledge(player, "ancient_history")
        else:
            print("The necklace sparkles beautifully, but nothing else happens.")
        return True
    elif item == "ancient_artifact":
        print("You examine the ancient artifact closely, turning it over in your hands.")
        if generate_random_event(events=[("wisdom", 40), ("curse", 30), (None, 30)]) == "wisdom":
            print("Suddenly, knowledge of the ancient world floods your mind!")
            print("You gain insight into the history of this land.")
            # update_player_knowledge(player, "ancient_history")
        elif generate_random_event(events=[("wisdom", 40), ("curse", 30), (None, 30)]) == "curse":
            print("A dark energy emanates from the artifact, making you feel weak.")
            damage_player(player, 10)
            print("You quickly put the artifact away, feeling drained.")
        else:
            print("Despite its age, the artifact remains inert and mysterious.")
        return True
    else:
        print(f"You're not sure how to use the {item}.")
        return False

def get_available_items(world, location):
    """Get items available at a location. Initialize with starting_items if items not set."""
    location_data = world["locations"][location]
    
    # Initialize items list if it doesn't exist (for backward compatibility)
    if "items" not in location_data:
        location_data["items"] = location_data.get("starting_items", []).copy()
    
    return location_data["items"]

def add_item_to_world(world, location, item):
    """Add an item to a location in the world."""
    location_data = world["locations"][location]
    
    # Initialize items list if it doesn't exist
    if "items" not in location_data:
        location_data["items"] = location_data.get("starting_items", []).copy()
    
    if item not in location_data["items"]:
        location_data["items"].append(item)
        print(f"A {item} has been added to {location}.")
    else:
        print(f"There's already a {item} in {location}.")

def remove_item_from_world(world, location, item):
    """Remove an item from a location in the world."""
    location_data = world["locations"][location]
    
    # Initialize items list if it doesn't exist
    if "items" not in location_data:
        location_data["items"] = location_data.get("starting_items", []).copy()
    
    if item in location_data["items"]:
        location_data["items"].remove(item)
        return True
    return False

def transfer_item(player, world, item, from_inventory_to_world=True):
    current_location = world["current_location"]

    if from_inventory_to_world:
        if remove_item_from_inventory(player, item):
            add_item_to_world(world, current_location, item)
            return True
    else:
        if remove_item_from_world(world, current_location, item):
            add_item_to_inventory(player, item)
            return True

    return False
