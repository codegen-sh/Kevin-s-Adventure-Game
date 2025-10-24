"""
Centralized logging configuration for Kevin's Adventure Game.
Provides structured logging with file rotation, multiple log levels, and debug mode support.
"""

import logging
import logging.handlers
import os
import sys
from datetime import datetime
from pathlib import Path
import json


# Log directory and file paths
LOG_DIR = Path("logs")
MAIN_LOG_FILE = LOG_DIR / "game.log"
ERROR_LOG_FILE = LOG_DIR / "errors.log"
DEBUG_LOG_FILE = LOG_DIR / "debug.log"
PLAYER_ACTIONS_LOG = LOG_DIR / "player_actions.log"
GAME_EVENTS_LOG = LOG_DIR / "game_events.log"

# Log format configurations
DETAILED_FORMAT = "%(asctime)s | %(name)s | %(levelname)s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s"
SIMPLE_FORMAT = "%(asctime)s | %(levelname)s | %(message)s"
JSON_FORMAT = "%(asctime)s | %(name)s | %(levelname)s | %(message)s | %(pathname)s | %(lineno)d"

# Global debug mode flag
DEBUG_MODE = False
VERBOSE_LOGGING = False


class JSONFormatter(logging.Formatter):
    """Custom JSON formatter for structured logging."""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
            'thread': record.thread,
            'process': record.process
        }
        
        # Add exception information if present
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        # Add extra fields if present
        if hasattr(record, 'player_name'):
            log_entry['player_name'] = record.player_name
        if hasattr(record, 'location'):
            log_entry['location'] = record.location
        if hasattr(record, 'action'):
            log_entry['action'] = record.action
        if hasattr(record, 'session_id'):
            log_entry['session_id'] = record.session_id
        
        return json.dumps(log_entry)


class GameLoggerAdapter(logging.LoggerAdapter):
    """Custom logger adapter that adds game context to log records."""
    
    def process(self, msg, kwargs):
        # Add context information to the log record
        extra = kwargs.get('extra', {})
        extra.update(self.extra)
        kwargs['extra'] = extra
        return msg, kwargs


def ensure_log_directory():
    """Ensure that the log directory exists."""
    LOG_DIR.mkdir(exist_ok=True)


def setup_file_handler(log_file, level=logging.INFO, max_bytes=10*1024*1024, backup_count=5, formatter=None):
    """
    Set up a rotating file handler.
    
    Args:
        log_file (Path): Path to the log file
        level (int): Logging level
        max_bytes (int): Maximum file size before rotation
        backup_count (int): Number of backup files to keep
        formatter (logging.Formatter): Log formatter
    
    Returns:
        logging.handlers.RotatingFileHandler: Configured file handler
    """
    handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    handler.setLevel(level)
    
    if formatter:
        handler.setFormatter(formatter)
    else:
        handler.setFormatter(logging.Formatter(DETAILED_FORMAT))
    
    return handler


def setup_console_handler(level=logging.INFO):
    """
    Set up console handler for logging to stdout.
    
    Args:
        level (int): Logging level
    
    Returns:
        logging.StreamHandler: Configured console handler
    """
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(SIMPLE_FORMAT))
    return handler


def setup_logger(name, level=logging.INFO, console_output=True, file_output=True):
    """
    Set up a logger with both file and console handlers.
    
    Args:
        name (str): Logger name
        level (int): Logging level
        console_output (bool): Whether to output to console
        file_output (bool): Whether to output to file
    
    Returns:
        logging.Logger: Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Clear existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Add console handler
    if console_output:
        console_handler = setup_console_handler(level)
        logger.addHandler(console_handler)
    
    # Add file handler
    if file_output:
        file_handler = setup_file_handler(MAIN_LOG_FILE, level)
        logger.addHandler(file_handler)
    
    # Add error-specific handler for ERROR and CRITICAL levels
    if level <= logging.ERROR:
        error_handler = setup_file_handler(
            ERROR_LOG_FILE,
            level=logging.ERROR,
            formatter=logging.Formatter(DETAILED_FORMAT)
        )
        logger.addHandler(error_handler)
    
    return logger


def setup_debug_logger():
    """Set up debug logger with verbose output."""
    debug_logger = logging.getLogger('debug')
    debug_logger.setLevel(logging.DEBUG)
    debug_logger.handlers.clear()
    
    # Debug file handler with JSON formatting
    debug_handler = setup_file_handler(
        DEBUG_LOG_FILE,
        level=logging.DEBUG,
        formatter=JSONFormatter()
    )
    debug_logger.addHandler(debug_handler)
    
    # Console handler for debug mode
    if DEBUG_MODE:
        console_handler = setup_console_handler(logging.DEBUG)
        debug_logger.addHandler(console_handler)
    
    return debug_logger


def setup_player_actions_logger():
    """Set up logger specifically for player actions."""
    actions_logger = logging.getLogger('player_actions')
    actions_logger.setLevel(logging.INFO)
    actions_logger.handlers.clear()
    
    # Player actions file handler
    actions_handler = setup_file_handler(
        PLAYER_ACTIONS_LOG,
        level=logging.INFO,
        formatter=JSONFormatter()
    )
    actions_logger.addHandler(actions_handler)
    
    return actions_logger


def setup_game_events_logger():
    """Set up logger specifically for game events."""
    events_logger = logging.getLogger('game_events')
    events_logger.setLevel(logging.INFO)
    events_logger.handlers.clear()
    
    # Game events file handler
    events_handler = setup_file_handler(
        GAME_EVENTS_LOG,
        level=logging.INFO,
        formatter=JSONFormatter()
    )
    events_logger.addHandler(events_handler)
    
    return events_logger


def initialize_logging(debug_mode=False, verbose=False, log_level=logging.INFO):
    """
    Initialize the complete logging system.
    
    Args:
        debug_mode (bool): Enable debug mode
        verbose (bool): Enable verbose logging
        log_level (int): Base logging level
    """
    global DEBUG_MODE, VERBOSE_LOGGING
    
    DEBUG_MODE = debug_mode
    VERBOSE_LOGGING = verbose
    
    # Ensure log directory exists
    ensure_log_directory()
    
    # Adjust log level based on debug mode
    if debug_mode:
        log_level = logging.DEBUG
    elif verbose:
        log_level = logging.INFO
    
    # Set up main loggers
    main_logger = setup_logger('main', log_level, console_output=True)
    game_logger = setup_logger('game', log_level, console_output=debug_mode)
    error_logger = setup_logger('error', logging.ERROR, console_output=True)
    
    # Set up specialized loggers
    debug_logger = setup_debug_logger()
    actions_logger = setup_player_actions_logger()
    events_logger = setup_game_events_logger()
    
    # Log initialization
    main_logger.info("Logging system initialized")
    if debug_mode:
        debug_logger.debug("Debug mode enabled")
    if verbose:
        main_logger.info("Verbose logging enabled")
    
    return {
        'main': main_logger,
        'game': game_logger,
        'error': error_logger,
        'debug': debug_logger,
        'actions': actions_logger,
        'events': events_logger
    }


def get_logger(name='main'):
    """
    Get a logger by name.
    
    Args:
        name (str): Logger name
    
    Returns:
        logging.Logger: Logger instance
    """
    return logging.getLogger(name)


def get_game_logger_adapter(player=None, session_id=None, **context):
    """
    Get a game logger adapter with context information.
    
    Args:
        player (dict): Player state for context
        session_id (str): Session identifier
        **context: Additional context information
    
    Returns:
        GameLoggerAdapter: Logger adapter with context
    """
    logger = get_logger('game')
    
    extra = {}
    if player:
        extra['player_name'] = player.get('name')
        extra['player_location'] = player.get('location')
    if session_id:
        extra['session_id'] = session_id
    extra.update(context)
    
    return GameLoggerAdapter(logger, extra)


def log_player_action(player, action, location=None, result=None, session_id=None):
    """
    Log a player action with context.
    
    Args:
        player (dict): Player state
        action (str): Action performed
        location (str): Location where action was performed
        result (str): Result of the action
        session_id (str): Session identifier
    """
    logger = get_logger('player_actions')
    
    extra = {
        'player_name': player.get('name') if player else 'unknown',
        'action': action,
        'location': location or (player.get('location') if player else 'unknown'),
        'player_health': player.get('health') if player else 'unknown',
        'inventory_count': len(player.get('inventory', [])) if player else 0
    }
    
    if result:
        extra['result'] = result
    if session_id:
        extra['session_id'] = session_id
    
    message = f"Player action: {action}"
    if result:
        message += f" -> {result}"
    
    logger.info(message, extra=extra)


def log_game_event(event_type, description, player=None, world=None, session_id=None, **context):
    """
    Log a game event with context.
    
    Args:
        event_type (str): Type of event
        description (str): Event description
        player (dict): Player state
        world (dict): World state
        session_id (str): Session identifier
        **context: Additional context information
    """
    logger = get_logger('game_events')
    
    extra = {
        'event_type': event_type,
        'description': description
    }
    
    if player:
        extra.update({
            'player_name': player.get('name'),
            'player_location': player.get('location'),
            'player_health': player.get('health')
        })
    
    if world:
        extra.update({
            'world_location': world.get('current_location'),
            'world_locations_count': len(world.get('locations', {}))
        })
    
    if session_id:
        extra['session_id'] = session_id
    
    extra.update(context)
    
    logger.info(f"Game event: {event_type} - {description}", extra=extra)


def log_error_with_context(error, player=None, world=None, action=None, session_id=None):
    """
    Log an error with full context information.
    
    Args:
        error (Exception): The error that occurred
        player (dict): Player state
        world (dict): World state
        action (str): Action being performed when error occurred
        session_id (str): Session identifier
    """
    logger = get_logger('error')
    
    extra = {
        'error_type': type(error).__name__,
        'error_message': str(error)
    }
    
    if player:
        extra.update({
            'player_name': player.get('name'),
            'player_location': player.get('location'),
            'player_health': player.get('health'),
            'inventory': player.get('inventory', [])
        })
    
    if world:
        extra.update({
            'world_location': world.get('current_location'),
            'available_locations': list(world.get('locations', {}).keys())
        })
    
    if action:
        extra['action'] = action
    
    if session_id:
        extra['session_id'] = session_id
    
    logger.error(f"Error occurred: {error}", extra=extra, exc_info=True)


def cleanup_old_logs(days_to_keep=30):
    """
    Clean up old log files.
    
    Args:
        days_to_keep (int): Number of days of logs to keep
    """
    if not LOG_DIR.exists():
        return
    
    cutoff_time = datetime.now().timestamp() - (days_to_keep * 24 * 60 * 60)
    
    for log_file in LOG_DIR.glob("*.log*"):
        if log_file.stat().st_mtime < cutoff_time:
            try:
                log_file.unlink()
                print(f"Deleted old log file: {log_file}")
            except OSError as e:
                print(f"Failed to delete log file {log_file}: {e}")


# Initialize logging on module import
if not logging.getLogger().handlers:
    initialize_logging()

