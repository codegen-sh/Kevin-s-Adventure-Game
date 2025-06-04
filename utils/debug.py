"""
Debug utilities and development tools for Kevin's Adventure Game.
Provides debug mode functionality, performance monitoring, and development aids.
"""

import time
import traceback
import sys
import os
from functools import wraps
from typing import Any, Dict, List, Optional, Callable
from datetime import datetime
import json

from utils.logging_config import get_logger, log_game_event
from exceptions import GameError

# Debug configuration
DEBUG_MODE = False
VERBOSE_MODE = False
PERFORMANCE_MONITORING = False
DEBUG_COMMANDS_ENABLED = False

# Performance tracking
performance_stats = {}
function_call_counts = {}
error_counts = {}

# Initialize logger
logger = get_logger('debug')


def enable_debug_mode(verbose: bool = False, performance: bool = False, commands: bool = False):
    """
    Enable debug mode with various options.
    
    Args:
        verbose (bool): Enable verbose logging
        performance (bool): Enable performance monitoring
        commands (bool): Enable debug commands
    """
    global DEBUG_MODE, VERBOSE_MODE, PERFORMANCE_MONITORING, DEBUG_COMMANDS_ENABLED
    
    DEBUG_MODE = True
    VERBOSE_MODE = verbose
    PERFORMANCE_MONITORING = performance
    DEBUG_COMMANDS_ENABLED = commands
    
    logger.info("Debug mode enabled")
    if verbose:
        logger.info("Verbose mode enabled")
    if performance:
        logger.info("Performance monitoring enabled")
    if commands:
        logger.info("Debug commands enabled")
    
    print("🐛 Debug mode activated!")
    if verbose:
        print("📝 Verbose logging enabled")
    if performance:
        print("⏱️  Performance monitoring enabled")
    if commands:
        print("🔧 Debug commands enabled")


def disable_debug_mode():
    """Disable debug mode and all related features."""
    global DEBUG_MODE, VERBOSE_MODE, PERFORMANCE_MONITORING, DEBUG_COMMANDS_ENABLED
    
    DEBUG_MODE = False
    VERBOSE_MODE = False
    PERFORMANCE_MONITORING = False
    DEBUG_COMMANDS_ENABLED = False
    
    logger.info("Debug mode disabled")
    print("Debug mode deactivated")


def is_debug_mode() -> bool:
    """Check if debug mode is enabled."""
    return DEBUG_MODE


def debug_print(*args, **kwargs):
    """Print debug information only if debug mode is enabled."""
    if DEBUG_MODE:
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[DEBUG {timestamp}]", *args, **kwargs)


def verbose_print(*args, **kwargs):
    """Print verbose information only if verbose mode is enabled."""
    if VERBOSE_MODE:
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[VERBOSE {timestamp}]", *args, **kwargs)


def performance_timer(func: Callable) -> Callable:
    """
    Decorator to measure function execution time.
    
    Args:
        func (Callable): Function to measure
    
    Returns:
        Callable: Wrapped function with timing
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not PERFORMANCE_MONITORING:
            return func(*args, **kwargs)
        
        start_time = time.perf_counter()
        
        try:
            result = func(*args, **kwargs)
            success = True
            error = None
        except Exception as e:
            result = None
            success = False
            error = str(e)
            raise
        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            
            # Track performance stats
            func_name = f"{func.__module__}.{func.__name__}"
            if func_name not in performance_stats:
                performance_stats[func_name] = {
                    'total_time': 0,
                    'call_count': 0,
                    'avg_time': 0,
                    'min_time': float('inf'),
                    'max_time': 0,
                    'errors': 0
                }
            
            stats = performance_stats[func_name]
            stats['total_time'] += execution_time
            stats['call_count'] += 1
            stats['avg_time'] = stats['total_time'] / stats['call_count']
            stats['min_time'] = min(stats['min_time'], execution_time)
            stats['max_time'] = max(stats['max_time'], execution_time)
            
            if not success:
                stats['errors'] += 1
            
            # Log slow functions
            if execution_time > 0.1:  # Log functions taking more than 100ms
                logger.warning(f"Slow function: {func_name} took {execution_time:.3f}s")
            
            verbose_print(f"⏱️  {func_name}: {execution_time:.3f}s")
        
        return result
    
    return wrapper


def debug_function_calls(func: Callable) -> Callable:
    """
    Decorator to log function calls in debug mode.
    
    Args:
        func (Callable): Function to log
    
    Returns:
        Callable: Wrapped function with call logging
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = f"{func.__module__}.{func.__name__}"
        
        # Track function call counts
        if func_name not in function_call_counts:
            function_call_counts[func_name] = 0
        function_call_counts[func_name] += 1
        
        if DEBUG_MODE:
            debug_print(f"🔧 Calling {func_name}")
            if VERBOSE_MODE:
                debug_print(f"   Args: {args}")
                debug_print(f"   Kwargs: {kwargs}")
        
        try:
            result = func(*args, **kwargs)
            if DEBUG_MODE and VERBOSE_MODE:
                debug_print(f"✅ {func_name} completed successfully")
            return result
        except Exception as e:
            if DEBUG_MODE:
                debug_print(f"❌ {func_name} failed: {e}")
            
            # Track error counts
            if func_name not in error_counts:
                error_counts[func_name] = 0
            error_counts[func_name] += 1
            
            raise
    
    return wrapper


def log_game_state(player: Dict[str, Any], world: Dict[str, Any], action: str = None):
    """
    Log current game state for debugging.
    
    Args:
        player (dict): Player state
        world (dict): World state
        action (str): Current action being performed
    """
    if not DEBUG_MODE:
        return
    
    state_info = {
        'player': {
            'name': player.get('name', 'unknown'),
            'health': player.get('health', 'unknown'),
            'location': player.get('location', 'unknown'),
            'inventory_count': len(player.get('inventory', [])),
            'gold': player.get('gold', 'unknown')
        },
        'world': {
            'current_location': world.get('current_location', 'unknown'),
            'locations_count': len(world.get('locations', {}))
        }
    }
    
    if action:
        state_info['action'] = action
    
    debug_print(f"🎮 Game State: {json.dumps(state_info, indent=2)}")
    
    if VERBOSE_MODE:
        verbose_print(f"📦 Full Player Inventory: {player.get('inventory', [])}")
        verbose_print(f"🗺️  Available Locations: {list(world.get('locations', {}).keys())}")


def debug_exception(exception: Exception, context: Dict[str, Any] = None):
    """
    Debug an exception with full context information.
    
    Args:
        exception (Exception): Exception to debug
        context (dict): Additional context information
    """
    if not DEBUG_MODE:
        return
    
    debug_print(f"🚨 Exception Debug Information:")
    debug_print(f"   Type: {type(exception).__name__}")
    debug_print(f"   Message: {str(exception)}")
    
    if isinstance(exception, GameError):
        debug_print(f"   Game Error Context: {exception.context}")
        debug_print(f"   Recovery Suggestion: {exception.recovery_suggestion}")
    
    if context:
        debug_print(f"   Additional Context: {json.dumps(context, indent=4, default=str)}")
    
    if VERBOSE_MODE:
        debug_print(f"   Traceback:")
        traceback.print_exc()


def get_performance_report() -> Dict[str, Any]:
    """
    Get a comprehensive performance report.
    
    Returns:
        dict: Performance statistics
    """
    report = {
        'performance_stats': performance_stats.copy(),
        'function_call_counts': function_call_counts.copy(),
        'error_counts': error_counts.copy(),
        'total_functions_called': len(function_call_counts),
        'total_errors': sum(error_counts.values()),
        'slowest_functions': [],
        'most_called_functions': [],
        'error_prone_functions': []
    }
    
    # Find slowest functions
    if performance_stats:
        slowest = sorted(
            performance_stats.items(),
            key=lambda x: x[1]['avg_time'],
            reverse=True
        )[:5]
        report['slowest_functions'] = [
            {'function': func, 'avg_time': stats['avg_time'], 'call_count': stats['call_count']}
            for func, stats in slowest
        ]
    
    # Find most called functions
    if function_call_counts:
        most_called = sorted(
            function_call_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        report['most_called_functions'] = [
            {'function': func, 'call_count': count}
            for func, count in most_called
        ]
    
    # Find error-prone functions
    if error_counts:
        error_prone = sorted(
            error_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        report['error_prone_functions'] = [
            {'function': func, 'error_count': count}
            for func, count in error_prone
        ]
    
    return report


def print_performance_report():
    """Print a formatted performance report."""
    if not PERFORMANCE_MONITORING:
        print("Performance monitoring is not enabled.")
        return
    
    report = get_performance_report()
    
    print("\n" + "="*60)
    print("🔍 PERFORMANCE REPORT")
    print("="*60)
    
    print(f"📊 Total Functions Called: {report['total_functions_called']}")
    print(f"❌ Total Errors: {report['total_errors']}")
    
    if report['slowest_functions']:
        print("\n⏱️  Slowest Functions:")
        for func_info in report['slowest_functions']:
            print(f"   {func_info['function']}: {func_info['avg_time']:.3f}s avg ({func_info['call_count']} calls)")
    
    if report['most_called_functions']:
        print("\n📞 Most Called Functions:")
        for func_info in report['most_called_functions']:
            print(f"   {func_info['function']}: {func_info['call_count']} calls")
    
    if report['error_prone_functions']:
        print("\n🚨 Error-Prone Functions:")
        for func_info in report['error_prone_functions']:
            print(f"   {func_info['function']}: {func_info['error_count']} errors")
    
    print("="*60)


def reset_performance_stats():
    """Reset all performance statistics."""
    global performance_stats, function_call_counts, error_counts
    
    performance_stats.clear()
    function_call_counts.clear()
    error_counts.clear()
    
    logger.info("Performance statistics reset")
    debug_print("📊 Performance statistics reset")


def debug_command_handler(command: str, player: Dict[str, Any] = None, world: Dict[str, Any] = None) -> bool:
    """
    Handle debug commands.
    
    Args:
        command (str): Debug command
        player (dict): Player state
        world (dict): World state
    
    Returns:
        bool: True if command was handled
    """
    if not DEBUG_COMMANDS_ENABLED:
        return False
    
    command = command.lower().strip()
    
    if command == "debug help":
        print_debug_help()
        return True
    
    elif command == "debug status":
        print_debug_status()
        return True
    
    elif command == "debug performance":
        print_performance_report()
        return True
    
    elif command == "debug reset":
        reset_performance_stats()
        return True
    
    elif command == "debug state" and player and world:
        log_game_state(player, world, "debug_command")
        return True
    
    elif command.startswith("debug heal ") and player:
        try:
            amount = int(command.split()[-1])
            old_health = player.get('health', 0)
            player['health'] = min(100, player.get('health', 0) + amount)
            print(f"🩹 Debug heal: {old_health} -> {player['health']}")
            return True
        except (ValueError, IndexError):
            print("Usage: debug heal <amount>")
            return True
    
    elif command.startswith("debug gold ") and player:
        try:
            amount = int(command.split()[-1])
            old_gold = player.get('gold', 0)
            player['gold'] = max(0, player.get('gold', 0) + amount)
            print(f"💰 Debug gold: {old_gold} -> {player['gold']}")
            return True
        except (ValueError, IndexError):
            print("Usage: debug gold <amount>")
            return True
    
    elif command.startswith("debug item ") and player:
        try:
            item = command.split("debug item ", 1)[1]
            if 'inventory' not in player:
                player['inventory'] = []
            player['inventory'].append(item)
            print(f"📦 Debug item added: {item}")
            return True
        except IndexError:
            print("Usage: debug item <item_name>")
            return True
    
    elif command.startswith("debug teleport ") and player:
        try:
            location = command.split("debug teleport ", 1)[1]
            old_location = player.get('location', 'unknown')
            player['location'] = location
            print(f"🚀 Debug teleport: {old_location} -> {location}")
            return True
        except IndexError:
            print("Usage: debug teleport <location>")
            return True
    
    return False


def print_debug_help():
    """Print available debug commands."""
    print("\n🔧 DEBUG COMMANDS:")
    print("  debug help        - Show this help")
    print("  debug status      - Show debug mode status")
    print("  debug performance - Show performance report")
    print("  debug reset       - Reset performance statistics")
    print("  debug state       - Show current game state")
    print("  debug heal <n>    - Heal player by n points")
    print("  debug gold <n>    - Add n gold to player")
    print("  debug item <name> - Add item to inventory")
    print("  debug teleport <location> - Teleport to location")


def print_debug_status():
    """Print current debug mode status."""
    print(f"\n🐛 DEBUG MODE STATUS:")
    print(f"  Debug Mode: {'✅ Enabled' if DEBUG_MODE else '❌ Disabled'}")
    print(f"  Verbose Mode: {'✅ Enabled' if VERBOSE_MODE else '❌ Disabled'}")
    print(f"  Performance Monitoring: {'✅ Enabled' if PERFORMANCE_MONITORING else '❌ Disabled'}")
    print(f"  Debug Commands: {'✅ Enabled' if DEBUG_COMMANDS_ENABLED else '❌ Disabled'}")


def setup_debug_from_args(args: List[str]):
    """
    Setup debug mode from command line arguments.
    
    Args:
        args (list): Command line arguments
    """
    if '--debug' in args:
        verbose = '--verbose' in args or '-v' in args
        performance = '--performance' in args or '-p' in args
        commands = '--debug-commands' in args or '-c' in args
        
        enable_debug_mode(verbose=verbose, performance=performance, commands=commands)


def create_debug_decorator(name: str = None):
    """
    Create a debug decorator with optional custom name.
    
    Args:
        name (str): Custom name for the function
    
    Returns:
        Callable: Debug decorator
    """
    def decorator(func: Callable) -> Callable:
        func_name = name or f"{func.__module__}.{func.__name__}"
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            if DEBUG_MODE:
                debug_print(f"🔧 Entering {func_name}")
            
            try:
                result = func(*args, **kwargs)
                if DEBUG_MODE:
                    debug_print(f"✅ Exiting {func_name}")
                return result
            except Exception as e:
                if DEBUG_MODE:
                    debug_print(f"❌ Exception in {func_name}: {e}")
                raise
        
        return wrapper
    return decorator


# Convenience decorators
debug_trace = create_debug_decorator()
debug_performance = lambda func: performance_timer(debug_function_calls(func))

