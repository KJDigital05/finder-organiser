from pathlib import Path
import collections

# Use current users Downloads folder automatically
downloads = Path.home() / "Downloads"

# Loop through each item within Downloads
print(f"Scanning: {downloads}\n")

# Define mapping to remove looping
EXT_MAP = {
    ".jpg": "Images", ".png": "Images", ".heic": "Images", ".gif": "Images", ".bmp": "Images", ".icns": "Images",
    ".mov": "Video", ".mp4": "Video", ".mkv": "Video", ".avi": "Video",
    ".docx": "Documents", ".pdf": "Documents", ".txt": "Documents", ".pages": "Documents", ".doc": "Documents",
    ".xlsx": "MS Excel", ".xls": "MS Excel", ".xlt": "MS Excel", ".pptx": "MS Powerpoint", ".ppt": "MS Powerpoint", ".mpp": "MS Project",
    ".cs": "Development", ".jar": "Development", ".exe": "Development",
    ".accdb": "Database", ".laccdb": "Database",
    ".html": "Web/Internet", ".webp": "Web/Internet", ".avif": "Web/Internet",
    ".dmg": "Installers", ".pkg": "Installers", ".iso": "Installers",
    ".DS_Store": "System", ".db": "System"
}

# Initialize the category counter
category_counts = collections.Counter()
other_files = [] # List to track "Other" files

# Ignore directories and only display files
for item in downloads.iterdir():
    if item.is_file():
        extension = item.suffix.lower()

        category = EXT_MAP.get(extension, "Other")

        category_counts[category] += 1
        if category == "Other":
            other_files.append(item.name)
        
        print(f"{item.name} -> {category}")

# Print summary of all file extensions and a count of how many files there are
print("\n--- Summary ---")
for category, count in category_counts.items():
    print(f"{category}: {count} files")

print("\n--- Files needing better organisation (Other) ---")
for name in other_files:
    print(f"- {name}")