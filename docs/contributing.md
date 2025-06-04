# Contributing to Kevin's Adventure Game

Thank you for your interest in contributing to Kevin's Adventure Game! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Process](#development-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Community](#community)

## Code of Conduct

### Our Pledge

We are committed to making participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team. All complaints will be reviewed and investigated promptly and fairly.

## Getting Started

### Prerequisites

Before contributing, make sure you have:

- Python 3.7 or higher installed
- Git for version control
- A GitHub account
- Basic understanding of Python programming

### Setting Up Your Development Environment

1. **Fork the Repository**
   ```bash
   # Fork the repo on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

4. **Verify Setup**
   ```bash
   python main.py  # Should start the game
   python -m pytest  # Should run tests (when available)
   ```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

1. **Bug Reports**: Help us identify and fix issues
2. **Feature Requests**: Suggest new functionality
3. **Code Contributions**: Implement features or fix bugs
4. **Documentation**: Improve or add documentation
5. **Testing**: Add or improve tests
6. **Content Creation**: Add new locations, items, or events

### Reporting Bugs

When reporting bugs, please include:

- **Clear Title**: Descriptive summary of the issue
- **Environment**: OS, Python version, game version
- **Steps to Reproduce**: Detailed steps to recreate the bug
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Screenshots/Logs**: If applicable
- **Additional Context**: Any other relevant information

**Bug Report Template:**
```markdown
## Bug Description
Brief description of the bug.

## Environment
- OS: [e.g., Windows 10, macOS 12.0, Ubuntu 20.04]
- Python Version: [e.g., 3.9.7]
- Game Version: [e.g., 1.0.0]

## Steps to Reproduce
1. Start the game
2. Go to the Forest
3. Use the map item
4. Error occurs

## Expected Behavior
The map should show available locations.

## Actual Behavior
Game crashes with TypeError.

## Error Message
```
TypeError: 'NoneType' object is not subscriptable
```

## Additional Context
This only happens when the player has visited the Cave first.
```

### Suggesting Features

When suggesting features, please include:

- **Use Case**: Why is this feature needed?
- **Description**: What should the feature do?
- **Implementation Ideas**: How might it work?
- **Alternatives**: Other ways to solve the problem
- **Impact**: How would this affect existing functionality?

**Feature Request Template:**
```markdown
## Feature Description
Brief description of the proposed feature.

## Use Case
Explain why this feature would be valuable.

## Detailed Description
Provide a detailed explanation of how the feature should work.

## Implementation Suggestions
Ideas for how this could be implemented.

## Alternatives Considered
Other approaches that were considered.

## Additional Context
Any other relevant information.
```

## Development Process

### Workflow

1. **Choose an Issue**: Look for issues labeled `good first issue` or `help wanted`
2. **Create a Branch**: Create a feature branch for your work
3. **Make Changes**: Implement your changes following our coding standards
4. **Test**: Ensure all tests pass and add new tests if needed
5. **Document**: Update documentation as necessary
6. **Submit PR**: Create a pull request with a clear description

### Branch Naming

Use descriptive branch names:

- `feature/add-desert-location`
- `fix/save-file-corruption`
- `docs/update-api-reference`
- `test/add-player-tests`

### Commit Messages

Follow the conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `style`: Code style changes
- `perf`: Performance improvements
- `chore`: Maintenance tasks

**Examples:**
```
feat(locations): add desert location with sandstorm events

Add a new desert location with unique events including sandstorms,
oasis discoveries, and mirage encounters. Includes comprehensive
tests and documentation.

Closes #123
```

```
fix(save): handle corrupted save files gracefully

Previously, corrupted save files would crash the game. Now the
game detects corruption and offers to start a new game or load
a different save file.

Fixes #456
```

### Pull Request Process

1. **Create PR**: Submit a pull request to the main repository
2. **Fill Template**: Use the PR template and provide all requested information
3. **Review Process**: Respond to feedback and make requested changes
4. **Approval**: Wait for approval from maintainers
5. **Merge**: Your PR will be merged once approved

**Pull Request Template:**
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] I have tested the changes manually

## Documentation
- [ ] I have updated the documentation accordingly
- [ ] I have added docstrings to new functions/classes

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] My changes generate no new warnings
- [ ] Any dependent changes have been merged and published

## Related Issues
Closes #(issue number)
```

## Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line Length**: Maximum 88 characters (Black default)
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Use double quotes for strings
- **Imports**: Group imports (standard library, third-party, local)

### Code Formatting

Use Black for automatic code formatting:

```bash
# Format all files
black .

# Check formatting
black --check .
```

### Linting

Use Flake8 for linting:

```bash
# Lint all files
flake8 .

# Lint specific files
flake8 game/ utils/ locations/
```

### Type Hints

Add type hints to new code:

```python
def create_player(name: str) -> dict:
    """Create a new player with the given name."""
    return {
        "name": name,
        "health": 100,
        "inventory": [],
        "location": "Village",
        "gold": 100
    }
```

### Docstrings

Use Google-style docstrings:

```python
def move_player(player: dict, new_location: str) -> None:
    """
    Move the player to a new location.
    
    Args:
        player: The player object to modify
        new_location: The name of the destination location
        
    Side Effects:
        Updates the player's location and prints a confirmation message
        
    Example:
        >>> player = create_player("Kevin")
        >>> move_player(player, "Forest")
        You moved to: Forest
    """
    player['location'] = new_location
    print(f"You moved to: {new_location}")
```

### Error Handling

Handle errors gracefully:

```python
def load_game(filename: str) -> tuple:
    """Load a game from a save file."""
    try:
        with open(f"saves/{filename}", 'r') as f:
            data = json.load(f)
        return data["player"], data["world"]
    except FileNotFoundError:
        print(f"Save file {filename} not found.")
        return None, None
    except json.JSONDecodeError:
        print(f"Save file {filename} is corrupted.")
        return None, None
    except KeyError as e:
        print(f"Save file {filename} is missing required data: {e}")
        return None, None
```

## Testing Guidelines

### Writing Tests

- Write tests for all new functionality
- Test both success and failure cases
- Use descriptive test names
- Keep tests simple and focused

```python
import unittest
from game.player import create_player, add_item_to_inventory

class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.player = create_player("Test Player")
    
    def test_create_player_with_valid_name(self):
        """Test that create_player creates a player with correct attributes."""
        self.assertEqual(self.player["name"], "Test Player")
        self.assertEqual(self.player["health"], 100)
        self.assertEqual(self.player["inventory"], [])
        self.assertEqual(self.player["location"], "Village")
        self.assertEqual(self.player["gold"], 100)
    
    def test_add_item_to_inventory_success(self):
        """Test that items are correctly added to inventory."""
        add_item_to_inventory(self.player, "sword")
        self.assertIn("sword", self.player["inventory"])
        self.assertEqual(len(self.player["inventory"]), 1)
    
    def test_add_multiple_items_to_inventory(self):
        """Test that multiple items can be added to inventory."""
        items = ["sword", "potion", "map"]
        for item in items:
            add_item_to_inventory(self.player, item)
        
        for item in items:
            self.assertIn(item, self.player["inventory"])
        self.assertEqual(len(self.player["inventory"]), 3)
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_player.py

# Run with coverage
python -m pytest --cov=game --cov=utils --cov=locations

# Run with verbose output
python -m pytest -v
```

### Test Coverage

- Aim for 80%+ code coverage
- Focus on testing public interfaces
- Test error conditions and edge cases
- Don't test private implementation details

## Documentation

### Types of Documentation

1. **Code Documentation**: Docstrings and inline comments
2. **API Documentation**: Function and class references
3. **User Documentation**: How to use the game
4. **Developer Documentation**: How to contribute and extend

### Writing Good Documentation

- **Be Clear**: Use simple, direct language
- **Be Complete**: Cover all important aspects
- **Be Accurate**: Keep documentation up to date
- **Include Examples**: Show how to use features
- **Consider Your Audience**: Write for the intended readers

### Documentation Standards

- Use Markdown for documentation files
- Include code examples in docstrings
- Update documentation when changing code
- Review documentation for clarity and accuracy

## Community

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and general discussion
- **Pull Requests**: Code review and collaboration

### Getting Help

If you need help:

1. Check existing documentation
2. Search GitHub issues for similar problems
3. Ask questions in GitHub Discussions
4. Reach out to maintainers if needed

### Helping Others

Ways to help the community:

- Answer questions in discussions
- Review pull requests
- Help with documentation
- Mentor new contributors
- Share your experiences

### Recognition

We appreciate all contributions and will:

- Credit contributors in release notes
- Maintain a contributors list
- Highlight significant contributions
- Provide feedback and support

## Specific Contribution Areas

### Adding New Locations

To add a new location:

1. Create a new file in `locations/` directory
2. Implement required functions:
   - `explore_[location](player, world)`
   - `get_[location]_description()`
   - `get_[location]_items()`
3. Add location to world initialization
4. Update location connections
5. Add comprehensive tests
6. Update documentation

### Adding New Items

To add a new item:

1. Add item description to `items.py`
2. Implement item usage function
3. Add item to appropriate locations
4. Test item functionality
5. Update documentation

### Adding New Events

To add a new random event:

1. Create event function in `random_events.py`
2. Add event to event generation system
3. Test event thoroughly
4. Document event behavior

### Improving Performance

Performance improvements are welcome:

1. Profile the code to identify bottlenecks
2. Implement optimizations
3. Measure performance impact
4. Ensure changes don't break functionality
5. Document performance improvements

### Enhancing User Experience

UX improvements might include:

- Better error messages
- Improved help system
- Enhanced text formatting
- More intuitive commands
- Better save/load experience

## Release Process

### Versioning

We use semantic versioning (SemVer):

- **Major** (X.0.0): Breaking changes
- **Minor** (0.X.0): New features, backward compatible
- **Patch** (0.0.X): Bug fixes, backward compatible

### Release Checklist

Before releasing:

- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Version number is bumped
- [ ] Changelog is updated
- [ ] Release notes are prepared

## Questions?

If you have questions about contributing, please:

1. Check this document first
2. Search existing GitHub issues
3. Create a new issue with the `question` label
4. Join our GitHub Discussions

Thank you for contributing to Kevin's Adventure Game! Your efforts help make this project better for everyone.

