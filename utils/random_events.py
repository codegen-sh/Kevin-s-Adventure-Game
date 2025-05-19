import random

from game.player import add_gold, add_item_to_inventory, damage_player, heal_player, spend_gold
from game.world import track_event

# from game.world import update_world_state
from utils.text_formatting import print_event


def generate_random_event(events):
    """Generate a random event based on probabilities."""
    return random.choices([event[0] for event in events], weights=[event[1] for event in events])[0]

def handle_random_encounter(player, world):
    """Handle a random encounter event. Handled alongside functions like find_treasure(), weather_event(), trap_event(), and special_discovery()"""
    encounters = [
        "friendly_traveler",
        "merchant",
        "lost_child",
        "wild_animal",
        "bandit"
    ]
    encounter = random.choice(encounters)
    
    # Track the encounter event
    track_event(world, "encounter", {"type": encounter})

    if encounter == "friendly_traveler":
        print_event("You meet a friendly traveler who shares some of their supplies with you.")
        heal_player(player, 10)
    elif encounter == "merchant":
        print_event("A wandering merchant offers to sell you a mysterious potion.")
        if player.get("gold", 0) >= 20:
            choice = input("Do you want to buy the potion for 20 gold? (y/n): ").lower()
            if choice == 'y':
                if spend_gold(player, 20, world):
                    add_item_to_inventory(player, "mysterious_potion", world)
                    print("You bought the mysterious potion.")
            else:
                print("You decline the offer.")
        else:
            print("You don't have enough gold to buy the potion.")
    elif encounter == "lost_child":
        print_event("You find a lost child. After helping them return to their village, the grateful parents reward you.")
        add_gold(player, 15, world)
    elif encounter == "wild_animal":
        print_event("A wild animal attacks you!")
        damage_player(player, 15)
    elif encounter == "bandit":
        print_event("A bandit tries to rob you!")
        if "sword" in player["inventory"]:
            print("You use your sword to fend off the bandit.")
        elif player.get("gold", 0) > 0:
            stolen_gold = min(player["gold"], 10)
            spend_gold(player, stolen_gold, world)
            print(f"The bandit steals {stolen_gold} gold from you.")
        else:
            print("The bandit finds nothing of value and leaves you alone.")

def find_treasure(player, world):
    """Handle finding a treasure."""
    treasures = [
        ("gold_coin", 5),
        ("silver_necklace", 10),
        ("ancient_artifact", 20),
        ("magic_ring", 30)
    ]
    treasure, value = random.choice(treasures)
    
    # Track the treasure event
    track_event(world, "treasure", {"item": treasure, "value": value})
    
    print_event(f"You found a {treasure} worth {value} gold!")
    add_item_to_inventory(player, treasure, world)
    add_gold(player, value, world)

def weather_event(world):
    """Handle a weather change event."""
    weathers = ["sunny", "rainy", "windy", "foggy", "stormy"]
    new_weather = random.choice(weathers)
    
    # Track the weather event
    track_event(world, "weather", {"type": new_weather})
    
    print_event(f"The weather changes to {new_weather}.")
    # update_world_state(world, f"weather_{new_weather}")
    # TODO: Implement weather system
    # change_weather(world, new_weather)

def trap_event(player, world):
    """Handle a trap event."""
    traps = ["pitfall", "snare", "poison_dart"]
    trap = random.choice(traps)
    
    # Track the trap event
    track_event(world, "trap", {"type": trap})
    
    print_event(f"You've triggered a {trap} trap!")
    damage = random.randint(5, 15)
    damage_player(player, damage)

def special_discovery(player, world):
    """Handle a special discovery event."""
    discoveries = [
        "hidden_cave",
        "ancient_ruins",
        "magical_spring",
        "abandoned_camp"
    ]
    discovery = random.choice(discoveries)
    
    # Track the discovery event
    track_event(world, "discovery", {"type": discovery})
    
    print_event(f"You've discovered a {discovery.replace('_', ' ')}!")

    if discovery == "hidden_cave":
        # update_world_state(world, "add_hidden_cave")
        print("You mark the location of the hidden cave on your map.")
    elif discovery == "ancient_ruins":
        add_item_to_inventory(player, "ancient_artifact", world)
        print("You find an ancient artifact among the ruins.")
    elif discovery == "magical_spring":
        heal_player(player, 30)
        print("You drink from the magical spring and feel rejuvenated.")
    elif discovery == "abandoned_camp":
        items = ["rope", "torch", "map"]
        found_item = random.choice(items)
        add_item_to_inventory(player, found_item, world)
        print(f"You search the abandoned camp and find a {found_item}.")

def apply_random_event(player, world):
    """Apply a random event to the game state."""
    event = generate_random_event(events=[("nothing", 20), ("find_item", 20), ("encounter", 20), ("weather_change", 10), ("trap", 10), ("special_discovery", 20)])

    if event == "nothing":
        return  # No event occurs
    elif event == "find_item":
        find_treasure(player, world)
    elif event == "encounter":
        handle_random_encounter(player, world)
    elif event == "weather_change":
        weather_event(world)
    elif event == "trap":
        trap_event(player, world)
    elif event == "special_discovery":
        special_discovery(player, world)
