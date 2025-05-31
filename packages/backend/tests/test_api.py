import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to Kevin's Adventure Game API" in response.json()["message"]

def test_create_new_game():
    """Test creating a new game session"""
    response = client.post("/game/new", json={"player_name": "TestPlayer"})
    assert response.status_code == 200
    data = response.json()
    assert "session_id" in data
    assert data["player"]["name"] == "TestPlayer"
    assert data["player"]["health"] == 100
    assert data["world"]["current_location"] == "Village"

def test_get_game_state():
    """Test getting game state"""
    # First create a game
    create_response = client.post("/game/new", json={"player_name": "TestPlayer"})
    session_id = create_response.json()["session_id"]
    
    # Then get the state
    response = client.get(f"/game/{session_id}/state")
    assert response.status_code == 200
    data = response.json()
    assert data["current_location"] == "Village"
    assert "available_actions" in data
    assert len(data["available_actions"]) > 0

def test_perform_action():
    """Test performing a game action"""
    # First create a game
    create_response = client.post("/game/new", json={"player_name": "TestPlayer"})
    session_id = create_response.json()["session_id"]
    
    # Perform an action
    response = client.post("/game/action", json={
        "session_id": session_id,
        "action": "look around"
    })
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Village" in data["message"]

def test_invalid_session():
    """Test with invalid session ID"""
    response = client.get("/game/invalid_session/state")
    assert response.status_code == 404
    assert "Game session not found" in response.json()["detail"]

def test_list_saves():
    """Test listing save files"""
    response = client.get("/game/saves")
    assert response.status_code == 200
    assert "saves" in response.json()

