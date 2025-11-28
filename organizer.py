import os
import shutil
import argparse
from pathlib import Path

# Define file type mappings
FILE_MAPPINGS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt', '.csv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'ZIP': ['.zip', '.rar', '.7z', '.tar', '.gz']
}

def get_folder_name(extension):
    """Determines the folder name based on the file extension."""
    for folder, extensions in FILE_MAPPINGS.items():
        if extension.lower() in extensions:
            return folder
    return 'Others'

def organize_files(folder_path):
    """Organizes files in the given folder into subfolders based on extension."""
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    print(f"Organizing files in: {folder_path}")

    # Iterate through all files in the directory
    for file_path in folder.iterdir():
        if file_path.is_dir():
            continue  # Skip directories

        # Get file extension
        extension = file_path.suffix
        if not extension:
            continue # Skip files without extension

        # Determine destination folder
        category = get_folder_name(extension)
        destination_folder = folder / category

        # Create destination folder if it doesn't exist
        destination_folder.mkdir(exist_ok=True)

        # Move the file
        destination_path = destination_folder / file_path.name
        try:
            shutil.move(str(file_path), str(destination_path))
            print(f"Moved: {file_path.name} -> {category}/{file_path.name}")
        except Exception as e:
            print(f"Error moving {file_path.name}: {e}")

    print("Organization complete!")

def main():
    parser = argparse.ArgumentParser(description="Organize files in a folder based on their type.")
    parser.add_argument("folder_path", nargs='?', help="Path to the folder to organize")
    
    args = parser.parse_args()
    
    folder_path = args.folder_path
    
    # If no argument provided, ask for input
    if not folder_path:
        folder_path = input("Enter the path of the folder to organize: ").strip()

    if folder_path:
        organize_files(folder_path)
    else:
        print("No folder path provided. Exiting.")

if __name__ == "__main__":
    main()
