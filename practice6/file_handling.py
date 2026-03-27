# Example: Copy and delete file

import shutil
import os

# Copy file
shutil.copy("sample.txt", "backup.txt")
print("File copied")

# Delete file
if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("Backup file deleted")

# Read and print file contents

with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:")
    print(content)

    # Create a file and write data

with open("sample.txt", "w") as f:
    f.write("Hello\n")
    f.write("Python file handling practice\n")

# Append new data

with open("sample.txt", "a") as f:
    f.write("New line added\n")

