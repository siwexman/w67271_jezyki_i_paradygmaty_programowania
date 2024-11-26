import os
import glob

# Get the current directory where the Python script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Search for .txt files in the current directory
txtFiles = glob.glob(os.path.join(current_directory, "*.txt"))

if txtFiles:
    print("Found the following .txt files:")
    for file in txtFiles:
        print(file)
else:
    print("No .txt files found.")
