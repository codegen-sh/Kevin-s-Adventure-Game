"""
Script to migrate files from the old structure to the new structure.
"""
import os
import shutil
from pathlib import Path

# Define source and destination directories
SOURCE_DIRS = {
    "game": "game",
    "locations": "locations",
    "utils": "utils",
}

DEST_PREFIX = "kevin_adventure_game"

# Files to skip (already created)
SKIP_FILES = [
    "game/actions.py",
    "locations/cave.py",
    "main.py",
]

def migrate_files():
    """Migrate files from old structure to new structure."""
    for source_dir, dest_subdir in SOURCE_DIRS.items():
        # Create destination directory if it doesn't exist
        dest_dir = os.path.join(DEST_PREFIX, dest_subdir)
        os.makedirs(dest_dir, exist_ok=True)
        
        # Copy files
        for file in os.listdir(source_dir):
            if file.endswith(".py"):
                source_path = os.path.join(source_dir, file)
                
                # Skip files that we've already created
                if source_path in SKIP_FILES:
                    print(f"Skipping {source_path} (already created)")
                    continue
                
                dest_path = os.path.join(dest_dir, file)
                print(f"Copying {source_path} to {dest_path}")
                
                # Read the file content
                with open(source_path, "r") as f:
                    content = f.read()
                
                # Update imports to use the new package structure
                for old_dir in SOURCE_DIRS.keys():
                    content = content.replace(
                        f"from {old_dir}.",
                        f"from {DEST_PREFIX}.{old_dir}."
                    )
                
                # Write the updated content to the destination file
                with open(dest_path, "w") as f:
                    f.write(content)

if __name__ == "__main__":
    migrate_files()

