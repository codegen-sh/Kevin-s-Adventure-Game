🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: May 7, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players can:
- Explore different locations (forest, mountain, village)
- Collect and use items
- Encounter mythical creatures
- Experience dynamic weather conditions
- Save and load game progress

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
2. Navigate through the world by typing commands like "go north", "go south", etc.
3. Interact with the environment using commands like "look", "take [item]", "use [item]".
4. Type "help" at any time to see available commands.
5. Type "quit" to save your progress and exit the game.

## Game Structure

The game is organized into several modules:

- **game/**: Core game mechanics
  - `items.py`: Defines collectible items and their properties
  - `mythical.py`: Mythical creatures you might encounter
  - `player.py`: Player character management
  - `state.py`: Game state tracking
  - `weather.py`: Dynamic weather system
  - `world.py`: World map and location management

- **locations/**: Different areas to explore
  - `forest.py`: Forest location and events
  - `mountain.py`: Mountain location and events
  - `village.py`: Village location and events

- **utils/**: Helper functions
  - `random_events.py`: Generates random encounters
  - `save_load.py`: Game saving and loading functionality
  - `text_formatting.py`: Text display utilities

## Contributing

Feel free to fork this repository and submit pull requests with new features, bug fixes, or improvements.

## License

This project is open source and available for educational purposes.

