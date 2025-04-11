🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with villages, forests, caves, and mountains. Collect items, interact with your environment, and embark on an exciting journey!

## Features

- Explore multiple locations including a village, forest, cave, and mountain
- Collect and use items throughout your adventure
- Manage your health and inventory
- Save and load game progress
- Random events and encounters
- Weather system that affects gameplay

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

## How to Play

1. When you start the game, you'll have the option to load a saved game or start a new one.
2. Navigate through the world by using the commands listed below.
3. Collect items, interact with locations, and manage your resources.
4. Your progress is automatically saved when you quit the game.

### Available Commands

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

## Game World

The game world consists of several interconnected locations:

- **Village**: A peaceful starting point with friendly inhabitants
- **Forest**: A mysterious woodland area with valuable resources
- **Cave**: A dark, challenging environment with hidden treasures
- **Mountain**: A treacherous climb with rewarding views and items

## Project Structure

- `main.py`: The main game loop and entry point
- `game/`: Core game mechanics and objects
  - `player.py`: Player character management
  - `world.py`: Game world and location management
  - `items.py`: Item definitions and interactions
  - `state.py`: Game state management
  - `weather.py`: Weather system that affects gameplay
  - `mythical.py`: Mythical creatures and encounters
- `locations/`: Location-specific interactions
  - `village.py`: Village location events
  - `forest.py`: Forest location events
  - `mountain.py`: Mountain location events
- `utils/`: Utility functions
  - `text_formatting.py`: Text display formatting
  - `save_load.py`: Game saving and loading
  - `random_events.py`: Random event generation

## Contributing

Contributions to improve the game are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is open source and available for educational purposes.
