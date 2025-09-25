🌈
from game.player import add_item_to_inventory, heal_player


def summon_mythical_creature(world, player, creature_type):
    """
    Summons a mythical creature to aid the player.

    Args:
    world (dict): The game world state
    player (dict): The player's current state
    creature_type (str): The type of mythical creature to summon

    Returns:
    bool: True if summoning was successful, False otherwise
    """
    if creature_type == "phoenix":
        print("A majestic phoenix appears in a burst of flames!")
        heal_player(player, 50)
    elif creature_type == "unicorn":
        print("A graceful unicorn materializes before you!")
        add_item_to_inventory(player, "unicorn_hair")
    elif creature_type == "dragon":
        print("A powerful dragon descends from the sky! The dragon is friendly and will help you.")
        add_item_to_inventory(player, "dragon_scale")
    else:
        print(f"Unknown creature type: {creature_type}")
        return False

    return True
