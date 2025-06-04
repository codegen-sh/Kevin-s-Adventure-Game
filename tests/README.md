# Kevin's Adventure Game - Test Suite

This directory contains the comprehensive test suite for Kevin's Adventure Game, designed to achieve 90%+ code coverage and ensure robust, reliable gameplay.

## Test Structure

```
tests/
├── unit/                   # Unit tests for individual modules
├── integration/            # Integration tests for module interactions
├── scenarios/              # End-to-end scenario tests
├── performance/            # Performance and benchmark tests
├── fixtures/               # Reusable test fixtures
├── mocks/                  # Mock objects for testing
├── conftest.py            # Pytest configuration and shared fixtures
└── README.md              # This file
```

## Test Categories

### Unit Tests (`tests/unit/`)
Test individual functions and modules in isolation:
- `test_player.py` - Player creation, status, inventory, health management
- `test_world.py` - World initialization, location management, navigation
- `test_actions.py` - Action processing and command handling
- `test_items.py` - Item descriptions, usage, and effects
- `test_save_load.py` - Save/load functionality
- `test_text_formatting.py` - Text formatting and display functions
- `test_random_events.py` - Random event generation

### Integration Tests (`tests/integration/`)
Test interactions between multiple modules:
- `test_game_flow.py` - Complete game flow and state management
- `test_location_interactions.py` - Player-location interactions
- `test_save_load_integration.py` - Save/load with game state
- `test_inventory_management.py` - Inventory across different game states

### Scenario Tests (`tests/scenarios/`)
Test complete gameplay scenarios:
- `test_complete_game_session.py` - Full game sessions from start to finish
- `test_exploration_scenarios.py` - World exploration and discovery
- `test_quest_completion.py` - Quest and objective completion

### Performance Tests (`tests/performance/`)
Test performance and benchmarks:
- `test_world_performance.py` - World operation performance
- `test_save_load_performance.py` - Save/load operation performance
- `test_inventory_performance.py` - Inventory operation performance

## Running Tests

### Prerequisites
Install test dependencies:
```bash
pip install -r requirements-test.txt
```

### Run All Tests
```bash
pytest
```

### Run Specific Test Categories
```bash
# Unit tests only
pytest tests/unit/

# Integration tests only
pytest tests/integration/

# Scenario tests only
pytest tests/scenarios/

# Performance tests only
pytest tests/performance/
```

### Run Tests with Coverage
```bash
# Generate coverage report
pytest --cov=game --cov=locations --cov=utils --cov=main

# Generate HTML coverage report
pytest --cov=game --cov=locations --cov=utils --cov=main --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Run Tests by Markers
```bash
# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration

# Run only scenario tests
pytest -m scenario

# Run only performance tests
pytest -m performance

# Run slow tests
pytest -m slow

# Skip slow tests
pytest -m "not slow"
```

### Run Specific Tests
```bash
# Run specific test file
pytest tests/unit/test_player.py

# Run specific test class
pytest tests/unit/test_player.py::TestCreatePlayer

# Run specific test method
pytest tests/unit/test_player.py::TestCreatePlayer::test_create_player_with_name

# Run tests matching pattern
pytest -k "test_player"
```

## Test Configuration

### Pytest Configuration (`pytest.ini`)
- Test discovery patterns
- Coverage settings (90% minimum)
- Output formatting
- Markers for test categorization
- Timeout settings

### Shared Fixtures (`conftest.py`)
- `sample_player` - Basic test player
- `sample_world` - Basic test world
- `player_with_items` - Player with inventory
- `damaged_player` - Player with reduced health
- `mock_input` - Mock user input
- `mock_print` - Mock print output
- `mock_random` - Mock random functions
- `temp_save_dir` - Temporary directory for save tests

## Test Fixtures

### Player Fixtures (`tests/fixtures/player_fixtures.py`)
Reusable player configurations:
- Basic players with default stats
- Players with specific health levels
- Players with different inventory states
- Players in various locations
- Edge case players (empty name, special characters)

### World Fixtures (`tests/fixtures/world_fixtures.py`)
Reusable world configurations:
- Basic world with default setup
- Empty world with no items
- Item-rich world with extra items
- Modified connection worlds
- Scenario-specific worlds

## Writing New Tests

### Test Naming Convention
- Test files: `test_<module_name>.py`
- Test classes: `Test<FeatureName>`
- Test methods: `test_<specific_behavior>`

### Example Test Structure
```python
class TestPlayerHealth:
    """Test player health management."""
    
    def test_heal_player_normal_case(self, sample_player):
        """Test healing a player with normal health."""
        # Arrange
        sample_player["health"] = 50
        
        # Act
        heal_player(sample_player, 30)
        
        # Assert
        assert sample_player["health"] == 80
    
    def test_heal_player_beyond_max(self, sample_player):
        """Test healing a player beyond maximum health."""
        # Arrange
        sample_player["health"] = 90
        
        # Act
        heal_player(sample_player, 30)
        
        # Assert
        assert sample_player["health"] == 100  # Capped at max
```

### Using Fixtures
```python
def test_with_custom_player(self, player_factory):
    """Test using custom player fixture."""
    player = player_factory.custom_player(
        name="TestPlayer",
        health=50,
        gold=200,
        inventory=["sword", "potion"]
    )
    
    # Test logic here
    assert player["name"] == "TestPlayer"
```

### Mocking External Dependencies
```python
@patch('builtins.input')
@patch('builtins.print')
def test_user_interaction(self, mock_print, mock_input):
    """Test user interaction with mocked input/output."""
    mock_input.return_value = "yes"
    
    # Test logic here
    
    mock_print.assert_called_with("Expected output")
```

## Coverage Requirements

### Minimum Coverage: 90%
All modules must maintain at least 90% code coverage:
- `game/` modules: 90%+
- `locations/` modules: 90%+
- `utils/` modules: 90%+
- `main.py`: 90%+

### Coverage Exclusions
Lines excluded from coverage:
- Debug print statements
- Error handling for impossible conditions
- Platform-specific code paths

### Viewing Coverage Reports
```bash
# Terminal report
pytest --cov=game --cov-report=term-missing

# HTML report (detailed)
pytest --cov=game --cov-report=html
open htmlcov/index.html

# XML report (for CI)
pytest --cov=game --cov-report=xml
```

## Continuous Integration

### GitHub Actions
Tests run automatically on:
- Push to main/develop branches
- Pull requests
- Multiple Python versions (3.8, 3.9, 3.10, 3.11)

### Test Pipeline
1. Lint with flake8
2. Format check with black
3. Import sort check with isort
4. Type check with mypy
5. Run unit tests with coverage
6. Run integration tests
7. Run scenario tests
8. Run performance tests
9. Generate coverage reports
10. Security checks with bandit

## Performance Testing

### Benchmarking
Performance tests use `pytest-benchmark`:
```bash
# Run performance tests
pytest tests/performance/ --benchmark-only

# Compare benchmarks
pytest tests/performance/ --benchmark-compare

# Save benchmark results
pytest tests/performance/ --benchmark-save=baseline
```

### Performance Targets
- World initialization: < 1ms
- Location changes: < 0.1ms
- Item operations: < 0.1ms
- Save/load operations: < 100ms

## Troubleshooting

### Common Issues

#### Import Errors
```bash
# Ensure Python path includes project root
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

#### Coverage Not Working
```bash
# Install coverage dependencies
pip install pytest-cov coverage

# Check coverage configuration in pytest.ini
```

#### Slow Tests
```bash
# Run without slow tests
pytest -m "not slow"

# Run only fast tests
pytest --maxfail=1 -x
```

#### Mock Issues
```bash
# Check mock import paths
# Use full module paths in patches
@patch('game.player.heal_player')
```

### Getting Help
- Check test output for detailed error messages
- Use `pytest -v` for verbose output
- Use `pytest --tb=long` for full tracebacks
- Check fixture definitions in `conftest.py`

## Contributing

### Adding New Tests
1. Follow naming conventions
2. Use appropriate fixtures
3. Include docstrings
4. Add appropriate markers
5. Ensure 90%+ coverage
6. Update this README if needed

### Test Review Checklist
- [ ] Tests follow naming conventions
- [ ] Appropriate fixtures used
- [ ] Edge cases covered
- [ ] Error conditions tested
- [ ] Performance considerations
- [ ] Documentation updated
- [ ] Coverage requirements met

