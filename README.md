# Kevin's Adventure Game

A text-based adventure game where you explore a world of mystery and danger as you navigate through forests, caves, villages, and mountains.

## Game Overview

In Kevin's Adventure Game, you play as a character exploring a fantasy world. You can:

- Travel between different locations (Village, Forest, Mountain, Cave)
- Collect and use items
- Interact with characters and creatures
- Complete quests
- Experience random events and weather changes

## How to Play

1. Run the game:
   ```
   python main.py
   ```

2. Follow the on-screen prompts to navigate the game world.

3. Use these commands to interact with the game:
   - `move [location]`: Move to a new location
   - `look`: Examine your surroundings
   - `inventory`: Check your inventory
   - `pickup [item]`: Pick up an item
   - `drop [item]`: Drop an item from your inventory
   - `use [item]`: Use an item
   - `examine [item]`: Get a description of an item
   - `status`: Check your current status
   - `interact`: Interact with your current location
   - `weather`: Check the current weather
   - `help`: Show the help message
   - `quit`: Save and exit the game

## Game Structure

The game has been refactored to use an object-oriented architecture:

- `src/game/`: Core game classes and logic
  - `player.py`: Player class for managing player state
  - `world.py`: World class for managing the game world
  - `location.py`: Base Location class for all locations
  - `item.py`: Item class and item registry
  - `weather.py`: Weather system
  - `game.py`: Main game controller
  - `actions.py`: Functions for handling player actions

- `src/locations/`: Location-specific classes
  - `village.py`: Village location
  - `forest.py`: Forest location
  - `mountain.py`: Mountain location
  - `cave.py`: Cave location

- `src/utils/`: Utility functions
  - `text_formatting.py`: Text formatting utilities
  - `random_events.py`: Random event generation
  - `save_load.py`: Save/load functionality

## Save/Load System

The game includes a save/load system that allows you to save your progress and continue later. Save files are stored in the `saves` directory.

## Weather System

The game includes a dynamic weather system that affects gameplay. Different weather conditions can impact your abilities and the environment.

## Enjoy Your Adventure!

Explore, discover, and have fun in the world of Kevin's Adventure Game!

