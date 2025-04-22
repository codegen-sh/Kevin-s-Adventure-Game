🌈🌈
# Kevin's Adventure Game

This is a text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: April 22, 2025
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Features

- Explore multiple locations including forests, mountains, and villages
- Collect and use items throughout your journey
- Experience dynamic weather effects
- Encounter mythical creatures
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

1. Start a new game or load a saved game
2. Navigate through different locations using directional commands
3. Interact with the environment using simple text commands
4. Collect items to help you on your journey
5. Type 'help' at any time to see available commands
6. Type 'quit' to save your progress and exit the game

## Game Structure

- `game/`: Core game mechanics
  - `items.py`: Item definitions and interactions
  - `player.py`: Player character management
  - `world.py`: World state and navigation
  - `weather.py`: Dynamic weather system
  - `mythical.py`: Mythical creatures encounters
  
- `locations/`: Different game locations
  - `forest.py`: Forest location and events
  - `mountain.py`: Mountain location and events
  - `village.py`: Village location and events
  
- `utils/`: Utility functions
  - `random_events.py`: Random event generation
  - `save_load.py`: Game saving and loading
  - `text_formatting.py`: Text display formatting

## Contributing

This is a test repository for TinySitter. Feel free to explore the code and suggest improvements!
