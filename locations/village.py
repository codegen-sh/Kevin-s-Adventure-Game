from game.player import add_item_to_inventory, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event
from utils.text_formatting import print_event


def visit_village(world, player):
    """
    Handle player interaction with the village location.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    """
    print_event("You enter the small village. Thatched-roof houses line the dirt streets, and villagers go about their daily business.")
    
    while True:
        print("\nWhat would you like to do in the village?")
        print("1. Visit the market")
        print("2. Talk to villagers")
        print("3. Visit the inn")
        print("4. Visit the blacksmith")
        print("5. Leave the village")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            visit_market(world, player)
        elif choice == "2":
            talk_to_villagers(world, player)
        elif choice == "3":
            visit_inn(world, player)
        elif choice == "4":
            visit_blacksmith(world, player)
        elif choice == "5":
            print("You decide to leave the village.")
            break
        else:
            print("Invalid choice. Please try again.")


def visit_market(world, player):
    """Visit the village market to buy and sell items."""
    print("You walk through the bustling village market. Vendors call out, advertising their wares.")
    
    while True:
        print("\nMarket Options:")
        print("1. Buy items")
        print("2. Sell items")
        print("3. Browse special goods")
        print("4. Leave the market")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            buy_items(player)
        elif choice == "2":
            sell_items(player)
        elif choice == "3":
            browse_special_goods(world, player)
        elif choice == "4":
            print("You leave the market.")
            break
        else:
            print("Invalid choice. Please try again.")


def buy_items(player):
    """Buy items from the market."""
    items_for_sale = {
        "bread": 5,
        "torch": 8,
        "rope": 12,
        "healing_potion": 25,
        "map": 15
    }
    
    print(f"You have {player['gold']} gold.")
    print("\nItems for sale:")
    for item, price in items_for_sale.items():
        print(f"{item}: {price} gold")
    
    item = input("\nWhat would you like to buy? (or 'cancel'): ").lower()
    
    if item == "cancel":
        return
    
    if item in items_for_sale:
        price = items_for_sale[item]
        if player["gold"] >= price:
            player["gold"] -= price
            add_item_to_inventory(player, item)
            print(f"You bought a {item} for {price} gold.")
        else:
            print("You don't have enough gold for that item.")
    else:
        print("That item is not for sale.")


def sell_items(player):
    """Sell items to the market."""
    if not player["inventory"]:
        print("You don't have any items to sell.")
        return
    
    # Item values (what the merchant will pay)
    item_values = {
        "bread": 2,
        "torch": 4,
        "rope": 6,
        "healing_potion": 15,
        "map": 8,
        "gemstone": 30,
        "berries": 3,
        "mushrooms": 3,
        "stick": 1
    }
    
    print("Your inventory:")
    for i, item in enumerate(player["inventory"], 1):
        value = item_values.get(item, 1)  # Default value of 1 gold
        print(f"{i}. {item}: worth {value} gold")
    
    try:
        choice = int(input("\nWhich item would you like to sell? (number, or 0 to cancel): "))
        if choice == 0:
            return
        
        if 1 <= choice <= len(player["inventory"]):
            item = player["inventory"][choice - 1]
            value = item_values.get(item, 1)
            
            player["inventory"].remove(item)
            player["gold"] += value
            print(f"You sold the {item} for {value} gold.")
            print(f"You now have {player['gold']} gold.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a number.")


def browse_special_goods(world, player):
    """Browse special or rare items at the market."""
    special_items = {
        "magic_ring": 100,
        "silver_dagger": 50,
        "ancient_map": 75
    }
    
    # Check if there's a special event or festival
    if "village_festival" in world.get("state", {}).get("special_events", []):
        print("The village is celebrating a festival! Special discounts are available.")
        special_items = {item: int(price * 0.8) for item, price in special_items.items()}
    
    print(f"You have {player['gold']} gold.")
    print("\nSpecial items available:")
    for item, price in special_items.items():
        print(f"{item}: {price} gold")
    
    item = input("\nWhat would you like to buy? (or 'cancel'): ").lower()
    
    if item == "cancel":
        return
    
    if item in special_items:
        price = special_items[item]
        if player["gold"] >= price:
            confirm = input(f"Are you sure you want to buy {item} for {price} gold? (y/n): ").lower()
            if confirm == "y":
                player["gold"] -= price
                add_item_to_inventory(player, item)
                print(f"You bought a {item} for {price} gold.")
        else:
            print("You don't have enough gold for that item.")
    else:
        print("That item is not available.")


def talk_to_villagers(world, player):
    """Talk to villagers to get information and quests."""
    print("You approach some of the villagers to strike up a conversation.")
    
    villagers = [
        "elderly_farmer",
        "young_child",
        "village_elder",
        "traveling_merchant",
        "local_guard"
    ]
    
    villager = villagers[generate_random_event(events=[(i, 1) for i in range(len(villagers))])]
    
    if villager == "elderly_farmer":
        print("An elderly farmer tells you about strange noises coming from the cave at night.")
        print("\"Be careful if you go there,\" he warns. \"Some say there's treasure, but others never return.\"")
        # Mark the cave as a point of interest
        update_world_state(world, "cave_rumor_heard")
    
    elif villager == "young_child":
        print("A young child excitedly tells you about seeing a unicorn in the forest clearing.")
        print("\"It was beautiful and white with a shiny horn! No one believes me though.\"")
        # This could unlock a special encounter
        update_world_state(world, "unicorn_rumor_heard")
    
    elif villager == "village_elder":
        print("The village elder shares ancient legends about the mountain.")
        print("\"They say a dragon once lived there, guarding a hoard of treasure.\"")
        print("\"Some believe the dragon still sleeps deep within the mountain.\"")
        # This could unlock a special encounter
        update_world_state(world, "dragon_rumor_heard")
    
    elif villager == "traveling_merchant":
        print("A traveling merchant tells you about valuable gemstones in the mountain caves.")
        print("\"If you find any, I'll pay good gold for them,\" he offers.")
        # This could unlock a special trading option
        update_world_state(world, "gemstone_trade_available")
    
    elif villager == "local_guard":
        print("A local guard warns you about bandits in the forest.")
        print("\"Travel carefully and keep your valuables hidden,\" he advises.")
        # This could increase the chance of bandit encounters
        update_world_state(world, "bandit_warning_received")


def visit_inn(world, player):
    """Visit the village inn to rest and gather information."""
    print("You enter the cozy village inn. A fire crackles in the hearth, and a few patrons enjoy food and drink.")
    
    while True:
        print("\nInn Options:")
        print("1. Rest and recover (10 gold)")
        print("2. Buy a meal (5 gold)")
        print("3. Listen to rumors")
        print("4. Leave the inn")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            if player["gold"] >= 10:
                player["gold"] -= 10
                heal_player(player, 50)
                print("You rent a room and get a good night's rest.")
                print("You feel completely refreshed!")
                # Chance for a random event after resting
                if generate_random_event(events=[("dream", 30), (None, 70)]) == "dream":
                    print("During the night, you have a strange dream that seems to reveal something important...")
                    # This could provide a hint or unlock a special event
                    update_world_state(world, "prophetic_dream_received")
            else:
                print("You don't have enough gold to rent a room.")
        
        elif choice == "2":
            if player["gold"] >= 5:
                player["gold"] -= 5
                heal_player(player, 20)
                print("You enjoy a hearty meal of stew, bread, and ale.")
                print("The food restores some of your health.")
            else:
                print("You don't have enough gold to buy a meal.")
        
        elif choice == "3":
            print("You sit at the bar, listening to conversations around you.")
            rumors = [
                "I heard there's a hidden treasure in the old cave.",
                "They say the forest is haunted by spirits at night.",
                "A merchant lost a valuable cargo on the mountain path last week.",
                "The blacksmith is looking for rare metals to forge special weapons.",
                "Strange lights have been seen in the sky over the mountain recently."
            ]
            rumor = rumors[generate_random_event(events=[(i, 1) for i in range(len(rumors))])]
            print(f"You overhear: \"{rumor}\"")
            # This could unlock special events or locations
            update_world_state(world, f"rumor_heard_{rumors.index(rumor)}")
        
        elif choice == "4":
            print("You leave the inn.")
            break
        
        else:
            print("Invalid choice. Please try again.")


def visit_blacksmith(world, player):
    """Visit the village blacksmith to buy weapons and armor."""
    print("You enter the blacksmith's forge. The heat is intense, and the sound of hammering fills the air.")
    
    while True:
        print("\nBlacksmith Options:")
        print("1. Buy weapons")
        print("2. Buy armor")
        print("3. Repair equipment")
        print("4. Commission special item")
        print("5. Leave the blacksmith")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            weapons = {
                "sword": 50,
                "dagger": 25,
                "bow": 40,
                "arrows (10)": 15
            }
            
            print(f"You have {player['gold']} gold.")
            print("\nWeapons for sale:")
            for weapon, price in weapons.items():
                print(f"{weapon}: {price} gold")
            
            weapon = input("\nWhat would you like to buy? (or 'cancel'): ").lower()
            
            if weapon == "cancel":
                continue
            
            if weapon in weapons:
                price = weapons[weapon]
                if player["gold"] >= price:
                    player["gold"] -= price
                    if weapon == "arrows (10)":
                        add_item_to_inventory(player, "arrows")
                        print("You bought 10 arrows.")
                    else:
                        add_item_to_inventory(player, weapon)
                        print(f"You bought a {weapon} for {price} gold.")
                else:
                    print("You don't have enough gold for that weapon.")
            else:
                print("That weapon is not available.")
        
        elif choice == "2":
            armor = {
                "leather_armor": 40,
                "shield": 30,
                "helmet": 35
            }
            
            print(f"You have {player['gold']} gold.")
            print("\nArmor for sale:")
            for item, price in armor.items():
                print(f"{item}: {price} gold")
            
            item = input("\nWhat would you like to buy? (or 'cancel'): ").lower()
            
            if item == "cancel":
                continue
            
            if item in armor:
                price = armor[item]
                if player["gold"] >= price:
                    player["gold"] -= price
                    add_item_to_inventory(player, item)
                    print(f"You bought {item} for {price} gold.")
                else:
                    print("You don't have enough gold for that armor.")
            else:
                print("That armor is not available.")
        
        elif choice == "3":
            print("The blacksmith offers to repair your damaged equipment.")
            print("However, you don't have any damaged equipment that needs repair.")
            # This could be implemented with an equipment durability system
        
        elif choice == "4":
            print("The blacksmith can create special items if you bring the right materials.")
            
            special_items = {
                "fire_sword": ["sword", "dragon_scale", 100],
                "reinforced_shield": ["shield", "iron_ore", 75],
                "enchanted_dagger": ["dagger", "magic_crystal", 80]
            }
            
            print("\nPossible commissions:")
            for item, requirements in special_items.items():
                base_item, material, gold = requirements
                print(f"{item}: Requires {base_item}, {material}, and {gold} gold")
            
            item = input("\nWhat would you like to commission? (or 'cancel'): ").lower()
            
            if item == "cancel":
                continue
            
            if item in special_items:
                base_item, material, gold = special_items[item]
                
                has_base = base_item in player["inventory"]
                has_material = material in player["inventory"]
                has_gold = player["gold"] >= gold
                
                if has_base and has_material and has_gold:
                    player["inventory"].remove(base_item)
                    player["inventory"].remove(material)
                    player["gold"] -= gold
                    add_item_to_inventory(player, item)
                    print(f"The blacksmith takes your {base_item}, {material}, and {gold} gold.")
                    print(f"After some time working at the forge, he presents you with a {item}!")
                else:
                    print("You don't have the required items or gold for this commission.")
                    if not has_base:
                        print(f"Missing: {base_item}")
                    if not has_material:
                        print(f"Missing: {material}")
                    if not has_gold:
                        print(f"Missing: {gold - player['gold']} more gold")
            else:
                print("That item is not available for commission.")
        
        elif choice == "5":
            print("You leave the blacksmith's forge.")
            break
        
        else:
            print("Invalid choice. Please try again.")

