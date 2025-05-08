🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

## About the Game

Kevin's Adventure Game is a simple yet engaging text-based adventure where players can explore various locations, collect items, and interact with the environment. The game features:

- Multiple locations to explore (Forest, Mountain, Village)
- Item collection and inventory management
- Weather system that affects gameplay
- Random events that create unique experiences
- Save/load functionality to continue your adventure

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

1. Follow the text prompts that appear on screen
2. Type commands to navigate and interact with the world
3. Common commands include:
   - `go [direction]` - Move in a direction (north, south, east, west)
   - `look` - Examine your surroundings
   - `inventory` or `i` - Check your inventory
   - `take [item]` - Pick up an item
   - `drop [item]` - Drop an item from your inventory
   - `use [item]` - Use an item in your inventory
   - `save` - Save your game progress
   - `load` - Load a saved game
   - `help` - Display available commands
   - `quit` - Exit the game

## Game Structure

The game is organized into several modules:
- `game/` - Core game mechanics and objects
  - Player stats and inventory management
  - World state tracking
  - Weather system
  - Mythical creatures
- `locations/` - Different areas to explore
  - Forest with hidden treasures
  - Mountain with challenging terrain
  - Village with NPCs to interact with
- `utils/` - Helper functions
  - Random event generation
  - Save/load functionality
  - Text formatting for better user experience

## Contributing

Feel free to fork this repository and add new features! Some ideas for contributions:
- New locations to explore
- Additional items with special effects
- More complex NPCs with dialogue
- Quest system
- Combat mechanics

## License

This project is open source and available for educational purposes.

Last updated: May 8, 2025

