import random
from game.player import add_to_inventory, heal_player, take_damage
from utils.text_formatting import print_event

def explore_cave(world, player):
    """Handle player interactions with the cave location."""
    print("You explore the dark, damp cave...")
    
    # Random events in the cave
    event_roll = random.randint(1, 10)
    
    if event_roll == 1:
        # Find a treasure
        print_event("You discover a hidden treasure chest tucked away in a corner of the cave!")
        treasure_items = ["gold coin", "ruby", "ancient amulet", "silver dagger"]
        found_item = random.choice(treasure_items)
        add_to_inventory(player, found_item)
        print(f"You found a {found_item} and added it to your inventory.")
    
    elif event_roll == 2:
        # Encounter a bat swarm
        print_event("A swarm of bats suddenly descends upon you, their wings flapping chaotically!")
        damage = random.randint(5, 15)
        take_damage(player, damage)
        print(f"The bats scratch and bite you, causing {damage} damage.")
    
    elif event_roll == 3:
        # Find healing crystals
        print_event("You notice some glowing crystals embedded in the cave wall. They emit a soothing light.")
        heal_amount = random.randint(10, 20)
        heal_player(player, heal_amount)
        print(f"The crystal's energy heals you for {heal_amount} health.")
    
    elif event_roll == 4:
        # Cave-in threat
        print_event("You hear a rumbling sound from above. Small rocks begin to fall from the ceiling!")
        print("You quickly move to a safer part of the cave.")
        
        # 50% chance of taking damage
        if random.random() < 0.5:
            damage = random.randint(5, 10)
            take_damage(player, damage)
            print(f"You couldn't avoid all the falling debris. You take {damage} damage.")
    
    elif event_roll == 5:
        # Find an underground stream
        print_event("You discover a clear underground stream flowing through the cave.")
        print("The water looks pure and refreshing.")
        
        # Add water to inventory if player doesn't have it
        if "water flask" not in player.get("inventory", []):
            print("You fill your flask with the crystal-clear water.")
            add_to_inventory(player, "water flask")
        else:
            print("You refill your water flask.")
    
    elif event_roll == 6:
        # Find ancient cave paintings
        print_event("You discover ancient cave paintings depicting strange creatures and symbols.")
        print("As you study them, you feel a sense of ancient knowledge washing over you.")
        
        # Add a clue to the player's knowledge
        if "cave_paintings_seen" not in player:
            player["cave_paintings_seen"] = True
            print("You've learned something about this world's history.")
    
    elif event_roll == 7:
        # Encounter a sleeping creature
        print_event("You come across a large, sleeping creature deeper in the cave.")
        print("It's breathing heavily, and you can see a valuable-looking item near it.")
        
        choice = input("Do you want to try to take the item? (y/n): ").lower()
        if choice == 'y':
            # Risk-reward scenario
            if random.random() < 0.3:  # 30% chance of waking the creature
                print("The creature stirs and wakes up! It roars in anger!")
                damage = random.randint(15, 25)
                take_damage(player, damage)
                print(f"The creature attacks you before you can escape! You take {damage} damage.")
            else:
                valuable_items = ["jeweled crown", "enchanted stone", "golden figurine"]
                found_item = random.choice(valuable_items)
                add_to_inventory(player, found_item)
                print(f"You carefully take the {found_item} without waking the creature.")
        else:
            print("You decide it's safer to leave the creature undisturbed.")
    
    elif event_roll == 8:
        # Find a mysterious altar
        print_event("You discover a mysterious stone altar in a chamber of the cave.")
        print("Strange symbols are carved into its surface, and it seems to hum with energy.")
        
        if player.get("inventory", []):
            print("You feel like you could place an item on the altar...")
            choice = input("Do you want to place an item on the altar? (y/n): ").lower()
            if choice == 'y':
                inventory = player.get("inventory", [])
                for i, item in enumerate(inventory, 1):
                    print(f"{i}. {item}")
                
                try:
                    item_choice = int(input("Which item? (number): ")) - 1
                    if 0 <= item_choice < len(inventory):
                        chosen_item = inventory[item_choice]
                        player["inventory"].remove(chosen_item)
                        
                        # Random effect based on the item
                        effect_roll = random.randint(1, 3)
                        if effect_roll == 1:
                            # Beneficial effect
                            heal_amount = random.randint(20, 30)
                            heal_player(player, heal_amount)
                            print(f"The altar glows with a warm light. You feel rejuvenated! (+{heal_amount} health)")
                        elif effect_roll == 2:
                            # Harmful effect
                            damage = random.randint(10, 20)
                            take_damage(player, damage)
                            print(f"The altar emits a pulse of dark energy! You feel weakened. (-{damage} health)")
                        else:
                            # Item transformation
                            magical_items = ["enchanted amulet", "glowing crystal", "magical ring"]
                            new_item = random.choice(magical_items)
                            add_to_inventory(player, new_item)
                            print(f"The {chosen_item} transforms into a {new_item}!")
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input.")
            else:
                print("You decide not to risk it.")
        else:
            print("You have nothing in your inventory to place on the altar.")
    
    elif event_roll == 9:
        # Find a narrow passage
        print_event("You discover a narrow passage that seems to lead deeper into the mountain.")
        print("It's too dark to see what lies beyond without a light source.")
        
        if "torch" in player.get("inventory", []):
            print("You use your torch to light the way and explore the passage.")
            
            # Secret area discovery
            secret_roll = random.randint(1, 3)
            if secret_roll == 1:
                print("The passage leads to a small chamber with a chest!")
                valuable_items = ["diamond", "ancient scroll", "magical staff"]
                found_item = random.choice(valuable_items)
                add_to_inventory(player, found_item)
                print(f"Inside the chest, you find a {found_item}!")
            elif secret_roll == 2:
                print("The passage leads to an underground lake with crystal-clear water.")
                heal_amount = random.randint(15, 25)
                heal_player(player, heal_amount)
                print(f"You take a drink from the lake and feel refreshed. (+{heal_amount} health)")
            else:
                print("The passage eventually loops back to where you started.")
        else:
            print("Without a light source, you decide it's too dangerous to proceed.")
    
    else:
        # Nothing special happens
        print("You explore the cave but find nothing of interest this time.")
    
    # Return to the main game loop
    return
