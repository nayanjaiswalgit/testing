import os
from hashlib import md5
from collections import defaultdict
import shutil
import sys

def find_duplicates(directory):
    # Dictionary to store file paths grouped by their hash
    hash_map = defaultdict(list)

    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)
            # Calculate the hash of the file
            with open(file_path, 'rb') as f:
                file_hash = md5(f.read()).hexdigest()
            # Add the file path to the dictionary with its hash
            hash_map[file_hash].append(file_path)

    # Filter out hashes with only one file (non-duplicates)
    duplicates = {hash: files for hash, files in hash_map.items() if len(files) > 1}

    return duplicates

def move_duplicates(duplicates, directory):
    duplicate_folder = os.path.join(directory, 'duplicates')
    if not os.path.exists(duplicate_folder):
        os.makedirs(duplicate_folder)

    for files in duplicates.values():
        for file in files[1:]:
            destination = os.path.join(duplicate_folder, os.path.basename(file))
            if not os.path.exists(destination):
                shutil.move(file, destination)
            else:
                # If duplicate file already exists in duplicates folder, rename it
                base, ext = os.path.splitext(os.path.basename(file))
                count = 1
                while os.path.exists(os.path.join(duplicate_folder, f"{base}_{count}{ext}")):
                    count += 1
                shutil.move(file, os.path.join(duplicate_folder, f"{base}_{count}{ext}"))

def list_duplicates(duplicates):
    print("Duplicate Images:")
    for files in duplicates.values():
        for file in files:
            print(file)
        print()

def main():
    directory = input("Enter directory path: ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        sys.exit(1)

    duplicates = find_duplicates(directory)
    if not duplicates:
        print("No duplicate images found.")
        sys.exit(0)

    list_duplicates(duplicates)

    move_duplicates(duplicates, directory)
    print("Duplicates moved to /duplicates folder.")

if __name__ == "__main__":
    main()
