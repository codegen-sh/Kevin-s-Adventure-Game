"""
Cave location for Kevin's Adventure Game.
"""

def explore_cave(world, player):
    """Explore the cave location."""
    print("You explore the dark, mysterious cave...")
    print("You hear the echo of dripping water and see glittering minerals on the walls.")
    
    # Simple cave exploration logic
    current_location = world["current_location"]
    if current_location == "Cave":
        available_items = world["locations"]["Cave"]["items"]
        if available_items:
            print(f"You see: {', '.join(available_items)}")
            
            # Simple item pickup
            action = input("Do you want to pick up an item? (y/n): ").lower()
            if action == 'y' and available_items:
                item = available_items.pop(0)
                player["inventory"].append(item)
                print(f"You picked up: {item}")
        else:
            print("The cave appears to be empty of useful items.")
    else:
        print("You are not in the cave!")

