🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with mysteries, challenges, and treasures.

Last updated: May 1, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Description

Kevin's Adventure Game is an interactive text-based adventure where players navigate through various locations including forests, mountains, and villages. Players can collect items, interact with characters, and uncover the secrets of this magical realm while facing random events and challenges.

## Features

- Explore multiple unique locations (forest, mountain, village)
- Collect and use various items
- Character interaction system
- Dynamic weather effects
- Save and load game progress
- Random events and encounters
- Inventory management

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

## Game Commands

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

- `main.py`: Main game loop and entry point
- `game/`: Core game mechanics
  - `player.py`: Player character management
  - `world.py`: World state and location management
  - `items.py`: Item definitions and interactions
  - `weather.py`: Dynamic weather system
  - `mythical.py`: Mythical creatures and encounters
- `locations/`: Different game locations
  - `forest.py`: Forest location and events
  - `mountain.py`: Mountain location and events
  - `village.py`: Village location and events
- `utils/`: Utility functions
  - `save_load.py`: Game saving and loading functionality
  - `text_formatting.py`: Text display formatting
  - `random_events.py`: Random event generation

## Saving and Loading

The game automatically saves your progress when you quit. You can load a previous save when starting the game by selecting the "load game" option.

## Contributing

This is a test repository. Feel free to fork and experiment with the code!

## License

This project is open source and available for educational purposes.

