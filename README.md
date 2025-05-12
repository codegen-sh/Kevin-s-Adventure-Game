🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: May 12, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players can:
- Explore different locations including forests, mountains, and villages
- Collect and use various items
- Encounter mythical creatures
- Experience dynamic weather conditions
- Save and load game progress

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

## Gameplay

1. When you start the game, you'll be asked if you want to load a saved game or start a new one.
2. Navigate through the world by typing commands like "go north", "go south", etc.
3. Interact with the environment using commands like "look", "take [item]", "use [item]".
4. Type "help" at any time to see available commands.
5. Type "quit" to save your progress and exit the game.

## Game Structure

- `game/`: Core game mechanics
  - `player.py`: Player character management
  - `world.py`: World map and location management
  - `items.py`: Item definitions and interactions
  - `mythical.py`: Mythical creatures and encounters
  - `weather.py`: Dynamic weather system
  - `state.py`: Game state management

- `locations/`: Different game locations
  - `forest.py`: Forest location and events
  - `mountain.py`: Mountain location and events
  - `village.py`: Village location and events

- `utils/`: Utility functions
  - `save_load.py`: Game saving and loading functionality
  - `text_formatting.py`: Text display formatting
  - `random_events.py`: Random event generation

## Contributing

This is a test repository. Feel free to fork and experiment with your own features!

## License

This project is open source and available for educational purposes.

