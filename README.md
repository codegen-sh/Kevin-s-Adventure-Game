🌈🌈
# Kevin's Adventure Game

A text-based adventure game featuring Kevin's journey through various locations with items, weather systems, and mythical encounters.

## Features

- **Player System**: Create and manage your character with inventory and status tracking
- **Dynamic World**: Explore different locations with unique descriptions and interactions
- **Weather System**: Experience changing weather conditions that affect gameplay
- **Item Management**: Collect, use, and manage various items throughout your adventure
- **Mythical Encounters**: Discover and interact with mythical creatures and elements
- **Save/Load System**: Save your progress and continue your adventure later
- **Interactive Commands**: Use various commands to navigate and interact with the world

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Ensure you have Python 3.x installed on your system

3. Run the game:
   ```bash
   python main.py
   ```

## Game Structure

- `main.py` - Main game loop and entry point
- `game/` - Core game mechanics
  - `player.py` - Player creation and management
  - `world.py` - World initialization and location management
  - `items.py` - Item system and inventory management
  - `weather.py` - Weather system implementation
  - `mythical.py` - Mythical creatures and encounters
  - `actions.py` - Game action handling
  - `state.py` - Game state management
- `locations/` - Location definitions and descriptions
- `utils/` - Utility functions for save/load and text formatting

## Usage

1. Start the game by running `python main.py`
2. Choose whether to load a saved game or start new
3. Follow the prompts and explore the world
4. Type 'help' at any time to see available commands
5. Use the save feature to preserve your progress

## Commands

The game supports various interactive commands that you can discover by typing 'help' during gameplay. Navigate through different locations, interact with items, and experience the adventure!

---

*Last updated: January 2025*
