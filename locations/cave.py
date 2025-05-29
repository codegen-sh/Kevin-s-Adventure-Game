from game.player import add_item_to_inventory, heal_player, damage_player
from game.state import update_world_state
from utils.random_events import generate_random_event
import random


def explore_cave(world, player):
    print("You enter the dark, mysterious cave. Water drips from stalactites above.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper")
        print("2. Search for treasures")
        print("3. Light a torch")
        print("4. Listen for sounds")
        print("5. Exit the cave")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            explore_deeper(world, player)
        elif choice == "2":
            search_for_treasures(world, player)
        elif choice == "3":
            light_torch(world, player)
        elif choice == "4":
            listen_for_sounds(world, player)
        elif choice == "5":
            print("You carefully make your way out of the cave.")
            break
        else:
            print("Invalid choice. Please try again.")


def explore_deeper(world, player):
    print("You venture deeper into the cave...")
    
    event = random.choice([
        "treasure", "danger", "nothing", "crystal"
    ])
    
    if event == "treasure":
        print("You discover a hidden chamber with ancient coins!")
        player["gold"] += random.randint(20, 50)
        print(f"You gained {player['gold'] - (player['gold'] - random.randint(20, 50))} gold!")
    elif event == "danger":
        print("You step on loose rocks and hurt yourself!")
        damage = random.randint(5, 15)
        damage_player(player, damage)
    elif event == "crystal":
        print("You find a glowing crystal!")
        add_item_to_inventory(player, "glowing crystal")
    else:
        print("You find nothing of interest in this part of the cave.")


def search_for_treasures(world, player):
    print("You carefully search the cave walls and floor...")
    
    if random.random() < 0.6:  # 60% chance of finding something
        treasures = ["gemstone", "ancient coin", "crystal shard", "cave pearl"]
        treasure = random.choice(treasures)
        add_item_to_inventory(player, treasure)
        print(f"You found a {treasure}!")
    else:
        print("You search thoroughly but find nothing valuable.")


def light_torch(world, player):
    if "torch" in player["inventory"]:
        print("You light your torch, illuminating the cave walls.")
        print("The light reveals beautiful mineral formations and ancient cave paintings!")
        
        # Chance to find hidden items with torch
        if random.random() < 0.4:
            add_item_to_inventory(player, "ancient artifact")
            print("The torch light reveals an ancient artifact hidden in a crevice!")
    else:
        print("You don't have a torch to light.")


def listen_for_sounds(world, player):
    print("You stand still and listen carefully...")
    
    sounds = [
        "You hear the distant sound of dripping water.",
        "An eerie echo bounces off the cave walls.",
        "You hear the flutter of bat wings in the darkness.",
        "A mysterious whisper seems to come from deep within the cave.",
        "The sound of your own breathing seems amplified in the silence."
    ]
    
    print(random.choice(sounds))
    
    # Small chance of discovering something by listening
    if random.random() < 0.2:
        print("Your careful listening helps you notice a hidden passage!")
        print("You find a small alcove with a healing potion!")
        add_item_to_inventory(player, "healing potion")

