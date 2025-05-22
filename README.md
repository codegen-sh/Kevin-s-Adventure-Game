🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world, collect items, and embark on quests.

## Game Overview

In Kevin's Adventure Game, you play as an adventurer exploring a world filled with different locations including:
- A peaceful village with friendly inhabitants
- A mysterious forest with hidden secrets
- Dark caves with valuable treasures
- Towering mountains with challenging paths

Throughout your journey, you'll:
- Collect and use various items
- Interact with the environment and characters
- Experience random events and weather changes
- Manage your health and inventory
- Complete quests and discover the world's secrets

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

## Game Commands

- `move [location]`: Travel to a connected location
- `look`: Examine your surroundings
- `inventory`: Check your current items
- `pickup [item]`: Add an item to your inventory
- `drop [item]`: Remove an item from your inventory
- `use [item]`: Use an item from your inventory
- `examine [item]`: Get details about an item
- `status`: Check your health, gold, and inventory
- `interact`: Interact with your current location
- `help`: Display available commands
- `quit`: Save your progress and exit the game

## Game Features

- **Save/Load System**: Save your progress and continue your adventure later
- **Dynamic Weather**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect, use, and manage various items
- **Health System**: Monitor and maintain your health throughout your journey
- **Multiple Locations**: Explore different areas with unique characteristics
- **Random Events**: Encounter unexpected situations during your adventure

## Project Structure

- `main.py`: Main game loop and initialization
- `game/`: Core game mechanics and objects
  - `player.py`: Player character functionality
  - `world.py`: World map and location management
  - `items.py`: Item definitions and interactions
  - `weather.py`: Weather system and effects
  - `mythical.py`: Mythical creatures and encounters
- `locations/`: Different game locations
  - `village.py`: Village location and interactions
  - `forest.py`: Forest location and interactions
  - `mountain.py`: Mountain location and interactions
- `utils/`: Helper functions
  - `text_formatting.py`: Text display formatting
  - `save_load.py`: Game state saving and loading
  - `random_events.py`: Random event generation

## Contributing

Contributions to Kevin's Adventure Game are welcome! Feel free to submit pull requests with new features, bug fixes, or improvements.

## License

This project is open source and available for educational purposes.

Last updated: May 22, 2025

