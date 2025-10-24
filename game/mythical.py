"""
Module for handling mythical creatures and encounters in the game.
"""
import random

from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.text_formatting import print_event


def summon_mythical_creature(world, player, creature_type):
    """
    Summon a mythical creature for the player to encounter.
    
    Args:
        world (dict): The world state dictionary
        player (dict): The player's state
        creature_type (str): The type of mythical creature to summon
    """
    print_event(f"A mythical {creature_type} appears before you!")
    
    if creature_type == "unicorn":
        encounter_unicorn(world, player)
    elif creature_type == "dragon":
        encounter_dragon(world, player)
    elif creature_type == "phoenix":
        encounter_phoenix(world, player)
    elif creature_type == "griffin":
        encounter_griffin(world, player)
    elif creature_type == "troll":
        encounter_troll(world, player)
    else:
        print(f"The {creature_type} looks at you curiously before disappearing into the mist.")


def encounter_unicorn(world, player):
    """Handle an encounter with a unicorn."""
    print("A majestic unicorn with a gleaming white coat and a spiraling horn approaches you.")
    print("Its eyes seem to shine with ancient wisdom and kindness.")
    
    print("\nWhat would you like to do?")
    print("1. Approach gently")
    print("2. Offer food")
    print("3. Try to touch its horn")
    print("4. Back away slowly")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("You approach the unicorn gently, speaking in soft tones.")
        print("The unicorn seems to appreciate your respect and comes closer.")
        print("It touches its horn to your forehead, and you feel a wave of healing energy.")
        heal_player(player, 30)
        print("You feel completely refreshed and invigorated!")
    
    elif choice == "2":
        if "berries" in player["inventory"] or "apple" in player["inventory"]:
            food_item = "berries" if "berries" in player["inventory"] else "apple"
            print(f"You offer the {food_item} to the unicorn.")
            player["inventory"].remove(food_item)
            print("The unicorn accepts your offering and eats from your hand.")
            print("As a thank you, it leaves behind a shimmering hair from its mane.")
            add_item_to_inventory(player, "unicorn_hair")
            print("The unicorn hair seems to glow with magical energy.")
        else:
            print("You don't have any suitable food to offer the unicorn.")
            print("The unicorn looks at you expectantly before turning away.")
    
    elif choice == "3":
        print("You reach out to touch the unicorn's horn.")
        print("The unicorn backs away, clearly uncomfortable with your boldness.")
        print("It disappears into the forest, leaving you alone.")
    
    elif choice == "4":
        print("You decide to back away slowly, respecting the unicorn's space.")
        print("The unicorn nods as if in approval before turning and disappearing into the forest.")
    
    else:
        print("The unicorn watches you curiously as you hesitate.")
        print("After a moment, it turns and gallops away into the forest.")


def encounter_dragon(world, player):
    """Handle an encounter with a dragon."""
    print("A massive dragon with scales like burnished copper looms before you.")
    print("Smoke curls from its nostrils, and its eyes gleam with intelligence.")
    
    print("\nWhat would you like to do?")
    print("1. Stand your ground")
    print("2. Offer treasure")
    print("3. Try to flee")
    print("4. Attempt to communicate")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("You stand your ground, showing courage in the face of the dragon.")
        print("The dragon seems to respect your bravery, but also sees you as a challenge.")
        
        if "sword" in player["inventory"] and player.get("strength", 0) > 15:
            print("With your sword in hand and your proven strength, you present a formidable opponent.")
            print("The dragon acknowledges you as a worthy adversary and offers a deal:")
            print("It will grant you passage through its territory in exchange for a future favor.")
            update_world_state(world, "dragon_pact_made")
        else:
            print("While brave, you are clearly outmatched by the dragon's power.")
            print("The dragon breathes a warning blast of fire near you.")
            damage_player(player, 20)
            print("The dragon then flies away, leaving you singed but alive.")
    
    elif choice == "2":
        if player.get("gold", 0) >= 50 or "gemstone" in player["inventory"]:
            if "gemstone" in player["inventory"]:
                print("You offer the gemstone to the dragon.")
                player["inventory"].remove("gemstone")
            else:
                print("You offer 50 gold to the dragon.")
                player["gold"] -= 50
            
            print("The dragon's eyes gleam with interest as it accepts your offering.")
            print("In return, it plucks a scale from its hide and drops it at your feet.")
            add_item_to_inventory(player, "dragon_scale")
            print("The dragon scale is warm to the touch and seems incredibly durable.")
        else:
            print("You have nothing valuable enough to interest the dragon.")
            print("It snorts dismissively, sending a puff of smoke in your direction.")
    
    elif choice == "3":
        print("You turn and run as fast as you can!")
        escape_chance = random.randint(1, 100)
        
        if escape_chance > 70:  # 30% chance of escape
            print("You manage to find cover and hide until the dragon loses interest.")
        else:
            print("The dragon is much faster than you. It cuts off your escape route with a blast of fire.")
            damage_player(player, 25)
            print("The dragon seems amused by your attempt to flee.")
    
    elif choice == "4":
        print("You attempt to communicate with the dragon, showing respect and curiosity.")
        
        if player.get("intelligence", 0) > 12:
            print("Your words seem to intrigue the dragon. It responds in a deep, rumbling voice.")
            print("The dragon shares ancient knowledge with you, speaking of hidden treasures and forgotten magic.")
            print("You gain valuable insights about the world.")
            update_world_state(world, "dragon_knowledge_gained")
        else:
            print("The dragon seems unimpressed by your attempt at communication.")
            print("It regards you for a moment before flying away without further interaction.")
    
    else:
        print("As you hesitate, the dragon grows impatient.")
        print("With a mighty beat of its wings, it takes to the sky and disappears over the mountains.")


def encounter_phoenix(world, player):
    """Handle an encounter with a phoenix."""
    print("A bird of living flame perches on a nearby branch, its feathers shifting between red, orange, and gold.")
    print("This is a phoenix, a legendary creature of rebirth and renewal.")
    
    print("\nWhat would you like to do?")
    print("1. Observe quietly")
    print("2. Reach out to it")
    print("3. Sing or make music")
    print("4. Show it something from your inventory")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("You observe the phoenix quietly, admiring its beauty.")
        print("The phoenix seems to appreciate your respectful distance.")
        print("After a while, it shakes its plumage, and a small feather drifts down to you.")
        add_item_to_inventory(player, "phoenix_feather")
        print("The feather is warm to the touch and seems to pulse with inner light.")
    
    elif choice == "2":
        print("You slowly reach out toward the magnificent bird.")
        print("The phoenix regards your hand with curiosity.")
        
        if player.get("health", 0) < 50:
            print("Sensing your weakened state, the phoenix flies to your shoulder.")
            print("It brushes its wing against your cheek, and you feel a surge of rejuvenating warmth.")
            heal_player(player, 50)
            print("The phoenix has restored your vitality!")
        else:
            print("The phoenix allows you to gently stroke its feathers.")
            print("The experience fills you with a sense of peace and wonder.")
    
    elif choice == "3":
        print("You begin to sing softly or make music for the phoenix.")
        print("The phoenix tilts its head, listening to your performance.")
        
        if "flute" in player["inventory"] or player.get("charisma", 0) > 10:
            print("The phoenix seems enchanted by your music.")
            print("It joins in with a haunting, melodious cry that seems to resonate with your very soul.")
            print("The harmonious connection leaves you feeling spiritually renewed.")
            heal_player(player, 20)
            update_world_state(world, "phoenix_song_heard")
        else:
            print("The phoenix seems unimpressed by your musical attempt.")
            print("It ruffles its feathers and looks away.")
    
    elif choice == "4":
        print("You decide to show the phoenix something from your inventory.")
        
        if player["inventory"]:
            print("What would you like to show the phoenix?")
            for i, item in enumerate(player["inventory"], 1):
                print(f"{i}. {item}")
            
            try:
                item_choice = int(input(f"Enter your choice (1-{len(player['inventory'])}): "))
                if 1 <= item_choice <= len(player["inventory"]):
                    shown_item = player["inventory"][item_choice - 1]
                    
                    if shown_item in ["gemstone", "ancient_artifact", "magic_ring"]:
                        print(f"The phoenix shows great interest in your {shown_item}.")
                        print("It touches the item with its beak, and the item briefly glows with enhanced power.")
                        print(f"Your {shown_item} seems to have gained magical properties!")
                        # This could be implemented as an item upgrade system
                    else:
                        print(f"The phoenix glances at your {shown_item} but shows little interest.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")
        else:
            print("You have nothing in your inventory to show the phoenix.")
    
    else:
        print("The phoenix watches you for a moment longer before spreading its wings.")
        print("In a burst of flame, it takes to the sky and disappears into the clouds.")


def encounter_griffin(world, player):
    """Handle an encounter with a griffin."""
    print("A majestic griffin - half eagle, half lion - stands proudly before you.")
    print("Its eagle eyes watch you intently, assessing whether you are friend or foe.")
    
    print("\nWhat would you like to do?")
    print("1. Bow respectfully")
    print("2. Offer meat or food")
    print("3. Try to mount it")
    print("4. Shield yourself defensively")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("You bow respectfully to the noble creature.")
        print("The griffin seems pleased by your show of respect.")
        print("It bows its head in return, acknowledging you as a worthy individual.")
        print("The griffin allows you to approach and even pet its feathered neck.")
    
    elif choice == "2":
        if any(item in player["inventory"] for item in ["meat", "fish", "bread"]):
            food_items = [item for item in player["inventory"] if item in ["meat", "fish", "bread"]]
            food_item = food_items[0]
            
            print(f"You offer the {food_item} to the griffin.")
            player["inventory"].remove(food_item)
            
            print("The griffin accepts your offering, carefully taking the food from your hand.")
            print("After eating, the griffin plucks a feather from its wing and drops it at your feet.")
            add_item_to_inventory(player, "griffin_feather")
            print("The griffin feather might be useful for crafting or trading.")
        else:
            print("You don't have any suitable food to offer the griffin.")
            print("The griffin looks disappointed and turns away.")
    
    elif choice == "3":
        print("You attempt to mount the griffin, hoping it might carry you through the skies.")
        
        if player.get("dexterity", 0) > 15 and player.get("charisma", 0) > 12:
            print("Surprisingly, the griffin allows you to climb onto its back!")
            print("With a powerful leap, it takes to the air with you holding on tightly.")
            print("The griffin gives you an exhilarating flight over the landscape.")
            print("From this vantage point, you notice several landmarks you hadn't seen before.")
            update_world_state(world, "griffin_flight_taken")
        else:
            print("The griffin is not pleased by your presumptuous attempt.")
            print("It screeches in protest and swipes at you with its talons.")
            damage_player(player, 15)
            print("The griffin backs away, eyeing you warily.")
    
    elif choice == "4":
        print("You take a defensive stance, unsure of the griffin's intentions.")
        print("The griffin seems to interpret your caution as fear or hostility.")
        print("It spreads its wings and screeches, creating an intimidating display.")
        print("After a tense moment, the griffin turns and bounds away, occasionally glancing back at you.")
    
    else:
        print("The griffin grows impatient with your indecision.")
        print("With a powerful leap, it takes to the sky and circles once overhead before flying away.")


def encounter_troll(world, player):
    """Handle an encounter with a troll."""
    print("A large, ugly troll blocks your path. Its skin is gray and warty, and it carries a crude club.")
    print("The troll grins, revealing yellowed teeth, and speaks in a gravelly voice:")
    print("\"Pay toll or face troll!\"")
    
    print("\nWhat would you like to do?")
    print("1. Pay the toll")
    print("2. Try to reason with the troll")
    print("3. Attempt to fight")
    print("4. Try to sneak past")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("You decide to pay the troll's toll.")
        
        if player.get("gold", 0) >= 20:
            print("You offer 20 gold to the troll.")
            player["gold"] -= 20
            print("The troll greedily snatches the gold and steps aside.")
            print("\"Good human. You pass.\"")
        else:
            print("You don't have enough gold to satisfy the troll.")
            print("The troll growls angrily and swings its club at you.")
            damage_player(player, 20)
            print("\"Next time bring gold!\" the troll shouts as you retreat.")
    
    elif choice == "2":
        print("You attempt to reason with the troll, suggesting an alternative arrangement.")
        
        if player.get("charisma", 0) > 12:
            print("Your diplomatic approach seems to confuse the troll, but in a good way.")
            print("\"Human talk good. Troll like smart human. You pass this time.\"")
            print("The troll steps aside, allowing you to pass without paying.")
        else:
            print("The troll doesn't seem impressed by your attempt at diplomacy.")
            print("\"Talk boring. Pay or pain!\"")
            print("The troll swings its club threateningly.")
            damage_player(player, 15)
    
    elif choice == "3":
        print("You decide to stand up to the troll and fight!")
        
        if "sword" in player["inventory"] and player.get("strength", 0) > 12:
            print("You draw your sword and prepare for battle.")
            print("The troll seems surprised by your readiness to fight.")
            print("After a fierce battle, you manage to drive the troll away.")
            print("The troll drops something as it flees.")
            add_item_to_inventory(player, "troll_tooth")
            damage_player(player, 10)  # You still take some damage in the fight
        else:
            print("You're not well-equipped to fight a troll.")
            print("The troll laughs at your attempt and easily overpowers you.")
            damage_player(player, 30)
            print("The troll lets you go, but takes some of your possessions as payment.")
            if player["inventory"]:
                lost_item = random.choice(player["inventory"])
                player["inventory"].remove(lost_item)
                print(f"You lost your {lost_item}!")
    
    elif choice == "4":
        print("You try to sneak past the troll while it's distracted.")
        
        if player.get("dexterity", 0) > 15:
            print("With careful movements, you manage to slip past the troll unnoticed.")
            print("You successfully avoid paying the toll!")
        else:
            print("The troll spots you trying to sneak by!")
            print("\"Sneaky human pay DOUBLE!\" it roars.")
            print("The troll swings its club, catching you off guard.")
            damage_player(player, 25)
    
    else:
        print("While you hesitate, the troll grows impatient.")
        print("\"Human too slow! Troll angry now!\"")
        print("The troll charges at you, forcing you to retreat hastily.")

