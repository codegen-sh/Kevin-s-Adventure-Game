import random

from game.player import add_item_to_inventory, damage_player, heal_player
from utils.text_formatting import print_event, print_info


def trigger_random_event(player, world):
    """
    Trigger a random event with a certain probability.
    
    Args:
        player (dict): The player's state
        world (dict): The game world state
    
    Returns:
        bool: True if an event was triggered, False otherwise
    """
    # 10% chance of a random event occurring after each action
    if random.random() < 0.10:
        apply_random_event(player, world)
        return True
    return False


def generate_random_event(events):
    """
    Generate a random event based on probabilities.
    
    Args:
        events (list): List of tuples containing (event_name, probability_weight)
    
    Returns:
        str: The selected event name
    """
    return random.choices(
        [event[0] for event in events], 
        weights=[event[1] for event in events]
    )[0]


def handle_random_encounter(player, world):
    """
    Handle a random encounter event.
    
    Args:
        player (dict): The player's state
        world (dict): The game world state
    """
    encounters = [
        ("friendly_traveler", 25),
        ("merchant", 20),
        ("lost_child", 15),
        ("wild_animal", 20),
        ("bandit", 20)
    ]
    
    encounter = generate_random_event(encounters)

    if encounter == "friendly_traveler":
        print_event("You meet a friendly traveler who shares some of their supplies with you.")
        heal_player(player, 10)
    elif encounter == "merchant":
        print_event("A wandering merchant offers to sell you a mysterious potion.")
        if player.get("gold", 0) >= 20:
            choice = input("Do you want to buy the potion for 20 gold? (y/n): ").lower()
            if choice == 'y':
                player["gold"] -= 20
                add_item_to_inventory(player, "mysterious_potion")
                print_info("You bought the mysterious potion.")
            else:
                print_info("You decline the offer.")
        else:
            print_info("You don't have enough gold to buy the potion.")
    elif encounter == "lost_child":
        print_event("You find a lost child. After helping them return to their village, the grateful parents reward you.")
        player["gold"] = player.get("gold", 0) + 15
    elif encounter == "wild_animal":
        print_event("A wild animal attacks you!")
        damage_player(player, random.randint(10, 20))
    elif encounter == "bandit":
        print_event("A bandit tries to rob you!")
        if "sword" in player["inventory"]:
            print_info("You use your sword to fend off the bandit.")
        elif player.get("gold", 0) > 0:
            stolen_gold = min(player["gold"], random.randint(5, 15))
            player["gold"] -= stolen_gold
            print_info(f"The bandit steals {stolen_gold} gold from you.")
        else:
            print_info("The bandit finds nothing of value and leaves you alone.")


def find_treasure(player):
    """
    Handle finding a treasure.
    
    Args:
        player (dict): The player's state
    """
    treasures = [
        ("gold_coins", 5, 30),
        ("silver_necklace", 10, 20),
        ("ancient_artifact", 20, 10),
        ("magic_ring", 30, 5)
    ]
    
    # Select treasure based on rarity weights
    treasure, value, weight = random.choices(treasures, weights=[t[2] for t in treasures])[0]
    
    print_event(f"You found a {treasure.replace('_', ' ')} worth {value} gold!")
    add_item_to_inventory(player, treasure)
    player["gold"] = player.get("gold", 0) + value


def weather_event(world):
    """
    Handle a weather change event.
    
    Args:
        world (dict): The game world state
    """
    weathers = [
        ("sunny", "The clouds clear and the sun shines brightly."),
        ("rainy", "Dark clouds gather and it starts to rain."),
        ("windy", "A strong wind picks up, rustling the trees."),
        ("foggy", "A thick fog rolls in, reducing visibility."),
        ("stormy", "Thunder rumbles as a storm approaches.")
    ]
    
    new_weather, description = random.choice(weathers)
    print_event(description)
    
    # Store the current weather in the world state
    world["weather"] = new_weather
    
    # Weather effects could be implemented here
    if new_weather == "rainy":
        print_info("The rain makes the ground slippery and harder to traverse.")
    elif new_weather == "foggy":
        print_info("The fog makes it difficult to see far ahead.")
    elif new_weather == "stormy":
        print_info("The storm makes travel dangerous. Be careful!")


def trap_event(player):
    """
    Handle a trap event.
    
    Args:
        player (dict): The player's state
    """
    traps = [
        ("pitfall", "You fall into a hidden pit!", 10, 20),
        ("snare", "A rope snare catches your leg!", 5, 10),
        ("poison_dart", "A poison dart shoots out from the wall!", 15, 25),
        ("falling_rocks", "Rocks fall from above!", 10, 15)
    ]
    
    trap, description, min_damage, max_damage = random.choice(traps)
    print_event(description)
    
    # Check if player has items that can help avoid or reduce trap damage
    damage_reduction = 0
    if trap == "pitfall" and "rope" in player["inventory"]:
        print_info("Your rope helps you climb out safely, reducing damage.")
        damage_reduction = 5
    elif trap == "poison_dart" and "antidote" in player["inventory"]:
        print_info("Your antidote counteracts the poison, reducing damage.")
        damage_reduction = 10
    
    damage = random.randint(min_damage, max_damage) - damage_reduction
    damage = max(0, damage)  # Ensure damage isn't negative
    
    if damage > 0:
        damage_player(player, damage)
    else:
        print_info("You managed to avoid taking any damage!")


def special_discovery(player, world):
    """
    Handle a special discovery event.
    
    Args:
        player (dict): The player's state
        world (dict): The game world state
    """
    discoveries = [
        "hidden_cave",
        "ancient_ruins",
        "magical_spring",
        "abandoned_camp",
        "mysterious_shrine"
    ]
    discovery = random.choice(discoveries)
    print_event(f"You've discovered a {discovery.replace('_', ' ')}!")

    if discovery == "hidden_cave":
        print_info("You mark the location of the hidden cave on your map.")
        # Add the hidden cave as a special location if not already discovered
        if "special_locations" not in world:
            world["special_locations"] = []
        if "hidden_cave" not in world["special_locations"]:
            world["special_locations"].append("hidden_cave")
    
    elif discovery == "ancient_ruins":
        add_item_to_inventory(player, "ancient_artifact")
        print_info("You find an ancient artifact among the ruins.")
    
    elif discovery == "magical_spring":
        heal_player(player, 30)
        print_info("You drink from the magical spring and feel rejuvenated.")
    
    elif discovery == "abandoned_camp":
        items = ["rope", "torch", "map", "bread", "healing_potion"]
        found_item = random.choice(items)
        add_item_to_inventory(player, found_item)
        print_info(f"You search the abandoned camp and find a {found_item.replace('_', ' ')}.")
    
    elif discovery == "mysterious_shrine":
        print_info("You feel a strange energy emanating from the shrine.")
        if random.random() < 0.5:
            print_info("The shrine bestows a blessing upon you.")
            heal_player(player, 20)
            player["gold"] += 10
        else:
            print_info("The shrine's energy feels ominous. You decide to leave it alone.")


def apply_random_event(player, world):
    """
    Apply a random event to the game state.
    
    Args:
        player (dict): The player's state
        world (dict): The game world state
    """
    events = [
        ("nothing", 20),       # No event
        ("find_item", 20),     # Find a treasure
        ("encounter", 20),     # Random encounter
        ("weather_change", 10), # Weather changes
        ("trap", 10),          # Trigger a trap
        ("special_discovery", 20) # Special discovery
    ]
    
    event = generate_random_event(events)

    if event == "nothing":
        return  # No event occurs
    elif event == "find_item":
        find_treasure(player)
    elif event == "encounter":
        handle_random_encounter(player, world)
    elif event == "weather_change":
        weather_event(world)
    elif event == "trap":
        trap_event(player)
    elif event == "special_discovery":
        special_discovery(player, world)
