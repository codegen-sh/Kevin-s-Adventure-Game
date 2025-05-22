# Contributing to Kevin's Adventure Game

Thank you for considering contributing to Kevin's Adventure Game! This document provides guidelines and instructions for contributing to the project.

## Development Environment

### Setting Up

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install development dependencies:
   ```bash
   make dev-install
   # or
   pip install -e ".[dev]"
   ```

### Development Workflow

1. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes
3. Format your code:
   ```bash
   make format
   # or
   black kevin_adventure_game tests
   isort kevin_adventure_game tests
   ```

4. Run the linter:
   ```bash
   make lint
   # or
   flake8 kevin_adventure_game tests
   ```

5. Run tests:
   ```bash
   make test
   # or
   pytest
   ```

6. Commit your changes:
   ```bash
   git commit -m "Add your meaningful commit message here"
   ```

7. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

8. Create a Pull Request on GitHub

## Code Style

This project follows the [Black](https://black.readthedocs.io/en/stable/) code style. Please ensure your code is formatted with Black before submitting a pull request.

## Testing

All new features should include tests. Run the test suite with:

```bash
make test
```

To run tests with coverage:

```bash
make test-cov
```

## Documentation

Please update documentation when changing code:

- Update docstrings for any modified functions/classes
- Update README.md if necessary
- Add comments for complex logic

## Adding New Features

### New Locations

To add a new location:

1. Create a new file in the `kevin_adventure_game/locations/` directory
2. Implement the location's interaction function
3. Add the location to the world initialization in `kevin_adventure_game/game/world.py`
4. Connect it to existing locations

### New Items

To add new items:

1. Add the item to the item descriptions in `kevin_adventure_game/game/items.py`
2. Implement the item's use function in the same file
3. Add the item to appropriate locations

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update the version number in `kevin_adventure_game/__init__.py` following [Semantic Versioning](https://semver.org/)
3. The PR will be merged once it passes all checks and receives approval

## Code of Conduct

Please be respectful and inclusive in all interactions related to this project.

## Questions?

If you have any questions, feel free to open an issue on GitHub.

