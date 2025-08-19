# Kevin's Adventure Game Gameplay Guide

This document provides a guide to playing Kevin's Adventure Game, a text-based adventure game.

## Getting Started

1. Start the game by running `python main.py`
2. Choose whether to load a saved game or start a new one
3. If starting a new game, you'll begin in the Village

## Game World

The game world consists of several locations:

### Village

A small, peaceful village with thatched-roof houses and friendly inhabitants.
- Items: map, bread
- Connections: Forest, Mountain

### Forest

A dense, mysterious forest with towering trees and the sound of rustling leaves.
- Items: stick, berries
- Connections: Village, Cave

### Cave

A dark, damp cave with echoing sounds and glittering minerals on the walls.
- Items: torch, gemstone
- Connections: Forest

### Mountain

A tall, snow-capped mountain with treacherous paths and breathtaking views.
- Items: rope, pickaxe
- Connections: Village

## Commands

### Movement

- `move [location]`: Move to a new location
  - Example: `move Forest`

### Exploration

- `look`: Examine your surroundings
- `interact`: Interact with your current location

### Inventory Management

- `inventory`: Check your inventory
- `pickup [item]` or `take [item]`: Pick up an item
  - Example: `pickup bread`
- `drop [item]`: Drop an item from your inventory
  - Example: `drop stick`
- `use [item]`: Use an item
  - Example: `use map`
- `examine [item]`: Get a description of an item
  - Example: `examine torch`

### Status

- `status`: Check your current status (health, gold, location, inventory)

### Help and Quit

- `help`: Show the help message
- `quit`: Save and exit the game

## Items

### Food Items

- **Bread**: Restores 20 health when eaten
- **Berries**: Restores 10 health when eaten

### Tools

- **Torch**: Can be used to illuminate dark areas
- **Map**: Shows all known locations
- **Rope**: Helps with climbing
- **Pickaxe**: Useful for mining

### Miscellaneous

- **Gemstone**: A mysterious glowing gemstone
- **Stick**: A simple wooden stick

## Random Events

Each location has its own set of random events that can occur when you interact with it:

### Village

- Meeting friendly villagers
- Finding a merchant
- Hearing rumors
- Resting at the inn

### Forest

- Finding wild berries
- Encountering wildlife
- Discovering a hidden path
- Getting lost

### Cave

- Finding treasure
- Encountering bats
- Discovering an underground stream
- Finding glowing crystals
- Encountering a rockfall

### Mountain

- Finding a vantage point
- Encountering a mountain goat
- Discovering a rare herb
- Experiencing a snowstorm

## Tips

1. **Explore thoroughly**: Each location has items to find and events to discover
2. **Manage your health**: Use food items to restore health when needed
3. **Use items strategically**: Some items have special effects in certain situations
4. **Save regularly**: Use the `quit` command to save your progress
5. **Interact with locations**: Use the `interact` command to trigger random events

