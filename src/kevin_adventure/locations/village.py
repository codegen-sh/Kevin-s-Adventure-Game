"""
Village location interaction handler.
"""
from typing import Any

from kevin_adventure.entities.item_registry import create_item
from kevin_adventure.ui.text_ui import TextUI
from kevin_adventure.utils.random_events import generate_random_event


def interact_with_village(location: Any, player: Any, world: Any) -> bool:
    """
    Interact with the village location.
    
    Args:
        location: The village location
        player: The player
        world: The game world
        
    Returns:
        bool: True if the interaction was successful, False otherwise
    """
    ui = TextUI()
    ui.display_message("You enter the bustling village. Villagers go about their daily lives around you.")

    while True:
        ui.display_message("\nWhat would you like to do in the village?")
        ui.display_message("1. Visit the shop")
        ui.display_message("2. Talk to villagers")
        ui.display_message("3. Visit the inn")
        ui.display_message("4. Check for quests")
        ui.display_message("5. Leave the village")

        choice = ui.get_input("Enter your choice (1-5): ")

        if choice == "1":
            visit_shop(player, ui)
        elif choice == "2":
            talk_to_villagers(player, ui)
        elif choice == "3":
            visit_inn(player, ui)
        elif choice == "4":
            perform_quest(player, ui)
        elif choice == "5":
            ui.display_message("You decide to leave the village.")
            break
        else:
            ui.display_message("Invalid choice. Please try again.")
    
    return True


def visit_shop(player: Any, ui: TextUI) -> None:
    """Visit the village shop."""
    ui.display_message("You enter the village shop. The shopkeeper greets you warmly.")
    ui.display_message("Available items: bread (5 gold), torch (10 gold), rope (15 gold), sword (50 gold)")

    while True:
        choice = ui.get_input("What would you like to buy? (or 'exit' to leave): ").lower()
        if choice == 'exit':
            break
        elif choice == 'bread' and player.gold >= 5:
            player.gold -= 5
            player.add_item(create_item("bread"))
            ui.display_message("You bought a loaf of bread.")
        elif choice == 'torch' and player.gold >= 10:
            player.gold -= 10
            player.add_item(create_item("torch"))
            ui.display_message("You bought a torch.")
        elif choice == 'rope' and player.gold >= 15:
            player.gold -= 15
            player.add_item(create_item("rope"))
            ui.display_message("You bought a coil of rope.")
        elif choice == 'sword' and player.gold >= 50:
            player.gold -= 50
            player.add_item(create_item("sword"))
            ui.display_message("You bought a sturdy sword.")
        else:
            ui.display_message("Invalid choice or not enough gold.")


def talk_to_villagers(player: Any, ui: TextUI) -> None:
    """Talk to the villagers."""
    ui.display_message("You approach a group of villagers to chat.")
    event = generate_random_event(events=[("hear_rumor", 40), ("receive_advice", 30), (None, 30)])

    if event == "hear_rumor":
        ui.display_message("You overhear an interesting rumor about treasure hidden in the nearby cave.")
    elif event == "receive_advice":
        ui.display_message("An old villager gives you advice about surviving in the forest.")
        player.heal(10)
        ui.display_message("Their wisdom makes you feel more prepared for your adventures.")
    else:
        ui.display_message("You have a pleasant but uneventful conversation with the villagers.")


def visit_inn(player: Any, ui: TextUI) -> None:
    """Visit the village inn."""
    ui.display_message("You enter the cozy village inn.")
    if player.gold >= 10:
        choice = ui.get_input("Would you like to rest for the night? (10 gold) [y/n]: ").lower()
        if choice == 'y':
            player.gold -= 10
            player.heal(50)
            ui.display_message("You have a good night's rest and feel rejuvenated.")
        else:
            ui.display_message("You decide not to stay the night.")
    else:
        ui.display_message("You don't have enough gold to stay the night.")


def perform_quest(player: Any, ui: TextUI) -> None:
    """Check for quests in the village."""
    ui.display_message("You check the village quest board.")
    if generate_random_event(events=[("receive_quest", 30), (None, 70)]) == "receive_quest":
        ui.display_message("You accept a quest to deliver a package to a hermit living on the mountain.")
        player.add_item(create_item("mysterious_package"))
        ui.display_message("Complete this quest by reaching the mountain peak.")

