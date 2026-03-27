# Example: Create directories and list files

import os

# Create nested directories
os.makedirs("folder1/folder2", exist_ok=True)

# List files and folders
files = os.listdir(".")
print("Files in current directory:")
print(files)



# Example: Move / copy files between directories

import shutil

# Copy sample file to folder1
shutil.copy("sample.txt", "folder1/sample.txt")

print("File moved to folder1")