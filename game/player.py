from utils.text_formatting import format_inventory, print_game_over
from exceptions import PlayerError, ValidationError, ItemError
from utils.logging_config import get_logger, log_player_action, log_error_with_context
from utils.validation import validate_player_name, validate_numeric_input, validate_item_name

# Initialize logger
logger = get_logger('player')

def create_player(name):
    """
    Create a new player with validated attributes.
    
    Args:
        name (str): Player name
    
    Returns:
        dict: Player state dictionary
    
    Raises:
        PlayerError: If player creation fails
    """
    try:
        # Validate player name
        validated_name = validate_player_name(name)
        
        player = {
            "name": validated_name,
            "health": 100,
            "inventory": [],
            "location": "Village",
            "gold": 100
        }
        
        logger.info(f"Created new player: {validated_name}")
        log_player_action(player, "player_created", result="success")
        
        return player
        
    except ValidationError as e:
        logger.error(f"Failed to create player due to validation error: {e}")
        raise PlayerError(f"Cannot create player: {e.message}", context=e.context)
    except Exception as e:
        logger.error(f"Unexpected error creating player: {e}")
        log_error_with_context(e, action="create_player")
        raise PlayerError(f"Failed to create player: {e}")

def get_player_status(player):
    """
    Get formatted player status with error handling.
    
    Args:
        player (dict): Player state
    
    Returns:
        str: Formatted status string
    
    Raises:
        PlayerError: If player state is invalid
    """
    try:
        if not isinstance(player, dict):
            raise PlayerError("Invalid player state: not a dictionary")
        
        required_fields = ['name', 'health', 'inventory', 'gold']
        missing_fields = [field for field in required_fields if field not in player]
        
        if missing_fields:
            raise PlayerError(
                f"Player state missing required fields: {missing_fields}",
                player_state=player,
                context={'missing_fields': missing_fields}
            )
        
        # Validate health value
        health = validate_numeric_input(player['health'], min_value=0, max_value=100, integer_only=True)
        gold = validate_numeric_input(player['gold'], min_value=0, integer_only=True)
        
        status = f"Health: {health} | Inventory: {format_inventory(player['inventory'])} | Gold: {gold}"
        logger.debug(f"Generated status for player {player['name']}: {status}")
        
        return status
        
    except ValidationError as e:
        logger.error(f"Validation error in get_player_status: {e}")
        raise PlayerError(f"Invalid player data: {e.message}", player_state=player)
    except Exception as e:
        logger.error(f"Error getting player status: {e}")
        log_error_with_context(e, player=player, action="get_player_status")
        raise PlayerError(f"Failed to get player status: {e}", player_state=player)

def add_item_to_inventory(player, item):
    """
    Add an item to player inventory with validation and logging.
    
    Args:
        player (dict): Player state
        item (str): Item to add
    
    Raises:
        PlayerError: If operation fails
        ItemError: If item is invalid
    """
    try:
        if not isinstance(player, dict) or 'inventory' not in player:
            raise PlayerError("Invalid player state", player_state=player)
        
        # Validate item name
        validated_item = validate_item_name(item)
        
        # Check inventory limits (optional)
        max_inventory_size = 20
        if len(player['inventory']) >= max_inventory_size:
            raise PlayerError(
                f"Inventory full (max {max_inventory_size} items)",
                player_state=player,
                context={'max_inventory_size': max_inventory_size, 'current_size': len(player['inventory'])}
            )
        
        # Add item to inventory
        player['inventory'].append(validated_item)
        
        logger.info(f"Player {player['name']} picked up: {validated_item}")
        log_player_action(player, "item_picked_up", result=f"added {validated_item}")
        
        print(f"You picked up: {validated_item}")
        
    except ValidationError as e:
        logger.error(f"Validation error adding item to inventory: {e}")
        raise ItemError(f"Invalid item: {e.message}", item_name=item, context=e.context)
    except (PlayerError, ItemError):
        raise
    except Exception as e:
        logger.error(f"Unexpected error adding item to inventory: {e}")
        log_error_with_context(e, player=player, action="add_item_to_inventory")
        raise PlayerError(f"Failed to add item to inventory: {e}", player_state=player)

def remove_item_from_inventory(player, item):
    """
    Remove an item from player inventory with validation and logging.
    
    Args:
        player (dict): Player state
        item (str): Item to remove
    
    Returns:
        bool: True if item was removed, False if not found
    
    Raises:
        PlayerError: If operation fails
    """
    try:
        if not isinstance(player, dict) or 'inventory' not in player:
            raise PlayerError("Invalid player state", player_state=player)
        
        # Validate item name
        validated_item = validate_item_name(item)
        
        if validated_item in player['inventory']:
            player['inventory'].remove(validated_item)
            
            logger.info(f"Player {player['name']} dropped: {validated_item}")
            log_player_action(player, "item_dropped", result=f"removed {validated_item}")
            
            print(f"You dropped: {validated_item}")
            return True
        else:
            logger.debug(f"Player {player['name']} tried to drop non-existent item: {validated_item}")
            print(f"You don't have {validated_item} in your inventory.")
            return False
            
    except ValidationError as e:
        logger.error(f"Validation error removing item from inventory: {e}")
        print(f"Invalid item name: {item}")
        return False
    except PlayerError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error removing item from inventory: {e}")
        log_error_with_context(e, player=player, action="remove_item_from_inventory")
        raise PlayerError(f"Failed to remove item from inventory: {e}", player_state=player)

def move_player(player, new_location):
    """
    Move player to a new location with validation and logging.
    
    Args:
        player (dict): Player state
        new_location (str): Target location
    
    Raises:
        PlayerError: If operation fails
    """
    try:
        if not isinstance(player, dict) or 'location' not in player:
            raise PlayerError("Invalid player state", player_state=player)
        
        # Validate location (basic validation - more detailed validation should be done by world module)
        if not isinstance(new_location, str) or not new_location.strip():
            raise PlayerError(f"Invalid location: {new_location}")
        
        old_location = player['location']
        player['location'] = new_location.strip()
        
        logger.info(f"Player {player['name']} moved from {old_location} to {new_location}")
        log_player_action(player, "player_moved", result=f"from {old_location} to {new_location}")
        
        print(f"You moved to: {new_location}")
        
    except PlayerError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error moving player: {e}")
        log_error_with_context(e, player=player, action="move_player")
        raise PlayerError(f"Failed to move player: {e}", player_state=player)

def heal_player(player, amount):
    """
    Heal player with validation and logging.
    
    Args:
        player (dict): Player state
        amount (int): Amount to heal
    
    Raises:
        PlayerError: If operation fails
    """
    try:
        if not isinstance(player, dict) or 'health' not in player:
            raise PlayerError("Invalid player state", player_state=player)
        
        # Validate heal amount
        heal_amount = validate_numeric_input(amount, min_value=0, max_value=100, integer_only=True)
        
        old_health = player['health']
        player['health'] = min(100, player['health'] + heal_amount)
        actual_heal = player['health'] - old_health
        
        logger.info(f"Player {player['name']} healed for {actual_heal} (attempted {heal_amount})")
        log_player_action(player, "player_healed", result=f"healed {actual_heal} points")
        
        print(f"You healed for {actual_heal} health. Current health: {player['health']}")
        
    except ValidationError as e:
        logger.error(f"Validation error healing player: {e}")
        raise PlayerError(f"Invalid heal amount: {e.message}", player_state=player)
    except PlayerError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error healing player: {e}")
        log_error_with_context(e, player=player, action="heal_player")
        raise PlayerError(f"Failed to heal player: {e}", player_state=player)

def damage_player(player, amount):
    """
    Damage player with validation and logging.
    
    Args:
        player (dict): Player state
        amount (int): Amount of damage
    
    Raises:
        PlayerError: If operation fails
    """
    try:
        if not isinstance(player, dict) or 'health' not in player:
            raise PlayerError("Invalid player state", player_state=player)
        
        # Validate damage amount
        damage_amount = validate_numeric_input(amount, min_value=0, max_value=100, integer_only=True)
        
        old_health = player['health']
        player['health'] = max(0, player['health'] - damage_amount)
        actual_damage = old_health - player['health']
        
        logger.info(f"Player {player['name']} took {actual_damage} damage")
        log_player_action(player, "player_damaged", result=f"took {actual_damage} damage")
        
        print(f"You took {actual_damage} damage. Current health: {player['health']}")
        
        if player['health'] == 0:
            logger.warning(f"Player {player['name']} has been defeated")
            log_player_action(player, "player_defeated", result="health reached 0")
            print("You have been defeated.")
            print_game_over()
        
    except ValidationError as e:
        logger.error(f"Validation error damaging player: {e}")
        raise PlayerError(f"Invalid damage amount: {e.message}", player_state=player)
    except PlayerError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error damaging player: {e}")
        log_error_with_context(e, player=player, action="damage_player")
        raise PlayerError(f"Failed to damage player: {e}", player_state=player)
