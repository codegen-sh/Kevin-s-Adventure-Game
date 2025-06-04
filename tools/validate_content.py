#!/usr/bin/env python3
"""
Content validation tool for Kevin's Adventure Game.

This tool validates game content including locations, items, events, and data structures.
"""

import json
import os
import sys
import importlib.util
from typing import Dict, List, Any, Tuple


class ContentValidator:
    """Validates game content for consistency and correctness."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def validate_location_module(self, module_path: str) -> bool:
        """Validate a location module."""
        try:
            spec = importlib.util.spec_from_file_location("location", module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            location_name = os.path.basename(module_path).replace('.py', '')
            
            # Check required functions
            required_functions = [
                f'explore_{location_name}',
                f'get_{location_name}_description',
                f'get_{location_name}_items',
                f'get_{location_name}_connections'
            ]
            
            for func_name in required_functions:
                if not hasattr(module, func_name):
                    self.errors.append(f"Missing function {func_name} in {module_path}")
            
            # Validate function signatures
            if hasattr(module, f'explore_{location_name}'):
                func = getattr(module, f'explore_{location_name}')
                if func.__code__.co_argcount != 2:
                    self.errors.append(f"Function explore_{location_name} should take 2 arguments (player, world)")
            
            return len(self.errors) == 0
            
        except Exception as e:
            self.errors.append(f"Error loading {module_path}: {e}")
            return False
    
    def validate_save_file(self, save_path: str) -> bool:
        """Validate a save file structure."""
        try:
            with open(save_path, 'r') as f:
                save_data = json.load(f)
            
            # Check required top-level keys
            required_keys = ['player', 'world']
            for key in required_keys:
                if key not in save_data:
                    self.errors.append(f"Missing required key '{key}' in {save_path}")
            
            # Validate player structure
            if 'player' in save_data:
                player = save_data['player']
                player_keys = ['name', 'health', 'inventory', 'location', 'gold']
                for key in player_keys:
                    if key not in player:
                        self.errors.append(f"Missing player key '{key}' in {save_path}")
                
                # Validate data types
                if 'health' in player and not isinstance(player['health'], int):
                    self.errors.append(f"Player health must be integer in {save_path}")
                
                if 'inventory' in player and not isinstance(player['inventory'], list):
                    self.errors.append(f"Player inventory must be list in {save_path}")
                
                if 'gold' in player and not isinstance(player['gold'], int):
                    self.errors.append(f"Player gold must be integer in {save_path}")
            
            # Validate world structure
            if 'world' in save_data:
                world = save_data['world']
                if 'locations' not in world:
                    self.errors.append(f"Missing world locations in {save_path}")
                
                if 'current_location' not in world:
                    self.errors.append(f"Missing current_location in {save_path}")
            
            return len(self.errors) == 0
            
        except json.JSONDecodeError:
            self.errors.append(f"Invalid JSON in {save_path}")
            return False
        except Exception as e:
            self.errors.append(f"Error validating {save_path}: {e}")
            return False
    
    def validate_world_consistency(self) -> bool:
        """Validate world location connections for consistency."""
        try:
            # Import world module
            sys.path.insert(0, '.')
            from game.world import initialize_world
            
            world = initialize_world()
            locations = world['locations']
            
            # Check that all connections are bidirectional
            for location_name, location_data in locations.items():
                connections = location_data.get('connections', [])
                
                for connected_location in connections:
                    if connected_location not in locations:
                        self.errors.append(f"Location {location_name} connects to non-existent {connected_location}")
                        continue
                    
                    # Check if connection is bidirectional
                    reverse_connections = locations[connected_location].get('connections', [])
                    if location_name not in reverse_connections:
                        self.warnings.append(f"Connection from {location_name} to {connected_location} is not bidirectional")
            
            return len(self.errors) == 0
            
        except Exception as e:
            self.errors.append(f"Error validating world consistency: {e}")
            return False
    
    def validate_item_descriptions(self) -> bool:
        """Validate that all items have descriptions."""
        try:
            sys.path.insert(0, '.')
            from game.items import item_descriptions
            
            # Check for empty descriptions
            for item, description in item_descriptions.items():
                if not description or not description.strip():
                    self.errors.append(f"Item '{item}' has empty description")
                
                if len(description) < 10:
                    self.warnings.append(f"Item '{item}' has very short description")
            
            return len(self.errors) == 0
            
        except Exception as e:
            self.errors.append(f"Error validating item descriptions: {e}")
            return False
    
    def run_all_validations(self) -> bool:
        """Run all validation checks."""
        print("Running content validation...")
        
        # Validate location modules
        locations_dir = 'locations'
        if os.path.exists(locations_dir):
            for filename in os.listdir(locations_dir):
                if filename.endswith('.py') and filename != '__init__.py':
                    module_path = os.path.join(locations_dir, filename)
                    self.validate_location_module(module_path)
        
        # Validate save files
        saves_dir = 'saves'
        if os.path.exists(saves_dir):
            for filename in os.listdir(saves_dir):
                if filename.endswith('.json'):
                    save_path = os.path.join(saves_dir, filename)
                    self.validate_save_file(save_path)
        
        # Validate world consistency
        self.validate_world_consistency()
        
        # Validate item descriptions
        self.validate_item_descriptions()
        
        # Report results
        if self.errors:
            print(f"\n❌ Found {len(self.errors)} errors:")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print(f"\n⚠️  Found {len(self.warnings)} warnings:")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if not self.errors and not self.warnings:
            print("✅ All validations passed!")
        elif not self.errors:
            print("✅ No errors found, but there are warnings to address.")
        
        return len(self.errors) == 0


def main():
    """Main function."""
    validator = ContentValidator()
    success = validator.run_all_validations()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
