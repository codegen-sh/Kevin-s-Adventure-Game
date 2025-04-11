🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with villages, forests, mountains, and caves. Collect items, interact with your environment, and embark on an exciting journey!

## Features

- Explore multiple locations including a village, forest, mountain, and cave
- Collect and use various items throughout your adventure
- Manage your health and inventory
- Save and load game progress
- Random events and weather effects
- Encounter mythical creatures

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

## Usage

### Basic Commands

- `move [location]`: Travel to a connected location
- `look`: Examine your surroundings
- `inventory`: Check your current inventory
- `pickup [item]`: Add an item to your inventory
- `drop [item]`: Remove an item from your inventory
- `use [item]`: Use an item from your inventory
- `examine [item]`: Get a description of an item
- `status`: Check your health, inventory, and gold
- `interact`: Interact with your current location
- `help`: Display available commands
- `quit`: Save and exit the game

### Game Locations

- **Village**: A peaceful starting point with friendly inhabitants
- **Forest**: A mysterious woodland with valuable resources
- **Mountain**: A challenging terrain with unique treasures
- **Cave**: A dark location with hidden gems and potential dangers

## Game Structure

The game is organized into several modules:

- `main.py`: Entry point and game loop
- `game/`: Core game mechanics (player, world, items)
- `locations/`: Different game locations and their interactions
- `utils/`: Helper functions for text formatting, saving/loading, and random events

## Contributing

Contributions to improve the game are welcome! Feel free to add new features, locations, items, or fix bugs.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
