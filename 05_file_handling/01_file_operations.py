"""
File Handling in Python

Learn how to read from and write to files.
"""

import os

print("=== WRITING TO FILES ===")

# Create a temporary directory for examples
temp_dir = "/tmp/python_file_examples"
os.makedirs(temp_dir, exist_ok=True)

# Write mode ('w') - creates new file or overwrites existing
file_path = os.path.join(temp_dir, "example.txt")
with open(file_path, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
    file.write("Python file handling is easy!")

print(f"File written to: {file_path}")

# Append mode ('a') - adds to end of file
with open(file_path, 'a') as file:
    file.write("\nThis line was appended.")

print("Line appended to file")

print("\n=== READING FROM FILES ===")

# Read entire file
with open(file_path, 'r') as file:
    content = file.read()
    print("Full content:")
    print(content)

# Read line by line
print("\nReading line by line:")
with open(file_path, 'r') as file:
    for line in file:
        print(f"  {line.strip()}")

# Read lines into list
with open(file_path, 'r') as file:
    lines = file.readlines()
    print(f"\nTotal lines: {len(lines)}")
    print(f"First line: {lines[0].strip()}")

print("\n=== FILE METHODS ===")

# readline() - read one line at a time
with open(file_path, 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")

print("\n=== WRITING LISTS TO FILES ===")
fruits = ["apple", "banana", "cherry", "date"]
fruits_file = os.path.join(temp_dir, "fruits.txt")

with open(fruits_file, 'w') as file:
    for fruit in fruits:
        file.write(f"{fruit}\n")

print(f"List written to: {fruits_file}")

# Read back
with open(fruits_file, 'r') as file:
    loaded_fruits = [line.strip() for line in file]
    print(f"Loaded fruits: {loaded_fruits}")

print("\n=== FILE POSITIONS ===")
with open(file_path, 'r') as file:
    print(f"Initial position: {file.tell()}")
    file.read(10)  # Read 10 characters
    print(f"Position after reading 10 chars: {file.tell()}")
    file.seek(0)  # Go back to beginning
    print(f"Position after seek(0): {file.tell()}")

print("\n=== CHECKING FILE EXISTENCE ===")
print(f"File exists: {os.path.exists(file_path)}")
print(f"Is file: {os.path.isfile(file_path)}")
print(f"Is directory: {os.path.isdir(temp_dir)}")

print("\n=== FILE INFORMATION ===")
file_size = os.path.getsize(file_path)
print(f"File size: {file_size} bytes")

print("\n=== WORKING WITH PATHS ===")
print(f"Absolute path: {os.path.abspath(file_path)}")
print(f"Directory name: {os.path.dirname(file_path)}")
print(f"File name: {os.path.basename(file_path)}")
print(f"Split: {os.path.split(file_path)}")

# Join paths
new_path = os.path.join(temp_dir, "subdir", "file.txt")
print(f"Joined path: {new_path}")

print("\n=== LISTING DIRECTORY CONTENTS ===")
contents = os.listdir(temp_dir)
print(f"Directory contents: {contents}")

print("\n=== BINARY FILES ===")
# Write binary data
binary_file = os.path.join(temp_dir, "binary.bin")
data = bytes([65, 66, 67, 68, 69])  # ASCII codes for ABCDE

with open(binary_file, 'wb') as file:
    file.write(data)

# Read binary data
with open(binary_file, 'rb') as file:
    binary_content = file.read()
    print(f"Binary content: {binary_content}")
    print(f"Decoded: {binary_content.decode('ascii')}")

print("\n=== BEST PRACTICES ===")
print("1. Always use 'with' statement (automatically closes file)")
print("2. Use appropriate modes: 'r' (read), 'w' (write), 'a' (append)")
print("3. Add 'b' for binary mode: 'rb', 'wb'")
print("4. Use os.path.join() for cross-platform paths")
print("5. Check file existence before reading")
print("6. Handle exceptions when working with files")

print("\n=== FILE MODES SUMMARY ===")
modes = {
    "'r'": "Read (default) - error if file doesn't exist",
    "'w'": "Write - creates new or overwrites existing",
    "'a'": "Append - adds to end of file",
    "'x'": "Exclusive creation - error if file exists",
    "'r+'": "Read and write",
    "'w+'": "Write and read (overwrites)",
    "'a+'": "Append and read",
    "'rb'": "Read binary",
    "'wb'": "Write binary",
}
for mode, description in modes.items():
    print(f"{mode:6} - {description}")

print("\n=== CLEANUP ===")
# Clean up temporary files (optional)
print(f"Temporary files created in: {temp_dir}")
print("Files can be cleaned up manually or left for system cleanup")

print("\nAll examples executed successfully!")
