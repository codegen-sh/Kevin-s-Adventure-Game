🌈🌈
# Kevin's Adventure Game

This is a text-based adventure game where you explore a magical world filled with different locations, items to collect, and challenges to overcome.

## Game Overview

In Kevin's Adventure Game, you play as a character named Kevin who navigates through various locations including:
- A peaceful village
- A mysterious forest
- A dark cave
- A treacherous mountain

During your journey, you'll collect items, manage your health and gold, and interact with your environment.

## Features

- **Multiple Locations**: Explore different areas with unique descriptions and items
- **Inventory System**: Collect, use, and drop items throughout your adventure
- **Health & Gold Management**: Monitor your health and manage your gold currency
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience unexpected events during your journey
- **Weather System**: Dynamic weather conditions that affect gameplay

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the game directory:
   ```
   cd Kevin-s-Adventure-Game
   ```

3. Run the game:
   ```
   python main.py
   ```

## How to Play

1. When you start the game, you'll be asked if you want to load a saved game or start a new one.
2. Use text commands to navigate and interact with the world.
3. Type 'help' at any time to see a list of available commands.

### Available Commands

- `move [location]`: Move to a new location
- `look`: Examine your surroundings
- `inventory`: Check your inventory
- `pickup [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message
- `quit`: Save and exit the game

## Game Structure

The game is organized into several modules:

- `main.py`: The main game loop and entry point
- `game/`: Core game mechanics
  - `player.py`: Player character management
  - `world.py`: World structure and location management
  - `items.py`: Item definitions and interactions
  - `mythical.py`: Mythical creatures and events
  - `state.py`: Game state management
  - `weather.py`: Weather system
- `locations/`: Different game locations
  - `village.py`: Village location and interactions
  - `forest.py`: Forest location and interactions
  - `mountain.py`: Mountain location and interactions
- `utils/`: Utility functions
  - `text_formatting.py`: Text display formatting
  - `save_load.py`: Game saving and loading
  - `random_events.py`: Random event generation

## Contributing

This is a test repository for TinySitter. Feel free to explore the code and suggest improvements!

## License

This project is open source and available for educational purposes.
