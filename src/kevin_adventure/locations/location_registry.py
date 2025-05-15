"""
Registry for location interaction handlers.
"""
from typing import Dict, Callable, Any, Optional

# Type alias for location interaction handlers
LocationInteractionHandler = Callable[['Location', Any, Any], bool]

# Dictionary to store location interaction handlers
_location_interaction_handlers: Dict[str, LocationInteractionHandler] = {}


def register_location_interaction_handler(location_name: str, handler: LocationInteractionHandler) -> None:
    """Register an interaction handler for a location type."""
    _location_interaction_handlers[location_name.lower()] = handler


def get_location_interaction_handler(location_name: str) -> Optional[LocationInteractionHandler]:
    """Get the interaction handler for a location type."""
    return _location_interaction_handlers.get(location_name.lower())


# Import location interaction handlers
from kevin_adventure.locations.village import interact_with_village
from kevin_adventure.locations.forest import interact_with_forest
from kevin_adventure.locations.mountain import interact_with_mountain
from kevin_adventure.locations.cave import interact_with_cave

# Register location interaction handlers
register_location_interaction_handler("Village", interact_with_village)
register_location_interaction_handler("Forest", interact_with_forest)
register_location_interaction_handler("Mountain", interact_with_mountain)
register_location_interaction_handler("Cave", interact_with_cave)

