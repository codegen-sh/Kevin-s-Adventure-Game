"""
Command parser for Kevin's Adventure Game.
Handles parsing and interpreting user input.
"""

from typing import List, Tuple, Optional
import re


class CommandParser:
    """Parses user input into commands and arguments."""
    
    def __init__(self):
        # Common synonyms and aliases
        self.synonyms = {
            # Movement
            'go': ['move', 'travel', 'walk', 'run'],
            'north': ['n'],
            'south': ['s'],
            'east': ['e'],
            'west': ['w'],
            
            # Interaction
            'look': ['l', 'examine', 'inspect', 'see'],
            'take': ['get', 'pick', 'pickup', 'grab'],
            'drop': ['put', 'place', 'leave'],
            'use': ['utilize', 'employ'],
            'talk': ['speak', 'chat', 'converse'],
            
            # Inventory
            'inventory': ['i', 'inv', 'items', 'bag'],
            
            # System
            'help': ['h', '?', 'commands'],
            'quit': ['q', 'exit', 'bye', 'goodbye'],
            'save': ['s'],
            'load': ['l'],
        }
        
        # Build reverse lookup
        self.alias_map = {}
        for command, aliases in self.synonyms.items():
            self.alias_map[command] = command
            for alias in aliases:
                self.alias_map[alias] = command
    
    def parse(self, user_input: str) -> Tuple[str, List[str]]:
        """
        Parse user input into command and arguments.
        
        Returns:
            Tuple of (command, arguments)
        """
        if not user_input or not user_input.strip():
            return "", []
        
        # Clean and tokenize input
        tokens = self._tokenize(user_input.strip().lower())
        
        if not tokens:
            return "", []
        
        # First token is the command
        raw_command = tokens[0]
        args = tokens[1:] if len(tokens) > 1 else []
        
        # Resolve command through alias map
        command = self.alias_map.get(raw_command, raw_command)
        
        # Handle special cases
        command, args = self._handle_special_cases(command, args)
        
        return command, args
    
    def _tokenize(self, text: str) -> List[str]:
        """Tokenize input text, handling quoted strings."""
        # Simple tokenization - split on whitespace but preserve quoted strings
        tokens = []
        current_token = ""
        in_quotes = False
        
        for char in text:
            if char == '"' or char == "'":
                in_quotes = not in_quotes
            elif char.isspace() and not in_quotes:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            else:
                current_token += char
        
        if current_token:
            tokens.append(current_token)
        
        return tokens
    
    def _handle_special_cases(self, command: str, args: List[str]) -> Tuple[str, List[str]]:
        """Handle special parsing cases."""
        
        # Handle directional movement without "go"
        directions = ['north', 'south', 'east', 'west', 'n', 's', 'e', 'w']
        if command in directions:
            return 'go', [command]
        
        # Handle location names as movement
        locations = ['village', 'forest', 'cave', 'mountain']
        if command in locations:
            return 'go', [command]
        
        # Handle "pick up" as "take"
        if command == 'pick' and args and args[0] == 'up':
            return 'take', args[1:]
        
        # Handle "look at" as "look"
        if command == 'look' and args and args[0] == 'at':
            return 'look', args[1:]
        
        # Handle "talk to" as "talk"
        if command == 'talk' and args and args[0] == 'to':
            return 'talk', args[1:]
        
        return command, args
    
    def suggest_command(self, invalid_command: str) -> Optional[str]:
        """Suggest a similar valid command for an invalid input."""
        invalid_command = invalid_command.lower()
        
        # Check for close matches
        for command in self.alias_map.keys():
            if self._is_similar(invalid_command, command):
                return self.alias_map[command]
        
        return None
    
    def _is_similar(self, word1: str, word2: str, threshold: int = 2) -> bool:
        """Check if two words are similar using simple edit distance."""
        if abs(len(word1) - len(word2)) > threshold:
            return False
        
        # Simple Levenshtein distance calculation
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        
        distances = range(len(word2) + 1)
        for i1, char1 in enumerate(word1):
            new_distances = [i1 + 1]
            for i2, char2 in enumerate(word2):
                if char1 == char2:
                    new_distances.append(distances[i2])
                else:
                    new_distances.append(1 + min(distances[i2], distances[i2 + 1], new_distances[-1]))
            distances = new_distances
        
        return distances[-1] <= threshold
    
    def get_help_text(self) -> str:
        """Get help text showing available commands."""
        help_text = "Available commands:\n\n"
        
        categories = {
            "Movement": ["go [location]", "north/south/east/west"],
            "Interaction": ["look [target]", "take [item]", "drop [item]", "use [item]", "talk [character]"],
            "Inventory": ["inventory", "status"],
            "System": ["help", "save", "load", "quit"]
        }
        
        for category, commands in categories.items():
            help_text += f"{category}:\n"
            for command in commands:
                help_text += f"  {command}\n"
            help_text += "\n"
        
        help_text += "You can also use common abbreviations like 'i' for inventory, 'l' for look, etc."
        
        return help_text

