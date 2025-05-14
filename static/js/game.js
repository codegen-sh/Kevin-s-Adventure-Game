document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const gameText = document.getElementById('game-text');
    const commandInput = document.getElementById('command-input');
    const submitCommand = document.getElementById('submit-command');
    const playerName = document.getElementById('player-name');
    const playerHealth = document.getElementById('player-health');
    const playerGold = document.getElementById('player-gold');
    const inventoryList = document.getElementById('inventory-list');
    const currentLocation = document.getElementById('current-location');
    const locationDescription = document.getElementById('location-description');
    const locationList = document.getElementById('location-list');
    const startGameModal = document.getElementById('start-game-modal');
    const playerNameInput = document.getElementById('player-name-input');
    const startGameBtn = document.getElementById('start-game-btn');
    const commandButtons = document.querySelectorAll('.command-btn');
    
    // Game state
    let gameInitialized = false;
    
    // Initialize the game
    function initGame(playerNameValue) {
        fetch('/api/game/init', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ player_name: playerNameValue })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                gameInitialized = true;
                updateGameState(data);
                startGameModal.style.display = 'none';
            }
        })
        .catch(error => {
            console.error('Error initializing game:', error);
            gameText.textContent += '\nError initializing game. Please try again.';
        });
    }
    
    // Send a command to the game
    function sendCommand(command) {
        if (!gameInitialized) {
            gameText.textContent += '\nPlease start a new game first.';
            return;
        }
        
        fetch('/api/game/action', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ action: command })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                updateGameState(data);
            }
        })
        .catch(error => {
            console.error('Error sending command:', error);
            gameText.textContent += '\nError processing command. Please try again.';
        });
    }
    
    // Update the game state based on the server response
    function updateGameState(data) {
        // Update player info
        playerName.textContent = data.player.name;
        playerHealth.textContent = data.player.health;
        playerGold.textContent = data.player.gold;
        
        // Update inventory
        inventoryList.innerHTML = '';
        if (data.player.inventory.length === 0) {
            const emptyItem = document.createElement('li');
            emptyItem.textContent = 'Empty';
            inventoryList.appendChild(emptyItem);
        } else {
            data.player.inventory.forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = item;
                inventoryList.appendChild(listItem);
            });
        }
        
        // Update location
        currentLocation.textContent = data.location.name;
        locationDescription.textContent = data.location.description;
        
        // Update available locations
        locationList.innerHTML = '';
        data.location.connections.forEach(location => {
            const listItem = document.createElement('li');
            listItem.textContent = location;
            listItem.addEventListener('click', () => {
                sendCommand(`move ${location}`);
            });
            locationList.appendChild(listItem);
        });
        
        // Update game text
        if (data.output && data.output.length > 0) {
            const newText = data.output.join('\n');
            gameText.textContent += '\n\n' + newText;
            gameText.scrollTop = gameText.scrollHeight;
        }
    }
    
    // Event Listeners
    submitCommand.addEventListener('click', () => {
        const command = commandInput.value.trim();
        if (command) {
            gameText.textContent += `\n\n> ${command}`;
            sendCommand(command);
            commandInput.value = '';
        }
    });
    
    commandInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const command = commandInput.value.trim();
            if (command) {
                gameText.textContent += `\n\n> ${command}`;
                sendCommand(command);
                commandInput.value = '';
            }
        }
    });
    
    startGameBtn.addEventListener('click', () => {
        const name = playerNameInput.value.trim() || 'Kevin';
        initGame(name);
    });
    
    commandButtons.forEach(button => {
        button.addEventListener('click', () => {
            const command = button.getAttribute('data-command');
            gameText.textContent += `\n\n> ${command}`;
            sendCommand(command);
        });
    });
    
    // Show the start game modal when the page loads
    startGameModal.style.display = 'flex';
});

