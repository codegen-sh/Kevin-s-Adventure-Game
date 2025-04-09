🌈🌈
# 🌈 Kevin's Adventure Game 🎮

This is a text-based adventure game where you play as Kevin, exploring a magical world filled with different locations, items, and challenges.

## 🚀 Features

- **Explore Different Locations**: Visit the Village, Forest, Cave, and Mountain
- **Inventory Management**: Collect, use, and drop items
- **Health System**: Manage your health as you face challenges
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Experience dynamic events that make each playthrough unique
- **Weather System**: Dynamic weather affects gameplay

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the game directory:
   ```bash
   cd Kevin-s-Adventure-Game
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. When you start the game, you'll have the option to load a saved game or start a new one.
2. Navigate through the world by typing commands like `move forest` or `move village`.
3. Interact with your surroundings using commands like `look` or `interact`.
4. Manage your inventory with commands like `pickup map` or `use potion`.
5. Type `help` at any time to see all available commands.

## 📋 Available Commands

- `move [location]`: Move to a new location
- `look`: Examine your surroundings
- `inventory`: Check your inventory
- `pickup [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message
- `quit`: Save and exit the game

## 🗺️ Game World

The game world consists of several interconnected locations:

- **Village**: A small, peaceful village with friendly inhabitants
- **Forest**: A dense, mysterious forest with various items and creatures
- **Cave**: A dark, damp cave with valuable treasures and potential dangers
- **Mountain**: A tall, snow-capped mountain with challenging paths and unique rewards

## 🧩 Game Structure

- `main.py`: Main game loop and initialization
- `game/`: Core game mechanics and objects
  - `actions.py`: Core game action handling
  - `player.py`: Player character management
  - `world.py`: World structure and location management
  - `items.py`: Item definitions and interactions
  - `weather.py`: Weather system
  - `mythical.py`: Mythical creatures and events
  - `state.py`: Game state management
- `locations/`: Location-specific interactions
  - `village.py`, `forest.py`, `mountain.py`
- `utils/`: Utility functions
  - `text_formatting.py`: Text display utilities
  - `save_load.py`: Game saving/loading functionality
  - `random_events.py`: Random event generation

## 🤝 Contributing

This is a test repository for TinySitter. Feel free to explore and experiment with the code!

## 📝 License

This project is open source and available for educational purposes.
