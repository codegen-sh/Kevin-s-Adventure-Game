# Kevin's Adventure Game - Monorepo

A modern web-based text adventure game built with FastAPI backend and Next.js frontend in a monorepo structure.

## 🎮 About

Kevin's Adventure Game is a classic text-based adventure where players explore mystical lands, collect items, interact with characters, and uncover secrets. This version features a modern web interface while preserving the classic gameplay experience.

## 🏗️ Architecture

This project uses a monorepo structure with two main packages:

- **Backend** (`packages/backend/`): FastAPI-based REST API serving the game logic
- **Frontend** (`packages/frontend/`): Next.js React application providing the web interface

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 18+** (for frontend)
- **npm** or **yarn** (for package management)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd kevins-adventure-monorepo
   ```

2. **Install dependencies**
   ```bash
   # Install root dependencies
   npm install
   
   # Install all package dependencies
   npm run install:all
   ```

### Development

**Start both backend and frontend in development mode:**
```bash
npm run dev
```

This will start:
- Backend API server at `http://localhost:8000`
- Frontend development server at `http://localhost:3000`

**Or start them individually:**
```bash
# Backend only
npm run dev:backend

# Frontend only  
npm run dev:frontend
```

### Production

**Build and start for production:**
```bash
npm run build
npm run start
```

## 📁 Project Structure

```
kevins-adventure-monorepo/
├── package.json                 # Root package.json with workspace config
├── README.md                    # This file
├── packages/
│   ├── backend/                 # FastAPI backend
│   │   ├── game/               # Core game logic
│   │   │   ├── player.py       # Player management
│   │   │   ├── world.py        # World and locations
│   │   │   ├── items.py        # Item system
│   │   │   ├── actions.py      # Game actions handler
│   │   │   ├── weather.py      # Weather system
│   │   │   ├── mythical.py     # Mythical creatures
│   │   │   └── state.py        # Game state management
│   │   ├── locations/          # Location modules
│   │   │   ├── village.py      # Village location
│   │   │   ├── forest.py       # Forest location
│   │   │   ├── mountain.py     # Mountain location
│   │   │   └── cave.py         # Cave location
│   │   ├── utils/              # Utility modules
│   │   │   ├── save_load.py    # Save/load functionality
│   │   │   ├── text_formatting.py # Text formatting
│   │   │   └── random_events.py # Random events
│   │   ├── api.py              # FastAPI application
│   │   ├── main.py             # Original CLI game entry
│   │   └── requirements.txt    # Python dependencies
│   └── frontend/               # Next.js frontend
│       ├── src/
│       │   ├── app/            # Next.js app directory
│       │   │   ├── layout.tsx  # Root layout
│       │   │   ├── page.tsx    # Home page
│       │   │   └── globals.css # Global styles
│       │   ├── components/     # React components
│       │   │   ├── GameTerminal.tsx    # Game output display
│       │   │   ├── PlayerStatus.tsx    # Player stats
│       │   │   ├── ActionPanel.tsx     # Action input
│       │   │   └── GameHeader.tsx      # Header with controls
│       │   ├── hooks/          # Custom React hooks
│       │   │   └── useGame.ts  # Game state management
│       │   ├── lib/            # Utility libraries
│       │   │   └── api.ts      # API client
│       │   └── types/          # TypeScript types
│       │       └── game.ts     # Game-related types
│       ├── package.json        # Frontend dependencies
│       ├── next.config.js      # Next.js configuration
│       ├── tailwind.config.js  # Tailwind CSS config
│       └── tsconfig.json       # TypeScript config
```

## 🎯 Features

### Game Features
- **Exploration**: Navigate through villages, forests, mountains, and caves
- **Inventory System**: Collect and manage items
- **Character Progression**: Gain experience and level up
- **Save/Load**: Save your progress and continue later
- **Weather System**: Dynamic weather affects gameplay
- **Mythical Creatures**: Encounter magical beings
- **Interactive Locations**: Each location offers unique interactions

### Technical Features
- **Modern Web Interface**: Responsive design with terminal-style output
- **Real-time Updates**: Live game state synchronization
- **RESTful API**: Clean separation between frontend and backend
- **TypeScript**: Full type safety in frontend
- **Monorepo Structure**: Organized codebase with shared tooling
- **Development Tools**: Hot reload, linting, formatting

## 🛠️ Available Scripts

### Root Level Scripts
- `npm run dev` - Start both backend and frontend in development mode
- `npm run build` - Build frontend for production
- `npm run start` - Start both services in production mode
- `npm run install:all` - Install dependencies for all packages
- `npm run test` - Run all tests
- `npm run lint` - Lint all packages
- `npm run format` - Format code in all packages

### Backend Scripts
- `npm run dev:backend` - Start backend development server
- `npm run start:backend` - Start backend production server
- `npm run test:backend` - Run backend tests
- `npm run lint:backend` - Lint backend code
- `npm run format:backend` - Format backend code

### Frontend Scripts
- `npm run dev:frontend` - Start frontend development server
- `npm run build:frontend` - Build frontend for production
- `npm run start:frontend` - Start frontend production server
- `npm run test:frontend` - Run frontend tests
- `npm run lint:frontend` - Lint frontend code
- `npm run format:frontend` - Format frontend code

## 🎮 How to Play

1. **Start a New Game**: Click "New Game" and enter your character name
2. **Explore**: Use commands like `go village`, `go forest`, `look`, `explore`
3. **Interact**: Pick up items with `take <item>`, use them with `use <item>`
4. **Manage**: Check your status with `status`, inventory with `inventory`
5. **Progress**: Rest to recover health, gain experience through actions
6. **Save**: Save your progress anytime with the Save button

### Common Commands
- `look` - Examine your surroundings
- `go <location>` - Move to a different location
- `take <item>` - Pick up an item
- `use <item>` - Use an item from your inventory
- `inventory` - Check your items
- `status` - View your character stats
- `explore` - Search for hidden items or secrets
- `rest` - Recover health
- `help` - Show all available commands

## 🔧 Development

### Backend Development
The backend is built with FastAPI and provides a REST API for the game logic. Key components:

- **Game Logic**: Core game mechanics in the `game/` directory
- **API Endpoints**: RESTful endpoints in `api.py`
- **Session Management**: In-memory session storage for active games
- **Save System**: File-based save/load functionality

### Frontend Development
The frontend is a Next.js React application with TypeScript. Key features:

- **Component Architecture**: Modular React components
- **State Management**: Custom hooks for game state
- **API Integration**: Axios-based API client
- **Responsive Design**: Tailwind CSS for styling
- **Type Safety**: Full TypeScript coverage

### Adding New Features

1. **Backend**: Add new endpoints in `api.py`, implement logic in appropriate modules
2. **Frontend**: Create new components, update types, extend API client
3. **Game Logic**: Extend existing modules or create new ones in `game/` or `locations/`

## 📝 API Documentation

When running the backend, visit `http://localhost:8000/docs` for interactive API documentation.

### Key Endpoints
- `POST /game/new` - Create new game session
- `POST /game/{session_id}/action` - Perform game action
- `GET /game/{session_id}/status` - Get player status
- `POST /game/{session_id}/save` - Save game
- `POST /game/load/{save_name}` - Load saved game

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Run linting and formatting
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎉 Acknowledgments

- Original Kevin's Adventure Game concept
- FastAPI for the excellent Python web framework
- Next.js for the React framework
- Tailwind CSS for styling utilities

