🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with mysteries, challenges, and adventures.

## Overview

Kevin's Adventure Game is an interactive text-based adventure where players navigate through various locations, collect items, interact with the environment, and experience random events. The game features a save/load system allowing players to continue their adventure at a later time.

## Features

- **Immersive World**: Explore forests, mountains, villages, and more
- **Item System**: Collect, use, and manage items in your inventory
- **Weather Effects**: Experience different weather conditions that affect gameplay
- **Mythical Creatures**: Encounter various mythical beings throughout your journey
- **Save/Load System**: Save your progress and continue your adventure later

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
2. Follow the on-screen prompts and type commands to interact with the game world.
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

- `main.py`: Entry point of the game
- `game/`: Core game mechanics and objects
  - `player.py`: Player character functionality
  - `world.py`: World map and location management
  - `items.py`: Item definitions and interactions
  - `state.py`: Game state management
  - `weather.py`: Weather system
  - `mythical.py`: Mythical creatures
- `locations/`: Different game locations
  - `forest.py`: Forest location
  - `mountain.py`: Mountain location
  - `village.py`: Village location
- `utils/`: Utility functions
  - `save_load.py`: Save and load game functionality
  - `text_formatting.py`: Text display utilities
  - `random_events.py`: Random event generation

## Contributing

Contributions to improve the game are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is open source and available for educational and entertainment purposes.
