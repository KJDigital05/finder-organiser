from pathlib import Path
from collections import Counter

# Use current users' Downloads folder automatically
downloads = Path.home() / "Documents"

# Loop through each item within Downloads
print(f"Scanning: {downloads}\n")

# Define mapping to assign file to corresponding categories based on suffix
EXT_MAP = {
    ".jpg": "Images", ".png": "Screenshots", ".heic": "Images", ".gif": "Images", ".bmp": "Images", ".icns": "Images",
    ".mov": "Video", ".mp4": "Video", ".mkv": "Video", ".avi": "Video",
    ".docx": "Documents", ".pdf": "Documents", ".txt": "Documents", ".pages": "Documents", ".doc": "Documents",
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
for item in downloads.iterdir():
    if item.is_file():
        extension = item.suffix.lower()
        category = EXT_MAP.get(extension, "Other")
        destination = downloads / category

        category_counts[category] += 1
        if category == "Other":
            other_files.append(item.name)

# Dry run mode showing where each file would be moved to 
        print(f"Would move:\n{item.name}")
        print(f"FROM: {downloads}")
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

# Print summary of all file extensions and a count of how many files there are of each
print("\n--- Summary ---")
for category, count in category_counts.items():
    print(f"{category}: {count} files")

# Print list of unorganised (other) files for better user organisation
print("\n--- Files needing better organisation (Other) ---")
for name in other_files:
    print(f"- {name}")


