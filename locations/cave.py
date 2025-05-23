from game.mythical import summon_mythical_creature
from game.player import add_item_to_inventory, heal_player, damage_player
from game.state import update_world_state
from utils.random_events import generate_random_event
import random


def explore_cave(world, player):
    """
    Handle cave exploration with various encounters and discoveries.
    """
    print("\n🕳️  You enter the dark, mysterious cave...")
    print("The air is cool and damp, and you can hear water dripping somewhere in the distance.")
    
    # Random cave events
    cave_events = [
        "discover_treasure",
        "encounter_bats",
        "find_underground_lake",
        "discover_ancient_paintings",
        "encounter_cave_troll",
        "find_crystal_formation"
    ]
    
    event = random.choice(cave_events)
    
    if event == "discover_treasure":
        treasure_items = ["gold_coins", "ancient_sword", "magic_crystal", "old_map"]
        treasure = random.choice(treasure_items)
        add_item_to_inventory(player, treasure)
        player["gold"] = player.get("gold", 0) + random.randint(20, 50)
        print(f"💰 You discover a hidden treasure chest containing {treasure} and some gold!")
        
    elif event == "encounter_bats":
        print("🦇 A swarm of bats suddenly flies out of the cave!")
        if random.random() < 0.3:
            damage_amount = random.randint(5, 15)
            damage_player(player, damage_amount)
            print(f"The bats scratch you as they fly past. You lose {damage_amount} health.")
        else:
            print("You duck just in time and avoid the bats.")
            
    elif event == "find_underground_lake":
        print("🌊 You discover a beautiful underground lake with crystal-clear water.")
        if input("Do you want to drink from the lake? (y/n): ").lower() == 'y':
            if random.random() < 0.7:
                heal_amount = random.randint(15, 25)
                heal_player(player, heal_amount)
                print(f"The water is refreshing and magical! You recover {heal_amount} health.")
            else:
                damage_amount = random.randint(5, 10)
                damage_player(player, damage_amount)
                print(f"The water tastes strange and makes you feel sick. You lose {damage_amount} health.")
                
    elif event == "discover_ancient_paintings":
        print("🎨 You find ancient cave paintings depicting mysterious rituals and creatures.")
        print("Studying them gives you insight into the world's history.")
        # Could add knowledge/lore system here
        
    elif event == "encounter_cave_troll":
        print("👹 A massive cave troll emerges from the shadows!")
        if "sword" in player.get("inventory", []):
            print("You brandish your sword and the troll retreats, impressed by your courage.")
            add_item_to_inventory(player, "troll_tooth")
        else:
            print("Without a weapon, you must flee deeper into the cave!")
            damage_amount = random.randint(10, 20)
            damage_player(player, damage_amount)
            
    elif event == "find_crystal_formation":
        print("💎 You discover a stunning crystal formation that glows with inner light.")
        add_item_to_inventory(player, "glowing_crystal")
        print("You carefully extract a small glowing crystal.")
    
    # Chance for mythical creature encounter
    if random.random() < 0.2:
        print("\n✨ The cave's mystical energy attracts a mythical creature...")
        creature_types = ["cave_dragon", "crystal_sprite", "earth_elemental"]
        creature = random.choice(creature_types)
        summon_mythical_creature(world, player, creature)
    
    # Random event chance
    if random.random() < 0.3:
        generate_random_event(world, player)
    
    # Update world state
    update_world_state(world, "cave_explored")
    
    print("\nYou emerge from the cave, enriched by your underground adventure.")


def search_cave_depths(world, player):
    """
    Deeper cave exploration for more experienced adventurers.
    """
    print("\n🔦 You venture deeper into the cave's unexplored depths...")
    
    if player.get("health", 0) < 30:
        print("You're too weak to explore the dangerous depths. Rest and heal first.")
        return
    
    # More dangerous encounters in the depths
    depth_events = [
        "ancient_guardian",
        "underground_river",
        "cave_in_danger",
        "hidden_chamber",
        "mineral_vein"
    ]
    
    event = random.choice(depth_events)
    
    if event == "ancient_guardian":
        print("⚔️  An ancient stone guardian awakens to protect the cave's secrets!")
        if "magic_crystal" in player.get("inventory", []):
            print("Your magic crystal resonates with the guardian, and it allows you to pass.")
            add_item_to_inventory(player, "guardian_blessing")
        else:
            damage_amount = random.randint(15, 30)
            damage_player(player, damage_amount)
            print(f"The guardian attacks! You take {damage_amount} damage but manage to escape.")
            
    elif event == "underground_river":
        print("🌊 You find a rushing underground river with ancient coins scattered on the bottom.")
        player["gold"] = player.get("gold", 0) + random.randint(30, 80)
        print("You collect the ancient coins, adding to your wealth.")
        
    elif event == "cave_in_danger":
        print("💥 The cave begins to shake! Rocks start falling from the ceiling!")
        if random.random() < 0.5:
            damage_amount = random.randint(20, 35)
            damage_player(player, damage_amount)
            print(f"You're hit by falling rocks and take {damage_amount} damage!")
        else:
            print("You quickly find shelter and wait for the cave-in to stop.")
            
    elif event == "hidden_chamber":
        print("🏛️  You discover a hidden chamber with ancient artifacts!")
        artifacts = ["ancient_tome", "mystical_orb", "enchanted_ring"]
        artifact = random.choice(artifacts)
        add_item_to_inventory(player, artifact)
        print(f"You find a {artifact.replace('_', ' ')} among the artifacts.")
        
    elif event == "mineral_vein":
        print("⛏️  You discover a rich vein of precious minerals!")
        if "pickaxe" in player.get("inventory", []):
            minerals = ["silver_ore", "gold_ore", "precious_gems"]
            mineral = random.choice(minerals)
            add_item_to_inventory(player, mineral)
            player["gold"] = player.get("gold", 0) + random.randint(40, 100)
            print(f"Using your pickaxe, you mine {mineral.replace('_', ' ')} and find additional gold!")
        else:
            print("You need a pickaxe to mine the minerals effectively.")

