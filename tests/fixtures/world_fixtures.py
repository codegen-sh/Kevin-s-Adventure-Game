"""
Test fixtures for world-related testing.
"""

import pytest

from game.world import initialize_world


class WorldFixtures:
    """Collection of world fixtures for testing."""

    @staticmethod
    def basic_world():
        """Create a basic world with default configuration."""
        return initialize_world()

    @staticmethod
    def empty_world():
        """Create a world with no items in any location."""
        world = initialize_world()
        for location in world["locations"]:
            world["locations"][location]["items"] = []
        return world

    @staticmethod
    def item_rich_world():
        """Create a world with extra items in all locations."""
        world = initialize_world()
        extra_items = {
            "Village": ["sword", "shield", "potion", "gold_coin"],
            "Forest": ["mushrooms", "herbs", "ancient_coin"],
            "Cave": ["crystal", "ancient_artifact", "treasure"],
            "Mountain": ["rare_ore", "mountain_herbs", "climbing_gear"],
        }

        for location, items in extra_items.items():
            world["locations"][location]["items"].extend(items)

        return world

    @staticmethod
    def modified_connections_world():
        """Create a world with modified location connections."""
        world = initialize_world()

        # Add a secret connection from Cave to Mountain
        world["locations"]["Cave"]["connections"].append("Mountain")
        world["locations"]["Mountain"]["connections"].append("Cave")

        return world

    @staticmethod
    def single_location_world():
        """Create a world with only one accessible location."""
        world = initialize_world()

        # Remove all connections except Village
        for location in world["locations"]:
            if location != "Village":
                world["locations"][location]["connections"] = []

        world["locations"]["Village"]["connections"] = []
        return world

    @staticmethod
    def linear_world():
        """Create a world with linear progression (Village -> Forest -> Cave -> Mountain)."""
        world = initialize_world()

        # Modify connections for linear progression
        world["locations"]["Village"]["connections"] = ["Forest"]
        world["locations"]["Forest"]["connections"] = ["Village", "Cave"]
        world["locations"]["Cave"]["connections"] = ["Forest", "Mountain"]
        world["locations"]["Mountain"]["connections"] = ["Cave"]

        return world

    @staticmethod
    def world_at_location(location):
        """Create a world with current location set to specified location."""
        world = initialize_world()
        world["current_location"] = location
        return world

    @staticmethod
    def custom_world(
        current_location="Village", location_items=None, location_connections=None
    ):
        """Create a custom world with specified configuration."""
        world = initialize_world()
        world["current_location"] = current_location

        if location_items:
            for location, items in location_items.items():
                if location in world["locations"]:
                    world["locations"][location]["items"] = items.copy()

        if location_connections:
            for location, connections in location_connections.items():
                if location in world["locations"]:
                    world["locations"][location]["connections"] = connections.copy()

        return world


# Pytest fixtures using the WorldFixtures class
@pytest.fixture
def basic_world():
    """Pytest fixture for basic world."""
    return WorldFixtures.basic_world()


@pytest.fixture
def empty_world():
    """Pytest fixture for empty world."""
    return WorldFixtures.empty_world()


@pytest.fixture
def item_rich_world():
    """Pytest fixture for item-rich world."""
    return WorldFixtures.item_rich_world()


@pytest.fixture
def modified_connections_world():
    """Pytest fixture for world with modified connections."""
    return WorldFixtures.modified_connections_world()


@pytest.fixture
def single_location_world():
    """Pytest fixture for single location world."""
    return WorldFixtures.single_location_world()


@pytest.fixture
def linear_world():
    """Pytest fixture for linear world."""
    return WorldFixtures.linear_world()


@pytest.fixture
def world_factory():
    """Pytest fixture that returns the WorldFixtures class for custom creation."""
    return WorldFixtures


# Parameterized fixtures for testing different world states
@pytest.fixture(params=["Village", "Forest", "Cave", "Mountain"])
def world_at_each_location(request):
    """Parameterized fixture for worlds starting at each location."""
    return WorldFixtures.world_at_location(request.param)


@pytest.fixture(
    params=[
        ("empty", {}),
        ("sparse", {"Village": ["map"], "Forest": ["stick"]}),
        ("normal", {"Village": ["map", "bread"], "Forest": ["stick", "berries"]}),
        (
            "abundant",
            {
                "Village": ["map", "bread", "sword", "gold_coin"],
                "Forest": ["stick", "berries", "mushrooms", "herbs"],
            },
        ),
    ]
)
def world_with_item_density(request):
    """Parameterized fixture for worlds with different item densities."""
    density_name, items = request.param
    return WorldFixtures.custom_world(location_items=items)


# Scenario-specific world fixtures
@pytest.fixture
def exploration_world():
    """World setup optimized for exploration scenarios."""
    return WorldFixtures.custom_world(
        current_location="Village",
        location_items={
            "Village": ["map", "bread", "torch"],
            "Forest": ["stick", "berries", "rope"],
            "Cave": ["gemstone", "ancient_artifact"],
            "Mountain": ["pickaxe", "rare_ore", "mountain_herbs"],
        },
    )


@pytest.fixture
def treasure_hunting_world():
    """World setup for treasure hunting scenarios."""
    return WorldFixtures.custom_world(
        current_location="Village",
        location_items={
            "Village": ["map"],
            "Forest": ["ancient_coin"],
            "Cave": ["gemstone", "crystal", "treasure", "ancient_artifact"],
            "Mountain": ["rare_ore", "gold_coin", "precious_metals"],
        },
    )


@pytest.fixture
def survival_world():
    """World setup for survival scenarios with limited resources."""
    return WorldFixtures.custom_world(
        current_location="Forest",
        location_items={
            "Village": ["bread"],
            "Forest": ["berries", "mushrooms"],
            "Cave": ["torch"],
            "Mountain": ["mountain_herbs"],
        },
    )


@pytest.fixture
def combat_world():
    """World setup for combat scenarios."""
    return WorldFixtures.custom_world(
        current_location="Village",
        location_items={
            "Village": ["sword", "bread"],
            "Forest": ["stick", "berries"],
            "Cave": ["torch", "ancient_artifact"],
            "Mountain": ["pickaxe", "mountain_herbs"],
        },
    )


# Edge case world fixtures
@pytest.fixture
def disconnected_world():
    """World where some locations are disconnected."""
    return WorldFixtures.custom_world(
        location_connections={
            "Village": ["Forest"],
            "Forest": ["Village"],
            "Cave": [],  # Disconnected
            "Mountain": [],  # Disconnected
        }
    )


@pytest.fixture
def fully_connected_world():
    """World where all locations are connected to all others."""
    all_locations = ["Village", "Forest", "Cave", "Mountain"]
    connections = {
        location: [loc for loc in all_locations if loc != location]
        for location in all_locations
    }

    return WorldFixtures.custom_world(location_connections=connections)


@pytest.fixture
def world_with_duplicate_items():
    """World with duplicate items in locations."""
    return WorldFixtures.custom_world(
        location_items={
            "Village": ["bread", "bread", "map", "map"],
            "Forest": ["stick", "stick", "berries"],
            "Cave": ["torch", "torch", "gemstone"],
            "Mountain": ["rope", "pickaxe", "pickaxe"],
        }
    )


# Complex scenario fixtures
@pytest.fixture
def progressive_difficulty_world():
    """World with increasing difficulty/value items by location."""
    return WorldFixtures.custom_world(
        location_items={
            "Village": ["map", "bread"],  # Basic items
            "Forest": ["stick", "berries", "rope"],  # Intermediate items
            "Cave": ["torch", "gemstone", "ancient_coin"],  # Valuable items
            "Mountain": [
                "pickaxe",
                "rare_ore",
                "ancient_artifact",
                "treasure",
            ],  # Rare items
        }
    )


@pytest.fixture
def quest_world():
    """World setup for quest-based scenarios."""
    return WorldFixtures.custom_world(
        location_items={
            "Village": ["quest_scroll", "map"],
            "Forest": ["quest_item_1", "berries"],
            "Cave": ["quest_item_2", "torch"],
            "Mountain": ["quest_reward", "pickaxe"],
        }
    )


# Batch fixtures for testing multiple worlds
@pytest.fixture
def world_progression():
    """Fixture with worlds representing different game progression stages."""
    return {
        "early_game": WorldFixtures.custom_world(
            location_items={"Village": ["map", "bread"], "Forest": ["stick"]}
        ),
        "mid_game": WorldFixtures.custom_world(
            location_items={
                "Village": ["map", "bread"],
                "Forest": ["stick", "berries"],
                "Cave": ["torch", "gemstone"],
            }
        ),
        "late_game": WorldFixtures.custom_world(
            location_items={
                "Village": ["map", "bread", "sword"],
                "Forest": ["stick", "berries", "rope"],
                "Cave": ["torch", "gemstone", "ancient_artifact"],
                "Mountain": ["pickaxe", "rare_ore", "treasure"],
            }
        ),
    }


@pytest.fixture
def worlds_for_stress_testing():
    """Fixture with worlds designed for stress testing."""
    return {
        "minimal": WorldFixtures.empty_world(),
        "maximal": WorldFixtures.item_rich_world(),
        "disconnected": WorldFixtures.single_location_world(),
        "linear": WorldFixtures.linear_world(),
    }
