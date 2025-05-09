🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a fantasy world, encounter mythical creatures, and embark on exciting quests.

Last updated: May 9, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Features

- Explore multiple locations including forests, mountains, and villages
- Encounter mythical creatures and interact with NPCs
- Collect items and manage your inventory
- Dynamic weather system that affects gameplay
- Save and load game progress
- Random events that make each playthrough unique

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

1. Create a new character or load a saved game
2. Explore different locations by using directional commands (north, south, east, west)
3. Interact with objects and characters using commands like "talk", "take", "use", etc.
4. Type 'help' at any time to see available commands
5. Save your progress with the "save" command

## Game Structure

- `game/` - Core game mechanics and objects
  - `items.py` - Item definitions and inventory management
  - `mythical.py` - Mythical creatures and encounters
  - `player.py` - Player character stats and actions
  - `state.py` - Game state management
  - `weather.py` - Dynamic weather system
  - `world.py` - World map and navigation

- `locations/` - Different game locations
  - `forest.py` - Forest area with unique encounters
  - `mountain.py` - Mountain area with challenges
  - `village.py` - Village with NPCs and quests

- `utils/` - Utility functions
  - `random_events.py` - Random event generation
  - `save_load.py` - Game saving and loading functionality
  - `text_formatting.py` - Text display utilities

## Contributing

This is a test repository. Feel free to fork and experiment with the code!

## License

This project is open source and available for educational purposes.

