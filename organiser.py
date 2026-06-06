from pathlib import Path
import collections

# Use current users Downloads folder automatically
downloads = Path.home() / "Downloads"

# Loop through each item within Downloads
print(f"Scanning: {downloads}\n")

# Initialize the category counter
category_counts = collections.Counter()
other_files = [] # List to track "Other" files

# Ignore directories and only display files
for item in downloads.iterdir():
    if item.is_file():
        ext = item.suffix.lower()

# Created variables for easy repitition        
        extension = item.suffix
        category = "Other"

# Organise extension suffixes for categories
        image_extensions = {".jpg", ".png", ".gif", ".bmp", ".icns", ".HEIC"}
        video_extensions = {".mov", ".mp4", ".mkv", ".avi"}
        document_extensions = {".docx", ".pdf", ".txt", ".pages", '.doc'}
        ms_extensions = {".xlsx", ".xls", ".pptx", ".xlt", ".ppt", ".mpp"}
        database_extensions = {".accdb", ".laccdb"} 
        dev_extensions = {".cs", ".jar", ".Program.cs", ".exe"}
        web_extensions = {".html", ".webp", ".avif"}
        installers_extensions = {".dmg", ".pkg", ".iso"}
        sys_extensions= {".DS_Store", ".db", ".localized", ".desktop.ini"}
        
        if extension in image_extensions:
            category = "Images"
        elif extension in video_extensions:
            category = "Video"
        elif extension in document_extensions:
            category = "Documents"
        elif extension in ms_extensions:
            category = "MS Office/Planning"
        elif extension in database_extensions:
            category = "Database"
        elif extension in dev_extensions:
            category = "Development/Code"
        elif extension in web_extensions:
            category = "Web/Internet"
        elif extension in installers_extensions:
            category = "Installers/Disk Images"
        elif extension in sys_extensions:
            category = "System"

        category_counts[category] += 1
        if category == "Other":
            other_files.append(item.name)

        print(f"{item.name} -> {category}")

print("\n--- Summary ---")
for category, count in category_counts.items():
    print(f"{category}: {count} files")

print("\n--- Files needing better organization (Other) ---")
for name in other_files:
    print(f"- {name}")
