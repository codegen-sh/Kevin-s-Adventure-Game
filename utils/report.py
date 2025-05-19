"""
Kevin's Adventure Game - Player Report Module

This module provides functionality to generate detailed reports about the player's
progress, achievements, and statistics in the game.
"""

import json
import os
from datetime import datetime


def generate_player_report(player, world):
    """
    Generate a comprehensive report of the player's progress and achievements.
    
    Args:
        player (dict): The player data dictionary
        world (dict): The world data dictionary
        
    Returns:
        dict: A report dictionary containing all player statistics and achievements
    """
    # Create the report structure
    report = {
        "player_name": player["name"],
        "report_generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "game_statistics": {
            "health": player["health"],
            "gold": player["gold"],
            "current_location": player["location"],
            "inventory_count": len(player["inventory"]),
            "inventory_items": player["inventory"],
        },
        "achievements": calculate_achievements(player, world),
        "location_visits": get_location_visits(world),
        "economic_summary": {
            "total_gold_earned": world.get("total_gold_earned", 0),
            "total_gold_spent": world.get("total_gold_spent", 0),
            "net_gold": world.get("total_gold_earned", 0) - world.get("total_gold_spent", 0),
        }
    }
    
    return report


def calculate_achievements(player, world):
    """
    Calculate the player's achievements based on their progress.
    
    Args:
        player (dict): The player data dictionary
        world (dict): The world data dictionary
        
    Returns:
        list: A list of achievement dictionaries
    """
    achievements = []
    
    # Check for inventory-based achievements
    if len(player["inventory"]) >= 10:
        achievements.append({
            "name": "Collector",
            "description": "Collected 10 or more items",
            "date_achieved": datetime.now().strftime("%Y-%m-%d")
        })
    
    if "sword" in player["inventory"]:
        achievements.append({
            "name": "Armed Adventurer",
            "description": "Found a sword",
            "date_achieved": datetime.now().strftime("%Y-%m-%d")
        })
    
    # Check for gold-based achievements
    if player["gold"] >= 200:
        achievements.append({
            "name": "Treasure Hunter",
            "description": "Accumulated 200 or more gold",
            "date_achieved": datetime.now().strftime("%Y-%m-%d")
        })
    
    # Check for location-based achievements
    visited_locations = world.get("visited_locations", [])
    if "Mountain" in visited_locations and "Forest" in visited_locations and "Village" in visited_locations:
        achievements.append({
            "name": "Explorer",
            "description": "Visited all main locations",
            "date_achieved": datetime.now().strftime("%Y-%m-%d")
        })
    
    return achievements


def get_location_visits(world):
    """
    Get statistics about location visits.
    
    Args:
        world (dict): The world data dictionary
        
    Returns:
        dict: A dictionary with location visit counts
    """
    location_visits = {}
    
    # Get the location visit counts from the world data
    for location, count in world.get("location_visits", {}).items():
        location_visits[location] = count
    
    return location_visits


def save_report_to_file(report, filename=None):
    """
    Save the generated report to a JSON file.
    
    Args:
        report (dict): The report dictionary
        filename (str, optional): Custom filename for the report
        
    Returns:
        str: The path to the saved report file
    """
    # Create reports directory if it doesn't exist
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{report['player_name']}_report_{timestamp}.json"
    
    filepath = os.path.join(reports_dir, filename)
    
    # Save the report to a file
    with open(filepath, 'w') as report_file:
        json.dump(report, report_file, indent=2)
    
    return filepath


def print_report_summary(report):
    """
    Print a formatted summary of the player's report to the console.
    
    Args:
        report (dict): The report dictionary
    """
    print("\n" + "=" * 60)
    print(f"ADVENTURE REPORT FOR: {report['player_name']}")
    print(f"Generated on: {report['report_generated']}")
    print("=" * 60)
    
    # Print game statistics
    print("\nGAME STATISTICS:")
    print(f"Health: {report['game_statistics']['health']}/100")
    print(f"Gold: {report['game_statistics']['gold']}")
    print(f"Current Location: {report['game_statistics']['current_location']}")
    print(f"Items Collected: {report['game_statistics']['inventory_count']}")
    
    # Print inventory
    if report['game_statistics']['inventory_items']:
        print("\nINVENTORY:")
        for item in report['game_statistics']['inventory_items']:
            print(f"- {item}")
    
    # Print achievements
    if report['achievements']:
        print("\nACHIEVEMENTS UNLOCKED:")
        for achievement in report['achievements']:
            print(f"- {achievement['name']}: {achievement['description']}")
    
    # Print location visits
    if report['location_visits']:
        print("\nLOCATION VISITS:")
        for location, count in report['location_visits'].items():
            print(f"- {location}: {count} visits")
    
    # Print economic summary
    print("\nECONOMIC SUMMARY:")
    print(f"Total Gold Earned: {report['economic_summary']['total_gold_earned']}")
    print(f"Total Gold Spent: {report['economic_summary']['total_gold_spent']}")
    print(f"Net Gold: {report['economic_summary']['net_gold']}")
    
    print("\n" + "=" * 60)
    print("END OF REPORT")
    print("=" * 60 + "\n")


def generate_and_save_report(player, world):
    """
    Generate a player report and save it to a file.
    
    Args:
        player (dict): The player data dictionary
        world (dict): The world data dictionary
        
    Returns:
        str: The path to the saved report file
    """
    report = generate_player_report(player, world)
    filepath = save_report_to_file(report)
    print_report_summary(report)
    print(f"\nDetailed report saved to: {filepath}")
    return filepath

