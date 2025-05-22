# Kevin's Adventure Game

A text-based adventure game where you explore a world of mystery and danger as you navigate through forests, caves, villages, and mountains.

## Features

- Explore different locations: Village, Forest, Cave, Mountain
- Collect and use items
- Interact with characters and environments
- Random events and encounters
- Save and load game progress
- Weather system that affects gameplay

## Installation

### Prerequisites

- Python 3.8 or higher

### From PyPI (recommended)

```bash
pip install kevin-adventure-game
```

### From Source

1. Clone the repository:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Install the package:
   ```bash
   pip install -e .
   ```

## Usage

### Starting the Game

```bash
# Run the game with default settings
kevin-adventure

# Start a new game (ignore existing saves)
kevin-adventure --new

# Load the most recent save
kevin-adventure --load

# Set a custom player name
kevin-adventure --player-name "YourName"

# Enable debug mode
kevin-adventure --debug
```

### Game Commands

- `move [location]`: Move to a new location
- `look`: Examine your surroundings
- `inventory`: Check your inventory
- `pickup [item]` or `take [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message
- `quit`: Save and exit the game

## Development

### Setting Up Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=kevin_adventure_game

# Generate coverage report
pytest --cov=kevin_adventure_game --cov-report=html
```

### Code Style

This project uses Black for code formatting and Flake8 for linting:

```bash
# Format code
black kevin_adventure_game tests

# Sort imports
isort kevin_adventure_game tests

# Lint code
flake8 kevin_adventure_game tests
```

## Project Structure

```
kevin_adventure_game/
├── game/               # Core game mechanics
│   ├── actions.py      # Player action handling
│   ├── items.py        # Item definitions and interactions
│   ├── mythical.py     # Mythical creatures
│   ├── player.py       # Player state and actions
│   ├── state.py        # Game state management
│   ├── weather.py      # Weather system
│   └── world.py        # World structure and navigation
├── locations/          # Location-specific interactions
│   ├── cave.py         # Cave location
│   ├── forest.py       # Forest location
│   ├── mountain.py     # Mountain location
│   └── village.py      # Village location
├── utils/              # Utility functions
│   ├── random_events.py    # Random event generation
│   ├── save_load.py        # Game saving and loading
│   └── text_formatting.py  # Text formatting utilities
└── main.py             # Main entry point
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Created by Kevin
- Refactored and improved by the Codegen team

