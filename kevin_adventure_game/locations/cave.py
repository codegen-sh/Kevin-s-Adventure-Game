"""
Cave location module for Kevin's Adventure Game.
This module handles all interactions in the cave location.
"""

import logging
import random

from kevin_adventure_game.game.player import (
    add_item_to_inventory,
    damage_player,
    heal_player,
)
from kevin_adventure_game.utils.random_events import generate_random_event

# Set up logger
logger = logging.getLogger(__name__)


def explore_cave(world, player):
    """
    Handle player interactions in the cave location.

    Args:
        world (dict): The game world state
        player (dict): The player's current state
    """
    print("You enter a dark, mysterious cave. The air is damp and cool.")

    # Check if player has a torch
    has_torch = "torch" in player["inventory"]
    if not has_torch:
        print("It's very dark in here. A torch would be helpful.")
        # Small chance of taking damage in the dark
        if random.random() < 0.3:
            print("You stumble in the darkness and hurt yourself.")
            damage_player(player, 5)

    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper")
        print("2. Search for minerals")
        print("3. Listen to the cave")
        print("4. Rest in a safe corner")
        print("5. Leave the cave")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            explore_deeper(world, player, has_torch)
        elif choice == "2":
            search_for_minerals(world, player, has_torch)
        elif choice == "3":
            listen_to_cave(world, player)
        elif choice == "4":
            rest_in_cave(world, player)
        elif choice == "5":
            print("You decide to leave the cave.")
            break
        else:
            print("Invalid choice. Please try again.")


def explore_deeper(world, player, has_torch):
    """Explore deeper into the cave."""
    print("You venture deeper into the cave...")

    # Different outcomes based on having a torch
    if has_torch:
        event = generate_random_event(
            events=[
                ("find_treasure", 30),
                ("encounter_bats", 20),
                ("discover_underground_lake", 15),
                (None, 35),
            ]
        )
    else:
        # Higher chance of negative outcomes without a torch
        event = generate_random_event(
            events=[
                ("find_treasure", 10),
                ("encounter_bats", 40),
                ("get_lost", 30),
                (None, 20),
            ]
        )

    if event == "find_treasure":
        print("You discover a small treasure chest hidden in a crevice!")
        add_item_to_inventory(player, "gemstone")
        logger.info("Player found a gemstone in the cave")
    elif event == "encounter_bats":
        print("A swarm of bats suddenly flies past you, startled by your presence!")
        if not has_torch:
            print("In the darkness, you panic and trip, hurting yourself.")
            damage_player(player, 10)
        else:
            print("Your torch helps you stay calm and avoid injury.")
    elif event == "discover_underground_lake":
        print("You discover a beautiful underground lake with crystal-clear water.")
        print("The water seems to have healing properties.")
        heal_player(player, 15)
        logger.info("Player healed at underground lake")
    elif event == "get_lost":
        print("Without proper light, you lose your way in the twisting passages.")
        print("It takes you a while to find your way back, leaving you exhausted.")
        damage_player(player, 15)
        logger.info("Player got lost in the cave")
    else:
        print("Your exploration yields nothing of note this time.")


def search_for_minerals(world, player, has_torch):
    """Search for valuable minerals in the cave."""
    print("You carefully examine the cave walls for valuable minerals...")

    # Better chances with a torch
    if has_torch:
        success_chance = 0.4
    else:
        success_chance = 0.2
        print("It's hard to see what you're doing in the dark.")

    if random.random() < success_chance:
        minerals = ["quartz", "amethyst", "iron_ore", "gold_nugget"]
        weights = [40, 30, 20, 10]
        found_mineral = random.choices(minerals, weights=weights)[0]

        print(f"You found some {found_mineral.replace('_', ' ')}!")
        add_item_to_inventory(player, found_mineral)
        logger.info(f"Player found {found_mineral} in the cave")
    else:
        print("You don't find anything valuable this time.")


def listen_to_cave(world, player):
    """Listen to the sounds in the cave."""
    print("You stand still and listen carefully to the sounds of the cave...")

    sounds = [
        "You hear water dripping somewhere in the distance.",
        "There's a faint howling sound as wind moves through the cave passages.",
        "You hear small rocks occasionally falling from the ceiling.",
        "There's complete silence, which feels somewhat unnerving.",
        "You hear what sounds like distant whispers, though it's probably just the wind.",
    ]

    print(random.choice(sounds))

    # Small chance of discovering something
    if random.random() < 0.2:
        print(
            "As you listen, you notice a pattern in the sounds that leads you to a hidden passage!"
        )
        print("You mark it on your mental map for future exploration.")
        # Could update world state here in a future implementation
        logger.info("Player discovered hidden passage in cave")


def rest_in_cave(world, player):
    """Rest in a safe corner of the cave."""
    print("You find a relatively dry and comfortable corner of the cave to rest in.")

    # Check for danger
    if random.random() < 0.2:
        print("As you're resting, you hear something approaching...")
        print("You quickly get up, but not before a cave creature snaps at you!")
        damage_player(player, 10)
        logger.info("Player was attacked while resting in cave")
    else:
        print("You rest peacefully for a while, recovering some energy.")
        heal_player(player, 10)
        logger.info("Player rested in cave and recovered health")
