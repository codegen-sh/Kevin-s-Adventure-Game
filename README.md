🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with mysteries, challenges, and adventures.

Last updated: May 2, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Description

Kevin's Adventure Game is an interactive text-based adventure where players navigate through various locations including forests, villages, and mountains. Players can collect items, interact with characters, experience random events, and uncover the secrets of this magical realm.

The game features:
- Multiple locations to explore
- Item collection and inventory management
- Character interactions
- Weather system that affects gameplay
- Mythical creatures to encounter
- Save/load game functionality

## Game Structure

The game is organized into several modules:
- `game/`: Core game mechanics and objects
  - `items.py`: Defines collectible items in the game
  - `player.py`: Player character functionality
  - `world.py`: Game world and location management
  - `weather.py`: Dynamic weather system
  - `mythical.py`: Mythical creatures and encounters
  - `state.py`: Game state management
- `locations/`: Different areas to explore
  - `forest.py`: Forest location and events
  - `village.py`: Village location and interactions
  - `mountain.py`: Mountain location and challenges
- `utils/`: Helper functions
  - `save_load.py`: Game saving and loading functionality
  - `random_events.py`: Random event generation
  - `text_formatting.py`: Text display formatting

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

1. Start the game by running `main.py`
2. Choose to start a new game or load a saved game
3. Navigate through the world using text commands
4. Collect items, interact with the environment, and progress through the story
5. Save your game at any time by typing "quit"

## Game Commands

- `move [location]`: Move to a new location
- `look`: Examine your surroundings
- `inventory`: Check your inventory
- `pickup [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message with available commands
- `quit`: Save and exit the game

## Game Features

### Dynamic Weather System
The game includes a weather system that changes over time and affects gameplay. Different weather conditions can impact your character's abilities and the environment.

### Mythical Creatures
Encounter various mythical creatures throughout your journey. Some may help you, while others present challenges to overcome.

### Save/Load System
Your progress can be saved at any time, allowing you to continue your adventure later. Multiple save files are supported.

### Random Events
The game includes random events that can occur during your journey, making each playthrough unique.

## Contributing

Contributions to Kevin's Adventure Game are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch for your feature
3. Add your changes
4. Submit a pull request

Please ensure your code follows the existing style and includes appropriate documentation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

