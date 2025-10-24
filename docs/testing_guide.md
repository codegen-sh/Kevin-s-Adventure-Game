# Kevin's Adventure Game - Testing Guide

This comprehensive guide covers all aspects of testing for Kevin's Adventure Game, from basic unit tests to advanced performance testing and continuous integration.

## Table of Contents

1. [Testing Philosophy](#testing-philosophy)
2. [Test Architecture](#test-architecture)
3. [Setting Up Testing Environment](#setting-up-testing-environment)
4. [Writing Effective Tests](#writing-effective-tests)
5. [Test Categories and Strategies](#test-categories-and-strategies)
6. [Coverage Requirements](#coverage-requirements)
7. [Performance Testing](#performance-testing)
8. [Continuous Integration](#continuous-integration)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

## Testing Philosophy

### Goals
- **Reliability**: Ensure the game works correctly under all conditions
- **Maintainability**: Make code changes with confidence
- **Documentation**: Tests serve as living documentation
- **Quality**: Maintain high code quality standards
- **Performance**: Ensure optimal game performance

### Principles
- **Test-Driven Development**: Write tests before or alongside code
- **Comprehensive Coverage**: Aim for 90%+ code coverage
- **Fast Feedback**: Tests should run quickly and provide clear feedback
- **Isolation**: Tests should be independent and not affect each other
- **Realistic Scenarios**: Test real-world usage patterns

## Test Architecture

### Pyramid Structure
```
    /\
   /  \     E2E/Scenario Tests (Few, Slow, High Value)
  /____\
 /      \    Integration Tests (Some, Medium Speed)
/________\   Unit Tests (Many, Fast, Focused)
```

### Test Organization
```
tests/
├── unit/           # Fast, isolated tests for individual functions
├── integration/    # Tests for module interactions
├── scenarios/      # End-to-end gameplay tests
├── performance/    # Benchmarks and performance tests
├── fixtures/       # Reusable test data and configurations
├── mocks/          # Mock objects and test doubles
└── conftest.py     # Shared pytest configuration
```

## Setting Up Testing Environment

### 1. Install Dependencies
```bash
# Install testing dependencies
pip install -r requirements-test.txt

# Verify installation
pytest --version
coverage --version
```

### 2. Configure IDE
#### VS Code
```json
{
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "python.testing.autoTestDiscoverOnSaveEnabled": true
}
```

#### PyCharm
- Go to Settings → Tools → Python Integrated Tools
- Set Default test runner to pytest
- Set Working directory to project root

### 3. Environment Variables
```bash
# Set Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Set test environment
export TESTING=true
```

## Writing Effective Tests

### Test Structure (AAA Pattern)
```python
def test_heal_player(self, sample_player):
    """Test that healing increases player health."""
    # Arrange - Set up test conditions
    sample_player["health"] = 50
    initial_health = sample_player["health"]
    
    # Act - Perform the action being tested
    heal_player(sample_player, 30)
    
    # Assert - Verify the expected outcome
    assert sample_player["health"] == initial_health + 30
    assert sample_player["health"] <= 100  # Health cap
```

### Naming Conventions
```python
# Test files
test_player.py          # Tests for player module
test_world.py           # Tests for world module

# Test classes
class TestPlayerHealth: # Group related tests
class TestWorldNavigation:

# Test methods
def test_create_player_with_valid_name(self):     # Specific behavior
def test_move_player_to_invalid_location(self):  # Edge case
def test_heal_player_beyond_maximum_health(self): # Boundary condition
```

### Documentation
```python
def test_complex_scenario(self):
    """
    Test complex player interaction scenario.
    
    This test verifies that when a player:
    1. Moves to a new location
    2. Takes an item
    3. Uses the item
    
    The game state is updated correctly and the player
    receives the expected benefits.
    """
    # Test implementation
```

## Test Categories and Strategies

### Unit Tests
**Purpose**: Test individual functions in isolation

**Characteristics**:
- Fast execution (< 1ms per test)
- No external dependencies
- High coverage of edge cases
- Clear, focused assertions

**Example**:
```python
class TestPlayerCreation:
    def test_create_player_with_name(self):
        player = create_player("Kevin")
        assert player["name"] == "Kevin"
        assert player["health"] == 100
        assert player["inventory"] == []
    
    def test_create_player_with_empty_name(self):
        player = create_player("")
        assert player["name"] == ""
        # Should still have valid default values
        assert player["health"] == 100
```

### Integration Tests
**Purpose**: Test interactions between modules

**Characteristics**:
- Medium execution time (1-100ms per test)
- Test module boundaries
- Verify data flow between components
- Use real implementations where possible

**Example**:
```python
def test_player_world_interaction(self):
    player = create_player("Kevin")
    world = initialize_world()
    
    # Test that player can move in world
    perform_action(player, world, "go forest")
    
    assert player["location"] == "Forest"
    assert world["current_location"] == "Forest"
```

### Scenario Tests
**Purpose**: Test complete user workflows

**Characteristics**:
- Slower execution (100ms+ per test)
- Test realistic user scenarios
- Verify end-to-end functionality
- May use mocks for external dependencies

**Example**:
```python
def test_complete_exploration_scenario(self):
    """Test a complete exploration session."""
    player = create_player("Explorer")
    world = initialize_world()
    
    # Simulate complete exploration
    actions = ["look", "take map", "go forest", "take stick", 
               "go cave", "take torch", "use torch"]
    
    for action in actions:
        perform_action(player, world, action)
    
    # Verify final state
    assert "torch" not in player["inventory"]  # Used
    assert player["location"] == "Cave"
    assert len(player["inventory"]) >= 2  # map, stick
```

### Performance Tests
**Purpose**: Ensure operations meet performance requirements

**Characteristics**:
- Measure execution time
- Test with realistic data volumes
- Identify performance regressions
- Set performance baselines

**Example**:
```python
def test_world_initialization_performance(self, benchmark):
    """World initialization should be fast."""
    result = benchmark(initialize_world)
    
    # Verify correctness
    assert "locations" in result
    assert len(result["locations"]) == 4
    
    # Performance is measured automatically by benchmark fixture
```

## Coverage Requirements

### Coverage Targets
- **Overall**: 90% minimum
- **Critical modules**: 95% minimum
- **New code**: 100% (no uncovered lines in new features)

### Measuring Coverage
```bash
# Basic coverage
pytest --cov=game --cov=locations --cov=utils

# Detailed coverage with missing lines
pytest --cov=game --cov-report=term-missing

# HTML report for detailed analysis
pytest --cov=game --cov-report=html
open htmlcov/index.html
```

### Coverage Configuration
```ini
# In pytest.ini
[tool:pytest]
addopts = 
    --cov=game
    --cov=locations
    --cov=utils
    --cov=main
    --cov-fail-under=90
    --cov-report=term-missing
    --cov-report=html
```

### Excluding Code from Coverage
```python
def debug_function():  # pragma: no cover
    """Debug function not included in coverage."""
    print("Debug information")

if sys.platform == "win32":  # pragma: no cover
    # Platform-specific code
    pass
```

## Performance Testing

### Benchmarking with pytest-benchmark
```python
def test_function_performance(self, benchmark):
    """Benchmark function execution time."""
    result = benchmark(function_to_test, arg1, arg2)
    assert result == expected_result
```

### Performance Targets
| Operation | Target Time | Critical Path |
|-----------|-------------|---------------|
| World initialization | < 1ms | Game startup |
| Location change | < 0.1ms | Navigation |
| Item usage | < 0.1ms | Gameplay |
| Save operation | < 100ms | Game persistence |
| Load operation | < 100ms | Game startup |

### Memory Testing
```python
import tracemalloc

def test_memory_usage():
    """Test memory usage of operations."""
    tracemalloc.start()
    
    # Perform operations
    worlds = [initialize_world() for _ in range(100)]
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Assert reasonable memory usage
    assert peak < 10 * 1024 * 1024  # Less than 10MB
```

## Continuous Integration

### GitHub Actions Workflow
```yaml
name: Test Suite
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, "3.10", "3.11"]
    
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: pip install -r requirements-test.txt
    
    - name: Run tests
      run: pytest --cov=game --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
```

### Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
```

## Best Practices

### Test Independence
```python
# Good - Each test is independent
def test_player_health_increase(self, sample_player):
    sample_player["health"] = 50
    heal_player(sample_player, 30)
    assert sample_player["health"] == 80

def test_player_health_cap(self, sample_player):
    sample_player["health"] = 90
    heal_player(sample_player, 30)
    assert sample_player["health"] == 100

# Bad - Tests depend on each other
class TestPlayerHealth:
    def test_setup_player(self):
        self.player = create_player("Test")
        self.player["health"] = 50
    
    def test_heal_player(self):  # Depends on previous test
        heal_player(self.player, 30)
        assert self.player["health"] == 80
```

### Effective Mocking
```python
# Good - Mock external dependencies
@patch('builtins.input')
def test_user_input_handling(self, mock_input):
    mock_input.return_value = "forest"
    result = get_user_choice()
    assert result == "forest"

# Good - Mock random for predictable tests
@patch('random.randint')
def test_random_damage(self, mock_randint):
    mock_randint.return_value = 10
    damage = calculate_random_damage()
    assert damage == 10

# Bad - Don't mock what you're testing
@patch('game.player.create_player')
def test_create_player(self, mock_create):  # Testing the mock, not the function
    mock_create.return_value = {"name": "Test"}
    result = create_player("Test")
    assert result["name"] == "Test"
```

### Error Testing
```python
def test_invalid_location_movement(self):
    """Test that invalid movements are handled gracefully."""
    player = create_player("Test")
    world = initialize_world()
    
    # Should not crash on invalid location
    perform_action(player, world, "go nonexistent")
    
    # Player should remain in original location
    assert player["location"] == "Village"
    assert world["current_location"] == "Village"

def test_empty_inventory_item_use(self):
    """Test using item when inventory is empty."""
    player = create_player("Test")
    world = initialize_world()
    
    # Should handle gracefully, not crash
    perform_action(player, world, "use sword")
    
    # Player state should be unchanged
    assert player["inventory"] == []
```

### Parameterized Tests
```python
@pytest.mark.parametrize("health,heal_amount,expected", [
    (50, 30, 80),    # Normal healing
    (90, 30, 100),   # Healing beyond max
    (100, 10, 100),  # Already at max
    (0, 50, 50),     # Healing from zero
])
def test_heal_player_scenarios(self, health, heal_amount, expected):
    player = create_player("Test")
    player["health"] = health
    
    heal_player(player, heal_amount)
    
    assert player["health"] == expected
```

## Troubleshooting

### Common Issues

#### Import Errors
```bash
# Problem: ModuleNotFoundError
# Solution: Set PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or use pytest with proper path
python -m pytest tests/
```

#### Fixture Not Found
```python
# Problem: fixture 'sample_player' not found
# Solution: Check conftest.py or import fixtures

# In test file
from tests.fixtures.player_fixtures import sample_player

# Or ensure conftest.py is in the right location
```

#### Slow Tests
```bash
# Problem: Tests taking too long
# Solution: Use markers to skip slow tests
pytest -m "not slow"

# Or run specific fast tests
pytest tests/unit/ -x --maxfail=1
```

#### Coverage Issues
```bash
# Problem: Coverage not working
# Solution: Check coverage configuration
pytest --cov=game --cov-config=.coveragerc

# Or install coverage dependencies
pip install pytest-cov coverage
```

### Debugging Tests
```python
# Use pytest debugging
def test_debug_example():
    import pdb; pdb.set_trace()  # Debugger breakpoint
    # Test code here

# Or use print statements (remove before commit)
def test_with_debug_output():
    result = some_function()
    print(f"Debug: result = {result}")  # Temporary debug
    assert result == expected
```

### Test Data Management
```python
# Good - Use fixtures for test data
@pytest.fixture
def game_state():
    return {
        "player": create_player("Test"),
        "world": initialize_world()
    }

# Good - Clean up after tests
@pytest.fixture
def temp_file():
    filename = "test_save.json"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)
```

## Advanced Testing Techniques

### Property-Based Testing
```python
from hypothesis import given, strategies as st

@given(st.text(min_size=1, max_size=50))
def test_create_player_with_any_name(self, name):
    """Test player creation with any valid name."""
    player = create_player(name)
    assert player["name"] == name
    assert player["health"] == 100

@given(st.integers(min_value=1, max_value=100))
def test_heal_player_with_any_amount(self, heal_amount):
    """Test healing with any valid amount."""
    player = create_player("Test")
    player["health"] = 50
    
    heal_player(player, heal_amount)
    
    assert 50 <= player["health"] <= 100
```

### Mutation Testing
```bash
# Install mutmut
pip install mutmut

# Run mutation testing
mutmut run

# View results
mutmut results
```

### Contract Testing
```python
def test_player_creation_contract():
    """Test that create_player follows its contract."""
    player = create_player("Test")
    
    # Contract: Player must have required fields
    required_fields = ["name", "health", "inventory", "location", "gold"]
    for field in required_fields:
        assert field in player
    
    # Contract: Health must be positive
    assert player["health"] > 0
    
    # Contract: Inventory must be a list
    assert isinstance(player["inventory"], list)
```

This testing guide provides a comprehensive framework for ensuring Kevin's Adventure Game is thoroughly tested, maintainable, and reliable. Follow these guidelines to write effective tests that catch bugs early and provide confidence in code changes.

