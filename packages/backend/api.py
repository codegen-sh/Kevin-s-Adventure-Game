"""
FastAPI backend for Kevin's Adventure Game.
Provides REST API endpoints for the game functionality.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import uuid
import json
from datetime import datetime

# Import game modules
from game.player import create_player, get_player_status
from game.world import create_world, get_current_location
from game.actions import perform_action
from utils.text_formatting import get_help_text
from utils.save_load import save_game_data, load_game_data, list_save_files

app = FastAPI(
    title="Kevin's Adventure Game API",
    description="REST API for the Kevin's Adventure text-based game",
    version="1.0.0"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for active game sessions
active_sessions: Dict[str, Dict] = {}

# Pydantic models for request/response
class GameAction(BaseModel):
    action: str

class SaveGameRequest(BaseModel):
    save_name: str

class GameResponse(BaseModel):
    success: bool
    message: str
    player_status: Optional[Dict] = None
    location: Optional[str] = None
    available_actions: Optional[List[str]] = None

class GameSession(BaseModel):
    session_id: str
    player_name: str
    created_at: str
    last_updated: str


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Kevin's Adventure Game API",
        "version": "1.0.0",
        "endpoints": {
            "new_game": "/game/new",
            "game_action": "/game/{session_id}/action",
            "game_status": "/game/{session_id}/status",
            "help": "/game/{session_id}/help",
            "save": "/game/{session_id}/save",
            "load": "/game/load/{save_name}",
            "saves": "/game/saves",
            "sessions": "/game/sessions"
        }
    }


@app.post("/game/new", response_model=GameSession)
async def create_new_game(player_name: str = "Kevin"):
    """Create a new game session."""
    try:
        session_id = str(uuid.uuid4())
        
        # Create new player and world
        player = create_player(player_name)
        world = create_world()
        
        # Store session
        active_sessions[session_id] = {
            "player": player,
            "world": world,
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat()
        }
        
        return GameSession(
            session_id=session_id,
            player_name=player_name,
            created_at=active_sessions[session_id]["created_at"],
            last_updated=active_sessions[session_id]["last_updated"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create new game: {str(e)}")


@app.get("/game/{session_id}/status")
async def get_game_status(session_id: str):
    """Get current player status and game state."""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    
    try:
        session = active_sessions[session_id]
        player = session["player"]
        world = session["world"]
        
        # Update player status
        status = get_player_status(player)
        location = get_current_location(world)
        
        return {
            "name": player["name"],
            "health": player["health"],
            "max_health": player["max_health"],
            "experience": player["experience"],
            "level": player["level"],
            "inventory": player["inventory"],
            "location": location,
            "status_text": status
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get game status: {str(e)}")


@app.post("/game/{session_id}/action", response_model=GameResponse)
async def perform_game_action(session_id: str, action: GameAction):
    """Perform a game action."""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    
    try:
        session = active_sessions[session_id]
        player = session["player"]
        world = session["world"]
        
        # Perform the action
        result_message = perform_action(player, world, action.action)
        
        # Update session timestamp
        session["last_updated"] = datetime.now().isoformat()
        
        # Get updated status
        location = get_current_location(world)
        
        return GameResponse(
            success=True,
            message=result_message,
            player_status={
                "name": player["name"],
                "health": player["health"],
                "max_health": player["max_health"],
                "experience": player["experience"],
                "level": player["level"],
                "inventory": player["inventory"],
                "location": location,
                "status_text": get_player_status(player)
            },
            location=location
        )
    except Exception as e:
        return GameResponse(
            success=False,
            message=f"Action failed: {str(e)}"
        )


@app.get("/game/{session_id}/help")
async def get_help(session_id: str):
    """Get help information."""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    
    return {"help_text": get_help_text()}


@app.post("/game/{session_id}/save")
async def save_game(session_id: str, save_request: SaveGameRequest):
    """Save the current game state."""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    
    try:
        session = active_sessions[session_id]
        player = session["player"]
        world = session["world"]
        
        save_game_data(player, world, save_request.save_name)
        
        return {
            "success": True,
            "message": f"Game saved as '{save_request.save_name}'"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Failed to save game: {str(e)}"
        }


@app.get("/game/saves")
async def list_saves():
    """List all available save files."""
    try:
        saves = list_save_files()
        # Remove .json extension from save names
        save_names = [save.replace('.json', '') for save in saves if save.endswith('.json')]
        return {"saves": save_names}
    except Exception as e:
        return {"saves": [], "error": str(e)}


@app.post("/game/load/{save_name}")
async def load_game(save_name: str):
    """Load a saved game."""
    try:
        player, world = load_game_data(save_name)
        
        if player is None or world is None:
            raise HTTPException(status_code=404, detail="Save file not found or corrupted")
        
        # Create new session for loaded game
        session_id = str(uuid.uuid4())
        active_sessions[session_id] = {
            "player": player,
            "world": world,
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat()
        }
        
        return {
            "success": True,
            "session_id": session_id,
            "message": f"Game loaded from '{save_name}'"
        }
    except Exception as e:
        return {
            "success": False,
            "session_id": None,
            "message": f"Failed to load game: {str(e)}"
        }


@app.delete("/game/{session_id}")
async def end_game_session(session_id: str):
    """End a game session."""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    
    del active_sessions[session_id]
    return {
        "success": True,
        "message": "Game session ended"
    }


@app.get("/game/sessions")
async def list_active_sessions():
    """List all active game sessions (for debugging)."""
    return {
        "active_sessions": len(active_sessions),
        "sessions": [
            {
                "session_id": sid,
                "player_name": session["player"]["name"],
                "created_at": session["created_at"],
                "last_updated": session["last_updated"]
            }
            for sid, session in active_sessions.items()
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

