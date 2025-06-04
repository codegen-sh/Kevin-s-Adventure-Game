#!/usr/bin/env python3
"""
Performance profiling tool for Kevin's Adventure Game.

This tool profiles the game's performance and identifies bottlenecks.
"""

import cProfile
import pstats
import time
import sys
import os
from io import StringIO


def profile_game_startup():
    """Profile game startup performance."""
    print("Profiling game startup...")
    
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Import and initialize game components
    sys.path.insert(0, '.')
    from game.player import create_player
    from game.world import initialize_world
    from utils.text_formatting import print_welcome_message
    
    # Simulate game startup
    player = create_player("Test Player")
    world = initialize_world()
    
    profiler.disable()
    
    # Generate report
    s = StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats(20)  # Top 20 functions
    
    print("Game startup profiling results:")
    print(s.getvalue())


def profile_save_load_operations():
    """Profile save and load operations."""
    print("Profiling save/load operations...")
    
    sys.path.insert(0, '.')
    from game.player import create_player
    from game.world import initialize_world
    from utils.save_load import save_game, load_game
    
    # Create test data
    player = create_player("Profile Test")
    world = initialize_world()
    
    # Profile save operation
    profiler = cProfile.Profile()
    profiler.enable()
    
    save_game(player, world, "profile_test.json")
    
    profiler.disable()
    
    s = StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats(10)
    
    print("Save operation profiling results:")
    print(s.getvalue())
    
    # Profile load operation
    profiler = cProfile.Profile()
    profiler.enable()
    
    loaded_player, loaded_world = load_game("profile_test.json")
    
    profiler.disable()
    
    s = StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats(10)
    
    print("Load operation profiling results:")
    print(s.getvalue())
    
    # Clean up
    if os.path.exists("saves/profile_test.json"):
        os.remove("saves/profile_test.json")


def profile_location_exploration():
    """Profile location exploration performance."""
    print("Profiling location exploration...")
    
    sys.path.insert(0, '.')
    from game.player import create_player
    from game.world import initialize_world, interact_with_location
    
    player = create_player("Profile Test")
    world = initialize_world()
    
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Simulate multiple location interactions
    for _ in range(10):
        interact_with_location(world, player)
    
    profiler.disable()
    
    s = StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats(15)
    
    print("Location exploration profiling results:")
    print(s.getvalue())


def benchmark_game_loop():
    """Benchmark the main game loop performance."""
    print("Benchmarking game loop performance...")
    
    sys.path.insert(0, '.')
    from game.player import create_player, get_player_status
    from game.world import initialize_world, get_current_location
    
    player = create_player("Benchmark Test")
    world = initialize_world()
    
    # Benchmark status checks
    start_time = time.time()
    for _ in range(1000):
        status = get_player_status(player)
        location = get_current_location(world)
    end_time = time.time()
    
    print(f"1000 status checks took {end_time - start_time:.4f} seconds")
    print(f"Average time per status check: {(end_time - start_time) / 1000 * 1000:.4f} ms")


def memory_usage_analysis():
    """Analyze memory usage of game components."""
    print("Analyzing memory usage...")
    
    try:
        import psutil
        import gc
        
        process = psutil.Process()
        
        # Baseline memory
        gc.collect()
        baseline_memory = process.memory_info().rss / 1024 / 1024  # MB
        print(f"Baseline memory usage: {baseline_memory:.2f} MB")
        
        # Memory after importing modules
        sys.path.insert(0, '.')
        from game.player import create_player
        from game.world import initialize_world
        from utils.save_load import save_game, load_game
        
        gc.collect()
        import_memory = process.memory_info().rss / 1024 / 1024
        print(f"Memory after imports: {import_memory:.2f} MB (+{import_memory - baseline_memory:.2f} MB)")
        
        # Memory after creating game objects
        player = create_player("Memory Test")
        world = initialize_world()
        
        gc.collect()
        objects_memory = process.memory_info().rss / 1024 / 1024
        print(f"Memory after creating objects: {objects_memory:.2f} MB (+{objects_memory - import_memory:.2f} MB)")
        
        # Memory after multiple operations
        for i in range(100):
            player_copy = create_player(f"Test Player {i}")
            world_copy = initialize_world()
        
        gc.collect()
        operations_memory = process.memory_info().rss / 1024 / 1024
        print(f"Memory after 100 operations: {operations_memory:.2f} MB (+{operations_memory - objects_memory:.2f} MB)")
        
    except ImportError:
        print("psutil not available. Install with: pip install psutil")


def main():
    """Main profiling function."""
    print("Kevin's Adventure Game - Performance Profiler")
    print("=" * 50)
    
    # Run all profiling tests
    profile_game_startup()
    print("\n" + "=" * 50)
    
    profile_save_load_operations()
    print("\n" + "=" * 50)
    
    profile_location_exploration()
    print("\n" + "=" * 50)
    
    benchmark_game_loop()
    print("\n" + "=" * 50)
    
    memory_usage_analysis()
    print("\n" + "=" * 50)
    
    print("Profiling complete!")


if __name__ == "__main__":
    main()
