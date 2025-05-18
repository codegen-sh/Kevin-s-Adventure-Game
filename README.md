🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with villages, forests, mountains, and caves.

Last updated: May 18, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Run the game:
   ```
   python main.py
   ```

## Game Features

- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay and character abilities
- **Mythical Creatures**: Encounter and summon magical beings like phoenixes, unicorns, and friendly dragons
- **Multiple Locations**: Explore a village, forest, mountain, and mysterious cave
- **Inventory System**: Collect, use, and manage various items throughout your adventure
- **Save/Load System**: Save your progress and continue your adventure later

## Game Mechanics

- **Health System**: Manage your character's health through healing items and avoiding damage
- **Gold Economy**: Earn and spend gold throughout your adventure
- **Location-based Interactions**: Each location offers unique experiences and challenges
- **Random Events**: Encounter unexpected situations that make each playthrough unique

## Game Structure

```
.
├── game/           # Core game mechanics
│   ├── items.py    # Item definitions and interactions
│   ├── mythical.py # Mythical creature interactions
│   ├── player.py   # Player state and actions
│   ├── state.py    # Game state management
│   ├── weather.py  # Weather system
│   └── world.py    # World structure and navigation
├── locations/      # Location-specific content
│   ├── forest.py   # Forest location events
│   ├── mountain.py # Mountain location events
│   └── village.py  # Village location events
├── utils/          # Utility functions
│   ├── random_events.py   # Random event generation
│   ├── save_load.py       # Game saving/loading
│   └── text_formatting.py # Text display utilities
└── main.py         # Main game loop
```

## Usage

1. Follow the prompts in the game.
2. Type 'help' at any time to see available commands.
3. Use directional commands to navigate between locations.
4. Interact with items by using commands like 'pick up [item]' or 'use [item]'.
5. Type 'quit' to save and exit the game.

## Contributing

Contributions to Kevin's Adventure Game are welcome! Feel free to add:

- New locations
- Additional items and creatures
- Enhanced game mechanics
- Bug fixes and improvements

Please ensure your code follows the existing structure and style.

