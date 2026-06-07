from pathlib import Path
from collections import Counter

# Get the Home directory path
home_dir = Path.home()

# Automatically list visible folders in the Home directory
print("Available folders to sort:")
folders = [item.name for item in home_dir.iterdir() if item.is_dir() and not item.name.startswith(".")]

for folder in folders:
    print(f" - {folder}")

# Allow user to select folder to sort
choice = input("\nWhich folder would you like to sort? ").strip()
target_dir = home_dir / choice

#Check if the folder exists before proceeding
if not target_dir.exists() or not target_dir.is_dir():
    print(f"Error: '{choice}' is not a valid folder.")
    exit()

    print(f"\nScanning: {target_dir}\n")

# Define mapping to assign file to corresponding categories based on suffix
EXT_MAP = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Screenshots", ".heic": "Images", ".gif": "Images", ".bmp": "Images", ".icns": "Images",
    ".mov": "Video", ".mp4": "Video", ".mkv": "Video", ".avi": "Video",
    ".docx": "Documents", ".pdf": "Documents", ".txt": "Documents", ".ppages": "Documents", ".doc": "Documents",
    ".xlsx": "MS Office/Excel", ".xls": "MS Office/Excel", ".xlt": "MS Office/Excel", ".pptx": "MS Office/Powerpoint", ".ppt": "MS Office/Powerpoint", ".mpp": "MS Office/Project",
    ".accdb": "MS Office/Database", ".laccdb": "MS Office/Database",
     ".cs": "Development", ".jar": "Development", ".exe": "Development",
    ".html": "Web/Internet", ".webp": "Web/Internet", ".avif": "Web/Internet",
    ".dmg": "Installers", ".pkg": "Installers", ".iso": "Installers", 
    ".db": "System"
}

# Initialise the category counter
category_counts = Counter()
other_files = [] # List to track any uncategorised files

# Ignore directories and only display files
for item in target_dir.iterdir():
    if item.is_file():
        extension = item.suffix.lower()
        category = EXT_MAP.get(extension, "Other")
        destination = target_dir / category

        category_counts[category] += 1
        if category == "Other":
            other_files.append(item.name)

# Dry run mode showing where each file would be moved to 
        print(f"Would move:\n{item.name}")
        print(f"FROM: {target_dir}")
        print(f"TO:   {destination}\n")

# Check wether destination file exists on users system
        if destination.is_dir():
            print(f"{destination} already exists.\n")
        else:
            print(f"{destination} folder not found.\n")

# Create any missing directories for destinations automatically
            destination.mkdir(parents=True, exist_ok=True)
            print(f"Created: {destination}\n")
        
        new_location = destination / item.name
        print(f"Moving:")
        print(f"FROM: {item}")
        print(f"TO: {new_location}\n")

# Move files to corresponding folders
        item.rename(new_location)

# Delete any empty folders inside chosen directory
print("--- Cleaning up empty folders ---")

for folder in target_dir.iterdir():
    if folder.is_dir() and not any(folder.iterdir()):
        print(f"Deleting empty folder: {folder.name}")
        folder.rmdir()

# Print summary of all file extensions and a count of how many files there are of each
print("\n--- Summary ---")
for category, count in category_counts.items():
    print(f"{category}: {count} files")

# Print list of unorganised (other) files for better user organisation
print("\n--- Files needing better organisation (Other) ---")
for name in other_files:
    print(f"- {name}")


