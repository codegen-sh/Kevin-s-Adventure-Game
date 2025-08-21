# Kevin's Adventure Game

A text-based adventure game where you explore a world of mystery and danger as you navigate through forests, caves, villages, and mountains. Collect items, interact with characters, and uncover the secrets of this magical realm.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
cd Kevin-s-Adventure-Game
```

2. Run the game:
```bash
python main.py
```

## How to Play

In Kevin's Adventure Game, you navigate through different locations, collect items, and interact with the environment using text commands.

### Basic Commands

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

### Locations

The game world consists of several locations:

- **Village**: A small, peaceful village with friendly inhabitants
- **Forest**: A dense, mysterious forest with towering trees
- **Cave**: A dark, damp cave with echoing sounds and glittering minerals
- **Mountain**: A tall, snow-capped mountain with treacherous paths

Each location has unique interactions and items to discover.

### Items

Throughout the game, you'll find various items that can be picked up, used, or traded:

- **Map**: Shows available locations
- **Bread**: Restores health when eaten
- **Stick**: A simple tool or weapon
- **Berries**: Can be eaten for health (but might be poisonous!)
- **Torch**: Provides light in dark areas
- **Gemstone**: A valuable item that can be sold
- **Rope**: Useful for climbing
- **Pickaxe**: Used for mining or breaking through rocks

And many more to discover!

### Game Mechanics

- **Health**: Your health starts at 100. If it reaches 0, you lose the game.
- **Inventory**: You can carry multiple items in your inventory.
- **Gold**: Used for buying items from shops.
- **Random Events**: Random events may occur as you explore, adding unpredictability to your adventure.
- **Weather**: The weather can change and affect gameplay.

## Save/Load System

The game automatically saves your progress when you quit. You can load a saved game when starting the game.

## Project Structure

- `main.py`: Entry point that initializes the game and handles the main game loop
- `game/`: Contains core game mechanics
  - `actions.py`: Handles player actions
  - `player.py`: Player state and actions
  - `world.py`: World state and navigation
  - `items.py`: Item interactions
  - `mythical.py`: Mythical creature interactions
  - `state.py`: World state updates
  - `weather.py`: Weather system
  - `models.py`: Data models
  - `exceptions.py`: Custom exceptions
  - `locations.py`: Base location class
- `locations/`: Contains location-specific code
  - `village.py`: Village location interactions
  - `forest.py`: Forest location interactions
  - `mountain.py`: Mountain location interactions
  - `cave.py`: Cave location interactions
- `utils/`: Contains utility functions
  - `text_formatting.py`: Text formatting utilities
  - `random_events.py`: Random event generation
  - `save_load.py`: Game saving and loading

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request

## License

This project is open source and available for anyone to use and modify.

## Acknowledgments

- Kevin, for inspiring this adventure game
- All contributors who have helped improve the game

