🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with challenges, treasures, and mythical creatures.

## About the Game

Kevin's Adventure Game is an interactive text-based adventure where players navigate through different locations, interact with characters, collect items, and face various challenges. The game features dynamic weather systems, random events, and a save/load functionality to continue your adventure later.

## Game Features

- **Multiple Locations**: Explore the forest, mountain, and village areas
- **Item Collection**: Find and use various items throughout your journey
- **Weather System**: Dynamic weather that affects gameplay
- **Mythical Creatures**: Encounter and interact with magical beings
- **Save/Load System**: Save your progress and continue later

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
2. Type commands to interact with the game world:
   - `go [direction]` - Move in a specific direction (north, south, east, west)
   - `look` - Examine your surroundings
   - `inventory` or `i` - Check your inventory
   - `take [item]` - Pick up an item
   - `use [item]` - Use an item in your inventory
   - `talk [character]` - Speak with a character
   - `save` - Save your current game
   - `load` - Load a previously saved game
   - `help` - Display available commands
   - `quit` - Exit the game

## Game Structure

- `main.py` - The entry point of the game
- `game/` - Core game mechanics and objects
  - `player.py` - Player character functionality
  - `items.py` - Item definitions and behaviors
  - `world.py` - World map and navigation
  - `state.py` - Game state management
  - `weather.py` - Weather system
  - `mythical.py` - Mythical creatures
- `locations/` - Different game locations
  - `forest.py` - Forest area
  - `mountain.py` - Mountain area
  - `village.py` - Village area
- `utils/` - Utility functions
  - `random_events.py` - Random event generation
  - `save_load.py` - Save/load functionality
  - `text_formatting.py` - Text formatting utilities

## Contributing

Contributions to improve the game are welcome! Feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available for educational purposes.

Last updated: May 8, 2025

