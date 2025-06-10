🌈🌈
# Kevin's Adventure Game

A text-based adventure game where players navigate through various locations, interact with items, and experience random events.

Last updated: May 3, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Features

- Multiple locations to explore (Forest, Mountain, Village)
- Item collection and inventory management
- Weather system that affects gameplay
- Random events and encounters
- Save/load game functionality
- Mythical creatures and characters

## Project Structure

- `game/`: Core game mechanics and objects
  - `items.py`: Item definitions and properties
  - `player.py`: Player character and stats
  - `state.py`: Game state management
  - `weather.py`: Weather system
  - `world.py`: World map and navigation
  - `mythical.py`: Mythical creatures and events
- `locations/`: Game world locations
  - `forest.py`: Forest location and events
  - `mountain.py`: Mountain location and events
  - `village.py`: Village location and events
- `utils/`: Utility functions
  - `random_events.py`: Random event generation
  - `save_load.py`: Game save/load functionality
  - `text_formatting.py`: Text formatting utilities
- `main.py`: Main game entry point

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Run the game:
   ```
   python main.py
   ```

## Gameplay

1. Follow the prompts in the game.
2. Type 'help' at any time to see available commands.
3. Explore different locations and collect items.
4. Watch out for changing weather and random events!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

