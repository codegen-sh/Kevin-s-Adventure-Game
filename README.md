🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world, collect items, and embark on exciting quests.

## About the Game

Kevin's Adventure Game is a simple yet engaging text-based adventure where players can:
- Explore different locations (Village, Forest, Cave, Mountain)
- Collect and use items
- Interact with the environment
- Save and load game progress
- Experience random events and weather changes

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the project directory:
   ```
   cd Kevin-s-Adventure-Game
   ```

3. Run the game:
   ```
   python main.py
   ```

## Game Controls

The game uses simple text commands:

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
  - `player.py`: Player creation and management
  - `world.py`: World creation and location management
  - `items.py`: Item definitions and interactions
  - `mythical.py`: Mythical creatures and events
  - `state.py`: Game state management
  - `weather.py`: Weather system
- `locations/`: Different game locations
  - `village.py`: Village location and interactions
  - `forest.py`: Forest location and interactions
  - `mountain.py`: Mountain location and interactions
- `utils/`: Utility functions
  - `save_load.py`: Game saving and loading
  - `text_formatting.py`: Text formatting utilities
  - `random_events.py`: Random event generation

## Save System

The game includes a save/load system that allows players to:
- Save their progress when quitting
- Load a previous save file
- View all available save files
- Automatically generate timestamped save files

## Contributing

This is a test repository for TinySitter. Feel free to explore the code and make improvements!

## License

This project is open source and available for educational purposes.
