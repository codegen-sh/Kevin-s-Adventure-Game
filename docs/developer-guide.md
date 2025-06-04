# Developer Setup Guide

## Overview

This guide will help you set up a development environment for Kevin's Adventure Game and get you started with contributing to the project.

## Prerequisites

### System Requirements

- **Python**: 3.7 or higher
- **Git**: For version control
- **Text Editor/IDE**: VS Code, PyCharm, or your preferred editor

### Recommended Tools

- **Virtual Environment**: `venv` or `conda`
- **Code Formatter**: `black`
- **Linter**: `flake8` or `pylint`
- **Type Checker**: `mypy`

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
cd Kevin-s-Adventure-Game
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Or install the package in development mode
pip install -e .
```

### 4. Run the Game

```bash
python main.py
```

### 5. Run Tests (when available)

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=game --cov=utils --cov=locations
```

## Development Environment Setup

### IDE Configuration

#### VS Code Setup

1. Install the Python extension
2. Configure the Python interpreter to use your virtual environment
3. Install recommended extensions:
   - Python
   - Python Docstring Generator
   - GitLens
   - Black Formatter

Create `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "editor.formatOnSave": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    }
}
```

#### PyCharm Setup

1. Open the project directory
2. Configure the Python interpreter to use your virtual environment
3. Enable code inspections for Python
4. Configure Black as the code formatter
5. Set up run configurations for main.py

### Code Quality Tools

#### Black (Code Formatting)

```bash
# Format all Python files
black .

# Check what would be formatted
black --check .

# Format specific files
black game/ utils/ locations/
```

#### Flake8 (Linting)

```bash
# Lint all Python files
flake8 .

# Lint specific directories
flake8 game/ utils/ locations/

# Generate HTML report
flake8 --format=html --htmldir=flake8-report .
```

#### MyPy (Type Checking)

```bash
# Type check all files
mypy .

# Type check specific modules
mypy game/ utils/

# Generate report
mypy --html-report mypy-report .
```

### Pre-commit Hooks

Set up pre-commit hooks to automatically run code quality checks:

```bash
# Install pre-commit
pip install pre-commit

# Install the git hook scripts
pre-commit install

# Run against all files
pre-commit run --all-files
```

## Project Structure

```
Kevin-s-Adventure-Game/
├── game/                   # Core game logic
│   ├── __init__.py
│   ├── actions.py         # Action processing
│   ├── items.py           # Item system
│   ├── mythical.py        # Mythical creatures
│   ├── player.py          # Player management
│   ├── state.py           # Game state
│   ├── weather.py         # Weather system
│   └── world.py           # World management
├── locations/             # Location-specific modules
│   ├── __init__.py
│   ├── cave.py
│   ├── forest.py
│   ├── mountain.py
│   └── village.py
├── utils/                 # Utility functions
│   ├── __init__.py
│   ├── random_events.py
│   ├── save_load.py
│   └── text_formatting.py
├── docs/                  # Documentation
│   ├── architecture.md
│   ├── developer-guide.md
│   └── ...
├── tests/                 # Test files
│   ├── __init__.py
│   ├── test_player.py
│   └── ...
├── scripts/               # Development scripts
│   ├── lint.sh
│   ├── format.sh
│   └── test.sh
├── tools/                 # Development tools
│   ├── validate_content.py
│   └── ...
├── main.py               # Entry point
├── requirements.txt      # Runtime dependencies
├── requirements-dev.txt  # Development dependencies
├── setup.py             # Package setup
└── README.md            # Project overview
```

## Development Workflow

### 1. Creating a New Feature

```bash
# Create a new branch
git checkout -b feature/your-feature-name

# Make your changes
# ... edit files ...

# Run tests and quality checks
python -m pytest
black .
flake8 .
mypy .

# Commit your changes
git add .
git commit -m "Add your feature description"

# Push to your fork
git push origin feature/your-feature-name

# Create a pull request
```

### 2. Working with Locations

To add a new location:

1. Create a new file in `locations/` (e.g., `desert.py`)
2. Implement required functions:
   ```python
   def explore_desert(player, world):
       """Handle desert exploration."""
       pass
   
   def get_desert_description():
       """Get desert description."""
       return "A vast, sandy desert..."
   ```
3. Add the location to `world.py` in `initialize_world()`
4. Update location connections
5. Add tests for the new location

### 3. Working with Items

To add a new item:

1. Add item description to `items.py`:
   ```python
   item_descriptions["new_item"] = "Description of the new item."
   ```
2. Implement item usage function:
   ```python
   def use_new_item(player, world):
       """Handle new item usage."""
       # Implementation here
       pass
   ```
3. Add the item to appropriate locations
4. Add tests for item functionality

### 4. Working with Events

To add a new random event:

1. Add event function to `random_events.py`:
   ```python
   def new_random_event(player, world):
       """Handle new random event."""
       # Implementation here
       pass
   ```
2. Add event to the event pool in `generate_random_event()`
3. Test the event thoroughly

## Testing Guidelines

### Writing Tests

Create test files in the `tests/` directory:

```python
# tests/test_player.py
import unittest
from game.player import create_player, add_item_to_inventory

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = create_player("Test Player")
    
    def test_create_player(self):
        self.assertEqual(self.player["name"], "Test Player")
        self.assertEqual(self.player["health"], 100)
        self.assertEqual(self.player["inventory"], [])
    
    def test_add_item_to_inventory(self):
        add_item_to_inventory(self.player, "sword")
        self.assertIn("sword", self.player["inventory"])

if __name__ == "__main__":
    unittest.main()
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_player.py

# Run with verbose output
python -m pytest -v

# Run with coverage
python -m pytest --cov=game --cov=utils --cov=locations

# Generate HTML coverage report
python -m pytest --cov=game --cov=utils --cov=locations --cov-report=html
```

### Test Coverage Goals

- Aim for 80%+ code coverage
- Test all public functions
- Test error conditions and edge cases
- Test integration between modules

## Debugging

### Common Issues

1. **Import Errors**: Make sure you're in the project root directory
2. **Module Not Found**: Check your Python path and virtual environment
3. **Save File Issues**: Check the `saves/` directory permissions

### Debugging Tools

```python
# Add debug prints
import pdb; pdb.set_trace()  # Python debugger

# Logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Debug message")
```

### Game State Debugging

Use the debug tools in `tools/debug_game.py`:

```bash
python tools/debug_game.py --player-info
python tools/debug_game.py --world-state
python tools/debug_game.py --validate-save saves/save_file.json
```

## Performance Profiling

### Basic Profiling

```python
import cProfile
import pstats

# Profile the main game loop
cProfile.run('main()', 'profile_stats')
stats = pstats.Stats('profile_stats')
stats.sort_stats('cumulative').print_stats(10)
```

### Memory Profiling

```bash
# Install memory profiler
pip install memory-profiler

# Profile memory usage
python -m memory_profiler main.py
```

### Using Profiling Tools

```bash
# Use the built-in profiling tools
python tools/profile_game.py
python tools/memory_profiler.py
```

## Documentation

### Writing Documentation

- Use clear, concise language
- Include code examples
- Document all public functions with docstrings
- Update documentation when making changes

### Docstring Format

Use Google-style docstrings:

```python
def example_function(param1, param2):
    """
    Brief description of the function.
    
    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2
        
    Returns:
        bool: Description of return value
        
    Raises:
        ValueError: When param1 is invalid
        
    Example:
        >>> result = example_function("test", 42)
        >>> print(result)
        True
    """
    pass
```

### Building Documentation

```bash
# Install Sphinx
pip install sphinx sphinx-rtd-theme

# Build documentation
cd docs/
make html

# View documentation
open _build/html/index.html
```

## Contributing Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use Black for code formatting
- Maximum line length: 88 characters
- Use meaningful variable and function names
- Add type hints where appropriate

### Commit Messages

Use conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

Examples:
- `feat(player): add experience point system`
- `fix(save): handle corrupted save files gracefully`
- `docs(api): update function documentation`
- `test(items): add tests for item usage`

### Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Update documentation
7. Submit a pull request

### Code Review Checklist

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New functionality has tests
- [ ] Documentation is updated
- [ ] No breaking changes (or properly documented)
- [ ] Performance impact is acceptable

## Getting Help

### Resources

- **Documentation**: Check the `docs/` directory
- **Issues**: GitHub Issues for bug reports and feature requests
- **Discussions**: GitHub Discussions for questions and ideas

### Community Guidelines

- Be respectful and inclusive
- Help others learn and grow
- Share knowledge and best practices
- Provide constructive feedback

### Reporting Issues

When reporting bugs:

1. Check if the issue already exists
2. Provide a clear description
3. Include steps to reproduce
4. Add relevant error messages
5. Specify your environment (OS, Python version)

### Suggesting Features

When suggesting new features:

1. Explain the use case
2. Describe the proposed solution
3. Consider alternative approaches
4. Discuss potential impact on existing code

## Advanced Topics

### Plugin Development

See `docs/plugin-development.md` for creating game plugins.

### Content Creation

See `docs/content-creation.md` for adding new game content.

### Performance Optimization

See `docs/performance-guide.md` for optimization techniques.

### Architecture Deep Dive

See `docs/architecture.md` for detailed architecture information.

This guide should get you started with development. For more specific topics, check the other documentation files in the `docs/` directory.

