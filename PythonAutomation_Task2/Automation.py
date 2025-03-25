import os
import shutil

# Define source folder path
source_folder = "C:\\Users\\DELL\\Downloads"

# Define destination folders
destination_folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
    'Programs': ['.exe', '.msi']
}

# Create destination folders if they don't exist
for folder in destination_folders.keys():
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

# File organization logic
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    
    if os.path.isfile(file_path):  # Check if it's a file
        file_ext = os.path.splitext(file)[1].lower()

        for folder, extensions in destination_folders.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(source_folder, folder))
                print(f"Moved: {file} → {folder}")
                break

print("File organization completed successfully!")
