# Kevin's Adventure Game

A text-based adventure game where you play as Kevin, exploring a world of mystery and danger.

## Game Overview

In Kevin's Adventure Game, you navigate through various locations including forests, caves, villages, and mountains. You can collect items, interact with characters, and uncover the secrets of this magical realm.

## Features

- **Multiple Locations**: Explore the Village, Forest, Cave, and Mountain, each with unique interactions and items.
- **Inventory System**: Collect, use, and manage items throughout your adventure.
- **Weather System**: Experience different weather conditions that affect gameplay.
- **Quest System**: Complete quests for rewards and to advance the story.
- **Save/Load System**: Save your progress and continue your adventure later.
- **Random Events**: Encounter various random events that make each playthrough unique.
- **Mythical Creatures**: Interact with mythical creatures like phoenixes, unicorns, and dragons.
- **Web Interface**: Play the game through a modern web browser with an intuitive UI.

## Installation

### Command Line Version

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Run the game:
   ```
   python main.py
   ```

### Web Version

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

4. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## How to Play

### Command Line Version

1. Run `python main.py` to start the game
2. Choose to load a saved game or start a new one
3. Use text commands to navigate and interact with the world

### Web Version

1. Run `python app.py` to start the web server
2. Open your browser and navigate to `http://localhost:5000`
3. Enter your character name and click "Start Adventure"
4. Use the command input or the quick command buttons to play the game

## Commands

- `move [location]`: Move to a new location
- `look`: Examine your surroundings
- `inventory`: Check your inventory
- `pickup [item]` or `take [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message
- `quit`: Save and exit the game

## Code Structure

The game is built with a modular, object-oriented architecture:

- `game/`: Core game mechanics
  - `actions.py`: Handles player actions
  - `entity.py`: Base class for all game entities
  - `items.py`: Item management and effects
  - `mythical.py`: Mythical creature interactions
  - `player.py`: Player character management
  - `state.py`: Game state tracking
  - `weather.py`: Weather system
  - `world.py`: World and location management
- `locations/`: Location-specific interactions
  - `cave.py`: Cave location interactions
  - `forest.py`: Forest location interactions
  - `mountain.py`: Mountain location interactions
  - `village.py`: Village location interactions
- `utils/`: Utility functions
  - `random_events.py`: Random event generation
  - `save_load.py`: Save and load functionality
  - `text_formatting.py`: Text formatting utilities
- `main.py`: Command line game loop and initialization
- `app.py`: Flask web application
- `static/`: Static files for the web interface
  - `css/`: CSS stylesheets
  - `js/`: JavaScript files
  - `images/`: Game images
- `templates/`: HTML templates for the web interface

## Development

The game is designed with extensibility in mind. New locations, items, creatures, and features can be added by extending the existing classes and integrating them into the game world.

### Adding a New Location

1. Create a new file in the `locations/` directory
2. Implement the location's interaction functions
3. Add the location to the world initialization in `world.py`
4. Add connections to the location from other locations

### Adding a New Item

1. Add the item to the `ITEM_DESCRIPTIONS` dictionary in `items.py`
2. Implement the item's use effect in the `use_item` function
3. Add the item to a location's items list in `world.py`

## Future Enhancements

- Combat system
- More locations to explore
- Character progression and skills
- More complex quests and storylines
- Enhanced NPC interactions
- Day/night cycle affecting gameplay
- Multiplayer functionality
- Mobile-responsive design
- Save/load functionality in the web interface

