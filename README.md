# 🌟 Kevin's Adventure Game

A rich, text-based adventure game featuring dynamic weather systems, mythical creatures, and immersive exploration across multiple locations.

## 🎮 Game Features

### Core Gameplay
- **Immersive Exploration**: Navigate through villages, forests, mountains, and caves
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect, use, and manage items throughout your journey
- **Save/Load System**: Continue your adventure anytime with persistent game saves
- **Player Progression**: Track health, gold, and inventory as you explore

### Advanced Systems
- **Mythical Creatures**: Encounter and summon legendary beings like phoenixes, unicorns, and dragons
- **Location-Specific Events**: Each area offers unique interactions and discoveries
- **Random Events**: Experience unexpected encounters that add variety to gameplay
- **Item Interactions**: Use items strategically to overcome challenges
- **Status Tracking**: Monitor your character's health, resources, and current state

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required

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

## 🎯 How to Play

### Starting Your Adventure
- Launch the game and choose to start new or load a saved game
- Follow the on-screen prompts to begin your journey
- Type `help` at any time to see available commands

### Available Commands
- `move [location]` - Travel to a new location
- `look` - Examine your current surroundings
- `inventory` - Check your items and resources
- `pickup [item]` - Collect items from your environment
- `drop [item]` - Remove items from your inventory
- `use [item]` - Utilize items for various effects
- `examine [item]` - Get detailed information about items
- `status` - View your current health, gold, and stats
- `interact` - Engage with your current location
- `help` - Display all available commands
- `quit` - Save your progress and exit the game

### Game World
Explore four distinct locations, each with unique characteristics:

- **🏘️ Village**: A peaceful starting area with friendly inhabitants and basic supplies
- **🌲 Forest**: A mysterious woodland filled with natural resources and hidden secrets
- **⛰️ Mountain**: Treacherous peaks offering valuable materials and breathtaking views
- **🕳️ Cave**: Dark underground chambers containing rare gems and ancient artifacts

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game loop and entry point
├── game/                   # Core game mechanics
│   ├── items.py           # Item definitions and interactions
│   ├── mythical.py        # Mythical creature summoning system
│   ├── player.py          # Player state and actions
│   ├── state.py           # Game state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World initialization and location data
├── locations/             # Location-specific interactions
│   ├── forest.py          # Forest area events and features
│   ├── mountain.py        # Mountain climbing and exploration
│   └── village.py         # Village interactions and NPCs
└── utils/                 # Utility functions
    ├── random_events.py   # Random encounter system
    ├── save_load.py       # Game persistence functionality
    └── text_formatting.py # Display and formatting utilities
```

## 🎨 Game Features in Detail

### Weather System
The game features a dynamic weather system that affects gameplay:
- **Clear**: Perfect conditions for exploration
- **Cloudy**: Slightly reduced visibility
- **Rainy**: Slippery conditions affecting movement
- **Stormy**: Severe weather impacting both movement and perception
- **Foggy**: Dramatically reduced visibility
- **Windy**: Strong winds affecting agility

### Mythical Creatures
Encounter and summon powerful mythical beings:
- **Phoenix**: Provides healing and restoration
- **Unicorn**: Grants rare unicorn hair for crafting
- **Dragon**: Offers dragon scales and protection

### Save System
- Automatic save on quit
- Multiple save file support
- Load any previous game state
- Persistent world and player data

## 🤝 Contributing

This project welcomes contributions! Whether you want to add new locations, creatures, items, or gameplay mechanics, your input is valuable.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🎯 Future Enhancements

- Combat system with enemies and battles
- Crafting system for creating new items
- Quest system with objectives and rewards
- Multiplayer support for shared adventures
- Enhanced graphics and ASCII art
- Sound effects and background music

---

**Ready for adventure?** Clone the repository and start your journey today! 🗺️✨
