// Kevin's Adventure Game - Interactive Elements

document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add interactive terminal simulation
    const terminalElement = document.getElementById('game-terminal');
    if (terminalElement) {
        const terminalOutput = document.getElementById('terminal-output');
        const terminalInput = document.getElementById('terminal-input');
        
        // Sample game responses
        const gameResponses = {
            'help': 'Available commands:\n- move [location]: Move to a new location\n- look: Examine your surroundings\n- inventory: Check your inventory\n- pickup [item]: Pick up an item\n- drop [item]: Drop an item from your inventory\n- use [item]: Use an item\n- examine [item]: Get a description of an item\n- status: Check your current status\n- interact: Interact with your current location\n- help: Show this help message\n- quit: Save and exit the game',
            'look': 'You are in the Village. A small, peaceful village with thatched-roof houses and friendly inhabitants. You can see a map and some bread on the ground.',
            'inventory': 'Your inventory is empty.',
            'status': 'Health: 100 | Inventory: empty | Gold: 100',
            'move forest': 'You moved to: Forest\nA dense, mysterious forest with towering trees and the sound of rustling leaves.',
            'pickup map': 'You picked up: map',
            'pickup bread': 'You picked up: bread',
            'examine map': 'A weathered map showing the surrounding areas. It marks the Village, Forest, Cave, and Mountain.',
            'use bread': 'You ate the bread. It was delicious and restored 10 health.',
            'interact': 'You talk to a villager. They tell you about a treasure hidden in the mountains.'
        };
        
        // Process terminal input
        function processCommand(command) {
            let response = '';
            
            // Check for known commands
            if (command in gameResponses) {
                response = gameResponses[command];
            } else if (command.startsWith('move ') || command.startsWith('pickup ') || 
                       command.startsWith('drop ') || command.startsWith('use ') || 
                       command.startsWith('examine ')) {
                // Check for partial command matches
                for (const key in gameResponses) {
                    if (key === command) {
                        response = gameResponses[key];
                        break;
                    }
                }
                
                // If no exact match, give a generic response
                if (!response) {
                    if (command.startsWith('move ')) {
                        const location = command.substring(5);
                        response = `You cannot move to ${location} from here.`;
                    } else if (command.startsWith('pickup ')) {
                        const item = command.substring(7);
                        response = `There is no ${item} here to pick up.`;
                    } else if (command.startsWith('drop ')) {
                        const item = command.substring(5);
                        response = `You don't have ${item} in your inventory.`;
                    } else if (command.startsWith('use ')) {
                        const item = command.substring(4);
                        response = `You don't have ${item} to use.`;
                    } else if (command.startsWith('examine ')) {
                        const item = command.substring(8);
                        response = `You don't see ${item} here.`;
                    }
                }
            } else if (command === 'quit') {
                response = 'Thanks for playing! Your progress has been saved.';
            } else {
                response = `I don't understand "${command}". Type 'help' for a list of commands.`;
            }
            
            return response;
        }
        
        // Add command to terminal output
        function addToTerminal(text, isCommand = false) {
            const line = document.createElement('div');
            line.className = isCommand ? 'terminal-command' : 'terminal-response';
            line.textContent = isCommand ? '> ' + text : text;
            terminalOutput.appendChild(line);
            terminalOutput.scrollTop = terminalOutput.scrollHeight;
        }
        
        // Initialize with welcome message
        addToTerminal('Welcome to Kevin\'s Adventure Game!');
        addToTerminal('Type \'help\' for a list of commands.');
        
        // Handle terminal input
        if (terminalInput) {
            terminalInput.addEventListener('keydown', function(e) {
                if (e.key === 'Enter') {
                    const command = terminalInput.value.trim().toLowerCase();
                    if (command) {
                        addToTerminal(command, true);
                        const response = processCommand(command);
                        addToTerminal(response);
                        terminalInput.value = '';
                    }
                }
            });
        }
    }

    // Add animation to location cards
    const locationCards = document.querySelectorAll('.location-card');
    if (locationCards.length > 0) {
        locationCards.forEach((card, index) => {
            card.style.animationDelay = `${index * 0.2}s`;
            card.classList.add('fade-in');
        });
    }

    // Add dark mode toggle
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
            
            // Save preference to localStorage
            const isDarkMode = document.body.classList.contains('dark-mode');
            localStorage.setItem('darkMode', isDarkMode);
            
            // Update toggle text
            darkModeToggle.textContent = isDarkMode ? '☀️ Light Mode' : '🌙 Dark Mode';
        });
        
        // Check for saved preference
        const savedDarkMode = localStorage.getItem('darkMode') === 'true';
        if (savedDarkMode) {
            document.body.classList.add('dark-mode');
            darkModeToggle.textContent = '☀️ Light Mode';
        }
    }
});

