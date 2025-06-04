"""
Test fixtures for player-related testing.
"""

import pytest

from game.player import create_player


class PlayerFixtures:
    """Collection of player fixtures for testing."""

    @staticmethod
    def basic_player():
        """Create a basic player with default stats."""
        return create_player("TestPlayer")

    @staticmethod
    def damaged_player():
        """Create a player with reduced health."""
        player = create_player("DamagedPlayer")
        player["health"] = 25
        return player

    @staticmethod
    def wealthy_player():
        """Create a player with lots of gold."""
        player = create_player("WealthyPlayer")
        player["gold"] = 1000
        return player

    @staticmethod
    def equipped_player():
        """Create a player with a full inventory."""
        player = create_player("EquippedPlayer")
        player["inventory"] = [
            "map",
            "bread",
            "stick",
            "berries",
            "torch",
            "gemstone",
            "rope",
            "pickaxe",
            "sword",
            "gold_coin",
        ]
        return player

    @staticmethod
    def explorer_player():
        """Create a player who has explored different locations."""
        player = create_player("Explorer")
        player["location"] = "Forest"
        player["inventory"] = ["map", "torch", "rope"]
        player["gold"] = 150
        return player

    @staticmethod
    def near_death_player():
        """Create a player with very low health."""
        player = create_player("NearDeath")
        player["health"] = 5
        return player

    @staticmethod
    def dead_player():
        """Create a player with zero health."""
        player = create_player("DeadPlayer")
        player["health"] = 0
        return player

    @staticmethod
    def custom_player(
        name="Custom", health=100, gold=100, location="Village", inventory=None
    ):
        """Create a custom player with specified attributes."""
        player = create_player(name)
        player["health"] = health
        player["gold"] = gold
        player["location"] = location
        player["inventory"] = inventory or []
        return player


# Pytest fixtures using the PlayerFixtures class
@pytest.fixture
def basic_player():
    """Pytest fixture for basic player."""
    return PlayerFixtures.basic_player()


@pytest.fixture
def damaged_player():
    """Pytest fixture for damaged player."""
    return PlayerFixtures.damaged_player()


@pytest.fixture
def wealthy_player():
    """Pytest fixture for wealthy player."""
    return PlayerFixtures.wealthy_player()


@pytest.fixture
def equipped_player():
    """Pytest fixture for equipped player."""
    return PlayerFixtures.equipped_player()


@pytest.fixture
def explorer_player():
    """Pytest fixture for explorer player."""
    return PlayerFixtures.explorer_player()


@pytest.fixture
def near_death_player():
    """Pytest fixture for near death player."""
    return PlayerFixtures.near_death_player()


@pytest.fixture
def dead_player():
    """Pytest fixture for dead player."""
    return PlayerFixtures.dead_player()


@pytest.fixture
def player_factory():
    """Pytest fixture that returns the PlayerFixtures class for custom creation."""
    return PlayerFixtures


# Parameterized fixtures for testing multiple player states
@pytest.fixture(
    params=[("healthy", 100), ("damaged", 50), ("critical", 10), ("near_death", 1)]
)
def player_with_health(request):
    """Parameterized fixture for players with different health levels."""
    health_name, health_value = request.param
    player = create_player(f"Player_{health_name}")
    player["health"] = health_value
    return player


@pytest.fixture(
    params=[("poor", 10), ("average", 100), ("rich", 500), ("wealthy", 1000)]
)
def player_with_gold(request):
    """Parameterized fixture for players with different gold amounts."""
    wealth_name, gold_value = request.param
    player = create_player(f"Player_{wealth_name}")
    player["gold"] = gold_value
    return player


@pytest.fixture(
    params=[
        ("Village", []),
        ("Forest", ["stick"]),
        ("Cave", ["torch"]),
        ("Mountain", ["rope", "pickaxe"]),
    ]
)
def player_in_location(request):
    """Parameterized fixture for players in different locations with appropriate items."""
    location, items = request.param
    player = create_player(f"Player_in_{location}")
    player["location"] = location
    player["inventory"] = items.copy()
    return player


# Complex scenario fixtures
@pytest.fixture
def survival_scenario_player():
    """Player setup for survival scenarios."""
    player = create_player("Survivor")
    player["health"] = 20
    player["gold"] = 50
    player["inventory"] = ["bread", "berries"]
    player["location"] = "Forest"
    return player


@pytest.fixture
def treasure_hunter_player():
    """Player setup for treasure hunting scenarios."""
    player = create_player("TreasureHunter")
    player["health"] = 100
    player["gold"] = 200
    player["inventory"] = ["map", "torch", "pickaxe"]
    player["location"] = "Cave"
    return player


@pytest.fixture
def combat_ready_player():
    """Player setup for combat scenarios."""
    player = create_player("Warrior")
    player["health"] = 100
    player["gold"] = 150
    player["inventory"] = ["sword", "bread", "torch"]
    player["location"] = "Mountain"
    return player


# Edge case fixtures
@pytest.fixture
def player_with_empty_name():
    """Player with empty name for edge case testing."""
    return create_player("")


@pytest.fixture
def player_with_long_name():
    """Player with very long name for edge case testing."""
    long_name = "A" * 100
    return create_player(long_name)


@pytest.fixture
def player_with_special_characters():
    """Player with special characters in name."""
    return create_player("Test-Player_123!@#")


# Batch fixtures for testing multiple players
@pytest.fixture
def player_party():
    """Fixture that returns multiple players for party-based testing."""
    return [
        PlayerFixtures.custom_player(
            "Leader", health=100, gold=200, inventory=["sword", "map"]
        ),
        PlayerFixtures.custom_player(
            "Healer", health=80, gold=150, inventory=["bread", "berries"]
        ),
        PlayerFixtures.custom_player(
            "Scout", health=90, gold=100, inventory=["torch", "rope"]
        ),
        PlayerFixtures.custom_player(
            "Miner", health=100, gold=50, inventory=["pickaxe", "torch"]
        ),
    ]


@pytest.fixture
def players_at_different_stages():
    """Fixture with players at different game progression stages."""
    return {
        "beginner": PlayerFixtures.custom_player("Beginner", inventory=["map"]),
        "intermediate": PlayerFixtures.custom_player(
            "Intermediate", gold=200, inventory=["map", "sword", "torch"]
        ),
        "advanced": PlayerFixtures.custom_player(
            "Advanced", gold=500, inventory=["sword", "pickaxe", "rope", "gemstone"]
        ),
        "expert": PlayerFixtures.custom_player(
            "Expert",
            gold=1000,
            inventory=["sword", "pickaxe", "rope", "gemstone", "ancient_artifact"],
        ),
    }
