from flask import Flask, render_template, request, jsonify, session
import os
import json
from game.player import Player
from game.world import create_world
from game.state import GameState
from game.weather import Weather
from game.actions import perform_action
from utils.text_formatting import print_welcome_message

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Custom print function to capture output
output_buffer = []

def capture_print(text):
    output_buffer.append(str(text))

# Override the built-in print function for game modules
import builtins
original_print = builtins.print
builtins.print = capture_print

class GameSession:
    def __init__(self):
        self.player = None
        self.world = None
        self.game_state = None
        self.weather = None
        self.output = []
        self.initialize_new_game()
    
    def initialize_new_game(self, player_name="Kevin"):
        """Initialize a new game."""
        self.player = Player(player_name)
        self.world = create_world()
        self.game_state = GameState()
        self.weather = Weather()
        
        # Add the weather to the world for easy access
        self.world.weather = self.weather
        self.world.game_state = self.game_state
        
        # Clear output buffer
        global output_buffer
        output_buffer = []
        
        # Print welcome message
        print_welcome_message()
        
        # Store the welcome message
        self.output = list(output_buffer)

@app.route('/')
def index():
    """Render the main game page."""
    # Initialize a new game session if one doesn't exist
    if 'game_session' not in session:
        session['game_session'] = GameSession()
        
    return render_template('index.html')

@app.route('/api/game/init', methods=['POST'])
def init_game():
    """Initialize a new game."""
    player_name = request.json.get('player_name', 'Kevin')
    
    # Create a new game session
    game_session = GameSession()
    game_session.initialize_new_game(player_name)
    
    # Store the game session in the session
    session['game_session'] = game_session
    
    return jsonify({
        'status': 'success',
        'output': game_session.output,
        'player': {
            'name': game_session.player.name,
            'health': game_session.player.health,
            'inventory': game_session.player.inventory,
            'location': game_session.player.location,
            'gold': game_session.player.gold
        },
        'location': {
            'name': game_session.world.get_current_location(),
            'description': game_session.world.get_location(game_session.world.get_current_location()).description,
            'connections': game_session.world.get_available_locations()
        }
    })

@app.route('/api/game/action', methods=['POST'])
def game_action():
    """Process a game action."""
    action = request.json.get('action', '')
    
    # Get the game session
    game_session = session.get('game_session')
    if not game_session:
        return jsonify({'status': 'error', 'message': 'No game session found'})
    
    # Clear output buffer
    global output_buffer
    output_buffer = []
    
    # Process the action
    perform_action(game_session.player, game_session.world, action)
    
    # Store the output
    game_session.output = list(output_buffer)
    
    # Update the session
    session['game_session'] = game_session
    
    return jsonify({
        'status': 'success',
        'output': game_session.output,
        'player': {
            'name': game_session.player.name,
            'health': game_session.player.health,
            'inventory': game_session.player.inventory,
            'location': game_session.player.location,
            'gold': game_session.player.gold
        },
        'location': {
            'name': game_session.world.get_current_location(),
            'description': game_session.world.get_location(game_session.world.get_current_location()).description,
            'connections': game_session.world.get_available_locations()
        }
    })

@app.route('/api/game/status', methods=['GET'])
def game_status():
    """Get the current game status."""
    # Get the game session
    game_session = session.get('game_session')
    if not game_session:
        return jsonify({'status': 'error', 'message': 'No game session found'})
    
    return jsonify({
        'status': 'success',
        'player': {
            'name': game_session.player.name,
            'health': game_session.player.health,
            'inventory': game_session.player.inventory,
            'location': game_session.player.location,
            'gold': game_session.player.gold
        },
        'location': {
            'name': game_session.world.get_current_location(),
            'description': game_session.world.get_location(game_session.world.get_current_location()).description,
            'connections': game_session.world.get_available_locations()
        }
    })

if __name__ == '__main__':
    app.run(debug=True)

