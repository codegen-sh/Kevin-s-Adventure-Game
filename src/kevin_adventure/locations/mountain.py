"""
Mountain location interaction handler.
"""
from typing import Any

from kevin_adventure.entities.item_registry import create_item
from kevin_adventure.ui.text_ui import TextUI
from kevin_adventure.utils.random_events import generate_random_event


def interact_with_mountain(location: Any, player: Any, world: Any) -> bool:
    """
    Interact with the mountain location.
    
    Args:
        location: The mountain location
        player: The player
        world: The game world
        
    Returns:
        bool: True if the interaction was successful, False otherwise
    """
    ui = TextUI()
    ui.display_message("You begin your ascent up the steep mountain path.")

    while True:
        ui.display_message("\nWhat would you like to do on the mountain?")
        ui.display_message("1. Check weather")
        ui.display_message("2. Use climbing gear")
        ui.display_message("3. Search for herbs")
        ui.display_message("4. Try to reach the peak")
        ui.display_message("5. Explore mountain cave")
        ui.display_message("6. Descend the mountain")

        choice = ui.get_input("Enter your choice (1-6): ")

        if choice == "1":
            check_weather(world, ui)
        elif choice == "2":
            use_climbing_gear(player, ui)
        elif choice == "3":
            search_for_herbs(player, ui)
        elif choice == "4":
            reach_peak(player, ui)
        elif choice == "5":
            explore_mountain_cave(player, ui)
        elif choice == "6":
            ui.display_message("You decide to descend the mountain.")
            break
        else:
            ui.display_message("Invalid choice. Please try again.")
    
    return True


def check_weather(world: Any, ui: TextUI) -> None:
    """Check the weather conditions on the mountain."""
    ui.display_message("You pause to check the weather conditions.")
    event = generate_random_event(events=[("clear_skies", 50), ("incoming_storm", 50)])

    if event == "clear_skies":
        ui.display_message("The skies are clear, offering a breathtaking view of the surrounding lands.")
        # world.update_state("mountain_visibility", "high")
    elif event == "incoming_storm":
        ui.display_message("You notice dark clouds gathering. A storm might be approaching.")
        # world.update_state("mountain_weather", "stormy")
    else:
        ui.display_message("The weather seems stable for now.")


def use_climbing_gear(player: Any, ui: TextUI) -> None:
    """Use climbing gear to navigate the mountain."""
    if player.has_item("rope"):
        ui.display_message("You use your rope to safely navigate a particularly treacherous part of the path.")
        player.heal(5)
        ui.display_message("Your careful climbing technique leaves you feeling confident.")
    else:
        ui.display_message("This part of the path looks dangerous. A rope would be useful here.")
        player.damage(10)
        ui.display_message("You slip and take some damage while climbing. Be more careful!")


def search_for_herbs(player: Any, ui: TextUI) -> None:
    """Search for rare herbs on the mountain."""
    ui.display_message("You search the mountainside for rare herbs.")
    if generate_random_event(events=[("find_herbs", 30), (None, 70)]) == "find_herbs":
        ui.display_message("You find some rare medicinal herbs!")
        player.add_item(create_item("mountain_herbs"))
    else:
        ui.display_message("You don't find any useful herbs this time.")


def reach_peak(player: Any, ui: TextUI) -> None:
    """Try to reach the mountain peak."""
    ui.display_message("You finally reach the mountain peak!")
    if player.has_item("mysterious_package"):
        ui.display_message("You find the hermit's hut and deliver the mysterious package.")
        player.remove_item("mysterious_package")
        player.add_item(create_item("hermit's_blessing"))
        ui.display_message("The hermit thanks you and gives you their blessing, which fills you with energy.")
        player.heal(100)
        # Future enhancement: Add mythical creature encounter
        # summon_mythical_creature(player, "phoenix")

    ui.display_message("The view from the top is spectacular. You can see the entire game world spread out before you.")
    # world.update_state("mountain_peak_reached", True)


def explore_mountain_cave(player: Any, ui: TextUI) -> None:
    """Explore a small cave on the mountainside."""
    ui.display_message("You discover a small cave entrance on the mountainside.")
    if player.has_item("torch"):
        ui.display_message("You use your torch to explore the mountain cave.")
        if generate_random_event(events=[("find_treasure", 20), (None, 80)]) == "find_treasure":
            ui.display_message("You discover an old treasure chest hidden in the cave!")
            player.add_item(create_item("ancient_coin"))
        else:
            ui.display_message("The cave is empty, but it provides good shelter from the elements.")
    else:
        ui.display_message("It's too dark to explore the cave without a torch.")

