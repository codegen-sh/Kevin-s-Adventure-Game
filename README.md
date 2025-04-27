🌈🌈
# Kevin's Adventure Game

This is a text-based adventure game where you navigate through different locations, collect items, and encounter mythical creatures.

Last updated: April 27, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Features

- Explore multiple locations including forests, mountains, and villages
- Collect and use items throughout your journey
- Encounter mythical creatures and weather events
- Save and load game progress
- Simple text-based interface

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

- `main.py`: The main game loop and entry point
- `game/`: Core game mechanics and objects
  - Player status and inventory management
  - World state and location tracking
  - Items and mythical creatures
- `locations/`: Different areas to explore
  - Forest, mountain, and village environments
- `utils/`: Helper functions
  - Save/load game functionality
  - Text formatting and display
  - Random event generation

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues for bugs and feature requests.

## License

This project is open source and available for educational purposes.
